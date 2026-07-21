"""Reviewed UniProt host mapping with independent KEGG supplementation."""

from __future__ import annotations

import hashlib
import json
from typing import Literal

import requests
from crewai.tools import BaseTool
from pydantic import BaseModel, ConfigDict, Field, PositiveInt, field_validator

from src.tools.base import BaseAPITool


UNIPROT_ENTRY_TYPE = "UniProtKB reviewed (Swiss-Prot)"
USER_AGENT = "ADRMATS-MicrobeCrew-Enzyme2Organism/1.0"
HTTP_TIMEOUT = (5.0, 20.0)


class StrictModel(BaseModel):
    """Shared strict configuration for the bounded M4a schema."""

    model_config = ConfigDict(extra="forbid")


class Enzyme2OrganismInput(StrictModel):
    """Distinct reviewed enzyme accessions to map in first-seen order."""

    enzyme_uids: list[str] = Field(min_length=1)

    @field_validator("enzyme_uids", mode="before")
    @classmethod
    def normalize_uids(cls, value: object) -> list[str]:
        if not isinstance(value, (list, tuple)) or not value:
            raise ValueError("enzyme_uids must be a non-empty list")
        normalized: list[str] = []
        seen: set[str] = set()
        for raw_uid in value:
            if not isinstance(raw_uid, str):
                raise ValueError("every enzyme UID must be a string")
            uid = raw_uid.strip()
            if not uid:
                raise ValueError("blank enzyme UIDs are not permitted")
            if uid not in seen:
                seen.add(uid)
                normalized.append(uid)
        return normalized


class UniProtReviewedHostEvidence(StrictModel):
    source_database: Literal["UniProtKB"] = "UniProtKB"
    source_url: str
    response_sha256: str
    primary_accession: str
    entry_type: Literal["UniProtKB reviewed (Swiss-Prot)"]
    reviewed: Literal[True]
    scientific_organism_name: str
    ncbi_taxon_id: PositiveInt
    lineage: list[str]
    annotation_score: float
    protein_existence: str


class KEGGSupplementEvidence(StrictModel):
    source_database: Literal["KEGG"] = "KEGG"
    source_url: str
    response_sha256: str
    gene_ids: list[str]
    multiplicity: int = Field(ge=0)
    state: Literal["missing", "single", "multiple"]


class SourceError(StrictModel):
    source_database: Literal["UniProtKB", "KEGG"]
    source_url: str
    error_type: str
    message: str


class EnzymeHostMapping(StrictModel):
    enzyme_uid: str
    uniprot_reviewed: UniProtReviewedHostEvidence | None = None
    kegg: KEGGSupplementEvidence | None = None
    source_errors: list[SourceError] = Field(default_factory=list)


class Enzyme2OrganismOutput(StrictModel):
    requested_uid_order: list[str]
    mappings: dict[str, EnzymeHostMapping]


