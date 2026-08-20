# HPC executor-only prompt: M4b C8-3/C8-4 bounded 30 rerun

Date: 2026-08-20

Executor role: Chenyu/HPC executor only.

## Mission

Run a C8-labeled 30-row bounded rerun for C8-3/C8-4:

```text
fixed 2026-08-18 C7-2 bounded 30 subset
  + C8-1 lookup index
  + C8-2A UID-source expansion eligibility
  -> C8 trait_annotation.jsonl
  -> C8 TRAIN_SET_MANIFEST.csv
  -> C8 validation and boundary reports
```

Plain-language meaning:

```text
This is a 30-row smoke/validator rerun to prove the C8 implementation chain
preserves the already accepted C7-2 schema and teacher boundaries.
It is not a real upstream enzyme candidate selection.
It is not the final all-enzyme candidate pool.
It must not limit later full-library C8 coverage.
```

## Why This 30-Row Rerun Exists

Teacher 2026-08-19 explicitly requires:

```text
C8-5 must first use 30-row bounded rerun + small candidate-table smoke.
Teacher confirmation is required before full rollout.
```

The 2026-08-18 C7-2 bounded 30 package already passed as a read-only
schema/validator proof. This run must rerun the same fixed 30 rows under C8
labels and C8-1/C8-2A inputs, then prove the C8 implementation still obeys:

```text
observed first
predicted soft-fill only where authorized
F5 never predicted
fungi identity-only
main universe remains original 2,478 source_signature
137 rescued outside-universe sources stay delta review only
no production mutation
no hard rejection
no trait_score
no uncalibrated confidence
```

## Teacher Authority

