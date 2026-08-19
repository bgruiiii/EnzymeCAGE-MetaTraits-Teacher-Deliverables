# MetaTraits C7-1 long-form mapping rerun2 (false-positive fix)

- task_id: `metatraits_c7_1_long_form_mapping_rerun2_false_positive_fix_20260819`
- data_dir: `/usrdata/EnzymeCAGE_data/data/metatraits/incoming/metatraits_bulk_tsv_snapshot_20260818`
- previous_return_dir: `/usrdata/EnzymeCAGE_data/EnzymeCAGE-master/HPC_Returned_Result_Summaries/metatraits_c7_1_long_form_mapping_correction_20260819`
- catalog_filter: `ALL_SIGNATURES` (total=37022, matched=28412)

## False-positive fixes

- **F3 pH**: `group_2` now exact-equals `pH` (was raw `ph` substring, which matched `Atmosphere`, `Morphology`, `Cell morphology`, `Cell size phenotype`). trait_name limited to real pH terms.
- **F12 Gram**: `group_2` exact-equals `Cell envelope`; trait_name matches `gram positive`/`gram negative`/`outer membrane`/`cell envelope` (was raw `gram`, which matched `produces: gramicidin`).

## Negative assertions

| assertion | status | violations |
|---|---|---|
| ASSERT_F3_NO_ATMOSPHERE_ROWS | PASS | 0 |
| ASSERT_F3_NO_MORPHOLOGY_ROWS | PASS | 0 |
| ASSERT_F3_NO_CELL_MORPHOLOGY_ROWS | PASS | 0 |
| ASSERT_F3_NO_CELL_SIZE_PHENOTYPE_ROWS | PASS | 0 |
| ASSERT_F3_NO_AEROTOLERANT_ROWS | PASS | 0 |
| ASSERT_F3_NO_CAPNOPHILIC_ROWS | PASS | 0 |
| ASSERT_F3_NO_CELL_SHAPE_OR_CELL_SIZE_ROWS | PASS | 0 |
| ASSERT_F12_NO_GRAMICIDIN_ROWS | PASS | 0 |

## F1-F15 mapping status

| trait_id | trait_name | mapping_status | observed | all |
|---|---|---|---|---|
| F1 | oxygen_tolerance | MAPPED_LONG_FORM_DRAFT | 178 | 1131 |
| F2 | temperature | MAPPED_LONG_FORM_DRAFT | 248 | 719 |
| F3 | pH | MAPPED_LONG_FORM_DRAFT | 132 | 442 |
| F4 | salinity | MAPPED_LONG_FORM_DRAFT | 60 | 184 |
| F5 | bacdive_availability | NOT_METATRAITS_SOURCE_BACDIVE_ONLY | - | - |
| F6 | respiration_electron_acceptor | MAPPED_LONG_FORM_DRAFT | 1135 | 1786 |
| F7 | carbon_and_substrate_utilization | MAPPED_LONG_FORM_DRAFT | 6678 | 7466 |
| F8 | degradation_capacity_broad | MAPPED_LONG_FORM_DRAFT | 1653 | 2247 |
| F9 | enzyme_activity | MAPPED_LONG_FORM_DRAFT | 756 | 1067 |
| F10 | motility | MAPPED_LONG_FORM_DRAFT | 90 | 566 |
| F11 | cell_morphology | MAPPED_LONG_FORM_DRAFT | 350 | 368 |
| F12 | cell_envelope_gram | MAPPED_LONG_FORM_DRAFT | 87 | 739 |
| F13 | sporulation | MAPPED_LONG_FORM_DRAFT | 87 | 483 |
| F14 | genome_basic | MAPPED_LONG_FORM_DRAFT | 108 | 120 |
| F15 | habitat_generalism | MAPPED_LONG_FORM_DRAFT | 0 | 18 |
