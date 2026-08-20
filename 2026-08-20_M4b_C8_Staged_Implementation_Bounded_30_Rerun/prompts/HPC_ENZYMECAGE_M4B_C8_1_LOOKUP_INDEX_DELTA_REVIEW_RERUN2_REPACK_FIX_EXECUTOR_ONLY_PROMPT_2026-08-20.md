# HPC executor-only prompt: M4b C8-1 lookup index + delta review rerun2 repack-fix

Date: 2026-08-20

Executor role: Chenyu/HPC executor only.

This is a narrow rerun2 / repack-fix for the already generated C8-1 dependency
payload rerun1 package.

Do not invent a new scientific route. Do not silently rebuild with changed
inputs. The goal is to repair two local-audit defects while preserving all
passing row counts and boundaries.

## Source Package To Fix

Rerun1 task ID:

```text
enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun1_20260820
```

Expected rerun1 archive:

```text
enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun1_20260820.tar.gz
```

Expected rerun1 archive SHA256:

```text
b2d14a0accf69bdd819f9579bc644b2b11e59d17cc76648ac2d69a3e93420e80
```

Expected rerun1 final status:

```text
C8_1_LOOKUP_INDEX_AND_DELTA_REVIEW_COMPLETE
```

Known rerun1 defects from local audit:

```text
1. Returned archive omitted MANIFEST.files and MANIFEST.sha256.
2. C8_METATRAITS_LOOKUP_INDEX.jsonl has 428 target_fungi + F5 rows with
   value_status_preview = NOT_METATRAITS_SOURCE.
   Under the stricter C8 boundary, fungi remain identity-only in the MetaTraits
   lookup, so those 428 rows must use value_status_preview = FUNGI_IDENTITY_ONLY.
3. C8_LOOKUP_INDEX_BUILD_REPORT reports metatraits_tsv_files_checked = 12 while
   other reports state 14 gzip files checked. Clarify as:
   14 gzip files validated; 12 bulk summary TSVs streamed; 2 crosswalks
   validated but not streamed into trait lookup.
4. Archive included scripts/__pycache__; exclude this from rerun2 archive.
```

## Mission

Create a corrected rerun2 return package:

```text
TASK_ID=enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820
```

This task should:

```text
1. Locate and verify rerun1.
2. Copy/extract rerun1 outputs into a fresh rerun2 RETURN_DIR.
3. Patch only the fungal F5 status-preview defect in
   C8_METATRAITS_LOOKUP_INDEX.jsonl.
4. Regenerate C8_METATRAITS_LOOKUP_INDEX_SUMMARY.csv from the patched JSONL.
5. Update validation/build/boundary reports to enforce and document the fix.
6. Add MANIFEST.files and MANIFEST.sha256 to the returned archive.
7. Exclude __pycache__ and temporary input payload directories from the archive.
8. Validate all counts and boundaries.
```

Do not rerun porTraits. Do not call APIs. Do not mutate production.

## Authority And Boundaries

Teacher authority:

```text
老师回复8.19.md
```

Effective requirements:

```text
C8-1 read-only lookup index is allowed.
Main denominator remains original 2,478 source_signature universe.
137 rescued-asset-linked outside-universe sources are delta review only.
C8 v1 does not auto-start porTraits.
Fungi remain identity-only.
No production D4 / production pool / formal asset mutation.
No hard rejection.
No trait_score.
No uncalibrated confidence.
F5 must not be predicted.
F8 must not be written as direct target-pollutant degradation fact.
F15 must not be used for ranking.
```

Hard boundaries:

```text
READ / COPY / PATCH STAGED OUTPUT / VALIDATE / PACKAGE ONLY.
Do not call MetaTraits API.
Do not call BacDive API.
Do not run porTraits.
Do not run genome prediction.
Do not download data.
Do not generate final trait_annotation.jsonl.
Do not edit source code outside RETURN_DIR.
Do not edit production data.
Do not write active_snapshot.json.
Do not mutate production D4 / pool / formal assets.
Do not merge 137 delta sources into the 2,478 main universe.
Do not change source_signature denominators.
```

