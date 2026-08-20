# HPC executor-only prompt: M4b C8-2 UID-to-source expansion staged-only

Date: 2026-08-20

Executor role: Chenyu/HPC executor only.

## Mission

Implement C8-2A as a read-only staged derivation / harness check:

```text
enzyme_uid candidate table -> microbe source_signature expansion
```

This step does **not** generate trait values. It does not create final
`trait_annotation.jsonl`. It only records which UID candidates can proceed to
C8-3 and why other candidates cannot proceed.

Important scope boundary:

```text
This run is NOT the final all-enzyme candidate pool.
This run is NOT the future full-library enzyme source.
This run is a bounded/staged implementation harness that uses teacher-accepted
M4 E2 staged status rows to validate the C8-2 schema, joins, boundary handling,
and downstream C8-3 readiness logic.
```

Future production/all-library use:

```text
Later, when the upstream enzyme candidate table is frozen, C8-2 must accept that
larger/full-library candidate table through the same schema:
query_id / pollutant / reaction_candidate / enzyme_uid / candidate source / rank.
This 4,681-row harness must not be used to limit future enzyme coverage.
```

Use the currently teacher-accepted M4 E2 staged status table as the bounded C8-2A
test input because no upstream pollutant/reaction enzyme candidate table is yet
frozen for C8. That means:

```text
bounded C8-2A test candidate table = FULL_4681_STAGED_STATUS_TABLE.csv
bounded test candidate rows = 4,681
PASS consumable enzyme assets = 1,704
blocked/non-consumable enzyme assets = 2,977
```

## Teacher Authority

Use teacher authority:

```text
老师回复8.19.md
```

Relevant decisions:

```text
C8 staged-only implementation is approved.
C8-0 through C8-4 may proceed before C8-5 bounded smoke.
Main microbe denominator remains original 2,478 source_signature universe.
137 outside-universe rescued source_signatures are delta review only.
Do not merge the 137 delta sources into the 2,478 main universe.
porTraits is not started in C8 v1.
Fungi remain identity-only.
No hard rejection, no trait_score, no uncalibrated confidence.
No production D4 / production pool / formal asset mutation.
```

## Hard Boundaries

```text
READ / JOIN / REPORT ONLY.
Do not call MetaTraits API.
Do not call BacDive API.
Do not run porTraits.
Do not run genome prediction.
Do not download data.
Do not read raw MetaTraits TSV gzip files in this step.
Do not generate trait_annotation.jsonl.
Do not generate trait values.
Do not edit production code.
Do not edit production data.
Do not write active_snapshot.json.
Do not connect to production D4 / production pool.
Do not mutate formal assets.
Do not hard reject organisms.
Do not output trait_score.
Do not output uncalibrated confidence.
Do not merge the 137 delta sources into the 2,478 main universe.
```

Allowed final statuses:

```text
C8_2A_BOUNDED_UID_SOURCE_EXPANSION_HARNESS_COMPLETE
BLOCKED_C8_2A_INPUT_MISSING_OR_SHA256_FAIL
BLOCKED_C8_2A_ROW_COUNT_VALIDATION_FAILED
BLOCKED_C8_2A_MAIN_DELTA_BOUNDARY_FAILED
BLOCKED_C8_2A_OUTPUT_PATH_EXISTS
BLOCKED_C8_2A_BOUNDARY_VALIDATION_FAILED
```

Do not write COMPLETE unless all validations pass.

## Fixed Chenyu Paths

Use these variables:

```bash
TASK_ID=enzymecage_m4b_c8_2a_bounded_uid_source_expansion_harness_20260820
CHENYU_DATA_ROOT=/usrdata/EnzymeCAGE_data
PROJECT_ROOT=${CHENYU_DATA_ROOT}/EnzymeCAGE-master
ALT_PROJECT_ROOT=/root/projects/EnzymeCAGE-master
RETURN_ROOT=${PROJECT_ROOT}/HPC_Returned_Result_Summaries
ALT_RETURN_ROOT=${ALT_PROJECT_ROOT}/HPC_Returned_Result_Summaries
RETURN_DIR=${RETURN_ROOT}/${TASK_ID}
ARCHIVE=${RETURN_ROOT}/${TASK_ID}.tar.gz
IDENTITY=${RETURN_ROOT}/${TASK_ID}.tar.gz.identity.txt
WORK_ROOT=/tmp/${TASK_ID}
```

Fresh-run rule:

