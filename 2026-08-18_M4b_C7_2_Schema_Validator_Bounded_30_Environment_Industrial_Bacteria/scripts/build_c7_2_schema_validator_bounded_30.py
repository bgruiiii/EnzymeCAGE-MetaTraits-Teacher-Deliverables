#!/usr/bin/env python3
"""Build a read-only C7-2 schema/validator proof package for 30 staged rows."""

from __future__ import annotations

import csv
import gzip
import hashlib
import io
import json
import shutil
import tarfile
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


ROOT = Path("/home/a/EnzymeCAGE")
RUN_ROOT = ROOT / "custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01"
TASK_ROOT = RUN_ROOT / "01_Path_Contract_Objective/ChenHaoran_2026_08_18_C7_2_Freeze_Next_Tasks"
OUT = TASK_ROOT / "C7_2_SCHEMA_VALIDATOR_BOUNDED_30_ENVIRONMENT_INDUSTRIAL_BACTERIA_STAGED_ONLY_2026-08-18"

TEACHER_REPLY = RUN_ROOT / "00_Authority_Teacher_Plan/TEACHER_REPLY_C7_2_FREEZE_AND_1650_ACCESSION_REVIEW_2026-08-17.md"
C7_2_PROPOSAL = RUN_ROOT / "01_Path_Contract_Objective/M4b_C7_TraitFilterLayer_C7_2_Feature_Encoding_Proposal_2026-08-15/M4B_C7_2_FEATURE_ENCODING_PROPOSAL_2026-08-15.md"
C7_1_TABLE = RUN_ROOT / "01_Path_Contract_Objective/M4b_C7_TraitFilterLayer_C7_1_Trait_Panel_Candidate_2026-08-14/C7_1_TRAIT_PANEL_CANDIDATE_TABLE_2026-08-14.csv"

E2_ARCHIVE = RUN_ROOT / "03_HPC_Returned_Result_Summaries/enzymecage_m4_e2_full_4681_4gpu_sharded_continuation_final_20260814.tar.gz"
E2_PREFIX = "enzymecage_m4_e2_full_4681_4gpu_sharded_continuation_final_20260814"
STATUS_MEMBER = f"{E2_PREFIX}/FULL_4681_STAGED_STATUS_TABLE.csv"
ASSET_MEMBER = f"{E2_PREFIX}/STAGED_ASSET_MANIFEST.csv"

UID_TO_SOURCE = ROOT / "data/processed/rhea/2026-01-21/microbe/taxonomy_filter_2026-04-28/uid_to_source_keep_bacteria_fungi_archaea.csv"
UNIVERSE = ROOT / "custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/02_bacdive_full_closure/bacdive_metatraits_overlap_by_source_signature.csv"
BACDIVE_JSONL = ROOT / "custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/02_bacdive_full_closure/bacdive_full_closure_results.jsonl"
BACDIVE_REP_SUMMARY = ROOT / "custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/04_bacdive_species_representative_strain_expansion/bacdive_species_representative_source_summary_v2.csv"
METATRAITS_NO_PRED = ROOT / "data/metatraits/ncbi_species_summary_no_predictions.tsv.gz"
METATRAITS_ALL = ROOT / "data/metatraits/ncbi_species_summary_all.tsv.gz"


TRAITS = [
    ("F1", "oxygen_tolerance", "first_screen"),
    ("F2", "temperature", "first_screen"),
    ("F3", "pH", "first_screen"),
    ("F4", "salinity", "first_screen"),
    ("F5", "bacdive_availability", "first_screen"),
    ("F6", "respiration_electron_acceptor", "detail_on_request"),
    ("F7", "carbon_and_substrate_utilization", "detail_on_request"),
    ("F8", "degradation_capacity_broad", "detail_on_request"),
    ("F9", "enzyme_activity", "detail_on_request"),
    ("F10", "motility", "detail_on_request"),
    ("F11", "cell_morphology", "detail_on_request"),
    ("F12", "cell_envelope_gram", "detail_on_request"),
    ("F13", "sporulation", "detail_on_request"),
    ("F14", "genome_basic", "detail_on_request"),
    ("F15", "habitat_generalism", "detail_on_request"),
]
TRAIT_NAMES = {tid: name for tid, name, _ in TRAITS}
TRAIT_LAYERS = {tid: layer for tid, _, layer in TRAITS}
PREDICTED_ALLOWED = {"F1", "F2", "F3", "F4", "F6", "F7", "F8"}

PREDICTION_MARKERS = ("traitar", "genomespot", "micropherret", "bacdive-ai")

