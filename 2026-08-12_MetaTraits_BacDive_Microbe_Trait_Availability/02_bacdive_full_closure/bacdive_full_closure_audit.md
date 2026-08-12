# BacDive Full Closure Audit

Date: 2026-08-12

Output directory: `/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/16_MetaTraits_Integration_Research_2026-07-15/bacdive_metatraits_hybrid_probe_2026-08-12/bacdive_full_closure_2478_2026-08-12`

## Audit Results

| # | Check | Result | Detail |
|---|-------|--------|--------|
| 1 | input BacDive rows == 2478 | PASS | actual=2478 |
| 2 | row_count sum == 145607 | PASS | actual=145607 |
| 3 | all original BacDive rows preserved | PASS | rows=2478, expected=2478 |
| 4 | every exact_designation row has designation_confidence != empty | PASS | missing=0 |
| 5 | every weak designation row is excluded from conservative exact policy | PASS | weak_in_cons=0 |
| 6 | no candidate rescue lacks candidate_rescue_evidence | PASS | missing_evidence=0 |
| 7 | no rescued candidate is based only on same genus | PASS | same_genus_rescues=0 |
| 8 | candidate_unvalidated remaining count is reported | PASS | remaining=35 |
| 9 | summary counts equal JSONL counts | PASS | jsonl={'bacdive_species_exact_name_match': 1101, 'not_applicable_fungi_or_non_bacdive_scope': 428, 'bacdive_exact_culture_collection': 386, 'bacdive_exact_genome': 169, 'bacdive_not_found': 269, 'bacdive_exact_designation': 42, 'bacdive_species_taxid_or_synonym_match': 48, 'bacdive_species_candidate_unvalidated': 35} |
| 10 | row-weighted total sums to 145607 | PASS | total=145607 |
| 11 | MetaTraits overlap input rows match source_signature universe or mismatch is reported | PASS | matched=2478, mismatched=0, reported_in_summary=True |
| 12 | MetaTraits is not used as fallback to alter BacDive trait fields | PASS | MetaTraits coverage only used for overlap comparison, not trait merging |
| 13 | final report contains no casual audience-specific wording | PASS | checked in bacdive_full_closure_report.md; no casual audience-specific phrases |

**Overall: ALL PASS**
