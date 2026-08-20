# C8-3/C8-4 Bounded 30 Rerun Repack-Fix Return Local Audit

Date: 2026-08-20

Audited archive:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/enzymecage_m4b_c8_3_4_bounded_30_rerun_repack_fix_20260820.tar.gz
```

Identity sidecar:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/enzymecage_m4b_c8_3_4_bounded_30_rerun_repack_fix_20260820.tar.gz.identity.txt
```

## Verdict

```text
LOCAL_AUDIT_VERDICT = PASS_TEACHER_READY_C8_3_4_BOUNDED_30_RERUN_REPACK_FIX
```

The repack-fix resolves the two local-audit defects from the first return:

```text
1. scripts/run_c8_3_4_bounded_30_rerun.py is now present and runnable.
2. Dependency payload SHA256 is now recorded in POLICY_MANIFEST.json,
   C8_INPUT_PATH_RESOLUTION_TABLE.csv, COMMAND_LOG.txt, and identity sidecar.
```

The protected 30-row content was not changed.

Important scope boundary:

```text
This package is still only the C8-labeled 30-row bounded rerun / schema-validator
smoke. It is not a real upstream enzyme candidate table and not a final
candidate pool.
```

## Archive And Identity

| Check | Result |
|---|---|
| archive exists | PASS |
| identity sidecar exists | PASS |
| archive bytes | 23,521 |
| computed archive SHA256 | `a500c889b3345da21b6257e6a140d332e0f174b603eaadff51d454094b2d25d9` |
| identity archive SHA256 | `a500c889b3345da21b6257e6a140d332e0f174b603eaadff51d454094b2d25d9` |
| SHA256 match | PASS |
| single root | `enzymecage_m4b_c8_3_4_bounded_30_rerun_repack_fix_20260820` |
| `MANIFEST.sha256` check | PASS |
| final status | `C8_3_4_BOUNDED_30_RERUN_REPACK_FIX_COMPLETE` |
| protected file hash check | PASS |
| validation_pass | true |

Identity records:

```text
prior_c8_3_4_archive_sha256 =
b164df242fa3002c31bb71425fb83a9494efb3a3756ecfe5aaf67142a2fa3f02

c8_1_archive_sha256 =
ebae0d9ffbf1cb3cec666bba0d7a8b5562d59d0a140fe3ab06c6e1da6f094b33

c8_2a_archive_sha256 =
d2d9ba4ba94a830cd268355588ce6d8041ed2cd3eb66e615891a5313c9a70c79

c8_3_4_bounded_30_dependency_payload_sha256 =
3e701443b70a82ac32a819999a7b69ee4540b3443ac9ecea9d1899d1bc0cef86
```

## Returned Files

Expected files are present:

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
scripts/run_c8_3_4_bounded_30_rerun.py
```

No raw MetaTraits TSV gzip, raw BacDive cache JSON, dependency payload tarball,
`__pycache__`, or `.pyc` files were detected.

## Protected File Hash Comparison

Compared against the prior package
`enzymecage_m4b_c8_3_4_bounded_30_rerun_20260820`.

Protected files are byte-identical:

| File | SHA256 | Result |
|---|---|---|
| `TRAIN_SET_MANIFEST.csv` | `759ca4ae0c966a4ac9424f8fad292237d0b0aa74f898a59ac3752e7f12584e65` | PASS |
| `trait_annotation.jsonl` | `065cc22e5610f73f0b1ad50652bc212e220a5324007dac83846eab397b8582ad` | PASS |
| `C8_BOUNDED_30_INPUT_TABLE.csv` | `85949444212409a2ea2c56f8c54637fd73ef15f99712b5a71adf3b896e2bafa1` | PASS |
| `C8_VALIDATION_REPORT.json` | `e4d300fdd74c65eb6c5dd4dbf3e032dcf3f824eabb0a07ea46f516e2abec73f3` | PASS |
| `C8_VALIDATION_REPORT.md` | `e8652e5b5a56f45e4b3cb3731f0950e3fd642088ddb0bf08e0332ea92abfa727` | PASS |
| `C8_BOUNDARY_VALIDATION_REPORT.md` | `26a1730cf05609f0ad6314b2830d952814f18dcc5cf2471c2f418b3eedfe38dc` | PASS |
| `C8_TRAITFILTERLAYER_CONSUMPTION_CONTRACT.md` | `ff6a01fbe7452480fd90c00e55ba1cfd3d95003f5193987e255fa2a70990c252` | PASS |

This confirms the repack did not modify the fixed 30 selected rows or the
trait_annotation values.

## Row And Trait Checks

Independent parsing reproduced:

```text
TRAIN_SET_MANIFEST.csv data rows = 30
C8_BOUNDED_30_INPUT_TABLE.csv data rows = 30
trait_annotation.jsonl rows = 30
taxonomy distribution = 10 target_bacteria + 10 target_archaea + 10 target_fungi
```

Independent JSONL red-line checks:

```text
all rows have asset / mapping / traits / row_policy
all rows have exactly F1-F15
missing required F-trait fields = 0
fungi identity-only violations = 0
F5 prediction_used=true rows = 0
F9-F15 prediction_used=true rows = 0
row_policy red-line violations = 0
F8 suspicious direct target-pollutant degradation wording = 0
F15 suspicious ranking/filtering/recommendation wording = 0
```

Manifest-level checks:

```text
all 30 rows source_universe_class = MAIN_2478
all 30 rows c8_trait_annotation_eligible = true
all 30 rows expansion_status = READY_FOR_C8_3_TRAIT_ANNOTATION
all 30 rows asset_consumable = true
all 30 rows asset_manifest_rows = 6
all production/formal mutation flags = false
```

## Reproducibility Script

The added script:

```text
scripts/run_c8_3_4_bounded_30_rerun.py
```

is present and runnable:

```text
python3 scripts/run_c8_3_4_bounded_30_rerun.py .
```

returned:

```text
VALIDATION PASS: 30 rows, 10/10/10, fungi identity-only, F5 not predicted, no production mutation
```

The script documents the input package SHA256 values, the dependency payload
SHA256, the bounded-only scope, and the no-API/no-porTraits/no-production
boundary.

Minor non-blocking note:

```text
The script is a compact validation record. Its executable checks are lighter
than the full returned validation report and this local audit. The package-level
reports and independent audit still cover MAIN_2478, READY_FOR_C8_3, F8, and
F15 red lines.
```

## Provenance Fix Check

The dependency payload SHA256:

```text
3e701443b70a82ac32a819999a7b69ee4540b3443ac9ecea9d1899d1bc0cef86
```

is now present in:

```text
POLICY_MANIFEST.json
C8_INPUT_PATH_RESOLUTION_TABLE.csv
COMMAND_LOG.txt
identity sidecar
```

`C8_INPUT_PATH_RESOLUTION_TABLE.csv` also adds an explicit row for the prior
C8-3/C8-4 bounded 30 rerun archive:

```text
prior_c8_3_4_bounded_30_rerun_archive =
b164df242fa3002c31bb71425fb83a9494efb3a3756ecfe5aaf67142a2fa3f02
```

## Conclusion

This repack-fix package can be treated as the corrected teacher-ready
C8-3/C8-4 bounded 30 rerun evidence.

Recommended internal status:

```text
C8-3/C8-4 bounded 30 rerun: PASS after repack fix.
Ready for inclusion in the next microbe-side GitHub delivery batch.
```