Use the active teacher authority:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/00_Authority_Teacher_Plan/老师回复8.19.md
```

Relevant active decisions:

```text
C8 staged-only implementation is approved.
C8-0 through C8-4 may proceed.
C8-5 requires 30-row bounded rerun + small candidate-table smoke before full rollout.
Main denominator remains original 2,478 source_signature universe.
137 outside-universe rescued source_signatures are delta review only.
Do not merge the 137 delta sources into the 2,478 main universe.
porTraits is not started in C8 v1.
Fungi remain identity-only.
F5 is observed-only and must never be predicted.
F8 is broad degradation context only, not direct target-pollutant degradation.
F15 is background only and must not rank/filter/recommend.
No production D4 / production pool / formal asset mutation.
```

## Hard Boundaries

```text
READ / JOIN / ANNOTATE / VALIDATE / REPORT ONLY.
Do not call MetaTraits API.
Do not call BacDive API.
Do not run porTraits.
Do not run genome prediction.
Do not download data.
Do not read raw MetaTraits TSV gzip files.
Do not read raw BacDive cache JSON files.
Do not generate enzyme assets.
Do not run ESM/GVP/P2Rank/AlphaFill.
Do not edit production code.
Do not edit production data.
Do not write active_snapshot.json.
Do not connect to production D4 / production pool.
Do not mutate formal assets.
Do not hard reject organisms.
Do not output trait_score.
Do not output uncalibrated confidence.
Do not merge the 137 delta sources into the 2,478 main universe.
Do not generate trait rows for delta / NOT_MAPPED / asset-blocked rows.
Do not infer biological absence from missing evidence.
Do not create new trait IDs outside F1-F15.
Do not treat these 30 rows as real upstream enzyme candidates.
```

Allowed final statuses:

```text
C8_3_4_BOUNDED_30_RERUN_COMPLETE
BLOCKED_C8_3_4_BOUNDED_30_OUTPUT_PATH_EXISTS
BLOCKED_C8_3_4_BOUNDED_30_INPUT_MISSING_OR_SHA256_FAIL
BLOCKED_C8_3_4_BOUNDED_30_REFERENCE_INVALID
BLOCKED_C8_3_4_BOUNDED_30_C8_2A_ELIGIBILITY_FAILED
BLOCKED_C8_3_4_BOUNDED_30_TRAIT_POLICY_VALIDATION_FAILED
BLOCKED_C8_3_4_BOUNDED_30_BOUNDARY_VALIDATION_FAILED
```

Do not write COMPLETE unless all required validations pass.

## Fixed Chenyu Paths

Use these variables:

```bash
TASK_ID=enzymecage_m4b_c8_3_4_bounded_30_rerun_20260820
CHENYU_DATA_ROOT=/usrdata/EnzymeCAGE_data
PROJECT_ROOT=${CHENYU_DATA_ROOT}/EnzymeCAGE-master
ALT_PROJECT_ROOT=/root/projects/EnzymeCAGE-master
RETURN_ROOT=${PROJECT_ROOT}/HPC_Returned_Result_Summaries
ALT_RETURN_ROOT=${ALT_PROJECT_ROOT}/HPC_Returned_Result_Summaries
PROMPT_ROOT=${PROJECT_ROOT}/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/07_HPC_Prompts
ALT_PROMPT_ROOT=${ALT_PROJECT_ROOT}/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/07_HPC_Prompts
GITHUB_UPLOAD_ROOT=${PROJECT_ROOT}/custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables
ALT_GITHUB_UPLOAD_ROOT=${ALT_PROJECT_ROOT}/custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables
RETURN_DIR=${RETURN_ROOT}/${TASK_ID}
ARCHIVE=${RETURN_ROOT}/${TASK_ID}.tar.gz
IDENTITY=${RETURN_ROOT}/${TASK_ID}.tar.gz.identity.txt
WORK_ROOT=/tmp/${TASK_ID}
```

Fresh-run rule:

```text
If RETURN_DIR, ARCHIVE, IDENTITY, or WORK_ROOT already exists, do not overwrite,
delete, reuse, or repair it. Return a small blocked package with
FINAL_STATUS = BLOCKED_C8_3_4_BOUNDED_30_OUTPUT_PATH_EXISTS.
```

Allowed write locations:

```text
RETURN_DIR
WORK_ROOT
```

## Required Inputs

### Input 1: C8-1 lookup index + delta review rerun2 package

Required package:

```text
enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820
```

Expected archive SHA256:

```text
ebae0d9ffbf1cb3cec666bba0d7a8b5562d59d0a140fe3ab06c6e1da6f094b33
```

Search paths:

```text
${RETURN_ROOT}/enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820.tar.gz
${ALT_RETURN_ROOT}/enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820.tar.gz
./enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820.tar.gz
```

Required files after extraction:

```text
C8_METATRAITS_LOOKUP_INDEX.jsonl
C8_BACDIVE_AVAILABILITY_LOOKUP.csv
C8_LOOKUP_SOURCE_UNIVERSE.csv
C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW.csv
C8_METATRAITS_LOOKUP_INDEX_SUMMARY.csv
C8_LOOKUP_INDEX_VALIDATION_REPORT.json
C8_BOUNDARY_VALIDATION_REPORT.md
FINAL_STATUS.txt
MANIFEST.sha256
```

Validate:

```text
FINAL_STATUS = C8_1_LOOKUP_INDEX_AND_DELTA_REVIEW_RERUN2_REPACK_FIX_COMPLETE
C8_METATRAITS_LOOKUP_INDEX.jsonl rows = 37,170
C8_BACDIVE_AVAILABILITY_LOOKUP.csv data rows = 2,478
C8_LOOKUP_SOURCE_UNIVERSE.csv data rows = 2,478
C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW.csv data rows = 137
F1-F15 each have exactly 2,478 lookup rows
all 428 fungal F5 lookup rows are FUNGI_IDENTITY_ONLY
delta source_signature set does not intersect main 2,478 set
```

### Input 2: C8-2A bounded UID-source expansion package

Required package:

```text
enzymecage_m4b_c8_2a_bounded_uid_source_expansion_harness_20260820
```

Expected archive SHA256:

```text
d2d9ba4ba94a830cd268355588ce6d8041ed2cd3eb66e615891a5313c9a70c79
```

Search paths:

```text
${RETURN_ROOT}/enzymecage_m4b_c8_2a_bounded_uid_source_expansion_harness_20260820.tar.gz
${ALT_RETURN_ROOT}/enzymecage_m4b_c8_2a_bounded_uid_source_expansion_harness_20260820.tar.gz
./enzymecage_m4b_c8_2a_bounded_uid_source_expansion_harness_20260820.tar.gz
```

Required files after extraction:

```text
C8_UID_SOURCE_EXPANSION_TABLE.csv
C8_UID_SOURCE_EXPANSION_VALIDATION_REPORT.json
C8_BOUNDARY_VALIDATION_REPORT.md
FINAL_STATUS.txt
MANIFEST.sha256
```

Validate:

```text
FINAL_STATUS = C8_2A_BOUNDED_UID_SOURCE_EXPANSION_HARNESS_COMPLETE
C8_UID_SOURCE_EXPANSION_TABLE.csv data rows = 4,681
READY_FOR_C8_3_TRAIT_ANNOTATION rows = 753
MAIN_2478 eligible rows = 753
DELTA_137_PENDING_TEACHER_DECISION rows = 209
delta rows marked eligible = 0
no final trait_annotation.jsonl in C8-2A package
```

### Input 3: fixed 2026-08-18 C7-2 bounded 30 reference

Preferred existing path:

```text
${GITHUB_UPLOAD_ROOT}/2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/
${ALT_GITHUB_UPLOAD_ROOT}/2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/
```

Fallback dependency payload archive:

```text
enzymecage_m4b_c8_3_4_bounded_30_dependency_payload_20260820.tar.gz
```

Expected dependency payload SHA256:

```text
3e701443b70a82ac32a819999a7b69ee4540b3443ac9ecea9d1899d1bc0cef86
```

Search paths for fallback payload:

```text
${PROMPT_ROOT}/enzymecage_m4b_c8_3_4_bounded_30_dependency_payload_20260820.tar.gz
${ALT_PROMPT_ROOT}/enzymecage_m4b_c8_3_4_bounded_30_dependency_payload_20260820.tar.gz
${RETURN_ROOT}/enzymecage_m4b_c8_3_4_bounded_30_dependency_payload_20260820.tar.gz
${ALT_RETURN_ROOT}/enzymecage_m4b_c8_3_4_bounded_30_dependency_payload_20260820.tar.gz
./enzymecage_m4b_c8_3_4_bounded_30_dependency_payload_20260820.tar.gz
```

Inside fallback payload, use:

```text
inputs/c7_2_bounded_30_reference/
```

Required reference files:

```text
POLICY_MANIFEST.json
TRAIN_SET_MANIFEST.csv
trait_annotation.jsonl
TRAIT_FEATURE_ENCODING_VALIDATION_REPORT.md
BOUNDARY_VALIDATION_REPORT.md
FINAL_STATUS.txt
LOCAL_AUDIT_C7_2_SCHEMA_VALIDATOR_BOUNDED_30_2026-08-18.md
MANIFEST.sha256
```

Validate the reference:

```text
TRAIN_SET_MANIFEST.csv data rows = 30
trait_annotation.jsonl rows = 30
taxonomy distribution = 10 target_bacteria + 10 target_archaea + 10 target_fungi
P0DXV0 absent
all formal_assets_mutated = false
all production_pool_mutated = false
all production_d4_mutated = false
FINAL_STATUS contains PASS/COMPLETE for the C7-2 bounded 30 package
local audit result = PASS
```

If both the preferred reference path and fallback payload are missing, block
with `BLOCKED_C8_3_4_BOUNDED_30_INPUT_MISSING_OR_SHA256_FAIL`. Do not recreate
or reselect the 30 rows.

## Required Work

### Step 1: Resolve and validate all inputs

Write:

```text
C8_INPUT_PATH_RESOLUTION_TABLE.csv
COMMAND_LOG.txt
```

The path table must record every input path, selected path, SHA256 if available,
row counts, and validation status.

### Step 2: Build fixed 30-row C8 input table

Use the C7-2 reference `TRAIN_SET_MANIFEST.csv` as the only source of the 30
selected UID/source rows.

Create:

```text
C8_BOUNDED_30_INPUT_TABLE.csv
```

Required checks:

```text
row count = 30
unique enzyme_uid / UniprotID count = 30
unique sequence_sha256 count = 30
taxonomy distribution = 10 target_bacteria + 10 target_archaea + 10 target_fungi
P0DXV0 absent
```

Then join each row to C8-2A `C8_UID_SOURCE_EXPANSION_TABLE.csv` using:

```text
reference UniprotID == C8-2A enzyme_uid
reference source_signature == C8-2A source_signature
```

Every one of the 30 rows must satisfy:

```text
asset_consumable = true
asset_manifest_rows = 6
source_universe_class = MAIN_2478
inside_original_2478_universe = true
inside_c8_delta_137_review = false
c8_trait_annotation_eligible = true
expansion_status = READY_FOR_C8_3_TRAIT_ANNOTATION
formal_assets_mutated = false
production_pool_mutated = false
production_d4_mutated = false
```

If any row fails, block with:

```text
BLOCKED_C8_3_4_BOUNDED_30_C8_2A_ELIGIBILITY_FAILED
```

Do not replace failed rows.

### Step 3: Generate C8 TRAIN_SET_MANIFEST.csv

Create:

```text
TRAIN_SET_MANIFEST.csv
```

This is the C8-labeled manifest for the same fixed 30 rows.

Required columns include at minimum:

```text
enzyme_uid
taxonomy_group
source_signature
taxid
organism_name
strain_name_or_null
sequence_sha256
sequence_length
asset_consumable
asset_manifest_rows
loader_validation_status
dataset0_constructed
evidence_tier
formal_assets_mutated
production_pool_mutated
production_d4_mutated
source_universe_class
c8_trait_annotation_eligible
expansion_status
inclusion_status
exclusion_reason
source_reference_train_set_manifest
source_c8_2a_expansion_table
source_c8_1_lookup_index
```

All 30 rows must have:

```text
inclusion_status = INCLUDED_C8_BOUNDED_30_RERUN
exclusion_reason empty/null
```

### Step 4: Generate C8 POLICY_MANIFEST.json

Create:

```text
POLICY_MANIFEST.json
```

Required policy content:

```text
package_id = enzymecage_m4b_c8_3_4_bounded_30_rerun_20260820
scope = staged_only_c8_bounded_30_rerun
teacher_authorization_id = TEACHER_REPLY_8_19_C8_STAGED_ONLY_IMPLEMENTATION
trait_panel_id = M4B_C7_PANEL_FROZEN_2026_08_14
feature_encoding_contract = M4B_C7_2_FEATURE_ENCODING_PROPOSAL_2026-08-15
metatraits_mapping_contract = C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_RERUN2
main_source_universe_size = 2478
delta_rescued_source_review_size = 137
upstream_candidate_scope = bounded_30_schema_validator_rerun_not_real_candidate_selection
production_integration_enabled = false
hard_rejection_enabled = false
trait_score_enabled = false
uncalibrated_confidence_enabled = false
fungal_trait_policy = identity_only
allowed_predicted_soft_fill = F1,F2,F3,F4,F6,F7,F8
forbidden_predicted_soft_fill = F5,F9,F10,F11,F12,F13,F14,F15
```

Include SHA256/provenance for C8-1, C8-2A, and the 30-row reference.

### Step 5: Generate trait_annotation.jsonl

Create:

```text
trait_annotation.jsonl
```

One JSON object per fixed C8 bounded 30 row.

Each object must contain exactly four top-level sections:

```text
asset
mapping
traits
row_policy
```

Also include:

```text
enzyme_uid
sequence_sha256
package_id
bounded_rerun_scope_note
```

`bounded_rerun_scope_note` must clearly say this is not a real upstream enzyme
candidate table and not a final candidate pool.

For each row, `traits` must contain all and only:

```text
F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15
```

For every trait, keep these fields:

```text
trait_id
trait_name
display_layer
observed_value
predicted_value
resolved_display_value
value_status
evidence_type
prediction_used
observed_available
predicted_available
source_database
source_resolution
provenance
missing_reason
warnings
```

Use C8-1 lookup rows as the primary C8 trait source:

```text
C8_METATRAITS_LOOKUP_INDEX.jsonl for F1-F4/F6-F15 MetaTraits-derived status
C8_BACDIVE_AVAILABILITY_LOOKUP.csv for F5 BacDive availability status
```

Important value rule:

```text
Do not invent values that are not present in the C8-1 lookup index or BacDive
availability lookup. If the lookup provides preview/example fields rather than
full raw values, encode those as observed_value/predicted_value summaries and
write the provenance as c8_1_lookup_preview. Do not claim they are full raw
MetaTraits records.
```

For non-fungi:

```text
observed first
prediction_used may be true only for F1-F4/F6-F8 when observed is unavailable
and predicted_soft_fill_candidate_available is true
F5 prediction_used must always be false
F9-F15 prediction_used must always be false
missing evidence must be marked as missing, not biological absence
```

For fungi:

```text
all F1-F15 value_status = FUNGI_IDENTITY_ONLY
prediction_used = false
observed_available = false
predicted_available = false
source_database = identity_only
missing_reason = fungi_no_local_trait_source
```

F5 rule:

```text
F5 uses only C8_BACDIVE_AVAILABILITY_LOOKUP.csv.
F5 must never be predicted.
For fungi, F5 must be FUNGI_IDENTITY_ONLY.
For non-fungi without BacDive observed availability, mark missing/not observed;
do not infer unavailable strain.
```

F8 rule:

```text
F8 must be broad degradation-capacity context only.
Never write that the organism degrades the user's target pollutant.
Never use direct target-pollutant degradation language.
```

F15 rule:

```text
F15 is background/context only.
It must not rank, filter, recommend, or score.
```

### Step 6: Generate validator and boundary reports

Create:

```text
C8_VALIDATION_REPORT.json
C8_VALIDATION_REPORT.md
C8_BOUNDARY_VALIDATION_REPORT.md
```

Validation layers must include:

```text
asset validation
mapping validation
trait policy validation
boundary validation
```

Minimum required validation checks:

```text
trait_annotation rows = 30
TRAIN_SET_MANIFEST rows = 30
all 30 rows are C8-2A READY_FOR_C8_3_TRAIT_ANNOTATION
all 30 rows are MAIN_2478
0 delta rows included
0 NOT_MAPPED rows included
0 asset-blocked rows included
every trait_annotation row has asset/mapping/traits/row_policy
every row has exactly F1-F15
every F trait has all required fields
fungi rows have all F1-F15 FUNGI_IDENTITY_ONLY
F5 predicted rows = 0
F9-F15 predicted rows = 0
F8 direct target-pollutant degradation wording = 0
F15 ranking/filtering/recommendation wording = 0
hard_rejection_applied = false for all rows
trait_score emitted = false for all rows
uncalibrated_confidence emitted = false for all rows
formal_assets_mutated = false for all rows
production_pool_mutated = false for all rows
production_d4_mutated = false for all rows
no API calls
no porTraits
no genome prediction
no raw MetaTraits TSV read
no raw BacDive cache read
```

If any red-line check fails, final status must be blocked.

### Step 7: Generate consumption contract

Create:

```text
C8_TRAITFILTERLAYER_CONSUMPTION_CONTRACT.md
```

This must explain:

```text
This 30-row rerun is a C8 schema/validator smoke test only.
Future real C8 input must be the upstream enzyme candidate table with fields:
query_id / pollutant / reaction_candidate / enzyme_uid /
enzyme_candidate_source / rank.
Candidate UID without staged asset must fail closed as ASSET_NOT_AVAILABLE.
One UID with multiple source_signature mappings must keep multiple rows.
First screen displays F1-F5 priority fields.
Additional F6-F15 fields are kept for follow-up explanation.
Observed/predicted/missing/fungi identity-only must be explicitly labelled.
No trait may hard filter.
No trait_score or uncalibrated confidence may be used.
137 delta sources remain pending teacher decision and outside main C8.
```

### Step 8: Package

Required final files in `RETURN_DIR`:

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

Archive:

```text
${ARCHIVE}
${IDENTITY}
```

Identity sidecar must include:

```text
archive path
archive byte size
archive sha256
created UTC time
task_id
final status
primary input archive sha256 values
```

Do not include:

```text
raw MetaTraits TSV gzip
raw BacDive cache JSON
dependency payload tarball
__pycache__
.pyc
production files
formal asset files
```

## Final Response Required From Executor

Report only:

```text
FINAL_STATUS
RETURN_DIR
ARCHIVE
IDENTITY
archive sha256
row counts
validation pass/fail summary
any blockers
```

Do not summarize biological conclusions beyond the bounded rerun scope.
