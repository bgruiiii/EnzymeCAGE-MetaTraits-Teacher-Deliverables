"""Bounded, network-denied M4a tests against frozen host fixtures."""

from __future__ import annotations

import json
import importlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pytest
import requests
from crewai.tools import BaseTool
from pydantic import ValidationError

import src.tools.base as base_module
from microbe_crew.tools.enzyme2organism_tool import (
    CrewAIEnzyme2OrganismTool,
    Enzyme2OrganismInput,
    Enzyme2OrganismOutput,
    Enzyme2OrganismTool,
    EnzymeHostMapping,
    KEGGSupplementEvidence,
    SourceError,
    UniProtReviewedHostEvidence,
    enzyme2organism_tool,
    get_enzyme2organism_tool,
)
from microbe_crew.tools.organism_aggregator import (
    EnzymeSourceProvenance,
    OrganismCandidate,
    SupportingEnzyme,
    aggregate_organisms,
)
from src.tools.base import BaseAPITool


e2o_module = importlib.import_module("microbe_crew.tools.enzyme2organism_tool")


FIXTURE_ROOT = Path(__file__).parent / "fixtures" / "M4A2C_HOST_MAPPING_FIXTURES_2026-07-19"
CASES = json.loads((FIXTURE_ROOT / "host_mapping_cases.json").read_text(encoding="utf-8"))["cases"]
CASE_BY_UID = {case["uid"]: case for case in CASES}


class FakeResponse:
    def __init__(self, body: bytes, status_code: int = 200) -> None:
        self.content = body
        self.status_code = status_code

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            error = requests.exceptions.HTTPError(f"HTTP {self.status_code} (test-only)")
            error.response = self
            raise error


@pytest.fixture(autouse=True)
def deny_unmocked_network(monkeypatch: pytest.MonkeyPatch) -> None:
    """Every biological request must use an explicit in-test byte fixture."""

    def denied(*args: Any, **kwargs: Any) -> None:
        raise AssertionError("unmocked network request denied by M4a offline guard")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)


def fixture_bytes(uid: str, source: str) -> bytes:
    relative = CASE_BY_UID[uid]["expected"][source]["raw_path"]
    return (FIXTURE_ROOT / relative).read_bytes()


def install_fixture_get(monkeypatch: pytest.MonkeyPatch, calls: list[str] | None = None) -> None:
    def fixture_get(url: str, **kwargs: Any) -> FakeResponse:
        if calls is not None:
            calls.append(url)
        if url.startswith("https://rest.uniprot.org/uniprotkb/") and url.endswith(".json"):
            uid = url.rsplit("/", 1)[1][:-5]
            return FakeResponse(fixture_bytes(uid, "uniprot"))
        if url.startswith("https://rest.kegg.jp/conv/genes/uniprot:"):
            uid = url.rsplit(":", 1)[1]
            return FakeResponse(fixture_bytes(uid, "kegg"))
        raise AssertionError(f"unmocked biological URL: {url}")

    monkeypatch.setattr(e2o_module.requests, "get", fixture_get)


def offline_tool() -> Enzyme2OrganismTool:
    tool = Enzyme2OrganismTool()
    tool._min_interval = 0.0
    return tool


def walk_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        keys.update(value)
        for nested in value.values():
            keys.update(walk_keys(nested))
    elif isinstance(value, list):
        for nested in value:
            keys.update(walk_keys(nested))
    return keys


