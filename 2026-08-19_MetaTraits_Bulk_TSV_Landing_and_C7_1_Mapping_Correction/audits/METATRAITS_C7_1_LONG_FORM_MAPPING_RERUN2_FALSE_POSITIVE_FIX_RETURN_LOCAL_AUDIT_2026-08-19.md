# MetaTraits C7-1 Long-Form Mapping Rerun2 False-Positive Fix Return Local Audit

Date: 2026-08-19

Audited package:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/metatraits_c7_1_long_form_mapping_rerun2_false_positive_fix_20260819.tar.gz
```

Identity sidecar:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/metatraits_c7_1_long_form_mapping_rerun2_false_positive_fix_20260819.tar.gz.identity.txt
```

## Verdict

**PASS. Ready to use as the corrected C7-1 MetaTraits long-form mapping evidence
package for teacher review.**

This rerun2 package closes the two local-audit blockers found in the previous
`metatraits_c7_1_long_form_mapping_correction_20260819` package:

1. F3 pH no longer matches raw substring `ph`; it no longer pulls in
   `Atmosphere` or `Morphology` rows.
2. F12 cell-envelope/Gram no longer matches raw substring `gram`; it no longer
   pulls in `produces: gramicidin`.

The package remains metadata/report only and stays within the teacher-required
boundaries: no new MetaTraits download, no MetaTraits API, no BacDive API, no
prediction run, no production mutation, and no snapshot activation.

## Identity And Integrity

Local archive SHA256:

```text
61940833695160553983d05e722af0ee1d10c7ce3d8f3bfbef79c0c567f30db9
```

Identity sidecar reports the same archive SHA256:

```text
archive_sha256=61940833695160553983d05e722af0ee1d10c7ce3d8f3bfbef79c0c567f30db9
archive_size_bytes=532734
single_root_dir=metatraits_c7_1_long_form_mapping_rerun2_false_positive_fix_20260819
final_status=METATRAITS_C7_1_LONG_FORM_MAPPING_RERUN2_FALSE_POSITIVE_FIX_COMPLETE
negative_assertions_passed=8
negative_assertions_total=8
```

Package internal manifest check:

```text
C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_RERUN2.csv: OK
C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_RERUN2.md: OK
COMMAND_LOG.txt: OK
FINAL_STATUS.txt: OK
METATRAITS_C7_1_MAPPING_EVIDENCE_EXAMPLES_RERUN2.csv: OK
METATRAITS_C7_1_MAPPING_SUMMARY_RERUN2.json: OK
METATRAITS_C7_1_NEGATIVE_ASSERTIONS_RERUN2.csv: OK
METATRAITS_LONG_FORM_TRAIT_CATALOG_RERUN2.csv: OK
VALIDATION_REPORT.json: OK
VALIDATION_REPORT.md: OK
```

## Required File Presence

Returned files are complete:

```text
C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_RERUN2.csv
C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_RERUN2.md
COMMAND_LOG.txt
FINAL_STATUS.txt
MANIFEST.files
MANIFEST.sha256
METATRAITS_C7_1_MAPPING_EVIDENCE_EXAMPLES_RERUN2.csv
METATRAITS_C7_1_MAPPING_SUMMARY_RERUN2.json
METATRAITS_C7_1_NEGATIVE_ASSERTIONS_RERUN2.csv
METATRAITS_LONG_FORM_TRAIT_CATALOG_RERUN2.csv
VALIDATION_REPORT.json
VALIDATION_REPORT.md
```

No `.tsv.gz` bulk data files are included in the returned archive.

## Teacher-Required Validation Evidence

Final status:

```text
METATRAITS_C7_1_LONG_FORM_MAPPING_RERUN2_FALSE_POSITIVE_FIX_COMPLETE
```

Data path on Chenyu:

```text
/usrdata/EnzymeCAGE_data/data/metatraits/incoming/metatraits_bulk_tsv_snapshot_20260818
```

