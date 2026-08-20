# C8-0 Input Source Audit

Date: 2026-08-20

Task: M4b / C8 TraitFilterLayer staged-only implementation, step C8-0.

Status: LOCAL_INPUT_FREEZE_COMPLETE_WITH_RUNTIME_PATH_CHECK_REQUIRED_BEFORE_C8_1

## 1. Purpose

C8-0 does not generate trait annotations and does not implement filtering. Its job is to freeze the exact input sources that later C8 steps are allowed to read.

This audit answers:

```text
Which teacher authority file authorizes C8?
Which enzyme asset table is the accepted 1,704 PASS source?
Which microbe universe remains the 2,478 denominator?
Which UID-to-source table can C8 use?
Which MetaTraits landing and C7-1 mapping version must C8 use?
Which C7-2 validator package is the starting schema/validator contract?
Which inputs are locally present, and which Chenyu runtime paths must be rechecked before C8-1?
```

## 2. Teacher Authority

| Item | Path | SHA256 | Status |
|---|---|---:|---|
| Latest teacher decision | `custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/00_Authority_Teacher_Plan/老师回复8.19.md` | `d5327712675dfc6321a59d8768655a57fc0faecbac70d5a56de8b0ac6206717b` | PASS |
| C8 approved plan | `custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/01_Path_Contract_Objective/M4b_C8_TraitFilterLayer_Implementation_Plan_2026-08-19/M4B_C8_TRAITFILTERLAYER_IMPLEMENTATION_PLAN_AND_TASK_BREAKDOWN_2026-08-19.md` | `79b9a74901117a5c73ea17bf5dc2288aaf0a4ca294e2142d8d663e45d3ea7cc8` | PASS |

Teacher 2026-08-19 decisions relevant to C8-0:

```text
MetaTraits TSV landing + C7-1 mapping rerun2 accepted.
C8 staged-only implementation approved.
C8 must use rerun2 long-form mapping, not older header-only mapping.
Main denominator remains the original 2,478 microbe source universe.
137 rescued-asset-linked sources outside 2,478 are delta review only.
porTraits is not started in C8 v1.
```

## 3. Frozen Inputs

### 3.1 Enzyme staged asset input

| Item | Path | Rows | SHA256 | Status |
|---|---|---:|---:|---|
| Full 4,681 staged status table | `custom/github_upload/EnzymeCAGE-Teacher-Deliverables/2026-08-14_M4_E2_Full_4681_Staged_Status_Table/tables/FULL_4681_STAGED_STATUS_TABLE.csv` | 4,681 data rows | `41b1166eef15d0c9dac0a2253369b7d5c9a324c6daefa5bc7481e4991f8b1b3a` | PASS |
| Staged asset manifest | `custom/github_upload/EnzymeCAGE-Teacher-Deliverables/2026-08-14_M4_E2_Full_4681_Staged_Status_Table/tables/STAGED_ASSET_MANIFEST.csv` | 10,224 data rows | `2f208865cbf487ad7fe1674761f87f0efbd4f2fd459c029726e7e71cfb27022f` | PASS |

Status table counts:

```text
PASS_AFDB_P2RANK_PREDICTED_POCKET_D4_LOADER: 1,704
BLOCKED_AFDB_P2RANK_NO_POCKET: 1,324
BLOCKED_AFDB_STRUCTURE_FETCH_FAILED: 1,650
BLOCKED_ESM2_3B_EXTRACTION_FAILED: 3
```

Mutation flags:

```text
formal_assets_mutated=False: 4,681 / 4,681
production_pool_mutated=False: 4,681 / 4,681
production_d4_mutated=False: 4,681 / 4,681
```

Allowed C8 interpretation:

```text
Only the 1,704 PASS rows are C8-consumable enzyme assets.
Blocked rows remain evidence/status rows and cannot be treated as usable assets.
```

### 3.2 UID to microbe source mapping

| Item | Path | Rows | Unique UID | Unique source_signature | SHA256 | Status |
|---|---|---:|---:|---:|---:|---|
| UID to source mapping | `data/processed/rhea/2026-01-21/microbe/taxonomy_filter_2026-04-28/uid_to_source_keep_bacteria_fungi_archaea.csv` | 168,335 | 168,335 | 3,234 | `7b92e8e625cb73f070c8e902687ea5bbdbf749f04a19828e550e3fe205684fe6` | PASS |