```text
If RETURN_DIR, ARCHIVE, IDENTITY, or WORK_ROOT already exists, do not overwrite,
delete, reuse, or repair it. Return a small blocked package with
FINAL_STATUS = BLOCKED_C8_2A_OUTPUT_PATH_EXISTS.
```

Allowed write locations:

```text
RETURN_DIR
WORK_ROOT
```

## Required Inputs

### 1. Full 4,681 staged status package

Required archive or directory:

```text
enzymecage_m4_e2_full_4681_4gpu_sharded_continuation_final_20260814
```

Expected archive SHA256:

```text
b01e717139f6eb48739e0861f82b339cdc0132ee4777acdd18354ee9da38bdd4
```

Search for archive:

```text
${RETURN_ROOT}/enzymecage_m4_e2_full_4681_4gpu_sharded_continuation_final_20260814.tar.gz
${ALT_RETURN_ROOT}/enzymecage_m4_e2_full_4681_4gpu_sharded_continuation_final_20260814.tar.gz
./enzymecage_m4_e2_full_4681_4gpu_sharded_continuation_final_20260814.tar.gz
```

Search for existing extracted directory:

```text
${RETURN_ROOT}/enzymecage_m4_e2_full_4681_4gpu_sharded_continuation_final_20260814/
${ALT_RETURN_ROOT}/enzymecage_m4_e2_full_4681_4gpu_sharded_continuation_final_20260814/
```

Required files:

```text
FULL_4681_STAGED_STATUS_TABLE.csv
STAGED_ASSET_MANIFEST.csv
FORMAL_ASSET_MUTATION_CHECK.json
PRODUCTION_MUTATION_CHECK.json
FINAL_STATUS.txt
```

Validate:

```text
FULL_4681_STAGED_STATUS_TABLE.csv data rows = 4,681
final_status counts:
  PASS_AFDB_P2RANK_PREDICTED_POCKET_D4_LOADER = 1,704
  BLOCKED_AFDB_P2RANK_NO_POCKET = 1,324
  BLOCKED_AFDB_STRUCTURE_FETCH_FAILED = 1,650
  BLOCKED_ESM2_3B_EXTRACTION_FAILED = 3
formal_assets_mutated = False for all 4,681 rows
production_pool_mutated = False for all 4,681 rows
production_d4_mutated = False for all 4,681 rows
STAGED_ASSET_MANIFEST.csv data rows = 10,224
STAGED_ASSET_MANIFEST unique UniprotID = 1,704
Each PASS UID has exactly 6 staged asset manifest rows.
Each non-PASS UID has 0 staged asset manifest rows.
```

### 2. C8-1 rerun2 lookup index + delta review package

Required archive or directory:

```text
enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820
```

Expected archive SHA256:

```text
ebae0d9ffbf1cb3cec666bba0d7a8b5562d59d0a140fe3ab06c6e1da6f094b33
```

Search for archive:

```text
${RETURN_ROOT}/enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820.tar.gz
${ALT_RETURN_ROOT}/enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820.tar.gz
./enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820.tar.gz
```

Required files:

```text
C8_LOOKUP_SOURCE_UNIVERSE.csv
C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW.csv
C8_LOOKUP_INDEX_VALIDATION_REPORT.json
C8_BOUNDARY_VALIDATION_REPORT.md
FINAL_STATUS.txt
MANIFEST.sha256
```

Validate:

```text
FINAL_STATUS.txt = C8_1_LOOKUP_INDEX_AND_DELTA_REVIEW_RERUN2_REPACK_FIX_COMPLETE
MANIFEST.sha256 check PASS if archive/directory includes it
C8_LOOKUP_SOURCE_UNIVERSE.csv data rows = 2,478
C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW.csv data rows = 137
delta taxonomy counts = 88 target_bacteria / 6 target_archaea / 43 target_fungi
delta recommended_status = PENDING_TEACHER_DECISION for all rows
delta ∩ main = 0
```

Use C8-1 outputs only to determine:

```text
inside_original_2478_universe
inside_c8_delta_137_review
metatraits_covered
bacdive_covered_main
overlap_bin_main
delta recommended_status
```

Do not read `C8_METATRAITS_LOOKUP_INDEX.jsonl` in this step unless needed only
to verify the C8-1 package identity. C8-2 does not assign trait values.

### 3. C8-1 dependency payload for UID-to-source mapping

Required archive:

```text
enzymecage_m4b_c8_1_dependency_payload_20260820.tar.gz
```

Expected archive SHA256:

```text
426b7b7933a5f98163c654df9a717d55924a62d36df9c6099a8819c4f417664e
```

Search paths:

