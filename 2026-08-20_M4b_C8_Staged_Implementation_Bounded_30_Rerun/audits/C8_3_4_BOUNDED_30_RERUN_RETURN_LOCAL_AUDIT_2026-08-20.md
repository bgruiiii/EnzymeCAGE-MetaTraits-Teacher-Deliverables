# C8-3/C8-4 Bounded 30 Rerun Return Local Audit

Date: 2026-08-20

Audited archive:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/enzymecage_m4b_c8_3_4_bounded_30_rerun_20260820.tar.gz
```

Identity sidecar:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/enzymecage_m4b_c8_3_4_bounded_30_rerun_20260820.tar.gz.identity.txt
```

## Verdict

```text
LOCAL_AUDIT_VERDICT = PASS_CORE_C8_30_ROW_VALIDATION_BUT_REPACKAGE_REQUIRED
```

The scientific/schema core of the C8 bounded 30 rerun passes independent local
checks:

```text
fixed 30 C7-2 rows preserved
30/30 rows remain MAIN_2478 and READY_FOR_C8_3_TRAIT_ANNOTATION
10 bacteria + 10 archaea + 10 fungi
fungi remain identity-only
F5 not predicted
F9-F15 not predicted
F8 no direct target-pollutant degradation wording detected
F15 no ranking/filtering/recommendation wording detected
no production/formal mutation flags detected
```

However, the package is not yet teacher-ready because it missed a prompt-required
reproducibility file and did not record the dependency payload SHA256 in the
returned provenance. This should be fixed by a repack-only rerun, without
changing the 30 trait rows.

## Archive And Identity

| Check | Result |
|---|---|
| archive exists | PASS |
| identity sidecar exists | PASS |
| archive bytes | 21,903 |
| computed archive SHA256 | `b164df242fa3002c31bb71425fb83a9494efb3a3756ecfe5aaf67142a2fa3f02` |
| identity archive SHA256 | `b164df242fa3002c31bb71425fb83a9494efb3a3756ecfe5aaf67142a2fa3f02` |
| SHA256 match | PASS |
| single root | `enzymecage_m4b_c8_3_4_bounded_30_rerun_20260820` |
| `MANIFEST.sha256` check | PASS |
| `FINAL_STATUS.txt` | `C8_3_4_BOUNDED_30_RERUN_COMPLETE` |
| identity validation_pass | `True` |

## Returned Files

Present:

```text
POLICY_MANIFEST.json
TRAIN_SET_MANIFEST.csv
trait_annotation.jsonl
C8_BOUNDED_30_INPUT_TABLE.csv
C8_INPUT_PATH_RESOLUTION_TABLE.csv
C8_VALIDATION_REPORT.json
C8_VALIDATION_REPORT.md
C8_BOUNDARY_VALIDATION_REPORT.md
C8_TRAITFILTERLAYER_CONSUMPTION_CONTRACT.md
COMMAND_LOG.txt
FINAL_STATUS.txt
MANIFEST.files
MANIFEST.sha256
```

Missing prompt-required file:

```text
scripts/run_c8_3_4_bounded_30_rerun.py
```

This is a packaging/reproducibility defect. The prompt explicitly required this
script in the final package.

## Independent Row Checks

Independent parsing reproduced the expected row counts:

| File | Observed |
|---|---:|
| `TRAIN_SET_MANIFEST.csv` | 30 data rows + header |
| `C8_BOUNDED_30_INPUT_TABLE.csv` | 30 data rows + header |
| `trait_annotation.jsonl` | 30 rows |

Taxonomy distribution from `TRAIN_SET_MANIFEST.csv`:

```text
target_bacteria = 10
target_archaea = 10
target_fungi = 10
```

Other fixed-subset checks:

```text
unique trait_annotation enzyme_uid = 30
unique manifest enzyme_uid = 30
P0DXV0 absent
same enzyme_uid/source_signature pairs as 2026-08-18 C7-2 bounded 30 reference = true
```

## C8-2A Eligibility Checks

For all 30 rows:

```text
asset_consumable = true
asset_manifest_rows = 6
source_universe_class = MAIN_2478
c8_trait_annotation_eligible = true
expansion_status = READY_FOR_C8_3_TRAIT_ANNOTATION
formal_assets_mutated = false
production_pool_mutated = false
production_d4_mutated = false
```

No delta, NOT_MAPPED, or asset-blocked row was included.

## Trait JSONL Checks

Independent JSONL validation found:

```text
rows with asset/mapping/traits/row_policy sections = 30/30
rows with exactly F1-F15 = 30/30
F trait entries with missing required fields = 0
fungi rows = 10
fungi non-identity trait violations = 0
F5 prediction_used=true rows = 0
F9-F15 prediction_used=true rows = 0
row_policy red-line violations = 0
F8 suspicious direct target-pollutant degradation wording = 0
F15 suspicious ranking/filtering/recommendation wording = 0
```

The records also include a bounded scope note:

```text
This is a 30-row C8 schema/validator bounded rerun. It is not a real upstream
enzyme candidate table and not a final candidate pool.
```

This wording is correct and prevents the 30 rows from being mistaken for real
candidate enzyme selection.

## Input Provenance Checks

The package records the C8-1 and C8-2A SHA256 values correctly:

```text
C8-1 rerun2 archive = ebae0d9ffbf1cb3cec666bba0d7a8b5562d59d0a140fe3ab06c6e1da6f094b33
C8-2A archive = d2d9ba4ba94a830cd268355588ce6d8041ed2cd3eb66e615891a5313c9a70c79
```

But the package does not record the dependency payload SHA256:

```text
expected dependency payload SHA256 =
3e701443b70a82ac32a819999a7b69ee4540b3443ac9ecea9d1899d1bc0cef86
```

`C8_INPUT_PATH_RESOLUTION_TABLE.csv` records the C7-2 reference path but leaves
the SHA256 empty. `POLICY_MANIFEST.json` records the reference source path but
does not include the dependency payload SHA256. The identity sidecar also omits
it.

This is a provenance defect and should be fixed in the repack.

## Boundary Checks

Returned reports and independent checks support:

```text
staged-only
no MetaTraits API call
no BacDive API call
no porTraits run
no raw MetaTraits TSV read
no raw BacDive cache read
no production D4 mutation
no production pool mutation
no formal asset mutation
no hard rejection
no trait_score
no uncalibrated confidence
main denominator preserved at 2,478
137 delta not merged
fungi identity-only
F5 not predicted
F8 no direct target-pollutant degradation claim
F15 not used for ranking
```

## Required Fix

Recommended next action:

```text
Ask Chenyu for a repack-only fix.
Do not change the 30 selected rows.
Do not change trait values unless a validation bug is discovered.
Add scripts/run_c8_3_4_bounded_30_rerun.py to the package.
Add dependency payload SHA256 to POLICY_MANIFEST.json,
C8_INPUT_PATH_RESOLUTION_TABLE.csv, COMMAND_LOG.txt, and identity sidecar.
Regenerate MANIFEST.files, MANIFEST.sha256, archive, and identity.
```

Internal status:

```text
C8-3/C8-4 bounded 30 rerun core: PASS.
C8-3/C8-4 bounded 30 returned package: NOT YET TEACHER-READY until repack fix.
```
