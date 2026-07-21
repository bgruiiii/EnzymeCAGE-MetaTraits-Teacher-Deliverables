"""Pure NCBI-taxon aggregation for reviewed enzyme host mappings."""

from __future__ import annotations

from typing import Literal, Protocol

from pydantic import BaseModel, ConfigDict, Field

from .enzyme2organism_tool import (
    Enzyme2OrganismOutput,
    KEGGSupplementEvidence,
    SourceError,
    UniProtReviewedHostEvidence,
)


class RankedEnzymeLike(Protocol):
    uid: str
    score: float
    rank: int
    ensemble_ci: tuple[float, float] | None


class AggregationModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class SupportingEnzyme(AggregationModel):
    uid: str
    score: float
    rank: int
    ensemble_ci: tuple[float, float] | None = None


class EnzymeSourceProvenance(AggregationModel):
    enzyme_uid: str
    uniprot_reviewed: UniProtReviewedHostEvidence
    kegg: KEGGSupplementEvidence | None = None
    source_errors: list[SourceError] = Field(default_factory=list)


class OrganismCandidate(AggregationModel):
    organism_uid: str
    taxonomy_namespace: Literal["NCBI_taxon"]
    ncbi_taxon_id: int
    organism_name: str
    organism_name_variants: list[str]
    supporting_enzymes: list[SupportingEnzyme]
    supporting_enzyme_count: int
    per_enzyme_source_provenance: list[EnzymeSourceProvenance]
    default_order_rank: int


def aggregate_organisms(
    enzyme_ranking: list[RankedEnzymeLike],
    e2o_output: Enzyme2OrganismOutput,
) -> list[OrganismCandidate]:
    """Group accepted reviewed hosts by NCBI taxon ID using the v1 order."""

    first_ranked: dict[str, RankedEnzymeLike] = {}
    for ranked in enzyme_ranking:
        if ranked.uid not in first_ranked:
            first_ranked[ranked.uid] = ranked

    grouped: dict[int, list[tuple[RankedEnzymeLike, object]]] = {}
    for uid, ranked in first_ranked.items():
        mapping = e2o_output.mappings.get(uid)
        if mapping is None or mapping.uniprot_reviewed is None:
            continue
        taxon_id = mapping.uniprot_reviewed.ncbi_taxon_id
        grouped.setdefault(taxon_id, []).append((ranked, mapping))

    candidates: list[OrganismCandidate] = []
    for taxon_id, members in grouped.items():
        members.sort(key=lambda item: (item[0].rank, item[0].uid))
        name_variants: list[str] = []
        for _, mapping in members:
            name = mapping.uniprot_reviewed.scientific_organism_name
            if name not in name_variants:
                name_variants.append(name)
        supporting = [
            SupportingEnzyme(
                uid=ranked.uid,
                score=ranked.score,
                rank=ranked.rank,
                ensemble_ci=ranked.ensemble_ci,
            )
            for ranked, _ in members
        ]
        provenance = [
            EnzymeSourceProvenance(
                enzyme_uid=ranked.uid,
                uniprot_reviewed=mapping.uniprot_reviewed,
                kegg=mapping.kegg,
                source_errors=mapping.source_errors,
            )
            for ranked, mapping in members
        ]
        candidates.append(
            OrganismCandidate(
                organism_uid=str(taxon_id),
                taxonomy_namespace="NCBI_taxon",
                ncbi_taxon_id=taxon_id,
                organism_name=name_variants[0],
                organism_name_variants=name_variants,
                supporting_enzymes=supporting,
                supporting_enzyme_count=len(supporting),
                per_enzyme_source_provenance=provenance,
                default_order_rank=0,
            )
        )

    candidates.sort(key=lambda candidate: (-candidate.supporting_enzyme_count, candidate.ncbi_taxon_id))
    for order_rank, candidate in enumerate(candidates, start=1):
        candidate.default_order_rank = order_rank
    return candidates