```text
${PROJECT_ROOT}/HPC_Inputs/enzymecage_m4b_c8_1_dependency_payload_20260820.tar.gz
${ALT_PROJECT_ROOT}/HPC_Inputs/enzymecage_m4b_c8_1_dependency_payload_20260820.tar.gz
${PROJECT_ROOT}/HPC_Prompts/enzymecage_m4b_c8_1_dependency_payload_20260820.tar.gz
${PROJECT_ROOT}/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/07_HPC_Prompts/enzymecage_m4b_c8_1_dependency_payload_20260820.tar.gz
${ALT_PROJECT_ROOT}/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/07_HPC_Prompts/enzymecage_m4b_c8_1_dependency_payload_20260820.tar.gz
./enzymecage_m4b_c8_1_dependency_payload_20260820.tar.gz
```

Extract task-locally under:

```text
${WORK_ROOT}/dependency_payload/
```

Run payload `MANIFEST.sha256` validation.

Required payload files:

```text
inputs/uid_to_source/uid_to_source_keep_bacteria_fungi_archaea.csv
inputs/main_2478_universe/bacdive_metatraits_overlap_by_source_signature.csv
inputs/c8_0_audit/C8_INPUT_SOURCE_AUDIT.json
```

Validate:

```text
uid_to_source_keep_bacteria_fungi_archaea.csv data rows = 168,335
unique UniprotID = 168,335
unique source_signature = 3,234
main universe data rows = 2,478
C8_INPUT_SOURCE_AUDIT.json parses
```

If any required input is missing or fails validation, stop with:

```text
BLOCKED_C8_2A_INPUT_MISSING_OR_SHA256_FAIL
```

## Required Outputs

Create under `RETURN_DIR`:

```text
C8_INPUT_CANDIDATE_TABLE.csv
C8_UID_SOURCE_EXPANSION_TABLE.csv
C8_UID_SOURCE_EXPANSION_SUMMARY.csv
C8_UID_SOURCE_EXPANSION_REPORT.md
C8_UID_SOURCE_EXPANSION_VALIDATION_REPORT.json
C8_UID_SOURCE_EXPANSION_VALIDATION_REPORT.md
C8_BOUNDARY_VALIDATION_REPORT.md
C8_INPUT_PATH_RESOLUTION_TABLE.csv
COMMAND_LOG.txt
FINAL_STATUS.txt
MANIFEST.files
MANIFEST.sha256
```

Then create:

```text
${ARCHIVE}
${IDENTITY}
```

Do not include input archives, extracted input directories, raw large assets, or
`trait_annotation.jsonl` in the returned archive.

## C8_INPUT_CANDIDATE_TABLE.csv

Create one row per `FULL_4681_STAGED_STATUS_TABLE.csv` row.

Expected data rows:

```text
4,681
```

Required columns:

```text
candidate_set_id
candidate_uid_order
query_id
pollutant_name_or_smiles
reaction_candidate_id
reaction_source
enzyme_uid
enzyme_candidate_source
enzyme_candidate_rank_or_order
full_4681_final_status
asset_consumable
input_status
input_exclusion_reason
source_status_table
source_asset_manifest
```

Use these staged placeholder values because no upstream pollutant/reaction
candidate table is frozen yet. These placeholders are only for this bounded
C8-2A implementation harness and must not be interpreted as the future
production/all-library candidate source:

```text
candidate_set_id = C8_2A_BOUNDED_FULL_4681_STAGED_STATUS_TABLE_20260814
query_id = C8_STAGED_ASSET_UNIVERSE
pollutant_name_or_smiles = not_applicable_staged_asset_universe
reaction_candidate_id = not_applicable_staged_asset_universe
reaction_source = not_applicable_staged_asset_universe
enzyme_candidate_source = M4_E2_FULL_4681_STAGED_STATUS_TABLE
enzyme_candidate_rank_or_order = candidate_uid_order
```

Rules:

```text
If final_status == PASS_AFDB_P2RANK_PREDICTED_POCKET_D4_LOADER:
  asset_consumable = true
  input_status = C8_CANDIDATE_ASSET_AVAILABLE
  input_exclusion_reason = ""
Else:
  asset_consumable = false
  input_status = ASSET_NOT_AVAILABLE
  input_exclusion_reason = final_status
```

## C8_UID_SOURCE_EXPANSION_TABLE.csv

Create expansion rows for all 4,681 bounded test candidate UIDs. A UID with no usable asset
or no mapping still receives one explicit status row.

Expected data rows for current frozen inputs:

```text
4,681
```