Allowed final statuses:

```text
C8_1_LOOKUP_INDEX_AND_DELTA_REVIEW_RERUN2_REPACK_FIX_COMPLETE
BLOCKED_C8_1_RERUN1_SOURCE_MISSING_OR_SHA256_FAIL
BLOCKED_C8_1_RERUN2_PATCH_VALIDATION_FAILED
BLOCKED_C8_1_RERUN2_OUTPUT_PATH_EXISTS
BLOCKED_C8_1_RERUN2_BOUNDARY_VALIDATION_FAILED
```

Do not write COMPLETE unless all required validations pass.

## Fixed Chenyu Paths

Use these variables:

```bash
TASK_ID=enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820
RERUN1_TASK_ID=enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun1_20260820
CHENYU_DATA_ROOT=/usrdata/EnzymeCAGE_data
PROJECT_ROOT=${CHENYU_DATA_ROOT}/EnzymeCAGE-master
ALT_PROJECT_ROOT=/root/projects/EnzymeCAGE-master
RETURN_ROOT=${PROJECT_ROOT}/HPC_Returned_Result_Summaries
ALT_RETURN_ROOT=${ALT_PROJECT_ROOT}/HPC_Returned_Result_Summaries
RETURN_DIR=${RETURN_ROOT}/${TASK_ID}
ARCHIVE=${RETURN_ROOT}/${TASK_ID}.tar.gz
IDENTITY=${RETURN_ROOT}/${TASK_ID}.tar.gz.identity.txt
WORK_ROOT=/tmp/${TASK_ID}
RERUN1_EXPECTED_SHA256=b2d14a0accf69bdd819f9579bc644b2b11e59d17cc76648ac2d69a3e93420e80
```

Fresh-run rule:

```text
If RETURN_DIR, ARCHIVE, IDENTITY, or WORK_ROOT already exists, do not overwrite
or repair it. Stop and create a small blocked package with
FINAL_STATUS = BLOCKED_C8_1_RERUN2_OUTPUT_PATH_EXISTS.
```

Allowed write locations:

```text
RETURN_DIR
WORK_ROOT
```

## Locate Rerun1

Search for rerun1 archive in:

```text
${RETURN_ROOT}/${RERUN1_TASK_ID}.tar.gz
${ALT_RETURN_ROOT}/${RERUN1_TASK_ID}.tar.gz
${PROJECT_ROOT}/HPC_Returned_Result_Summaries/${RERUN1_TASK_ID}.tar.gz
${ALT_PROJECT_ROOT}/HPC_Returned_Result_Summaries/${RERUN1_TASK_ID}.tar.gz
./${RERUN1_TASK_ID}.tar.gz
```

Also search for an existing rerun1 directory in:

```text
${RETURN_ROOT}/${RERUN1_TASK_ID}
${ALT_RETURN_ROOT}/${RERUN1_TASK_ID}
```

Validation:

```text
If using archive, compute SHA256 and require exact match to RERUN1_EXPECTED_SHA256.
If using existing directory only, require FINAL_STATUS.txt to equal
C8_1_LOOKUP_INDEX_AND_DELTA_REVIEW_COMPLETE and require all expected core files.
Prefer archive if both archive and directory exist.
```

If rerun1 cannot be verified, stop with:

```text
BLOCKED_C8_1_RERUN1_SOURCE_MISSING_OR_SHA256_FAIL
```

## Required Rerun1 Core Files

Rerun1 source must contain:

```text
C8_BACDIVE_AVAILABILITY_LOOKUP.csv
C8_BOUNDARY_VALIDATION_REPORT.md
C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW.csv
C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW.md
C8_INPUT_PATH_RESOLUTION_TABLE.csv
C8_LOOKUP_INDEX_BUILD_REPORT.json
C8_LOOKUP_INDEX_BUILD_REPORT.md
C8_LOOKUP_INDEX_VALIDATION_REPORT.json
C8_LOOKUP_INDEX_VALIDATION_REPORT.md
C8_LOOKUP_SOURCE_UNIVERSE.csv
C8_METATRAITS_LOOKUP_INDEX.jsonl
C8_METATRAITS_LOOKUP_INDEX_SUMMARY.csv
COMMAND_LOG.txt
FINAL_STATUS.txt
scripts/run_c8_1_lookup_index.py
```

