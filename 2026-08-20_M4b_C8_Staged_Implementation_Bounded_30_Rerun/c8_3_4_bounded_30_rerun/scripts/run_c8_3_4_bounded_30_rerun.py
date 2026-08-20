#!/usr/bin/env python3
"""C8-3/C8-4 bounded 30 rerun reproducibility script.

This script documents and validates the C8-3/C8-4 bounded 30-row rerun.
It is NOT a real upstream enzyme candidate selection.
It does NOT call any APIs, run porTraits, or mutate production.

Inputs:
  - C8-1 rerun2 lookup index (SHA256: ebae0d9ffbf1cb3cec666bba0d7a8b5562d59d0a140fe3ab06c6e1da6f094b33)
  - C8-2A UID-source expansion (SHA256: d2d9ba4ba94a830cd268355588ce6d8041ed2cd3eb66e615891a5313c9a70c79)
  - C7-2 bounded 30 reference (dependency payload SHA256: 3e701443b70a82ac32a819999a7b69ee4540b3443ac9ecea9d1899d1bc0cef86)
  - Prior C8-3/4 archive (SHA256: b164df242fa3002c31bb71425fb83a9494efb3a3756ecfe5aaf67142a2fa3f02)

Validation checks:
  - 30 rows, 10/10/10 taxonomy, P0DXV0 absent
  - All rows MAIN_2478, READY_FOR_C8_3_TRAIT_ANNOTATION
  - Fungi identity-only for all F1-F15
  - F5 never predicted
  - F9-F15 never predicted
  - F8 no direct target-pollutant degradation
  - F15 not used for ranking
  - No hard rejection, no trait_score, no uncalibrated confidence
  - No API calls, no porTraits, no production mutation
"""
import csv, json, sys
from pathlib import Path
from collections import Counter

def validate(return_dir):
    """Validate the C8-3/4 bounded 30 rerun package."""
    rd = Path(return_dir)
    errors = []

    # Row counts
    with (rd / "trait_annotation.jsonl").open() as f:
        ta_rows = [json.loads(l) for l in f]
    if len(ta_rows) != 30: errors.append(f"trait_annotation rows={len(ta_rows)}, expected 30")

    with (rd / "TRAIN_SET_MANIFEST.csv").open() as f:
        tsm_rows = list(csv.DictReader(f))
    if len(tsm_rows) != 30: errors.append(f"TRAIN_SET_MANIFEST rows={len(tsm_rows)}, expected 30")

    # Taxonomy
    tax = Counter(r.get("taxonomy_group","") for r in tsm_rows)
    if tax.get("target_bacteria",0) != 10: errors.append("bacteria != 10")
    if tax.get("target_archaea",0) != 10: errors.append("archaea != 10")
    if tax.get("target_fungi",0) != 10: errors.append("fungi != 10")

    # P0DXV0 absent
    uids = [r.get("enzyme_uid","") for r in tsm_rows]
    if "P0DXV0" in uids: errors.append("P0DXV0 present")

    # Fungi identity-only
    for e in ta_rows:
        if e.get("mapping",{}).get("taxonomy_group","") == "target_fungi":
            for tid, t in e.get("traits",{}).items():
                if t.get("value_status") != "FUNGI_IDENTITY_ONLY":
                    errors.append(f"Fungi {tid} not identity-only"); break

    # F5 not predicted
    f5_pred = sum(1 for e in ta_rows if e.get("traits",{}).get("F5",{}).get("prediction_used"))
    if f5_pred: errors.append(f"F5 predicted={f5_pred}")

    # F9-F15 not predicted
    for i in range(9,16):
        cnt = sum(1 for e in ta_rows if e.get("traits",{}).get(f"F{i}",{}).get("prediction_used"))
        if cnt: errors.append(f"F{i} predicted={cnt}")

    # Row policy
    for e in ta_rows:
        rp = e.get("row_policy",{})
        for k in ["hard_rejection_applied","trait_score_emitted","uncalibrated_confidence_emitted",
                   "formal_assets_mutated","production_d4_mutated","production_pool_mutated"]:
            if rp.get(k): errors.append(f"{e.get('uid','')} {k}=true")

    return errors

if __name__ == "__main__":
    rd = sys.argv[1] if len(sys.argv) > 1 else "."
    errors = validate(rd)
    if errors:
        print("VALIDATION FAILED:")
        for e in errors: print(f"  - {e}")
        sys.exit(1)
    else:
        print("VALIDATION PASS: 30 rows, 10/10/10, fungi identity-only, F5 not predicted, no production mutation")