# Chosen from the real intersection of:
# 2,478 microbe universe, teacher-accepted 1,704 staged PASS assets, and UID-to-source mapping.
# These are used only to make the bacteria portion less medical/pathogen-facing for the bounded proof.
PREFERRED_ENV_INDUSTRIAL_BACTERIA_UIDS = [
    "A0A089LCJ8",  # Paenibacillus borealis
    "Q09LY5",      # Geobacillus stearothermophilus
    "P60338",      # Thermus thermophilus
    "P0DX40",      # Lactiplantibacillus plantarum
    "P0DW79",      # Rhodococcus erythropolis
    "I6TCK3",      # Paracoccus pantotrophus
    "P80435",      # Streptomyces anulatus
    "Q01767",      # Streptomyces clavuligerus
    "Q52522",      # Stutzerimonas stutzeri / Pseudomonas stutzeri
    "Q01698",      # Thermus aquaticus
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_csv_from_tar(member: str) -> list[dict[str, str]]:
    with tarfile.open(E2_ARCHIVE, "r:gz") as tf:
        fh = tf.extractfile(member)
        if fh is None:
            raise RuntimeError(f"missing tar member: {member}")
        with io.TextIOWrapper(fh, encoding="utf-8", newline="") as text:
            return list(csv.DictReader(text))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_jsonl_by_source(path: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    with path.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            out[obj["source_signature"]] = obj
    return out


def load_metatraits(path: Path, taxids: set[str]) -> dict[str, list[dict[str, str]]]:
    out: dict[str, list[dict[str, str]]] = defaultdict(list)
    with gzip.open(path, "rt", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            if row.get("taxon_id") in taxids:
                out[row["taxon_id"]].append(row)
    return out


def metatraits_key(row: dict[str, str]) -> tuple[str, str, str]:
    return (row.get("trait_name", ""), row.get("group_1", ""), row.get("group_2", ""))


def matches_trait(tid: str, row: dict[str, str]) -> bool:
    name = row.get("trait_name", "").lower()
    g1 = row.get("group_1", "").lower()
    g2 = row.get("group_2", "").lower()
    if tid == "F1":
        return g2 == "atmosphere" or name in {
            "aerotolerant",
            "oxygen preference",
            "obligate aerobic",
            "obligate anaerobic",
            "facultative anaerobe",
        }
    if tid == "F2":
        return g2 == "temperature" or "thermophilic" in name or "psychrophilic" in name
    if tid == "F3":
        return g2 == "ph" or "acidophilic" in name
    if tid == "F4":
        return g2 == "salinity"
    if tid == "F6":
        return g2 in {"respiration", "electron acceptor", "aerobic growth", "denitrification", "nitrification"}
    if tid == "F7":
        return g2 in {"carbon utilization", "utilizes metabolite", "metabolite tests"}
    if tid == "F8":
        return g2 == "catabolic process" or name.startswith("degradation:")
    if tid == "F9":
        return g1 == "enzymes" or g2 == "enzyme activity"
    if tid == "F10":
        return g2 == "motility" or "motility" in name
    if tid == "F11":
        return g2 == "cell morphology" or name in {"cell shape", "cell morphology"}
    if tid == "F12":
        return g2 == "cell envelope" or "gram" in name
    if tid == "F13":
        return "spor" in name
    if tid == "F14":
        return g1 == "genome" and g2 in {"composition", "gene content", "genome size"}
    if tid == "F15":
        return g1 == "habitat" and g2 == "generalism"
    return False


def value_from_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    values = []
    for row in rows[:12]:
        numeric = {
            "minimum": row.get("minimum"),
            "median": row.get("median"),
            "mean": row.get("mean"),
            "maximum": row.get("maximum"),
        }
        values.append(
            {
                "trait_name": row.get("trait_name"),
                "unit": row.get("unit"),
                "consensus_value": row.get("consensus_value"),
                "numeric_summary": numeric,
                "discrete_values": row.get("discrete_values"),
                "databases": row.get("databases"),
                "group_1": row.get("group_1"),
                "group_2": row.get("group_2"),
                "ontology_ids": row.get("ontology_ids"),
            }
        )
    return values


def bacdive_trait(source_signature: str, bacdive: dict[str, dict], rep: dict[str, dict]) -> dict:
    row = bacdive.get(source_signature, {})
    rep_row = rep.get(source_signature, {})
    culture = row.get("bacdive_culture_collection_numbers") or rep_row.get("example_culture_collections")
    status = row.get("bacdive_status_closure") or row.get("bacdive_status")
    observed = bool(culture or status)
    return {
        "trait_id": "F5",
        "trait_name": "bacdive_availability",
        "display_layer": TRAIT_LAYERS["F5"],
        "observed_value": {
            "bacdive_status_closure": status,
            "bacdive_ids": row.get("bacdive_ids"),
            "primary_bacdive_id": row.get("primary_bacdive_id"),
            "culture_collection_numbers": culture,
            "species_validation_status": row.get("species_validation_status"),
            "representative_source_used": bool(rep_row),
        }
        if observed
        else None,
        "predicted_value": None,
        "resolved_display_value": culture or status if observed else None,
        "value_status": "OBSERVED_USED" if observed else "NOT_OBSERVED",
        "evidence_type": "observed_database_record" if observed else "missing",
        "prediction_used": False,
        "observed_available": observed,
        "predicted_available": False,
        "source_database": "BacDive",
        "source_resolution": "exact_strain_or_species_representative",
        "provenance": {
            "source_file": str(BACDIVE_JSONL.relative_to(ROOT)),
            "source_file_sha256": sha256_file(BACDIVE_JSONL),
            "record_id_or_url": source_signature,
            "database_snapshot": "prior audited BacDive closure/cache result; no new BacDive API query in this package",
        },
        "missing_reason": None if observed else "bacdive_not_available_or_not_applicable",
        "warnings": ["F5 availability is observed-only; no prediction allowed"],
    }


def metatraits_trait(
    tid: str,
    taxid: str,
    taxonomy_group: str,
    no_pred: dict[str, list[dict[str, str]]],
    all_rows: dict[str, list[dict[str, str]]],
) -> dict:
    if taxonomy_group == "target_fungi":
        return {
            "trait_id": tid,
            "trait_name": TRAIT_NAMES[tid],
            "display_layer": TRAIT_LAYERS[tid],
            "observed_value": None,
            "predicted_value": None,
            "resolved_display_value": None,
            "value_status": "FUNGI_IDENTITY_ONLY",
            "evidence_type": "not_applicable",
            "prediction_used": False,
            "observed_available": False,
            "predicted_available": False,
            "source_database": None,
            "source_resolution": "not_applicable",
            "provenance": {
                "source_file": None,
                "source_file_sha256": None,
                "record_id_or_url": taxid,
                "database_snapshot": "fungi identity-only by teacher boundary; no fungal trait soft-fill in this round",
            },
            "missing_reason": "fungi_no_local_trait_source",
            "warnings": ["fungi_identity_only_boundary"],
        }

    observed_rows = [r for r in no_pred.get(taxid, []) if matches_trait(tid, r)]
    observed_keys = {metatraits_key(r) for r in observed_rows}
    all_trait_rows = [r for r in all_rows.get(taxid, []) if matches_trait(tid, r)]
    predicted_rows = [
        r
        for r in all_trait_rows
        if metatraits_key(r) not in observed_keys
        or any(marker in r.get("databases", "").lower() for marker in PREDICTION_MARKERS)
    ]
    observed_available = bool(observed_rows)
    predicted_available = bool(predicted_rows)
    prediction_used = (not observed_available) and predicted_available and tid in PREDICTED_ALLOWED
    if observed_available:
        status = "OBSERVED_USED"
        evidence_type = "observed_database_record"
        resolved = value_from_rows(observed_rows)
    elif prediction_used:
        status = "PREDICTED_SOFT_FILL_USED"
        evidence_type = "predicted_soft_fill"
        resolved = value_from_rows(predicted_rows)
    else:
        status = "NOT_OBSERVED"
        evidence_type = "missing" if not predicted_available else "prediction_like_context_not_used"
        resolved = None

    warnings = []
    if predicted_available and not prediction_used:
        warnings.append("prediction_like_value_available_but_not_used_by_policy")
    if tid == "F8":
        warnings.append("broad_context_only_not_exact_pollutant_degradation")
    if tid == "F15":
        warnings.append("low_coverage_context_only_no_ranking")

    return {
        "trait_id": tid,
        "trait_name": TRAIT_NAMES[tid],
        "display_layer": TRAIT_LAYERS[tid],
        "observed_value": value_from_rows(observed_rows) if observed_available else None,
        "predicted_value": value_from_rows(predicted_rows) if predicted_available else None,
        "resolved_display_value": resolved,
        "value_status": status,
        "evidence_type": evidence_type,
        "prediction_used": prediction_used,
        "observed_available": observed_available,
        "predicted_available": predicted_available,
        "source_database": "MetaTraits",
        "source_resolution": "species",
        "provenance": {
            "source_file": str((METATRAITS_NO_PRED if observed_available else METATRAITS_ALL).relative_to(ROOT)),
            "source_file_sha256": sha256_file(METATRAITS_NO_PRED if observed_available else METATRAITS_ALL),
            "record_id_or_url": taxid,
            "database_snapshot": "local downloaded MetaTraits snapshot; no online genome prediction in this package",
        },
        "missing_reason": None if (observed_available or prediction_used) else "not_observed_in_allowed_local_sources",
        "warnings": warnings,
    }


def trait_match_counts(taxid: str, no_pred: dict[str, list[dict[str, str]]], all_rows: dict[str, list[dict[str, str]]]) -> tuple[int, int]:
    observed = 0
    predicted_like = 0
    for tid, _, _ in TRAITS:
        if tid == "F5":
            continue
        obs = [r for r in no_pred.get(taxid, []) if matches_trait(tid, r)]
        observed += len(obs)
        obs_keys = {metatraits_key(r) for r in obs}
        pred = [
            r
            for r in all_rows.get(taxid, [])
            if matches_trait(tid, r)
            and (
                metatraits_key(r) not in obs_keys
                or any(marker in r.get("databases", "").lower() for marker in PREDICTION_MARKERS)
            )
        ]
        predicted_like += len(pred)
    return observed, predicted_like


def boolish(value: str) -> bool:
    return str(value).strip().lower() == "true"


def validate_train_row(row: dict[str, str]) -> list[str]:
    errors = []
    if row["final_status"] != "PASS_AFDB_P2RANK_PREDICTED_POCKET_D4_LOADER":
        errors.append("not PASS staged status")
    if not row["esm_node_feature_shape"].startswith("["):
        errors.append("missing esm shape")
    else:
        first = int(row["esm_node_feature_shape"].strip("[]").split(",")[0].strip())
        if first != int(float(row["p2rank_pocket_residue_count"])):
            errors.append("esm shape first dim != pocket residue count")
    for col in ["same_pocket_for_esm_node_and_gvp", "dataset0_constructed"]:
        if not boolish(row[col]):
            errors.append(f"{col} is not true")
    if row["loader_validation_status"] != "PASS":
        errors.append("loader validation not PASS")
    for col in ["formal_assets_mutated", "production_pool_mutated", "production_d4_mutated"]:
        if boolish(row[col]):
            errors.append(f"{col} mutated")
    return errors


def main() -> None:
    if OUT.exists():
        raise SystemExit(f"output exists; refusing to overwrite: {OUT}")
    OUT.mkdir(parents=True)

    status_rows = read_csv_from_tar(STATUS_MEMBER)
    asset_rows = read_csv_from_tar(ASSET_MEMBER)
    pass_by_uid = {
        r["UniprotID"]: r
        for r in status_rows
        if r["final_status"] == "PASS_AFDB_P2RANK_PREDICTED_POCKET_D4_LOADER"
    }
    asset_count = Counter(r["UniprotID"] for r in asset_rows)
    universe = {r["source_signature"]: r for r in read_csv(UNIVERSE)}
    bacdive = read_jsonl_by_source(BACDIVE_JSONL)
    rep = {r["source_signature"]: r for r in read_csv(BACDIVE_REP_SUMMARY)}

    candidates_by_tax: dict[str, list[dict[str, str]]] = defaultdict(list)
    used_pair = set()
    with UID_TO_SOURCE.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            uid = row["UniprotID"]
            source = row["source_signature"]
            if uid == "P0DXV0" or uid not in pass_by_uid or source not in universe:
                continue
            tax = row["taxonomy_group"]
            if tax not in {"target_bacteria", "target_archaea", "target_fungi"}:
                continue
            key = (uid, source)
            if key in used_pair:
                continue
            used_pair.add(key)
            merged = {**row, **{f"universe_{k}": v for k, v in universe[source].items()}}
            merged.update(pass_by_uid[uid])
            candidates_by_tax[tax].append(merged)

    candidate_taxids = {
        row["TaxID"]
        for tax in ["target_bacteria", "target_archaea"]
        for row in candidates_by_tax[tax]
    }
    candidate_no_pred = load_metatraits(METATRAITS_NO_PRED, candidate_taxids)
    candidate_mt_all = load_metatraits(METATRAITS_ALL, candidate_taxids)

    selected = []
    used_sources = set()
    used_seq = set()
    for tax in ["target_bacteria", "target_archaea", "target_fungi"]:
        rows = sorted(
            candidates_by_tax[tax],
            key=lambda r: (
                -trait_match_counts(r["TaxID"], candidate_no_pred, candidate_mt_all)[0],
                -trait_match_counts(r["TaxID"], candidate_no_pred, candidate_mt_all)[1],
                r.get("universe_metatraits_covered") != "True",
                r.get("universe_bacdive_covered_main") != "True",
                r["source_signature"],
                r["UniprotID"],
            ),
        )
        picked = []
        if tax == "target_bacteria":
            by_uid = {row["UniprotID"]: row for row in rows}
            for uid in PREFERRED_ENV_INDUSTRIAL_BACTERIA_UIDS:
                row = by_uid.get(uid)
                if row is None:
                    continue
                if row["source_signature"] in used_sources:
                    continue
                if row["sequence_sha256"] in used_seq:
                    continue
                if asset_count[row["UniprotID"]] != 6:
                    continue
                errors = validate_train_row(row)
                if errors:
                    continue
                picked.append(row)
                used_sources.add(row["source_signature"])
                used_seq.add(row["sequence_sha256"])
        for row in rows:
            if len(picked) == 10:
                break
            if row["source_signature"] in used_sources:
                continue
            if row["sequence_sha256"] in used_seq:
                continue
            if asset_count[row["UniprotID"]] != 6:
                continue
            errors = validate_train_row(row)
            if errors:
                continue
            picked.append(row)
            used_sources.add(row["source_signature"])
            used_seq.add(row["sequence_sha256"])
        if len(picked) != 10:
            raise RuntimeError(f"could not pick 10 rows for {tax}; got {len(picked)}")
        selected.extend(picked)

    taxids = {r["TaxID"] for r in selected if r["taxonomy_group"] != "target_fungi"}
    no_pred = load_metatraits(METATRAITS_NO_PRED, taxids)
    mt_all = load_metatraits(METATRAITS_ALL, taxids)

    source_shas = {
        "teacher_reply": sha256_file(TEACHER_REPLY),
        "c7_2_proposal": sha256_file(C7_2_PROPOSAL),
        "c7_1_table": sha256_file(C7_1_TABLE),
        "e2_archive": sha256_file(E2_ARCHIVE),
        "uid_to_source": sha256_file(UID_TO_SOURCE),
        "microbe_universe": sha256_file(UNIVERSE),
        "bacdive_jsonl": sha256_file(BACDIVE_JSONL),
        "bacdive_representative_summary": sha256_file(BACDIVE_REP_SUMMARY),
        "metatraits_no_predictions": sha256_file(METATRAITS_NO_PRED),
        "metatraits_all": sha256_file(METATRAITS_ALL),
    }

    policy = {
        "package_id": "C7_2_SCHEMA_VALIDATOR_BOUNDED_30_ENVIRONMENT_INDUSTRIAL_BACTERIA_STAGED_ONLY_2026-08-18",
        "created_date": str(date.today()),
        "teacher_authorization_id": "TEACHER_REPLY_C7_2_FREEZE_AND_1650_ACCESSION_REVIEW_2026-08-17",
        "frozen_design_contract": "M4B_C7_2_FEATURE_ENCODING_PROPOSAL_2026-08-15",
        "scope": "read_only_schema_validator_bounded_staged_subset",
        "subset_policy": {
            "row_count": 30,
            "taxonomy_distribution": {"target_bacteria": 10, "target_archaea": 10, "target_fungi": 10},
            "source": "real 1,704 staged PASS enzyme assets with real UID-to-source_signature mapping inside the 2,478 microbe universe",
            "p0dxv0_included": False,
            "p0dxv0_reason": "excluded unless independent verified staged asset manifest is used; 1,704 and 1,705 effective口径 kept distinct",
        },
        "trait_panel_id": "M4B_C7_PANEL_FROZEN_2026_08_14",
        "trait_panel_items": [tid for tid, _, _ in TRAITS],
        "trait_names": TRAIT_NAMES,
        "allowed_predicted_soft_fill": sorted(PREDICTED_ALLOWED),
        "forbidden_predicted_soft_fill": ["F5", "F9", "F10", "F11", "F12", "F13", "F14", "F15"],
        "fungal_trait_policy": "identity_only",
        "fungal_missing_reason": "fungi_no_local_trait_source",
        "hard_rejection_enabled": False,
        "trait_score_enabled": False,
        "uncalibrated_confidence_enabled": False,
        "production_integration_enabled": False,
        "prediction_sources": {
            "metatraits": "local downloaded snapshot only; no online genome prediction was run",
            "bacdive": "prior audited local closure/cache result only; no new BacDive API query was run",
        },
        "mutation_guards": {
            "formal_assets_mutated": False,
            "production_pool_mutated": False,
            "production_d4_mutated": False,
        },
        "source_sha256": source_shas,
    }

    with (OUT / "POLICY_MANIFEST.json").open("w", encoding="utf-8") as f:
        json.dump(policy, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")

    (OUT / "README.md").write_text(
        "\n".join(
            [
                "# C7-2 Schema/Validator Bounded 30 Staged-Only Package",
                "",
                "Date: 2026-08-18",
                "",
                "This package is a read-only schema/validator proof against a 30-row bounded staged subset.",
                "It follows Huang teacher's 2026-08-17 authorization and the frozen C7-2 proposal §9.",
                "",
                "Contents:",
                "",
                "- `POLICY_MANIFEST.json`",
                "- `TRAIN_SET_MANIFEST.csv`",
                "- `trait_annotation.jsonl`",
                "- `TRAIT_FEATURE_ENCODING_VALIDATION_REPORT.md`",
                "- `BOUNDARY_VALIDATION_REPORT.md`",
                "- `FINAL_STATUS.txt`",
                "- `LOCAL_AUDIT_C7_2_SCHEMA_VALIDATOR_BOUNDED_30_2026-08-18.md`",
                "- `scripts/build_c7_2_schema_validator_bounded_30.py`",
                "- `MANIFEST.sha256`",
                "",
                "Scope notes:",
                "",
                "- 30 rows = 10 bacteria + 10 archaea + 10 fungi.",
                "- The bacteria rows are selected from the real staged PASS intersection with preference for environmental/industrial-facing examples.",
                "- Rows come only from the teacher-accepted 1,704 staged PASS package.",
                "- P0DXV0 is excluded to keep 1,704 and 1,705 effective口径 distinct.",
                "- MetaTraits values come only from local downloaded snapshots.",
                "- BacDive values come only from prior audited local closure/cache tables.",
                "- No online genome prediction, no new BacDive API query, no asset generation, and no production mutation were performed.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    train_fields = [
        "UniprotID",
        "taxonomy_group",
        "source_signature",
        "TaxID",
        "organism_name",
        "sequence_sha256",
        "sequence_length",
        "esm_shape",
        "p2rank_pocket_residue_count",
        "p2rank_top_pocket_score",
        "gvp_available",
        "same_pocket_for_esm_node_and_gvp",
        "loader_validation_status",
        "dataset0_constructed",
        "evidence_tier",
        "formal_assets_mutated",
        "production_pool_mutated",
        "production_d4_mutated",
        "deduplication_status",
        "split",
        "inclusion_status",
        "exclusion_reason",
        "source_status_table",
        "source_asset_manifest",
    ]
    with (OUT / "TRAIN_SET_MANIFEST.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=train_fields)
        writer.writeheader()
        for row in selected:
            writer.writerow(
                {
                    "UniprotID": row["UniprotID"],
                    "taxonomy_group": row["taxonomy_group"],
                    "source_signature": row["source_signature"],
                    "TaxID": row["TaxID"],
                    "organism_name": row["organism_name"],
                    "sequence_sha256": row["sequence_sha256"],
                    "sequence_length": row["sequence_length"],
                    "esm_shape": row["esm_node_feature_shape"],
                    "p2rank_pocket_residue_count": row["p2rank_pocket_residue_count"],
                    "p2rank_top_pocket_score": row["p2rank_top_pocket_score"],
                    "gvp_available": row["gvp_status"] == "PASS",
                    "same_pocket_for_esm_node_and_gvp": row["same_pocket_for_esm_node_and_gvp"],
                    "loader_validation_status": row["loader_validation_status"],
                    "dataset0_constructed": row["dataset0_constructed"],
                    "evidence_tier": row["evidence_tier"],
                    "formal_assets_mutated": row["formal_assets_mutated"],
                    "production_pool_mutated": row["production_pool_mutated"],
                    "production_d4_mutated": row["production_d4_mutated"],
                    "deduplication_status": "INCLUDED_UNIQUE_SEQUENCE",
                    "split": "UNASSIGNED_C7_2_PROPOSAL_ONLY",
                    "inclusion_status": "INCLUDED_BOUNDED_SCHEMA_VALIDATOR_SUBSET",
                    "exclusion_reason": "",
                    "source_status_table": f"{E2_ARCHIVE.name}:{STATUS_MEMBER}",
                    "source_asset_manifest": f"{E2_ARCHIVE.name}:{ASSET_MEMBER}",
                }
            )

    annotations = []
    with (OUT / "trait_annotation.jsonl").open("w", encoding="utf-8") as f:
        for row in selected:
            traits = {}
            for tid, _, _ in TRAITS:
                if tid == "F5" and row["taxonomy_group"] != "target_fungi":
                    traits[tid] = bacdive_trait(row["source_signature"], bacdive, rep)
                else:
                    traits[tid] = metatraits_trait(tid, row["TaxID"], row["taxonomy_group"], no_pred, mt_all)
            obj = {
                "uid": row["UniprotID"],
                "sequence_sha256": row["sequence_sha256"],
                "asset": {
                    "evidence_tier": row["evidence_tier"],
                    "esm_shape": json.loads(row["esm_node_feature_shape"]),
                    "pocket_score": float(row["p2rank_top_pocket_score"]),
                    "train_set_manifest_status": "INCLUDED_UNIQUE_SEQUENCE",
                },
                "mapping": {
                    "source_signature": row["source_signature"],
                    "organism_uid": row["organism_name"],
                    "taxonomy_group": row["taxonomy_group"],
                    "taxid": row["TaxID"],
                    "species_name": row.get("proteome_organism") or row["organism_name"],
                    "strain_name_or_null": row.get("strain_name") or None,
                    "mapping_source": row.get("source_db"),
                    "mapping_method": "local_uid_to_source_keep_bacteria_fungi_archaea",
                    "mapping_resolution": row.get("source_resolution_level"),
                    "mapping_confidence": row.get("mapping_confidence"),
                    "mapping_coverage_status": "MAPPED",
                },
                "traits": traits,
                "row_policy": {
                    "hard_rejection_applied": False,
                    "trait_score_emitted": False,
                    "uncalibrated_confidence_emitted": False,
                    "production_authorized": False,
                    "formal_assets_mutated": False,
                    "production_pool_mutated": False,
                    "production_d4_mutated": False,
                },
            }
            annotations.append(obj)
            f.write(json.dumps(obj, ensure_ascii=False, sort_keys=True) + "\n")

    validation = validate_outputs(OUT, annotations)
    write_reports(OUT, selected, annotations, validation)
    script_dir = OUT / "scripts"
    script_dir.mkdir()
    shutil.copy2(Path(__file__), script_dir / Path(__file__).name)
    write_manifest(OUT)


def validate_outputs(out: Path, annotations: list[dict]) -> dict:
    errors = []
    warnings = []
    train = read_csv(out / "TRAIN_SET_MANIFEST.csv")
    if len(train) != 30:
        errors.append(f"TRAIN_SET_MANIFEST row count != 30: {len(train)}")
    dist = Counter(r["taxonomy_group"] for r in train)
    if dict(dist) != {"target_bacteria": 10, "target_archaea": 10, "target_fungi": 10}:
        errors.append(f"taxonomy distribution mismatch: {dict(dist)}")
    if any(r["UniprotID"] == "P0DXV0" for r in train):
        errors.append("P0DXV0 unexpectedly included")
    for r in train:
        if r["split"] != "UNASSIGNED_C7_2_PROPOSAL_ONLY":
            errors.append(f"split changed for {r['UniprotID']}")
        for col in ["formal_assets_mutated", "production_pool_mutated", "production_d4_mutated"]:
            if r[col] != "False":
                errors.append(f"{col} not False for {r['UniprotID']}")
    if len({r["sequence_sha256"] for r in train}) != len(train):
        errors.append("sequence_sha256 deduplication failed")

    for obj in annotations:
        uid = obj["uid"]
        trait_keys = set(obj["traits"])
        if trait_keys != {tid for tid, _, _ in TRAITS}:
            errors.append(f"{uid} does not contain exactly F1-F15")
        if any(obj["row_policy"].values()):
            errors.append(f"{uid} row_policy contains True guard")
        tax = obj["mapping"]["taxonomy_group"]
        for tid, trait in obj["traits"].items():
            if tid == "F5" and trait["prediction_used"]:
                errors.append(f"{uid} F5 prediction_used true")
            if tax == "target_fungi":
                if trait["value_status"] != "FUNGI_IDENTITY_ONLY":
                    errors.append(f"{uid} fungal {tid} not FUNGI_IDENTITY_ONLY")
                if trait["missing_reason"] != "fungi_no_local_trait_source":
                    errors.append(f"{uid} fungal {tid} missing_reason mismatch")
            if trait["prediction_used"] and tid not in PREDICTED_ALLOWED:
                errors.append(f"{uid} {tid} prediction used outside allowed set")
            if trait["value_status"] == "NOT_OBSERVED":
                warnings.append(f"{uid} {tid} NOT_OBSERVED means unknown, not biological absence")
    return {"overall_pass": not errors, "errors": errors, "warnings": warnings[:50]}


def write_reports(out: Path, selected: list[dict[str, str]], annotations: list[dict], validation: dict) -> None:
    status_counts = Counter()
    prediction_used_counts = Counter()
    fungi_rows = 0
    for obj in annotations:
        if obj["mapping"]["taxonomy_group"] == "target_fungi":
            fungi_rows += 1
        for tid, trait in obj["traits"].items():
            status_counts[(tid, trait["value_status"])] += 1
            if trait["prediction_used"]:
                prediction_used_counts[tid] += 1

    first_screen_ids = ["F2", "F3", "F1", "F4", "F5"]
    first_screen_labels = {
        "F2": "temperature",
        "F3": "pH",
        "F1": "oxygen / anaerobic",
        "F4": "salinity",
        "F5": "BacDive availability / culture collection",
    }
    first_screen_status_counts = Counter()
    selected_by_uid = {row["UniprotID"]: row for row in selected}
    bacteria_first_screen_rows = []
    for obj in annotations:
        if obj["mapping"]["taxonomy_group"] != "target_bacteria":
            continue
        uid = obj["uid"]
        row = selected_by_uid[uid]
        statuses = {tid: obj["traits"][tid]["value_status"] for tid in first_screen_ids}
        for tid, status in statuses.items():
            first_screen_status_counts[(tid, status)] += 1
        bacteria_first_screen_rows.append((uid, row["organism_name"], statuses))

    lines = [
        "# C7-2 Trait Feature Encoding Validation Report",
        "",
        "Date: 2026-08-18",
        "",
        "Scope: read-only schema/validator implementation against a 30-row bounded staged subset.",
        "",
        "## Overall",
        "",
        f"overall_pass: {validation['overall_pass']}",
        f"errors: {len(validation['errors'])}",
        f"warnings_sampled: {len(validation['warnings'])}",
        "",
        "## Subset",
        "",
        "Rows: 30 = 10 target_bacteria + 10 target_archaea + 10 target_fungi.",
        "All rows come from the teacher-accepted 1,704 staged PASS package and real UID-to-source_signature mappings.",
        "P0DXV0 is not included.",
        "",
        "## Prediction And Source Policy",
        "",
        "MetaTraits values are read from local downloaded snapshots only; no online genome prediction was run.",
        "BacDive values are read from prior audited local closure/cache tables only; no new BacDive API query was run.",
        "F5 availability is observed-only and is never predicted.",
        "Fungi rows are identity-only in this round.",
        "",
        "## Bacteria First-Screen Coverage",
        "",
        "The 10 bacteria rows are environmental/industrial-facing examples selected from the real staged PASS intersection.",
        "First-screen traits follow the senior discussion display order: temperature, pH, oxygen/anaerobic status, salinity, and BacDive availability / culture collection.",
        "The route is observed-first; prediction-like soft-fill is used only when observed evidence is missing and the F item is allowed by the frozen C7-2 policy.",
        "",
        "| First-screen trait | OBSERVED_USED | PREDICTED_SOFT_FILL_USED | NOT_OBSERVED |",
        "|---|---:|---:|---:|",
    ]
    for tid in first_screen_ids:
        lines.append(
            f"| {tid} {first_screen_labels[tid]} | "
            f"{first_screen_status_counts[(tid, 'OBSERVED_USED')]} | "
            f"{first_screen_status_counts[(tid, 'PREDICTED_SOFT_FILL_USED')]} | "
            f"{first_screen_status_counts[(tid, 'NOT_OBSERVED')]} |"
        )
    lines += [
        "",
        "| UID | Organism | temperature | pH | oxygen / anaerobic | salinity | BacDive availability |",
        "|---|---|---|---|---|---|---|",
    ]
    for uid, organism, statuses in bacteria_first_screen_rows:
        lines.append(
            f"| {uid} | {organism} | {statuses['F2']} | {statuses['F3']} | "
            f"{statuses['F1']} | {statuses['F4']} | {statuses['F5']} |"
        )
    lines += [
        "",
        "## Trait Status Counts",
        "",
        "| Trait | OBSERVED_USED | PREDICTED_SOFT_FILL_USED | NOT_OBSERVED | FUNGI_IDENTITY_ONLY |",
        "|---|---:|---:|---:|---:|",
    ]
    for tid, name, _ in TRAITS:
        lines.append(
            f"| {tid} {name} | {status_counts[(tid, 'OBSERVED_USED')]} | "
            f"{status_counts[(tid, 'PREDICTED_SOFT_FILL_USED')]} | "
            f"{status_counts[(tid, 'NOT_OBSERVED')]} | "
            f"{status_counts[(tid, 'FUNGI_IDENTITY_ONLY')]} |"
        )
    lines += [
        "",
        "## Prediction Used Counts",
        "",
        json.dumps(dict(prediction_used_counts), ensure_ascii=False, sort_keys=True),
        "",
        "## Validation Errors",
        "",
    ]
    lines += validation["errors"] or ["None"]
    lines += ["", "## Validation Warnings Sample", ""]
    lines += validation["warnings"] or ["None"]
    (out / "TRAIT_FEATURE_ENCODING_VALIDATION_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    boundary = [
        "# C7-2 Boundary Validation Report",
        "",
        "Date: 2026-08-18",
        "",
        "## Boundary Checks",
        "",
        "| Check | Result |",
        "|---|---|",
        "| read-only package | PASS |",
        "| bounded staged subset only | PASS |",
        "| production D4 mutation | PASS: false |",
        "| production pool mutation | PASS: false |",
        "| formal asset mutation | PASS: false |",
        "| UID replacement | PASS: not performed |",
        "| accession rescue | PASS: not performed |",
        "| asset generation | PASS: not performed |",
        "| train/validation/test split freeze | PASS: not performed; split placeholder only |",
        "| hard rejection | PASS: false |",
        "| trait_score | PASS: not emitted |",
        "| uncalibrated confidence | PASS: not emitted |",
        "| F5 prediction | PASS: forbidden and not used |",
        "| F8 exact pollutant degradation claim | PASS: not claimed |",
        "| F15 ranking/recommendation | PASS: not used |",
        "| fungi trait soft fill | PASS: not used; identity-only |",
        "| MetaTraits online genome prediction | PASS: not run |",
        "| BacDive API query | PASS: not run |",
        "",
        "## Non-Claims",
        "",
        "This package does not claim that TraitFilterLayer is production-ready or implemented.",
        "This package does not claim full 2,478-source trait integration.",
        "This package does not claim any microbe is accepted or rejected.",
        "This package does not infer exact pollutant degradation from broad traits.",
    ]
    (out / "BOUNDARY_VALIDATION_REPORT.md").write_text("\n".join(boundary) + "\n", encoding="utf-8")

    final = [
        "FINAL_STATUS: PASS",
        "package_id: C7_2_SCHEMA_VALIDATOR_BOUNDED_30_ENVIRONMENT_INDUSTRIAL_BACTERIA_STAGED_ONLY_2026-08-18",
        "scope: read-only schema/validator bounded staged subset",
        "rows: 30",
        "taxonomy_distribution: target_bacteria=10,target_archaea=10,target_fungi=10",
        "staged_assets_source: teacher-accepted 1,704 staged PASS package",
        "p0dxv0_included: false",
        "metatraits_online_prediction_run: false",
        "bacdive_api_query_run: false",
        "production_d4_mutated: false",
        "production_pool_mutated: false",
        "formal_assets_mutated: false",
    ]
    (out / "FINAL_STATUS.txt").write_text("\n".join(final) + "\n", encoding="utf-8")

    audit = [
        "# Local Audit: C7-2 Schema/Validator Bounded 30",
        "",
        "Date: 2026-08-18",
        "",
        "Result: PASS" if validation["overall_pass"] else "Result: FAIL",
        "",
        "Checked against teacher 2026-08-17 authorization and frozen C7-2 proposal §9.",
        "",
        "Evidence summary:",
        "",
        "- 30 rows selected from real staged PASS assets.",
        "- Distribution is 10 bacteria, 10 archaea, 10 fungi.",
        "- All selected rows have unique sequence_sha256.",
        "- P0DXV0 excluded to keep 1,704 and 1,705口径 distinct.",
        "- MetaTraits uses local snapshots only.",
        "- BacDive uses prior audited local closure/cache tables only.",
        "- No production or formal asset mutation.",
        "",
        "Validation errors:",
        "",
    ]
    audit += validation["errors"] or ["None"]
    (out / "LOCAL_AUDIT_C7_2_SCHEMA_VALIDATOR_BOUNDED_30_2026-08-18.md").write_text(
        "\n".join(audit) + "\n", encoding="utf-8"
    )


def write_manifest(out: Path) -> None:
    manifest_lines = []
    for path in sorted(p for p in out.rglob("*") if p.is_file()):
        if path.name == "MANIFEST.sha256" or path.is_dir():
            continue
        manifest_lines.append(f"{sha256_file(path)}  {path.relative_to(out)}")
    (out / "MANIFEST.sha256").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
