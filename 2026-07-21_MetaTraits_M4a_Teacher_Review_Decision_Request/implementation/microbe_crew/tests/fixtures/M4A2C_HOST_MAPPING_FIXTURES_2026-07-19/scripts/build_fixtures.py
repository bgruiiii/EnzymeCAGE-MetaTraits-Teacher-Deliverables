#!/usr/bin/env python3
"""Build frozen M4a host-mapping fixtures from accepted MT-D5 evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
from pathlib import Path


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


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_source_manifest(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        digest, relative_path = line.split("  ", 1)
        entries[relative_path] = digest
    return entries


def selected_kegg_path(raw_evidence_paths: str) -> str:
    matches = [
        path
        for path in raw_evidence_paths.split(";")
        if path.startswith("raw/kegg/") and "/conversion.txt" in path
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one selected KEGG conversion path: {matches}")
    return matches[0]


def parse_kegg(path: Path, uid: str) -> list[str]:
    gene_ids: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line:
            continue
        source, gene_id = line.split("\t", 1)
        if source != f"up:{uid}":
            raise ValueError(f"unexpected KEGG source for {uid}: {source}")
        gene_ids.append(gene_id)
    return gene_ids


def copy_verified(
    source_root: Path,
    output_root: Path,
    relative_path: str,
    source_manifest: dict[str, str],
) -> str:
    source = source_root / relative_path
    if relative_path not in source_manifest:
        raise ValueError(f"source path absent from accepted manifest: {relative_path}")
    actual = sha256(source)
    if actual != source_manifest[relative_path]:
        raise ValueError(f"source hash mismatch: {relative_path}")
    destination = output_root / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    if sha256(destination) != actual:
        raise ValueError(f"copied body hash mismatch: {relative_path}")
    return actual


def write_fixture_manifest(output_root: Path, relative_paths: list[str]) -> None:
    lines = [f"{sha256(output_root / path)}  {path}" for path in sorted(relative_paths)]
    (output_root / "FIXTURE_MANIFEST.sha256").write_text(
        "\n".join(lines) + "\n", encoding="utf-8", newline="\n"
    )


def build(source_root: Path, output_root: Path) -> None:
    source_root = source_root.resolve()
    output_root = output_root.resolve()
    source_manifest_path = source_root / "MANIFEST.sha256"
    if sha256(source_manifest_path) != EXPECTED_SOURCE_MANIFEST_SHA256:
        raise ValueError("accepted MT-D5 source manifest identity mismatch")
    source_manifest = load_source_manifest(source_manifest_path)

    mapping_path = source_root / "outputs/enzyme_organism_mapping.csv"
    with mapping_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if [row["UID"] for row in rows] != EXPECTED_UIDS:
        raise ValueError("fixed UID order or membership mismatch")

    cases: list[dict[str, object]] = []
    copied_paths: list[str] = []
    for row in rows:
        uid = row["UID"]
        uniprot_relative = f"raw/uniprot/{uid}/response.json"
        kegg_relative = selected_kegg_path(row["raw_evidence_paths"])
        uniprot_hash = copy_verified(
            source_root, output_root, uniprot_relative, source_manifest
        )
        kegg_hash = copy_verified(source_root, output_root, kegg_relative, source_manifest)
        copied_paths.extend([uniprot_relative, kegg_relative])

        uniprot = json.loads((source_root / uniprot_relative).read_text(encoding="utf-8"))
        organism = uniprot["organism"]
        if uniprot["primaryAccession"] != uid or row["primary_accession"] != uid:
            raise ValueError(f"UniProt accession mismatch: {uid}")
        if uniprot["entryType"] != "UniProtKB reviewed (Swiss-Prot)":
            raise ValueError(f"unreviewed record in v1 fixture: {uid}")
        if row["entry_type_reviewed_state"] != "reviewed":
            raise ValueError(f"mapping CSV reviewed-state mismatch: {uid}")
        if organism["scientificName"] != row["scientific_organism_name"]:
            raise ValueError(f"organism-name mismatch: {uid}")
        if organism["taxonId"] != int(row["UniProt_NCBI_taxon_ID"]):
            raise ValueError(f"NCBI taxon mismatch: {uid}")
        if uniprot["annotationScore"] != float(row["annotation_score"]):
            raise ValueError(f"annotation-score mismatch: {uid}")
        if uniprot["proteinExistence"] != row["protein_existence"]:
            raise ValueError(f"protein-existence mismatch: {uid}")

        kegg_gene_ids = parse_kegg(source_root / kegg_relative, uid)
        csv_kegg_ids = [item for item in row["KEGG_IDs"].split(";") if item]
        if kegg_gene_ids != csv_kegg_ids:
            raise ValueError(f"KEGG mapping mismatch: {uid}")
        multiplicity = len(kegg_gene_ids)
        kegg_state = "missing" if multiplicity == 0 else "single" if multiplicity == 1 else "multiple"

        cases.append(
            {
                "uid": uid,
                "input": {
                    "example_id": row["example_id"],
                    "rhea_id": int(row["RHEA_ID"]),
                    "positive_rank": int(row["positive_rank"]),
                    "enzyme_score_text": row["ensemble_mean"],
                },
                "source_probe": {
                    "d5_mapping_state": row["mapping_state"],
                    "note": "D5 diagnostic provenance; not an M4a expected output field",
                },
                "expected": {
                    "uniprot": {
                        "primary_accession": uid,
                        "entry_type": uniprot["entryType"],
                        "reviewed": True,
                        "annotation_score": uniprot["annotationScore"],
                        "protein_existence": uniprot["proteinExistence"],
                        "scientific_organism_name": organism["scientificName"],
                        "ncbi_taxon_id": organism["taxonId"],
                        "lineage": organism["lineage"],
                        "raw_path": uniprot_relative,
                        "raw_sha256": uniprot_hash,
                    },
                    "kegg": {
                        "gene_ids": kegg_gene_ids,
                        "multiplicity": multiplicity,
                        "state": kegg_state,
                        "raw_path": kegg_relative,
                        "raw_sha256": kegg_hash,
                    },
                },
            }
        )

    fixture = {
        "fixture_version": "m4a2c_host_mapping_20260719_v1",
        "authority": {
            "teacher_reply": "TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md",
            "accepted_mt_d5_source_manifest_sha256": EXPECTED_SOURCE_MANIFEST_SHA256,
            "pinned_adrmats_commit": PINNED_ADRMATS_COMMIT,
        },
        "contract": {
            "uniprot_reviewed_primary": True,
            "trembl_included": False,
            "kegg_independent_supplement": True,
            "kegg_multiplicity_preserved": True,
            "taxonomy_key": "NCBI_taxon_ID",
            "organism_confidence_present": False,
            "abc_complete_formula_encoded": False,
        },
        "expected_summary": {
            "uid_count": 10,
            "uniprot_exact": 10,
            "uniprot_unreviewed": 0,
            "kegg_single": 7,
            "kegg_missing": 1,
            "kegg_multiple": 2,
        },
        "boundaries": [
            "ten fixed UIDs do not prove production-wide coverage",
            "missing KEGG is preserved as missing",
            "species evidence does not prove strain preservation",
            "host mapping is not wastewater suitability",
            "no confidence float or complete A/B/C formula is derived",
        ],
        "cases": cases,
    }
    output_root.mkdir(parents=True, exist_ok=True)
    fixture_path = output_root / "host_mapping_cases.json"
    fixture_path.write_text(
        json.dumps(fixture, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    write_fixture_manifest(output_root, copied_paths + ["host_mapping_cases.json"])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--output-root", required=True, type=Path)
    args = parser.parse_args()
    build(args.source_root, args.output_root)
    print("BUILT:M4A2C_HOST_MAPPING_FIXTURES")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
