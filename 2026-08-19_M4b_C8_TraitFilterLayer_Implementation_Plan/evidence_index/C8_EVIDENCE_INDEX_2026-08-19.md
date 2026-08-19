# C8 Evidence Index

Date: 2026-08-19

Purpose: list the already accepted/frozen evidence used by the C8
TraitFilterLayer implementation plan.

## Teacher Authority

Included in this folder:

```text
authority_reference/TEACHER_REPLY_FULL_4681_ACCEPTANCE_AND_C7_1_FREEZE_2026-08-14.md
authority_reference/TEACHER_REPLY_C7_2_FREEZE_AND_1650_ACCESSION_REVIEW_2026-08-17.md
authority_reference/TEACHER_REPLY_NEXT_ACTIONS_2026-08-18.md
```

Key authority points:

```text
2026-08-14: 1,704 staged PASS enzyme assets accepted; C7-1 F1-F15 frozen.
2026-08-17: C7-2 feature encoding proposal frozen; bounded schema/validator authorized.
2026-08-18: C8 staged-only TraitFilterLayer implementation plan / breakdown requested.
```

## C7-1 Frozen Trait Panel

Repository path:

```text
../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/
```

Important files:

```text
C7_1_TRAIT_PANEL_CANDIDATE_TABLE_2026-08-14.csv
M4B_C7_1_TRAIT_PANEL_CANDIDATE_REPORT_2026-08-14.md
audits/M4B_C7_1_TRAIT_PANEL_CANDIDATE_LOCAL_AUDIT_2026-08-14.md
```

Use in C8:

```text
F1-F15 IDs are fixed.
First screen = F1-F5.
Detail-on-request = F6-F15.
Observed first; predicted soft-fill only where allowed.
```

## C7-2 Frozen Feature Encoding Contract

Repository path:

```text
../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/
```

Important file:

```text
M4B_C7_2_FEATURE_ENCODING_PROPOSAL_2026-08-15.md
```

Use in C8:

```text
reuse value_status five-state schema;
preserve F1-F15 explicit IDs;
preserve provenance;
keep fungi identity-only;
do not emit hard rejection, trait_score, or uncalibrated confidence.
```

## C7-2 Bounded Schema/Validator Proof

Repository path:

```text
../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/
```

Important files:

```text
POLICY_MANIFEST.json
TRAIN_SET_MANIFEST.csv
trait_annotation.jsonl
TRAIT_FEATURE_ENCODING_VALIDATION_REPORT.md
BOUNDARY_VALIDATION_REPORT.md
FINAL_STATUS.txt
LOCAL_AUDIT_C7_2_SCHEMA_VALIDATOR_BOUNDED_30_2026-08-18.md
```

Use in C8:

```text
this is the starting schema/validator implementation pattern;
C8 should extend it through a staged-only consumption contract, not replace it.
```

## MetaTraits TSV Landing And C7-1 Long-Form Mapping

Repository path:

```text
../2026-08-19_MetaTraits_Bulk_TSV_Landing_and_C7_1_Mapping_Correction/
```

Important files:

```text
metatraits_landing_metadata/METATRAITS_BULK_TSV_FILE_MANIFEST.csv
metatraits_landing_metadata/SHA256SUMS.txt
metatraits_landing_metadata/VALIDATION_REPORT.md
c7_1_mapping_rerun2/C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_RERUN2.md
c7_1_mapping_rerun2/METATRAITS_C7_1_NEGATIVE_ASSERTIONS_RERUN2.csv
audits/METATRAITS_BULK_TSV_LANDED_CHENYU_RETURN_LOCAL_AUDIT_2026-08-18.md
audits/METATRAITS_C7_1_LONG_FORM_MAPPING_RERUN2_FALSE_POSITIVE_FIX_RETURN_LOCAL_AUDIT_2026-08-19.md
```

Use in C8:

```text
MetaTraits data source is local TSV snapshot only.
Mapping must use long-form row fields, not header-only matching.
F3 pH false positives and F12 Gram false positives are fixed in rerun2.
```

## Microbe Universe And BacDive Evidence

Repository path:

```text
../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/
```

Important evidence:

```text
final clean microbe source universe = 2,478 source_signatures
MetaTraits coverage = 1,638 / 2,478
BacDive validated species-or-better = 1,746 / 2,478
BacDive exact_strain_main = 597 / 2,478
BacDive hard exact strain = 555 / 2,478
```

Use in C8:

```text
BacDive supports F5 availability / culture collection evidence.
MetaTraits supports species-level trait evidence.
Species-level and representative-strain evidence must be labelled and not
silently upgraded to exact strain.
```