Do not require rerun1 `MANIFEST.files` or `MANIFEST.sha256`; their absence is
one reason for this rerun2 fix.

## Patch Requirements

Patch `C8_METATRAITS_LOOKUP_INDEX.jsonl` as follows:

```text
For every JSON object where:
  taxonomy_group == "target_fungi"
  trait_id == "F5"

Set:
  value_status_preview = "FUNGI_IDENTITY_ONLY"
  source_type_preview = "identity_only"
  mapping_status = "FUNGI_IDENTITY_ONLY"

Keep:
  fungi_identity_only = true
  metatraits_applicable = false
  observed_available = false
  predicted_soft_fill_candidate_available = false
  prediction_allowed_for_trait = false
  observed_scope_match_count = 0
  all_scope_match_count = 0
  matched_observed_examples = ""
  matched_all_examples = ""
```

Do not change any non-fungal row.
Do not change any fungal row except F5 unless required only to regenerate
summary counts from unchanged values.

Expected patch count:

```text
patched target_fungi + F5 rows = 428
```

If patch count is not exactly 428, stop with:

```text
BLOCKED_C8_1_RERUN2_PATCH_VALIDATION_FAILED
```

## Regenerate Summary

Regenerate `C8_METATRAITS_LOOKUP_INDEX_SUMMARY.csv` from the patched JSONL.

Expected summary shape:

```text
15 data rows + header
one row for each F1-F15
main_universe_rows = 2,478 for every trait
```

Expected F5 summary after patch:

```text
trait_id = F5
observed_available_count = 0
predicted_soft_fill_candidate_count = 0
not_observed_count = 0
fungi_identity_only_count = 428
not_metatraits_source_count = 2050
prediction_allowed_for_trait = False
first_screen = observed_evidence_only
```

Do not hand-edit only the summary. It must be regenerated from the patched
JSONL or independently validated against the patched JSONL.

## Required Validation

Validate directly from returned files, not just from prior reports.

### Row counts

```text
C8_METATRAITS_LOOKUP_INDEX.jsonl rows = 37,170
C8_BACDIVE_AVAILABILITY_LOOKUP.csv data rows = 2,478
C8_LOOKUP_SOURCE_UNIVERSE.csv data rows = 2,478
C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW.csv data rows = 137
C8_METATRAITS_LOOKUP_INDEX_SUMMARY.csv data rows = 15
```

### Main/delta separation

```text
main unique source_signature count = 2,478
BacDive lookup unique source_signature count = 2,478
MetaTraits lookup unique source_signature count = 2,478
every main source has exactly 15 MetaTraits lookup rows
delta unique source_signature count = 137
delta ∩ main = 0
delta taxonomy counts = 88 target_bacteria / 6 target_archaea / 43 target_fungi
delta recommended_status = PENDING_TEACHER_DECISION for all rows
delta inside_original_2478_universe = false for all rows
```

### Fungal identity-only validation

Require:

```text
For all rows where taxonomy_group == target_fungi:
  value_status_preview == FUNGI_IDENTITY_ONLY
  fungi_identity_only == true
  metatraits_applicable == false

For F5 specifically:
  target_fungi + F5 rows = 428
  all 428 have value_status_preview == FUNGI_IDENTITY_ONLY
```

### Trait red lines

Require:

```text
F5 predicted rows = 0
F8 target-pollutant direct degradation wording = 0
F15 predicted rows = 0
No final trait_annotation.jsonl exists in RETURN_DIR.
No raw MetaTraits TSV gzip files included in RETURN_DIR.
No dependency payload archive or extracted dependency payload directory included.
No __pycache__ files or directories included.
```

### Boundary red lines

Require:

```text
no API calls
no porTraits
no production mutation
no final trait_annotation
main denominator preserved at 2,478
137 delta sources not merged
F5 not predicted
F8 no direct target-pollutant degradation claim
F15 not used for ranking
fungi identity-only
```

