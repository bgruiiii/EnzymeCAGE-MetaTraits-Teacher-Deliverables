# Codex Local Audit: BacDive Full Closure 2,478 Source Signatures

Date: 2026-08-12

Audited result directory:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/16_MetaTraits_Integration_Research_2026-07-15/bacdive_metatraits_hybrid_probe_2026-08-12/bacdive_full_closure_2478_2026-08-12/
```

## 1. Audit conclusion

The latest local AI closure result is usable as the current BacDive full-table evidence closure baseline.

Core status:

```text
Overall audit judgment: PASS WITH ONE REPORTING CAVEAT
```

The result correctly preserves the 2,478-source universe, recomputes closure statuses, separates weak designation evidence, rescues a subset of previously unvalidated species candidates with documented evidence, and computes BacDive / MetaTraits overlap without using MetaTraits as a fallback to alter BacDive fields.

The main caveat is about trait-coverage interpretation: `bacdive_full_closure_trait_coverage.csv` reports the 12 configured BacDive trait fields by policy bin, but the `unique_traits=12` value should not be read as “all 12 fields are non-empty”. For true trait availability, use non-empty `trait_summary` values from `bacdive_full_closure_results.jsonl`.

## 2. Files checked

All expected closure files are present:

| File | Status |
|---|---|
| `bacdive_full_closure_results.jsonl` | present |
| `bacdive_full_closure_summary.json` | present |
| `bacdive_full_closure_report.md` | present |
| `bacdive_full_closure_audit.md` | present |
| `bacdive_full_designation_confidence.csv` | present |
| `bacdive_candidate_rescue_review.csv` | present |
| `bacdive_candidate_rescue_synonym_rules.csv` | present |
| `bacdive_metatraits_overlap_summary.json` | present |
| `bacdive_metatraits_overlap_by_source_signature.csv` | present |
| `bacdive_metatraits_overlap_by_group.csv` | present |
| `bacdive_metatraits_overlap_examples.csv` | present |

## 3. Input universe integrity

Recomputed from `bacdive_full_closure_results.jsonl`:

```text
source_signature rows: 2,478
row_count sum: 145,607
```

This matches the expected final clean EnzymeCAGE microbe-side universe.

## 4. Closure status counts

Recomputed status counts match `bacdive_full_closure_summary.json`.

| Status | Count |
|---|---:|
| `bacdive_species_exact_name_match` | 1,101 |
| `bacdive_exact_culture_collection` | 386 |
| `bacdive_exact_genome` | 169 |
| `bacdive_species_taxid_or_synonym_match` | 48 |
| `bacdive_exact_designation` | 42 |
| `bacdive_species_candidate_unvalidated` | 35 |
| `bacdive_not_found` | 269 |
| `not_applicable_fungi_or_non_bacdive_scope` | 428 |

The validated species-or-better count after candidate rescue is:

```text
1,746 / 2,478 = 70.5%
row-weighted: 121,243 / 145,607 = 83.3%
```

## 5. Exact strain evidence

Exact strain policy counts:

| Policy | Count | Fraction |
|---|---:|---:|
| exact_strain_main | 597 / 2,478 | 24.1% |
| exact_strain_conservative | 592 / 2,478 | 23.9% |
| exact_strain_hard | 555 / 2,478 | 22.4% |

Policy interpretation:

- `exact_strain_main` includes genome accession exact matches, culture collection exact matches, and all exact designation matches.
- `exact_strain_conservative` excludes weak short-token designation matches.
- `exact_strain_hard` includes only genome accession and culture collection exact matches.

Designation-confidence binning was present for all 42 exact-designation rows:

| Designation confidence | Count |
|---|---:|
| `designation_strong` | 25 |
| `designation_medium` | 12 |
| `designation_weak_short_token` | 5 |

The 5 weak designation rows are correctly treated as weaker evidence and should not be used as hard exact-strain evidence.

Weak examples observed during audit:

| source_signature | source organism | BacDive strain designation | overlap token |
|---|---|---|---|
| `proteome:UP000001260` | Chlamydia felis strain Fe/C-56 | Fe/Pn-1, FP Baker | `fe` |
| `proteome:UP000001933` | Syntrophus aciditrophicus strain SB | SB | `sb` |
| `proteome:UP000008321` | Salmonella gallinarum strain 287/91 / NCTC 13346 | M491, 91 | `91` |
| `taxon:469008|organism:escherichia coli (strain b / bl21-de3)` | Escherichia coli strain B / BL21-DE3 | B | `b` |
| `taxon:413997|organism:escherichia coli (strain b / rel606)` | Escherichia coli strain B / REL606 | B | `b` |

These are useful as diagnostic or main-policy matches, but should remain excluded from conservative exact-strain claims unless supported by culture collection or genome accession evidence.

## 6. Candidate rescue audit

Original candidate-unvalidated rows:

```text
56
```

Closure outcome:

```text
rescued_to_validated_species: 21
remains_candidate_unvalidated: 35
```

The local AI audit reports that no rescue was based only on same-genus matching and that no rescued row lacks evidence. This is consistent with the reviewed closure summary.

Important interpretation:

- Candidate rescue promotes rows only to validated species-level evidence.
- Candidate rescue should not be interpreted as exact-strain evidence.
- The remaining 35 candidate-unvalidated rows should stay diagnostic-only unless additional taxonomy evidence is added.

## 7. Culture collection / strain availability evidence

Culture collection availability is strong among BacDive-validated records.

Recomputed from `bacdive_full_closure_results.jsonl`:

| Scope | Source count | With BacDive culture collection numbers | Fraction |
|---|---:|---:|---:|
| all source_signatures | 2,478 | 1,771 | 71.5% |
| validated species-or-better | 1,746 | 1,737 | 99.5% |

Interpretation:

- BacDive should not be claimed to recover the exact original UniProt strain for all covered rows.
- However, for BacDive validated species-or-better rows, almost all have one or more BacDive culture collection numbers.
- For species-level matches, these should be labeled as species-level representative BacDive strain records, not as exact source strain records.

This supports using BacDive as a dedicated source for:

- exact strain evidence where available;
- culture collection numbers;
- representative strain availability at species level;
- culture medium;
- isolation source;
- country / geographic source.

## 8. BacDive / MetaTraits overlap audit

The overlap file reports a successful match between the BacDive universe and the MetaTraits coverage table:

```text
BacDive source_signatures: 2,478
MetaTraits coverage file rows: 3,234
BacDive signatures found in MetaTraits file: 2,478
MetaTraits coverage column: union_in_ncbi_all
```

Main-policy overlap:

| Category | Source count |
|---|---:|
| both covered | 1,508 |
| BacDive only | 238 |
| MetaTraits only | 130 |
| neither | 602 |

Row-weighted main-policy overlap:

| Category | Row-weighted count |
|---|---:|
| both covered | 107,812 |
| BacDive only | 13,431 |
| MetaTraits only | 6,513 |
| neither | 17,851 |

Interpretation:

- BacDive and MetaTraits are complementary.
- BacDive adds 238 source signatures not covered by MetaTraits.
- MetaTraits adds 130 source signatures not covered by BacDive.
- The 602 neither-covered rows remain the principal availability gap.

## 9. Trait coverage caveat

The closure report's `Trait Coverage Recomputation` section lists `unique_traits=12` for multiple policy bins. This reflects the 12 configured BacDive extraction fields, not necessarily 12 non-empty fields per source.

A direct non-empty-value recomputation from `trait_summary` gives the following counts for validated species-or-better rows:

| BacDive trait field | Non-empty source count |
|---|---:|
| `temperature_range` | 1,391 |
| `isolation_source` | 1,346 |
| `country` | 1,346 |
| `culture_medium` | 1,159 |
| `oxygen_tolerance` | 754 |
| `metabolite_utilization` | 743 |
| `gram_stain` | 446 |
| `cell_shape` | 429 |
| `motility` | 413 |
| `temperature_optimum` | 0 |
| `biosafety_or_pathogenicity` | 0 |
| `enzyme_activity` | 0 |

Therefore, for final reporting and feature-design decisions, use this non-empty-value table rather than treating `unique_traits=12` as actual coverage.

## 10. Design implication

The latest result supports the current hybrid design:

```text
MetaTraits = primary species-level trait matrix
BacDive = strain identity + culture collection + culture medium + isolation/source metadata
```

Recommended interpretation:

- MetaTraits should remain the main source for broad species-level trait vectors.
- BacDive should be used to add availability and provenance evidence, especially culture collection numbers and representative strain records.
- Exact-strain BacDive matches should be separated from species-level representative strain matches.
- Fungi should remain marked separately because BacDive is primarily prokaryote-oriented.

## 11. Next step

The next useful experiment is a BacDive species-level representative strain expansion:

For each BacDive validated species-level source, expand beyond the current primary BacDive record and extract one or more representative strain records under that species, including:

- BacDive ID;
- species name;
- strain designation;
- culture collection numbers;
- whether type-strain evidence is present, if available;
- genome accession, if available;
- culture medium;
- isolation source;
- country.

This will answer whether species-level fallback can provide multiple practical, obtainable strain options rather than only one primary matched BacDive record.