class Enzyme2OrganismTool(BaseAPITool):
    """Map reviewed UniProt accessions and retain KEGG multiplicity verbatim."""

    def __init__(self) -> None:
        super().__init__(min_interval=1.0, max_retries=3, cache_ttl=600)
        self.headers = {"User-Agent": USER_AGENT, "Accept": "application/json, text/plain"}

    @staticmethod
    def _uniprot_url(uid: str) -> str:
        return f"https://rest.uniprot.org/uniprotkb/{uid}.json"

    @staticmethod
    def _kegg_url(uid: str) -> str:
        return f"https://rest.kegg.jp/conv/genes/uniprot:{uid}"

    def _request_bytes(self, url: str) -> bytes:
        def do_request() -> bytes:
            response = requests.get(url, headers=self.headers, timeout=HTTP_TIMEOUT)
            response.raise_for_status()
            return bytes(response.content)

        return self._execute_with_retry(do_request)

    def _query_uniprot(
        self, uid: str
    ) -> tuple[UniProtReviewedHostEvidence | None, SourceError | None]:
        url = self._uniprot_url(uid)
        body = self._request_bytes(url)
        digest = hashlib.sha256(body).hexdigest()
        try:
            payload = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            return None, SourceError(
                source_database="UniProtKB",
                source_url=url,
                error_type="malformed_response",
                message=f"invalid UTF-8 JSON: {exc}",
            )

        if not isinstance(payload, dict):
            return None, SourceError(
                source_database="UniProtKB",
                source_url=url,
                error_type="malformed_response",
                message="top-level UniProt response is not an object",
            )
        if payload.get("primaryAccession") != uid:
            return None, SourceError(
                source_database="UniProtKB",
                source_url=url,
                error_type="primary_accession_mismatch",
                message="primaryAccession does not exactly match the requested UID",
            )
        if payload.get("entryType") != UNIPROT_ENTRY_TYPE:
            return None, SourceError(
                source_database="UniProtKB",
                source_url=url,
                error_type="unreviewed_or_unsupported_entry",
                message="entryType is not UniProtKB reviewed (Swiss-Prot)",
            )

        organism = payload.get("organism")
        if not isinstance(organism, dict):
            organism = {}
        name = organism.get("scientificName")
        taxon_id = organism.get("taxonId")
        if not isinstance(name, str) or not name.strip():
            return None, SourceError(
                source_database="UniProtKB",
                source_url=url,
                error_type="missing_reviewed_host",
                message="reviewed record lacks a scientific organism name",
            )
        if isinstance(taxon_id, bool) or not isinstance(taxon_id, int) or taxon_id <= 0:
            return None, SourceError(
                source_database="UniProtKB",
                source_url=url,
                error_type="missing_reviewed_host",
                message="reviewed record lacks a positive integer NCBI taxon ID",
            )

        try:
            evidence = UniProtReviewedHostEvidence(
                source_url=url,
                response_sha256=digest,
                primary_accession=payload["primaryAccession"],
                entry_type=payload["entryType"],
                reviewed=True,
                scientific_organism_name=name,
                ncbi_taxon_id=taxon_id,
                lineage=organism.get("lineage", []),
                annotation_score=payload["annotationScore"],
                protein_existence=payload["proteinExistence"],
            )
        except (KeyError, TypeError, ValueError) as exc:
            return None, SourceError(
                source_database="UniProtKB",
                source_url=url,
                error_type="malformed_response",
                message=f"reviewed evidence fields are malformed: {exc}",
            )
        return evidence, None

    def _query_kegg(self, uid: str) -> KEGGSupplementEvidence:
        url = self._kegg_url(uid)
        body = self._request_bytes(url)
        digest = hashlib.sha256(body).hexdigest()
        text = body.decode("utf-8")
        expected_left = f"up:{uid}"
        gene_ids: list[str] = []
        seen: set[str] = set()
        for line_number, raw_line in enumerate(text.splitlines(), start=1):
            if not raw_line.strip():
                continue
            fields = raw_line.split("\t")
            if len(fields) != 2 or fields[0] != expected_left or not fields[1] or ":" not in fields[1]:
                raise ValueError(f"invalid KEGG conversion row {line_number}")
            gene_id = fields[1]
            if gene_id not in seen:
                seen.add(gene_id)
                gene_ids.append(gene_id)
        multiplicity = len(gene_ids)
        state: Literal["missing", "single", "multiple"]
        state = "missing" if multiplicity == 0 else "single" if multiplicity == 1 else "multiple"
        return KEGGSupplementEvidence(
            source_url=url,
            response_sha256=digest,
            gene_ids=gene_ids,
            multiplicity=multiplicity,
            state=state,
        )

    @staticmethod
    def _request_error(source: Literal["UniProtKB", "KEGG"], url: str, exc: Exception) -> SourceError:
        return SourceError(
            source_database=source,
            source_url=url,
            error_type=type(exc).__name__,
            message=str(exc),
        )

    def _map_one(self, uid: str) -> EnzymeHostMapping:
        cache_key = ("enzyme2organism", uid)
        cached = self._get_cached(cache_key)
        if cached is not None:
            return cached

        errors: list[SourceError] = []
        uniprot: UniProtReviewedHostEvidence | None = None
        kegg: KEGGSupplementEvidence | None = None
        try:
            uniprot, exclusion = self._query_uniprot(uid)
            if exclusion is not None:
                errors.append(exclusion)
        except Exception as exc:
            errors.append(self._request_error("UniProtKB", self._uniprot_url(uid), exc))
        try:
            kegg = self._query_kegg(uid)
        except Exception as exc:
            errors.append(self._request_error("KEGG", self._kegg_url(uid), exc))

        mapping = EnzymeHostMapping(
            enzyme_uid=uid,
            uniprot_reviewed=uniprot,
            kegg=kegg,
            source_errors=errors,
        )
        self._set_cache(cache_key, mapping)
        return mapping

    def map_enzyme_uids(self, enzyme_uids: list[str]) -> Enzyme2OrganismOutput:
        normalized = Enzyme2OrganismInput(enzyme_uids=enzyme_uids).enzyme_uids
        mappings = {uid: self._map_one(uid) for uid in normalized}
        return Enzyme2OrganismOutput(requested_uid_order=normalized, mappings=mappings)


_enzyme2organism_core: Enzyme2OrganismTool | None = None


def get_enzyme2organism_tool() -> Enzyme2OrganismTool:
    """Return the process-wide core tool instance."""

    global _enzyme2organism_core
    if _enzyme2organism_core is None:
        _enzyme2organism_core = Enzyme2OrganismTool()
    return _enzyme2organism_core


class CrewAIEnzyme2OrganismTool(BaseTool):
    """CrewAI adapter; it serializes core evidence without invoking an LLM."""

    name: str = "Reviewed enzyme to organism mapping"
    description: str = (
        "Map reviewed UniProt enzyme accessions to NCBI organism evidence and "
        "retain independent KEGG gene conversion multiplicity."
    )
    args_schema: type[BaseModel] = Enzyme2OrganismInput

    def _run(self, enzyme_uids: list[str]) -> str:
        result = get_enzyme2organism_tool().map_enzyme_uids(enzyme_uids)
        return result.model_dump_json(indent=2)


enzyme2organism_tool = CrewAIEnzyme2OrganismTool()