## Report Updates

Update or create these reports in rerun2:

```text
C8_LOOKUP_INDEX_VALIDATION_REPORT.json
C8_LOOKUP_INDEX_VALIDATION_REPORT.md
C8_LOOKUP_INDEX_BUILD_REPORT.json
C8_LOOKUP_INDEX_BUILD_REPORT.md
C8_BOUNDARY_VALIDATION_REPORT.md
COMMAND_LOG.txt
FINAL_STATUS.txt
```

The validation report must include explicit checks for:

```text
fungal_f5_patch_count = 428
fungal_f5_identity_only_rows = 428
all_fungi_metatraits_lookup_identity_only = true
manifest_files_present = true
manifest_sha256_present = true
pycache_excluded = true
```

The build report must clarify MetaTraits gzip handling:

```text
metatraits_gzip_files_validated = 14
metatraits_bulk_summary_tsv_files_streamed = 12
metatraits_crosswalk_gzip_files_validated_not_streamed = 2
```

Do not claim the 2 crosswalk files were streamed into trait lookup.

`COMMAND_LOG.txt` must say this was a rerun2 repack-fix derived from rerun1 and
must list the exact patched-row count.

## Required Return Files

The rerun2 `RETURN_DIR` must include:

```text
C8_BACDIVE_AVAILABILITY_LOOKUP.csv
C8_BOUNDARY_VALIDATION_REPORT.md
C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW.csv
C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW.md
C8_INPUT_PATH_RESOLUTION_TABLE.csv
C8_LOOKUP_INDEX_BUILD_REPORT.json
C8_LOOKUP_INDEX_BUILD_REPORT.md
C8_LOOKUP_INDEX_VALIDATION_REPORT.json
C8_LOOKUP_INDEX_VALIDATION_REPORT.md
C8_LOOKUP_SOURCE_UNIVERSE.csv
C8_METATRAITS_LOOKUP_INDEX.jsonl
C8_METATRAITS_LOOKUP_INDEX_SUMMARY.csv
COMMAND_LOG.txt
FINAL_STATUS.txt
MANIFEST.files
MANIFEST.sha256
scripts/run_c8_1_lookup_index.py
```

Allowed optional file:

```text
scripts/patch_rerun2_repack_fix.py
```

Forbidden in returned archive:

```text
__pycache__/
*.pyc
_input_payload/
*.tar.gz input dependency payloads
raw MetaTraits TSV gzip files
trait_annotation.jsonl
production data copies
```

## Manifest And Archive

Create `MANIFEST.files` with relative path and byte size for every returned
regular file.

Create `MANIFEST.sha256` with SHA256 for every returned regular file except
`MANIFEST.sha256` itself.

Run:

```bash
sha256sum -c MANIFEST.sha256
```

It must pass before archiving.

Then create:

```text
${ARCHIVE}
${IDENTITY}
```

Identity sidecar must include:

```text
archive_name
archive_bytes
archive_sha256
single_root
manifest_file_count
final_status
source_rerun1_archive_sha256
fungal_f5_patch_count
fungal_f5_identity_only_rows
all_fungi_metatraits_lookup_identity_only
main_universe_rows
metatraits_lookup_rows
bacdive_lookup_rows
source_universe_rows
delta_rows
delta_bacteria
delta_archaea
delta_fungi
metatraits_gzip_files_validated
metatraits_bulk_summary_tsv_files_streamed
metatraits_crosswalk_gzip_files_validated_not_streamed
no_api_calls
no_porTraits
no_production_mutation
no_final_trait_annotation
manifest_sha256_check
pycache_excluded
created_utc
```

## Final Status

If all validations pass, write:

```text
C8_1_LOOKUP_INDEX_AND_DELTA_REVIEW_RERUN2_REPACK_FIX_COMPLETE
```

If any validation fails, return a small fail-closed package with the failed
check and final status:

```text
BLOCKED_C8_1_RERUN2_PATCH_VALIDATION_FAILED
```

Do not leave rerun2 marked complete if the manifest is missing, fungal F5 is not
fixed, pycache is present, or row counts changed.