Taxonomy distribution by mapping row:

```text
target_bacteria: 152,044
target_archaea: 8,637
target_fungi: 7,654
```

Allowed C8 interpretation:

```text
This table may be used to expand enzyme UID to source_signature.
One UID to multiple source_signatures must remain multiple rows.
Unmapped UID must be recorded as NOT_MAPPED, not silently dropped.
```

### 3.3 Main 2,478 microbe universe

| Item | Path | Rows | SHA256 | Status |
|---|---|---:|---:|---|
| BacDive + MetaTraits overlap by source_signature | `custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/02_bacdive_full_closure/bacdive_metatraits_overlap_by_source_signature.csv` | 2,478 data rows | `278867b69aa191e430cddfe5a6ad19047b6805f02db58bf230542eed1327a7ff` | PASS |

Taxonomy distribution:

```text
target_bacteria: 1,897
target_archaea: 153
target_fungi: 428
```

Coverage bins:

```text
both_covered: 1,508
bacdive_only: 238
metatraits_only: 130
neither: 602
```

Coverage totals:

```text
MetaTraits covered: 1,638 / 2,478
BacDive main covered: 1,746 / 2,478
```

Allowed C8 interpretation:

```text
This file is the C8 main denominator.
Do not replace it with the larger 3,234-row MetaTraits coverage probe table.
Do not silently add the 137 outside-universe rescued sources to this denominator.
```

### 3.4 MetaTraits coverage probe table

| Item | Path | Rows | SHA256 | Status |
|---|---|---:|---:|---|
| Source-level MetaTraits coverage probe | `custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/01_metatraits_species_coverage/source_signature_metatraits_coverage.csv` | 3,234 data rows | `ae343b93910ed7dad53db89d73ec1fc082956d446e5096e9e22d2142dc5a4560` | PASS_AS_AUXILIARY_TABLE |

Important boundary:

```text
This 3,234-row table is useful for lookup/context checks.
It is not the C8 main denominator.
For C8 main universe counts, use the 2,478-row overlap table above.
```

### 3.5 MetaTraits TSV landing identity

| Item | Path | Rows | SHA256 | Status |
|---|---|---:|---:|---|
| MetaTraits bulk TSV file manifest | `custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-19_MetaTraits_Bulk_TSV_Landing_and_C7_1_Mapping_Correction/metatraits_landing_metadata/METATRAITS_BULK_TSV_FILE_MANIFEST.csv` | 14 data rows | `5748c8bd4e24e28c2849b945b3b4e52c12a525eef03bb23ea4fa9df50e4342ab` | PASS |
| MetaTraits landing SHA256SUMS | `custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-19_MetaTraits_Bulk_TSV_Landing_and_C7_1_Mapping_Correction/metatraits_landing_metadata/SHA256SUMS.txt` | 14 entries | `54af97554c6576b6bc36d65e72c3cfa46c43e7f004e88c96ac216b8f28959cd5` | PASS |

Landing summary:

```text
required summary TSV expected: 12
required summary TSV present: 12
companion crosswalk present: 2
gzip test PASS: 14 / 14
official index last modified: 2026-06-10 10:23
Chenyu DATA_DIR: /usrdata/EnzymeCAGE_data/data/metatraits/incoming/metatraits_bulk_tsv_snapshot_20260818
```

Runtime boundary:

```text
The local workspace contains the accepted landing metadata and returned archive identity.
The raw 12 TSV gzip files are staged on Chenyu under DATA_DIR.
C8-1 must recheck path existence and SHA256 on Chenyu immediately before reading them.
```

### 3.6 C7-1 long-form MetaTraits mapping rerun2