Validation report key fields:

```text
required_summary_expected_count=12
required_summary_present_count=12
required_summary_gzip_pass_count=12
long_form_header_valid_count=12
crosswalk_present_count=2
mapping_rerun2_created=true
trait_panel_rows_written=15/15
catalog_filter=ALL_SIGNATURES
total_unique_signatures=37022
matched_unique_signatures=28412
negative_assertions_passed=8/8
negative_assertions_failed=0
boundary_no_download=true
boundary_no_api_call=true
boundary_no_prediction_run=true
boundary_no_production_mutation=true
boundary_no_snapshot_activation=true
```

## Trait Panel Check

`C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_RERUN2.csv` contains all 15
frozen C7-1 trait IDs:

```text
F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15
```

Mapping status counts:

```text
MAPPED_LONG_FORM_DRAFT = 14
NOT_METATRAITS_SOURCE_BACDIVE_ONLY = 1
```

F5 is correctly kept out of MetaTraits:

```text
F5 bacdive_availability
mapping_status=NOT_METATRAITS_SOURCE_BACDIVE_ONLY
boundary_notes=NOT a MetaTraits source. BacDive/culture-collection closure evidence only.
```

## False-Positive Fix Checks

Machine-readable negative assertions all pass:

```text
ASSERT_F3_NO_ATMOSPHERE_ROWS = PASS, violating_row_count=0
ASSERT_F3_NO_MORPHOLOGY_ROWS = PASS, violating_row_count=0
ASSERT_F3_NO_CELL_MORPHOLOGY_ROWS = PASS, violating_row_count=0
ASSERT_F3_NO_CELL_SIZE_PHENOTYPE_ROWS = PASS, violating_row_count=0
ASSERT_F3_NO_AEROTOLERANT_ROWS = PASS, violating_row_count=0
ASSERT_F3_NO_CAPNOPHILIC_ROWS = PASS, violating_row_count=0
ASSERT_F3_NO_CELL_SHAPE_OR_CELL_SIZE_ROWS = PASS, violating_row_count=0
ASSERT_F12_NO_GRAMICIDIN_ROWS = PASS, violating_row_count=0
```

Independent catalog scan found:

```text
bad_f3_count=0
bad_f12_count=0
```

F3 catalog group distribution after rerun2:

```text
Environmental preferences / pH = 473135
```

This confirms F3 no longer includes `Atmosphere`, `Morphology`,
`Cell morphology`, or `Cell size phenotype`.

F12 catalog examples after rerun2:

```text
gram negative | Morphology | Cell envelope
gram positive | Morphology | Cell envelope
```

No `gramicidin` rows remain assigned to F12.

Independent evidence-example scan found:

```text
bad_evidence_count=0
```

## Scope And Boundary Notes

This package is a C7-1 mapping-evidence correction package only. It does not
activate a MetaTraits snapshot and does not implement C8 production logic.

Observed/no-prediction and all-scope counts remain separate. The summary reports:

```text
per_scope_data_rows:
  all = 12855974
  no_predictions = 1526644
```

Selected per-trait match counts:

```text
F3 observed_scope_match_count=132, all_scope_match_count=442
F5 observed_scope_match_count=0, all_scope_match_count=0
F8 observed_scope_match_count=1653, all_scope_match_count=2247
F12 observed_scope_match_count=87, all_scope_match_count=739
F15 observed_scope_match_count=0, all_scope_match_count=18
```

Non-blocking note: `created_at_local` is recorded with `+0000`, so it should be
read as UTC-style time rather than China local time. This does not affect the
data integrity or mapping conclusion.

## Final Audit Conclusion

The rerun2 return fixes the previous C7-1 mapping false positives and satisfies
the 2026-08-18 teacher requirement for an explicit MetaTraits TSV field to C7-1
trait-panel mapping口径, using the already-landed Chenyu TSV snapshot and
remaining inside the staged/read-only boundary.
