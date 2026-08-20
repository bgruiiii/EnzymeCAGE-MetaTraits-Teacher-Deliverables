# C8-3/C8-4 Bounded 30 Rerun Prompt Local Audit

Date: 2026-08-20

Audited prompt:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/07_HPC_Prompts/HPC_ENZYMECAGE_M4B_C8_3_4_BOUNDED_30_RERUN_EXECUTOR_ONLY_PROMPT_2026-08-20.md
```

Dependency payload:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/07_HPC_Prompts/enzymecage_m4b_c8_3_4_bounded_30_dependency_payload_20260820.tar.gz
```

Dependency payload SHA256:

```text
3e701443b70a82ac32a819999a7b69ee4540b3443ac9ecea9d1899d1bc0cef86
```

## Verdict

```text
LOCAL_AUDIT_VERDICT = PASS_READY_TO_SEND_TO_CHENYU
```

## Scope Check

The prompt correctly defines this run as:

```text
C8-labeled 30-row bounded rerun / schema-validator smoke only.
Not a real upstream enzyme candidate selection.
Not the final all-enzyme candidate pool.
Not a future full-library coverage limit.
```

This addresses the prior scope risk from the superseded 753-row draft.

## Required Inputs

The prompt requires:

```text
1. C8-1 lookup index + delta review rerun2 package
2. C8-2A bounded UID-source expansion harness package
3. fixed 2026-08-18 C7-2 bounded 30 reference
```

It includes exact SHA256 checks for:

```text
C8-1 archive = ebae0d9ffbf1cb3cec666bba0d7a8b5562d59d0a140fe3ab06c6e1da6f094b33
C8-2A archive = d2d9ba4ba94a830cd268355588ce6d8041ed2cd3eb66e615891a5313c9a70c79
C8-3/4 bounded 30 dependency payload = 3e701443b70a82ac32a819999a7b69ee4540b3443ac9ecea9d1899d1bc0cef86
```

The dependency payload was created only to carry the already uploaded 2026-08-18
C7-2 bounded 30 reference files, so Chenyu does not need to guess old GitHub
upload paths.

## Boundary Check

The prompt forbids:

```text
MetaTraits API
BacDive API
porTraits
genome prediction
raw MetaTraits TSV gzip reads
raw BacDive cache JSON reads
ESM/GVP/P2Rank/AlphaFill execution
production D4 / production pool / formal asset mutation
hard rejection
trait_score
uncalibrated confidence
delta merge into the 2,478 main universe
```

It requires the output to keep:

```text
main universe = original 2,478 source_signature
137 rescued outside-universe sources = delta review only
fungi = identity-only
F5 = never predicted
F8 = broad context only, not direct target-pollutant degradation
F15 = background only, not ranking/filtering/recommendation
```

## 30-Row Eligibility Check

The prompt requires the executor to use the fixed C7-2 `TRAIN_SET_MANIFEST.csv`
as the only source of the 30 rows.

It explicitly forbids replacing failed rows.

Each fixed 30-row item must be joined to C8-2A and satisfy:

```text
asset_consumable = true
asset_manifest_rows = 6
source_universe_class = MAIN_2478
inside_original_2478_universe = true
inside_c8_delta_137_review = false
c8_trait_annotation_eligible = true
expansion_status = READY_FOR_C8_3_TRAIT_ANNOTATION
no production/formal mutation
```

If any fixed row fails, the executor must block rather than silently selecting
a replacement.

## Output Check

The prompt requires the C8 package to contain:

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

The prompt also requires archive and identity sidecar generation.

## Local Payload Verification

The dependency payload source directory manifest was verified locally:

```text
sha256sum -c MANIFEST.sha256 = PASS
TRAIN_SET_MANIFEST.csv = 30 data rows + header
trait_annotation.jsonl = 30 rows
```

## Residual Risk

The C8-1 lookup index contains lookup/status/preview fields, not the full raw
MetaTraits TSV records. The prompt therefore instructs the executor not to
invent full raw values and to label lookup-derived summaries as
`c8_1_lookup_preview` when necessary.

This is acceptable for this bounded C8 rerun because teacher's current requested
gate is schema/validator smoke plus boundary validation, not full production
trait activation.