Required columns:

```text
candidate_set_id
candidate_uid_order
enzyme_uid
full_4681_final_status
asset_consumable
asset_manifest_rows
sequence_sha256
sequence_length
loader_validation_status
dataset0_constructed
formal_assets_mutated
production_pool_mutated
production_d4_mutated
source_signature
taxonomy_group
taxid
organism_name
strain_name
source_resolution_level
mapping_source
mapping_method
mapping_confidence
mapping_query_status
uid_to_source_row_count_for_uid
source_universe_class
inside_original_2478_universe
inside_c8_delta_137_review
metatraits_covered
bacdive_covered_main
overlap_bin_main
delta_recommended_status
c8_trait_annotation_eligible
expansion_status
expansion_exclusion_reason
boundary_notes
```

Expansion rules:

```text
For non-PASS UID:
  one row
  asset_consumable = false
  source_signature = ""
  source_universe_class = NOT_APPLICABLE_ASSET_NOT_AVAILABLE
  c8_trait_annotation_eligible = false
  expansion_status = ASSET_NOT_AVAILABLE
  expansion_exclusion_reason = full_4681_final_status

For PASS UID with no UID-to-source row:
  one row
  asset_consumable = true
  source_signature = ""
  source_universe_class = NOT_MAPPED
  c8_trait_annotation_eligible = false
  expansion_status = NOT_MAPPED
  expansion_exclusion_reason = UID_NOT_FOUND_IN_UID_TO_SOURCE_MAPPING

For PASS UID with one or more UID-to-source rows:
  one row per UID-to-source row
  keep all mappings; do not collapse multiple sources
  mapping_method = uid_to_source_keep_bacteria_fungi_archaea
```

Source universe classification:

```text
If source_signature in C8_LOOKUP_SOURCE_UNIVERSE.csv:
  source_universe_class = MAIN_2478
  inside_original_2478_universe = true
  inside_c8_delta_137_review = false
  delta_recommended_status = ""
  c8_trait_annotation_eligible = true

Else if source_signature in C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW.csv:
  source_universe_class = DELTA_137_PENDING_TEACHER_DECISION
  inside_original_2478_universe = false
  inside_c8_delta_137_review = true
  delta_recommended_status = PENDING_TEACHER_DECISION
  c8_trait_annotation_eligible = false
  expansion_status = DELTA_REVIEW_ONLY_NOT_MAIN_C8
  expansion_exclusion_reason = PENDING_TEACHER_DECISION_NOT_MERGED

Else:
  source_universe_class = OUTSIDE_MAIN_AND_DELTA_REVIEW_REQUIRED
  inside_original_2478_universe = false
  inside_c8_delta_137_review = false
  c8_trait_annotation_eligible = false
  expansion_status = OUTSIDE_REVIEW_REQUIRED
  expansion_exclusion_reason = SOURCE_SIGNATURE_NOT_IN_MAIN_2478_OR_C8_DELTA_137
```

For `MAIN_2478` rows:

```text
expansion_status = READY_FOR_C8_3_TRAIT_ANNOTATION
expansion_exclusion_reason = ""
```

Expected current counts:

```text
C8_INPUT_CANDIDATE_TABLE.csv rows = 4,681
C8_UID_SOURCE_EXPANSION_TABLE.csv rows = 4,681
asset_consumable true rows = 1,704
asset_consumable false rows = 2,977
source_universe_class MAIN_2478 rows = 753
source_universe_class DELTA_137_PENDING_TEACHER_DECISION rows = 209
source_universe_class NOT_MAPPED rows = 742
source_universe_class NOT_APPLICABLE_ASSET_NOT_AVAILABLE rows = 2,977
source_universe_class OUTSIDE_MAIN_AND_DELTA_REVIEW_REQUIRED rows = 0
c8_trait_annotation_eligible true rows = 753
c8_trait_annotation_eligible false rows = 3,928
PASS UID with staged asset rows not equal to 6 = 0
```

Expected taxonomy counts among mapped PASS rows:

```text
MAIN_2478:
  target_bacteria = 495
  target_archaea = 73
  target_fungi = 185

DELTA_137_PENDING_TEACHER_DECISION:
  target_bacteria = 116
  target_archaea = 8
  target_fungi = 85
```

If counts differ, fail closed with:

```text
BLOCKED_C8_2A_ROW_COUNT_VALIDATION_FAILED
```

## C8_UID_SOURCE_EXPANSION_SUMMARY.csv

Create one row per summary metric:

```text
metric
value
expected_value
status
notes
```