def test_all_ten_frozen_p0_uids_and_exact_evidence(monkeypatch: pytest.MonkeyPatch) -> None:
    install_fixture_get(monkeypatch)
    uids = [case["uid"] for case in CASES]
    output = offline_tool().map_enzyme_uids(uids)
    assert output.requested_uid_order == uids
    assert set(output.mappings) == set(uids)

    states = {"missing": 0, "single": 0, "multiple": 0}
    for case in CASES:
        uid = case["uid"]
        expected_u = case["expected"]["uniprot"]
        expected_k = case["expected"]["kegg"]
        mapping = output.mappings[uid]
        assert mapping.source_errors == []
        assert mapping.uniprot_reviewed is not None
        assert mapping.kegg is not None
        uniprot = mapping.uniprot_reviewed
        kegg = mapping.kegg
        assert uniprot.primary_accession == expected_u["primary_accession"] == uid
        assert uniprot.entry_type == expected_u["entry_type"]
        assert uniprot.reviewed is True
        assert uniprot.scientific_organism_name == expected_u["scientific_organism_name"]
        assert uniprot.ncbi_taxon_id == expected_u["ncbi_taxon_id"]
        assert uniprot.lineage == expected_u["lineage"]
        assert uniprot.annotation_score == expected_u["annotation_score"]
        assert uniprot.protein_existence == expected_u["protein_existence"]
        assert uniprot.response_sha256 == expected_u["raw_sha256"]
        assert uniprot.source_url == f"https://rest.uniprot.org/uniprotkb/{uid}.json"
        assert kegg.gene_ids == expected_k["gene_ids"]
        assert kegg.multiplicity == expected_k["multiplicity"] == len(kegg.gene_ids)
        assert kegg.state == expected_k["state"]
        assert kegg.response_sha256 == expected_k["raw_sha256"]
        assert kegg.source_url == f"https://rest.kegg.jp/conv/genes/uniprot:{uid}"
        states[kegg.state] += 1

    assert states == {"missing": 1, "single": 7, "multiple": 2}
    assert output.mappings["P71875"].kegg.gene_ids == ["mtu:Rv3526", "mtv:RVBD_3526"]
    assert output.mappings["P76113"].kegg.gene_ids == [
        "eco:b1449",
        "ecj:JW5907",
        "ecoc:C3026_08430",
    ]
    assert output.mappings["P29931"].uniprot_reviewed is not None
    assert output.mappings["P29931"].kegg.state == "missing"


