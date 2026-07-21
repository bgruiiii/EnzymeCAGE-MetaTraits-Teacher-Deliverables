#!/usr/bin/env python3
"""Validate frozen M4a host-mapping fixtures without network access."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import NoReturn


EXPECTED_UIDS = [
    "Q8EFP8",
    "Q12WS1",
    "A0A0H3C8X0",
    "P29931",
    "Q6BQK1",
    "P71875",
    "S5SC42",
    "P76113",
    "C8WLM1",
    "Q02198",
]
EXPECTED_SOURCE_MANIFEST_SHA256 = (
    "9f646442d7ccd8ac24de4feb446825309059a92be8ca9d5d60b3d002edcb9503"
)
PINNED_ADRMATS_COMMIT = "ca5eabe1d521bbcb8aae67c0b2fd24f9f16667a5"
FORBIDDEN_FIELDS = {"organism_confidence", "confidence"}


def fail(code: str) -> NoReturn:
    print(f"INVALID:{code}", file=sys.stderr)
    raise SystemExit(1)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def contains_forbidden_field(value: object) -> bool:
    if isinstance(value, dict):
        return bool(FORBIDDEN_FIELDS.intersection(value)) or any(
            contains_forbidden_field(item) for item in value.values()
        )
    if isinstance(value, list):
        return any(contains_forbidden_field(item) for item in value)
    return False


def parse_kegg(path: Path, uid: str) -> list[str]:
    result: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line:
            continue
        try:
            source, gene_id = line.split("\t", 1)
        except ValueError:
            fail("KEGG_BODY_FORMAT")
        if source != f"up:{uid}":
            fail("KEGG_SOURCE_UID_MISMATCH")
        result.append(gene_id)
    return result


def validate(root: Path) -> None:
    root = root.resolve()
    manifest_path = root / "FIXTURE_MANIFEST.sha256"
    fixture_path = root / "host_mapping_cases.json"
    if not manifest_path.is_file() or not fixture_path.is_file():
        fail("REQUIRED_FILE_MISSING")

    manifest: dict[str, str] = {}
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        try:
            digest, relative_path = line.split("  ", 1)
        except ValueError:
            fail("MANIFEST_FORMAT")
        if relative_path in manifest:
            fail("MANIFEST_DUPLICATE_PATH")
        manifest[relative_path] = digest
    if len(manifest) != 21:
        fail("MANIFEST_ENTRY_COUNT")
    for relative_path, expected_hash in manifest.items():
        path = root / relative_path
        if not path.is_file() or sha256(path) != expected_hash:
            fail("MANIFEST_HASH_OR_PATH_MISMATCH")

    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    if contains_forbidden_field(fixture):
        fail("FORBIDDEN_CONFIDENCE_FIELD")
    authority = fixture.get("authority", {})
    if authority.get("accepted_mt_d5_source_manifest_sha256") != EXPECTED_SOURCE_MANIFEST_SHA256:
        fail("SOURCE_MANIFEST_IDENTITY")
    if authority.get("pinned_adrmats_commit") != PINNED_ADRMATS_COMMIT:
        fail("ADRMATS_COMMIT_IDENTITY")
    contract = fixture.get("contract", {})
    expected_contract = {
        "uniprot_reviewed_primary": True,
        "trembl_included": False,
        "kegg_independent_supplement": True,
        "kegg_multiplicity_preserved": True,
        "taxonomy_key": "NCBI_taxon_ID",
        "organism_confidence_present": False,
        "abc_complete_formula_encoded": False,
    }
    if contract != expected_contract:
        fail("TEACHER_CONTRACT_MISMATCH")

    cases = fixture.get("cases", [])
    if [case.get("uid") for case in cases] != EXPECTED_UIDS:
        fail("UID_ORDER_OR_MEMBERSHIP_MISMATCH")
    state_counts = {"missing": 0, "single": 0, "multiple": 0}
    seen_paths: set[str] = {"host_mapping_cases.json"}
    for case in cases:
        uid = case["uid"]
        expected = case["expected"]
        uniprot_expected = expected["uniprot"]
        kegg_expected = expected["kegg"]
        if uniprot_expected.get("reviewed") is not True:
            fail("UNREVIEWED_CASE")
        if uniprot_expected.get("primary_accession") != uid:
            fail("UNIPROT_ACCESSION_MISMATCH")
        if uniprot_expected.get("entry_type") != "UniProtKB reviewed (Swiss-Prot)":
            fail("UNIPROT_ENTRY_TYPE_MISMATCH")
        uniprot_path = root / uniprot_expected["raw_path"]
        if sha256(uniprot_path) != uniprot_expected["raw_sha256"]:
            fail("UNIPROT_RAW_HASH_MISMATCH")
        uniprot = json.loads(uniprot_path.read_text(encoding="utf-8"))
        organism = uniprot.get("organism", {})
        if uniprot.get("primaryAccession") != uid:
            fail("UNIPROT_RAW_ACCESSION_MISMATCH")
        if uniprot.get("entryType") != uniprot_expected["entry_type"]:
            fail("UNIPROT_RAW_ENTRY_TYPE_MISMATCH")
        if uniprot.get("annotationScore") != uniprot_expected["annotation_score"]:
            fail("UNIPROT_RAW_ANNOTATION_SCORE_MISMATCH")
        if uniprot.get("proteinExistence") != uniprot_expected["protein_existence"]:
            fail("UNIPROT_RAW_PROTEIN_EXISTENCE_MISMATCH")
        if organism.get("scientificName") != uniprot_expected["scientific_organism_name"]:
            fail("UNIPROT_RAW_ORGANISM_MISMATCH")
        if organism.get("taxonId") != uniprot_expected["ncbi_taxon_id"]:
            fail("UNIPROT_RAW_TAXON_MISMATCH")
        if organism.get("lineage") != uniprot_expected["lineage"]:
            fail("UNIPROT_RAW_LINEAGE_MISMATCH")

        kegg_path = root / kegg_expected["raw_path"]
        if sha256(kegg_path) != kegg_expected["raw_sha256"]:
            fail("KEGG_RAW_HASH_MISMATCH")
        raw_gene_ids = parse_kegg(kegg_path, uid)
        if raw_gene_ids != kegg_expected["gene_ids"]:
            fail("KEGG_GENE_IDS_RAW_MISMATCH")
        multiplicity = len(raw_gene_ids)
        if multiplicity != kegg_expected["multiplicity"]:
            fail("KEGG_MULTIPLICITY_MISMATCH")
        state = "missing" if multiplicity == 0 else "single" if multiplicity == 1 else "multiple"
        if state != kegg_expected["state"]:
            fail("KEGG_STATE_MISMATCH")
        state_counts[state] += 1
        seen_paths.update([uniprot_expected["raw_path"], kegg_expected["raw_path"]])

    if state_counts != {"single": 7, "missing": 1, "multiple": 2}:
        fail("KEGG_SUMMARY_COUNTS")
    if set(manifest) != seen_paths:
        fail("MANIFEST_FIXTURE_PATH_SET_MISMATCH")
    expected_summary = fixture.get("expected_summary", {})
    if expected_summary != {
        "uid_count": 10,
        "uniprot_exact": 10,
        "uniprot_unreviewed": 0,
        "kegg_single": 7,
        "kegg_missing": 1,
        "kegg_multiple": 2,
    }:
        fail("EXPECTED_SUMMARY_MISMATCH")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_fixtures.py FIXTURE_ROOT", file=sys.stderr)
        return 2
    validate(Path(sys.argv[1]))
    print("VALID:M4A2C_HOST_MAPPING_FIXTURES:UIDS=10:UNIPROT=10:KEGG=7/1/2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