Must include at least:

```text
candidate_rows
pass_asset_uids
blocked_asset_uids
staged_asset_manifest_rows
main_2478_expansion_rows
delta_137_expansion_rows
not_mapped_pass_uids
asset_not_available_rows
outside_main_and_delta_rows
c8_trait_annotation_eligible_rows
main_target_bacteria_rows
main_target_archaea_rows
main_target_fungi_rows
delta_target_bacteria_rows
delta_target_archaea_rows
delta_target_fungi_rows
production_mutation_rows
formal_asset_mutation_rows
```

## Validation Requirements

Fail closed unless all pass:

```text
All required inputs found and SHA256/manifest checks pass.
Candidate table rows = 4,681.
Expansion table rows = 4,681.
PASS asset rows = 1,704.
Blocked asset rows = 2,977.
Each PASS UID has exactly 6 staged asset manifest rows.
No blocked UID has staged asset manifest rows.
MAIN_2478 expansion rows = 753.
DELTA_137_PENDING_TEACHER_DECISION expansion rows = 209.
NOT_MAPPED PASS rows = 742.
ASSET_NOT_AVAILABLE rows = 2,977.
OUTSIDE_MAIN_AND_DELTA_REVIEW_REQUIRED rows = 0.
c8_trait_annotation_eligible rows = 753.
No delta row is marked c8_trait_annotation_eligible.
No NOT_MAPPED or ASSET_NOT_AVAILABLE row is marked c8_trait_annotation_eligible.
Main/delta source_signature sets remain disjoint.
No production mutation flags are true.
No formal asset mutation flags are true.
No trait_annotation.jsonl exists in RETURN_DIR.
No trait values are generated.
No API call occurred.
No porTraits run occurred.
No hard rejection / trait_score / uncalibrated confidence emitted.
```

## Reports

`C8_UID_SOURCE_EXPANSION_REPORT.md` must explain in plain terms:

```text
C8-2A used FULL_4681 as a bounded/staged implementation harness because no
upstream pollutant/reaction enzyme candidate table is frozen yet.
This is not the final all-enzyme candidate pool and must not limit later
full-library C8 use.
The schema is intentionally compatible with later upstream full-library
candidate tables carrying query_id / pollutant / reaction_candidate /
enzyme_uid / candidate source / rank.
Only 1,704 PASS UIDs are consumable assets.
753 PASS UID-source rows are eligible for C8-3 main trait annotation.
209 PASS UID-source rows link to the 137 delta source review and remain
PENDING_TEACHER_DECISION, not merged into main C8.
742 PASS UIDs have no UID-to-source mapping and are NOT_MAPPED.
2,977 UIDs are asset blockers and cannot proceed to C8-3.
```

`C8_BOUNDARY_VALIDATION_REPORT.md` must report PASS/FAIL for:

```text
staged-only
no production D4 mutation
no production pool mutation
no formal asset mutation
no MetaTraits API call
no BacDive API call
no porTraits run
no raw MetaTraits TSV read
no trait_annotation generated
no trait values generated
main denominator preserved at 2,478
137 delta not merged
no hard rejection
no trait_score
no uncalibrated confidence
```

## Manifest And Identity

Create:

```text
MANIFEST.files
MANIFEST.sha256
${ARCHIVE}
${IDENTITY}
```

Run `sha256sum -c MANIFEST.sha256` before archiving.

Do not include:

```text
input archives
extracted input directories
raw large staged assets
raw MetaTraits TSV gzip files
trait_annotation.jsonl
__pycache__
*.pyc
```

Identity sidecar must include:

```text
archive_name
archive_bytes
archive_sha256
single_root
manifest_file_count
final_status
candidate_rows
expansion_rows
pass_asset_uids
blocked_asset_uids
main_2478_expansion_rows
delta_137_expansion_rows
not_mapped_pass_uids
asset_not_available_rows
outside_main_and_delta_rows
c8_trait_annotation_eligible_rows
main_target_bacteria_rows
main_target_archaea_rows
main_target_fungi_rows
delta_target_bacteria_rows
delta_target_archaea_rows
delta_target_fungi_rows
source_full_4681_archive_sha256
source_c8_1_rerun2_archive_sha256
source_dependency_payload_sha256
no_api_calls
no_porTraits
no_production_mutation
no_trait_annotation
manifest_sha256_check
created_utc
```

If all validations pass, write:

```text
FINAL_STATUS.txt = C8_2A_BOUNDED_UID_SOURCE_EXPANSION_HARNESS_COMPLETE
```