def test_input_order_deduplication_and_blank_rejection(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []
    install_fixture_get(monkeypatch, calls)
    output = offline_tool().map_enzyme_uids([" Q02198 ", "Q02198", "P29931"])
    assert output.requested_uid_order == ["Q02198", "P29931"]
    assert len(calls) == 4
    with pytest.raises(ValidationError, match="blank enzyme UIDs"):
        Enzyme2OrganismInput(enzyme_uids=["Q02198", "   "])


def test_synthetic_unreviewed_mutation_is_excluded(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test-only mutation; it is rejection behavior, not biological evidence."""

    uid = "Q02198"
    mutated = json.loads(fixture_bytes(uid, "uniprot"))
    mutated["entryType"] = "UniProtKB unreviewed (TrEMBL)"

    def get(url: str, **kwargs: Any) -> FakeResponse:
        return FakeResponse(json.dumps(mutated).encode()) if "uniprotkb" in url else FakeResponse(fixture_bytes(uid, "kegg"))

    monkeypatch.setattr(e2o_module.requests, "get", get)
    mapping = offline_tool().map_enzyme_uids([uid]).mappings[uid]
    assert mapping.uniprot_reviewed is None
    assert [error.error_type for error in mapping.source_errors] == ["unreviewed_or_unsupported_entry"]


def test_synthetic_primary_accession_mismatch_is_excluded(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test-only mutation; it is rejection behavior, not biological evidence."""

    uid = "Q02198"
    mutated = json.loads(fixture_bytes(uid, "uniprot"))
    mutated["primaryAccession"] = "TEST_ONLY_MISMATCH"

    def get(url: str, **kwargs: Any) -> FakeResponse:
        return FakeResponse(json.dumps(mutated).encode()) if "uniprotkb" in url else FakeResponse(fixture_bytes(uid, "kegg"))

    monkeypatch.setattr(e2o_module.requests, "get", get)
    mapping = offline_tool().map_enzyme_uids([uid]).mappings[uid]
    assert mapping.uniprot_reviewed is None
    assert [error.error_type for error in mapping.source_errors] == ["primary_accession_mismatch"]


def test_sparse_debaryomyces_path_has_no_invented_traits(monkeypatch: pytest.MonkeyPatch) -> None:
    install_fixture_get(monkeypatch)
    mapping = offline_tool().map_enzyme_uids(["Q6BQK1"]).mappings["Q6BQK1"]
    assert mapping.uniprot_reviewed.scientific_organism_name.startswith("Debaryomyces hansenii")
    assert mapping.uniprot_reviewed.ncbi_taxon_id == 284592
    assert not ({"trait", "traits", "safety", "safety_value"} & walk_keys(mapping.model_dump()))


def test_no_prohibited_fields_in_models_or_output(monkeypatch: pytest.MonkeyPatch) -> None:
    install_fixture_get(monkeypatch)
    models = [
        Enzyme2OrganismInput,
        UniProtReviewedHostEvidence,
        KEGGSupplementEvidence,
        SourceError,
        EnzymeHostMapping,
        Enzyme2OrganismOutput,
        SupportingEnzyme,
        EnzymeSourceProvenance,
        OrganismCandidate,
    ]
    for model in models:
        schema_keys = walk_keys(model.model_json_schema())
        assert "confidence" not in schema_keys
        assert "organism_confidence" not in schema_keys
    output = offline_tool().map_enzyme_uids(["Q02198"])
    assert "confidence" not in walk_keys(output.model_dump())
    assert "organism_confidence" not in walk_keys(output.model_dump())


def test_required_base_inheritance() -> None:
    assert issubclass(Enzyme2OrganismTool, BaseAPITool)
    assert Enzyme2OrganismTool._execute_with_retry is BaseAPITool._execute_with_retry


def test_transient_failure_uses_inherited_retry_then_succeeds(monkeypatch: pytest.MonkeyPatch) -> None:
    uid = "Q02198"
    uniprot_attempts = 0

    def get(url: str, **kwargs: Any) -> FakeResponse:
        nonlocal uniprot_attempts
        if "uniprotkb" in url:
            uniprot_attempts += 1
            if uniprot_attempts == 1:
                raise requests.exceptions.ConnectionError("test-only transient failure")
            return FakeResponse(fixture_bytes(uid, "uniprot"))
        return FakeResponse(fixture_bytes(uid, "kegg"))

    monkeypatch.setattr(e2o_module.requests, "get", get)
    monkeypatch.setattr(base_module.time, "sleep", lambda seconds: None)
    monkeypatch.setattr(base_module.random, "uniform", lambda low, high: 0.0)
    mapping = offline_tool().map_enzyme_uids([uid]).mappings[uid]
    assert uniprot_attempts == 2
    assert mapping.uniprot_reviewed is not None
    assert mapping.source_errors == []


def test_http_4xx_is_not_retried(monkeypatch: pytest.MonkeyPatch) -> None:
    uid = "Q02198"
    uniprot_attempts = 0

    def get(url: str, **kwargs: Any) -> FakeResponse:
        nonlocal uniprot_attempts
        if "uniprotkb" in url:
            uniprot_attempts += 1
            return FakeResponse(b"not found", status_code=404)
        return FakeResponse(fixture_bytes(uid, "kegg"))

    monkeypatch.setattr(e2o_module.requests, "get", get)
    monkeypatch.setattr(base_module.time, "sleep", lambda seconds: None)
    mapping = offline_tool().map_enzyme_uids([uid]).mappings[uid]
    assert uniprot_attempts == 1
    assert mapping.uniprot_reviewed is None
    assert mapping.kegg is not None
    assert mapping.source_errors[0].error_type == "HTTPError"


def test_inherited_rate_limit_sleeps_exact_remaining_interval(monkeypatch: pytest.MonkeyPatch) -> None:
    tool = Enzyme2OrganismTool()
    tool._last_request_time = 10.0
    sleeps: list[float] = []
    monkeypatch.setattr(base_module.time, "time", lambda: 10.25)
    monkeypatch.setattr(base_module.time, "sleep", sleeps.append)
    assert tool._execute_with_retry(lambda: "ok") == "ok"
    assert sleeps == [pytest.approx(0.75)]


def test_inherited_ttl_cache_prevents_repeat_requests(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []
    install_fixture_get(monkeypatch, calls)
    tool = offline_tool()
    first = tool.map_enzyme_uids(["Q02198"])
    second = tool.map_enzyme_uids(["Q02198"])
    assert len(calls) == 2
    assert first == second


def test_singleton_factory_identity() -> None:
    assert get_enzyme2organism_tool() is get_enzyme2organism_tool()


def test_crewai_adapter_schema_and_parseable_json(monkeypatch: pytest.MonkeyPatch) -> None:
    install_fixture_get(monkeypatch)
    core = offline_tool()
    monkeypatch.setattr(e2o_module, "_enzyme2organism_core", core)
    assert isinstance(enzyme2organism_tool, BaseTool)
    assert isinstance(enzyme2organism_tool, CrewAIEnzyme2OrganismTool)
    assert enzyme2organism_tool.args_schema is Enzyme2OrganismInput
    output = json.loads(enzyme2organism_tool._run(enzyme_uids=["Q02198"]))
    assert output["requested_uid_order"] == ["Q02198"]
    assert output["mappings"]["Q02198"]["uniprot_reviewed"]["ncbi_taxon_id"] == 303


@dataclass
class SyntheticRankedEnzyme:
    uid: str
    score: float
    rank: int
    ensemble_ci: tuple[float, float] | None


def synthetic_mapping(uid: str, taxon_id: int, name: str) -> EnzymeHostMapping:
    """Build test-only aggregation evidence; it is not biological evidence."""

    return EnzymeHostMapping(
        enzyme_uid=uid,
        uniprot_reviewed=UniProtReviewedHostEvidence(
            source_url=f"https://rest.uniprot.org/uniprotkb/{uid}.json",
            response_sha256="0" * 64,
            primary_accession=uid,
            entry_type="UniProtKB reviewed (Swiss-Prot)",
            reviewed=True,
            scientific_organism_name=name,
            ncbi_taxon_id=taxon_id,
            lineage=[],
            annotation_score=1.0,
            protein_existence="test-only",
        ),
        kegg=None,
        source_errors=[],
    )


def test_aggregator_grouping_default_order_dedup_and_name_variants() -> None:
    rankings = [
        SyntheticRankedEnzyme("E2", 0.82, 2, (0.80, 0.84)),
        SyntheticRankedEnzyme("E1", 0.91, 1, (0.90, 0.92)),
        SyntheticRankedEnzyme("E2", 0.01, 99, None),  # test-only duplicate ignored
        SyntheticRankedEnzyme("E3", 0.70, 3, None),
        SyntheticRankedEnzyme("E4", 0.60, 4, (0.50, 0.70)),
    ]
    output = Enzyme2OrganismOutput(
        requested_uid_order=["E1", "E2", "E3", "E4"],
        mappings={
            "E1": synthetic_mapping("E1", 20, "Representative name"),
            "E2": synthetic_mapping("E2", 20, "Name variant"),
            "E3": synthetic_mapping("E3", 3, "Taxon three"),
            "E4": synthetic_mapping("E4", 11, "Taxon eleven"),
        },
    )
    candidates = aggregate_organisms(rankings, output)
    assert [candidate.ncbi_taxon_id for candidate in candidates] == [20, 3, 11]
    assert [candidate.supporting_enzyme_count for candidate in candidates] == [2, 1, 1]
    assert [candidate.default_order_rank for candidate in candidates] == [1, 2, 3]
    shared = candidates[0]
    assert [support.uid for support in shared.supporting_enzymes] == ["E1", "E2"]
    assert shared.organism_name == "Representative name"
    assert shared.organism_name_variants == ["Representative name", "Name variant"]
    assert shared.supporting_enzymes[1].score == 0.82
    assert shared.supporting_enzymes[1].rank == 2
    assert shared.supporting_enzymes[1].ensemble_ci == (0.80, 0.84)


def test_authoritative_ranked_enzyme_objects_preserve_fields() -> None:
    from enzymecage_wrapper.schema import RankedEnzyme

    ranked = RankedEnzyme(uid="AUTH1", score=0.87654321, rank=7, ensemble_ci=(0.81, 0.93))
    output = Enzyme2OrganismOutput(
        requested_uid_order=["AUTH1"],
        mappings={"AUTH1": synthetic_mapping("AUTH1", 42, "Authoritative shape test")},
    )
    support = aggregate_organisms([ranked], output)[0].supporting_enzymes[0]
    assert support.uid == ranked.uid
    assert support.score == ranked.score
    assert support.rank == ranked.rank
    assert support.ensemble_ci == ranked.ensemble_ci
