# HPC executor-only prompt: MetaTraits C7-1 long-form mapping rerun2 false-positive fix

Date: 2026-08-19

Executor role: Chenyu/HPC executor only.

## Mission

Run a small rule-only rerun for the MetaTraits C7-1 long-form mapping
correction. The previous package correctly used the long-form MetaTraits route,
but local audit found two false-positive bugs:

1. F3 pH matched raw substring `ph`, causing `Atmosphere` and `Morphology` rows
   to be mapped to pH.
2. F12 Gram/cell-envelope matched raw substring `gram`, causing
   `produces: gramicidin` rows to be mapped to Gram/cell-envelope.

This task must regenerate the mapping outputs with stricter F3/F12 rules and
must include machine-checkable negative assertions proving these two false
positives are gone.

## Hard boundaries

```text
READ / PARSE / REPORT ONLY.
Do not download MetaTraits again.
Do not call the MetaTraits API.
Do not call the BacDive API.
Do not run genome-based online prediction.
Do not generate new trait predictions.
Do not edit production code.
Do not edit existing production data.
Do not activate the MetaTraits snapshot.
Do not write active_snapshot.json.
Do not connect to production D4 / production pool.
Do not mutate any existing EnzymeCAGE formal asset.
Do not include the large TSV gzip files inside the returned archive.
```

If any required input TSV is missing or any negative assertion fails, return a
metadata package with:

```text
FINAL_STATUS=BLOCKED_METATRAITS_C7_1_MAPPING_RERUN2_VALIDATION_FAILED
```

Do not write a COMPLETE final status unless all assertions pass.

## Fixed paths on Chenyu

Use these exact paths:

```bash
TASK_ID=metatraits_c7_1_long_form_mapping_rerun2_false_positive_fix_20260819
CHENYU_DATA_ROOT=/usrdata/EnzymeCAGE_data
PROJECT_ROOT=${CHENYU_DATA_ROOT}/EnzymeCAGE-master
DATA_DIR=${CHENYU_DATA_ROOT}/data/metatraits/incoming/metatraits_bulk_tsv_snapshot_20260818
PREVIOUS_RETURN_DIR=${PROJECT_ROOT}/HPC_Returned_Result_Summaries/metatraits_c7_1_long_form_mapping_correction_20260819
RETURN_ROOT=${PROJECT_ROOT}/HPC_Returned_Result_Summaries
RETURN_DIR=${RETURN_ROOT}/${TASK_ID}
ARCHIVE=${RETURN_ROOT}/${TASK_ID}.tar.gz
IDENTITY=${RETURN_ROOT}/${TASK_ID}.tar.gz.identity.txt
```

Create `RETURN_DIR` only if it does not already contain a completed run for this
`TASK_ID`. If `ARCHIVE` or `IDENTITY` already exists, stop with a path-conflict
message.

## Required input files

Read the same already landed files under `DATA_DIR`. These 12 bulk summary TSV
gzip files must exist and pass `gzip -t`:

```text
gtdb_family_summary_all.tsv.gz
gtdb_family_summary_no_predictions.tsv.gz
gtdb_genus_summary_all.tsv.gz
gtdb_genus_summary_no_predictions.tsv.gz
gtdb_species_summary_all.tsv.gz
gtdb_species_summary_no_predictions.tsv.gz
ncbi_family_summary_all.tsv.gz
ncbi_family_summary_no_predictions.tsv.gz
ncbi_genus_summary_all.tsv.gz
ncbi_genus_summary_no_predictions.tsv.gz
ncbi_species_summary_all.tsv.gz
ncbi_species_summary_no_predictions.tsv.gz
```

These 2 crosswalk files may be checked for presence only, but do not treat them
as trait summary tables:

```text
GTDB2NCBI.tsv.gz
NCBI2GTDB.tsv.gz
```

## Long-form interpretation

MetaTraits summary TSVs are long-form tables. Mapping must use row-level fields:

```text
trait_name
unit
consensus_value
minimum
median
mean
maximum
discrete_values
databases
group_1
group_2
ontology_ids
```

Do not decide mapping only from header column names.