| Item | Path | Rows | SHA256 | Status |
|---|---|---:|---:|---|
| C7-1 trait panel to MetaTraits long-form mapping rerun2 | `custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-19_MetaTraits_Bulk_TSV_Landing_and_C7_1_Mapping_Correction/c7_1_mapping_rerun2/C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_RERUN2.csv` | 15 data rows | `ae7000b210c3add4daa1801bd03f3f7fcade3fee74c373809a36f9a2a90de4da` | PASS |
| Rerun2 validation report | `custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-19_MetaTraits_Bulk_TSV_Landing_and_C7_1_Mapping_Correction/c7_1_mapping_rerun2/VALIDATION_REPORT_RERUN2.json` | n/a | `e4d1b1d459fee902555c5770786c2b64e20020c2253ab52428b52d12d608c60a` | PASS |

Rerun2 validation summary:

```text
trait_panel_rows_expected: 15
trait_panel_rows_written: 15
negative_assertions_total: 8
negative_assertions_passed: 8
negative_assertions_failed: 0
boundary_no_download: true
boundary_no_api_call: true
boundary_no_prediction_run: true
boundary_no_production_mutation: true
boundary_no_snapshot_activation: true
final_status: METATRAITS_C7_1_LONG_FORM_MAPPING_RERUN2_FALSE_POSITIVE_FIX_COMPLETE
```

Allowed C8 interpretation:

```text
C8 must use this rerun2 long-form mapping.
C8 must not use the superseded header-only mapping.
```

### 3.7 C7-2 bounded validator contract

| Item | Path | SHA256 | Status |
|---|---|---:|---|
| Policy manifest | `custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/POLICY_MANIFEST.json` | `d0feb729f4033e1dca26a42b8a0333e96d7839e51e9aa7255856dccfcb7a1a41` | PASS |
| Train set manifest | `custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/TRAIN_SET_MANIFEST.csv` | `c18ba2c4920d88a0e27e7a7673e08b438d18a9c9373eb7f3f9cde042e6a7794b` | PASS |
| Trait annotation sample | `custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/trait_annotation.jsonl` | `49c39c7e75130959ea59dff114012c64d483d384bc98159e4398ee35042b251b` | PASS |

C7-2 bounded validator summary:

```text
FINAL_STATUS: PASS
rows: 30
taxonomy_distribution: target_bacteria=10, target_archaea=10, target_fungi=10
staged_assets_source: teacher-accepted 1,704 staged PASS package
p0dxv0_included: false
metatraits_online_prediction_run: false
bacdive_api_query_run: false
production_d4_mutated: false
production_pool_mutated: false
formal_assets_mutated: false
overall_pass: true
errors: 0
```

Frozen C7-2 policy:

```text
Allowed predicted soft-fill: F1, F2, F3, F4, F6, F7, F8
Forbidden predicted soft-fill: F5, F9, F10, F11, F12, F13, F14, F15
Fungal trait policy: identity_only
Fungal missing reason: fungi_no_local_trait_source
Hard rejection enabled: false
Trait score enabled: false
Uncalibrated confidence enabled: false
```

## 4. Required C8-0 Output Files

This C8-0 step creates:

```text
C8_INPUT_SOURCE_AUDIT.md
C8_INPUT_SOURCE_AUDIT.json
```

No C8 trait lookup index, UID-source expansion table, trait_annotation, validator report, or delta review table is generated in C8-0.

## 5. Red Lines Frozen For Later Steps

```text
staged-only
no production D4 mutation
no production pool mutation
no formal asset mutation
no hard rejection
no trait_score
no uncalibrated confidence
no MetaTraits API
no BacDive API
no online genome prediction
no porTraits run in C8 v1
fungi identity-only
F5 availability / culture collection evidence cannot be predicted
F8 broad degradation context cannot be written as direct target-pollutant degradation fact
F15 is low-coverage ecological background only and cannot participate in ranking
original 2,478 denominator must not be silently changed
137 outside-universe rescued sources remain delta review only
```

## 6. C8-0 Verdict

```text
C8-0 local input freeze: PASS
C8-0 local metadata/path preflight: PASS
Chenyu raw MetaTraits TSV runtime path check before C8-1: REQUIRED
Ready to proceed to C8-1 planning/implementation: YES, with runtime path recheck guard
```

The next step should not start by reading arbitrary files. It should use the frozen inputs in this audit and recheck the Chenyu `DATA_DIR` before reading the raw MetaTraits TSV gzip files.