Use `no_predictions` files as observed/no-prediction scope. Use `all` files as
the broader scope that may include prediction-like soft-fill candidates. Keep
observed/all counts separate.

## Frozen C7-1 policy to preserve

```text
F1 oxygen_tolerance
F2 temperature
F3 pH
F4 salinity
F5 bacdive_availability
F6 respiration_electron_acceptor
F7 carbon_and_substrate_utilization
F8 degradation_capacity_broad
F9 enzyme_activity
F10 motility
F11 cell_morphology
F12 cell_envelope_gram
F13 sporulation
F14 genome_basic
F15 habitat_generalism
```

Teacher-frozen policy:

```text
F1-F4/F6-F8: observed first; predicted soft-fill allowed when explicitly labelled.
F5: BacDive availability / culture collection; observed only; must not be predicted.
F8: broad degradation context only; never claim exact pollutant degradation from it.
F9-F14: source-labelled context only; no hard rejection.
F15: low-coverage ecological background only; must not participate in ranking.
Fungi: identity-only in the current C7-2 bounded route; no bacterial/archaeal soft fill.
```

## Required rule corrections

### F3 pH

Allowed F3 matches:

```text
group_2 exactly equals "pH" case-insensitively
trait_name contains a real pH term:
  "pH growth"
  "pH minimum"
  "pH maximum"
  "pH optimum"
  "optimum pH"
  "acidophilic"
  "alkaliphilic"
  "neutrophilic"
```

Forbidden F3 matching:

```text
Do not match raw substring "ph" inside unrelated words.
Do not map group_2 == "Atmosphere" to F3.
Do not map group_2 == "Morphology" to F3.
Do not map group_2 == "Cell morphology" to F3.
Do not map group_2 == "Cell size phenotype" to F3.
```

The following examples must not be assigned to F3:

```text
aerotolerant
capnophilic
cell color: yellow pigment
cell shape
cell length maximum
cell width minimum
```

### F12 cell envelope / Gram

Allowed F12 matches:

```text
group_2 exactly equals "Cell envelope" case-insensitively
trait_name exactly or semantically matches:
  "gram positive"
  "gram negative"
  "outer membrane"
  "cell envelope"
```

Forbidden F12 matching:

```text
Do not match raw substring "gram" inside unrelated chemical/product names.
Do not map "produces: gramicidin" to F12.
```

## Other mapping rules

Carry forward the previous long-form mapping logic for F1/F2/F4/F6-F11/F13-F15,
but keep these boundaries:

```text
F5: NOT_METATRAITS_SOURCE_BACDIVE_ONLY.
F8: broad degradation context only; no exact pollutant degradation claim.
F15: ecological background only; not a ranking input.
All mappings are draft evidence mappings, not production implementation.
```

If a mapping is ambiguous, use:

```text
mapping_status=REVIEW_REQUIRED_AMBIGUOUS
```

and explain it. Do not force a mapping.

## Mandatory negative validation assertions

Create a machine-readable assertion report and fail the run if any assertion is
nonzero:

```text
ASSERT_F3_NO_ATMOSPHERE_ROWS
ASSERT_F3_NO_MORPHOLOGY_ROWS
ASSERT_F3_NO_CELL_MORPHOLOGY_ROWS
ASSERT_F3_NO_CELL_SIZE_PHENOTYPE_ROWS
ASSERT_F3_NO_AEROTOLERANT_ROWS
ASSERT_F3_NO_CAPNOPHILIC_ROWS
ASSERT_F3_NO_CELL_SHAPE_OR_CELL_SIZE_ROWS
ASSERT_F12_NO_GRAMICIDIN_ROWS
```

For each assertion, report:

```text
assertion_name
status = PASS | FAIL
violating_row_count
example_violating_trait_names
example_violating_group_1_group_2
```

`FINAL_STATUS` may be COMPLETE only if every assertion status is PASS.

## Required returned files

Create these files under `RETURN_DIR`:

```text
C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_RERUN2.csv
C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_RERUN2.md
METATRAITS_LONG_FORM_TRAIT_CATALOG_RERUN2.csv
METATRAITS_C7_1_MAPPING_EVIDENCE_EXAMPLES_RERUN2.csv
METATRAITS_C7_1_MAPPING_SUMMARY_RERUN2.json
METATRAITS_C7_1_NEGATIVE_ASSERTIONS_RERUN2.csv
VALIDATION_REPORT.json
VALIDATION_REPORT.md
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

The archive must include metadata/report files only. Do not include `.tsv.gz`
bulk files.

## Output schemas

### C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_RERUN2.csv

One row per C7-1 trait. Required columns:

```text
trait_id
trait_name
first_screen
teacher_policy
metatraits_long_form_fields_to_use
observed_scope_files_to_check
all_scope_files_to_check
candidate_trait_name_patterns
candidate_group_1_patterns
candidate_group_2_patterns
candidate_units
observed_scope_match_count
all_scope_match_count
example_trait_names_observed_scope
example_trait_names_all_scope
mapping_status
boundary_notes
rerun2_false_positive_fix_notes
```

Allowed `mapping_status`:

```text
MAPPED_LONG_FORM_DRAFT
NOT_METATRAITS_SOURCE_BACDIVE_ONLY
NOT_MAPPED_FROM_METATRAITS_AFTER_LONG_FORM_SCAN
REVIEW_REQUIRED_AMBIGUOUS
```

### METATRAITS_LONG_FORM_TRAIT_CATALOG_RERUN2.csv

Required columns:

```text
file_name
taxonomy_namespace
taxonomic_rank
prediction_scope
trait_name
unit
group_1
group_2
ontology_ids
databases
row_count
candidate_c7_trait_ids
candidate_c7_mapping_status
```

### METATRAITS_C7_1_MAPPING_EVIDENCE_EXAMPLES_RERUN2.csv

Keep up to 50 example rows per C7 trait and per prediction scope. Required
columns:

```text
trait_id
trait_name
prediction_scope
file_name
taxonomy_namespace
taxonomic_rank
metatraits_trait_name
unit
group_1
group_2
ontology_ids
databases
example_taxon_id
example_taxon_name
example_consensus_value
example_minimum
example_median
example_mean
example_maximum
why_matched
boundary_note
```

## VALIDATION_REPORT.json required fields

```text
task_id
data_dir
return_dir
previous_return_dir
required_summary_expected_count
required_summary_present_count
required_summary_gzip_pass_count
long_form_header_valid_count
crosswalk_present_count
mapping_rerun2_created
trait_panel_rows_expected
trait_panel_rows_written
catalog_filter
total_unique_signatures
matched_unique_signatures
negative_assertions_total
negative_assertions_passed
negative_assertions_failed
boundary_no_download
boundary_no_api_call
boundary_no_prediction_run
boundary_no_production_mutation
boundary_no_snapshot_activation
final_status
created_at_utc
created_at_local
```

## Final status

If all 12 summary files are present, pass gzip validation, have expected
long-form columns, 15 trait panel rows are written, and all negative assertions
PASS, write:

```text
METATRAITS_C7_1_LONG_FORM_MAPPING_RERUN2_FALSE_POSITIVE_FIX_COMPLETE
```

Otherwise write:

```text
BLOCKED_METATRAITS_C7_1_MAPPING_RERUN2_VALIDATION_FAILED
```

`FINAL_STATUS.txt` must include exact `DATA_DIR`, `RETURN_DIR`, `ARCHIVE`,
`IDENTITY`, `trait_panel_rows_written`, and `negative_assertions_passed/total`.

## Identity sidecar

Create `${IDENTITY}` with:

```text
task_id
archive_path
archive_size_bytes
archive_sha256
single_root_dir
data_dir
previous_return_dir
final_status
negative_assertions_passed
negative_assertions_total
created_at_utc
created_at_local
```

## Final executor response

Return only:

```text
FINAL_STATUS=<...>
DATA_DIR=<...>
RETURN_DIR=<...>
ARCHIVE=<...>
IDENTITY=<...>
trait_panel_rows_written=<...>/15
negative_assertions_passed=<...>/<...>
archive_sha256=<...>
```
