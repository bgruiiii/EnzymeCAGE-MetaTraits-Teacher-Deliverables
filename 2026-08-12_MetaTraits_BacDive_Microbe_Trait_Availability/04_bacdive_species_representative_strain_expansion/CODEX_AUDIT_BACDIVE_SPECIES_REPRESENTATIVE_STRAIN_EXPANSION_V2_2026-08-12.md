# Codex Audit: BacDive Species-Level Representative Strain Expansion v2

Date: 2026-08-12

Audited directory:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/16_MetaTraits_Integration_Research_2026-07-15/bacdive_metatraits_hybrid_probe_2026-08-12/bacdive_species_representative_strain_expansion_2026-08-12/
```

Input closure result:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/16_MetaTraits_Integration_Research_2026-07-15/bacdive_metatraits_hybrid_probe_2026-08-12/bacdive_full_closure_2478_2026-08-12/bacdive_full_closure_results.jsonl
```

## 1. Audit conclusion

The v2 species-level representative strain expansion is usable as the current BacDive availability/provenance expansion result.

Main conclusion:

```text
For all 1,149 BacDive species-level validated source_signatures, v2 found at least one representative BacDive strain record and at least one culture collection number.
```

This result supports the intended hybrid design:

```text
MetaTraits = primary species-level trait matrix
BacDive = strain identity, representative strain availability, culture collection numbers, culture medium, isolation/source metadata
```

Important boundary:

Species-level representative strain records must not be described as the exact original UniProt strain unless the source already has exact-strain evidence from the BacDive closure table. For these 1,149 rows, the correct label is species-level representative BacDive strain availability.

## 2. Why v2 was needed

An initial expansion pass used a stricter species-name filter. That first pass incorrectly produced 9 source_signatures with zero representative records, even though the cache contained BacDive records.

Cause:

- Some BacDive records use older names, renamed genera, subspecies names, or synonym-equivalent species labels.
- The closure step had already validated these rows by species name normalization, TaxID evidence, synonym evidence, or validated BacDive IDs.
- A strict `source_species_normalized == bacdive_species_normalized` filter was too narrow for representative strain expansion.

v2 fixed this by allowing inclusion when at least one of the following evidence routes holds:

| Inclusion basis | Meaning | Record count |
|---|---|---:|
| `normalized_species_exact` | Source species and BacDive species match after normalization | 46,243 |
| `base_binomial_match_or_subspecies` | BacDive record is a subspecies / binomial-compatible record under the same base species | 3,535 |
| `validated_bacdive_id_from_closure` | Record BacDive ID is already in the closure-validated BacDive ID list | 2,779 |
| `validated_bacdive_species_exact` | Record matches the closure-validated BacDive species label | 399 |

This is a controlled expansion, not an unrestricted same-genus expansion.

## 3. Output files checked

| File | Description | Status |
|---|---|---|
| `bacdive_species_representative_expansion_summary_v2.json` | v2 aggregate summary | present |
| `bacdive_species_representative_source_summary_v2.csv` | one row per species-level source_signature | present |
| `bacdive_species_representative_strain_records_v2.csv` | expanded BacDive strain-record table | present |
| `bacdive_species_representative_strain_records_v2.jsonl` | JSONL version of expanded strain records | present |

## 4. Scope

The expansion targets species-level BacDive validated rows only:

```text
bacdive_species_exact_name_match
bacdive_species_taxid_or_synonym_match
```

Exact-strain rows are not the main target of this expansion because they already have an exact-strain identity route in the closure table.

Species-level expansion scope:

| Metric | Count |
|---|---:|
| source_signatures | 1,149 |
| row-weighted enzyme-source rows | 68,788 |
| `bacdive_species_exact_name_match` | 1,101 |
| `bacdive_species_taxid_or_synonym_match` | 48 |

## 5. Representative strain expansion results

v2 expanded the 1,149 species-level source_signatures to:

```text
52,956 representative BacDive strain-record rows
```

Source-level availability:

| Metric | Source count | Fraction among 1,149 |
|---|---:|---:|
| at least one representative BacDive record | 1,149 | 100.0% |
| at least one culture collection number | 1,149 | 100.0% |
| at least one type-strain record | 1,099 | 95.6% |
| at least one culture medium | 1,067 | 92.9% |
| at least one isolation source | 1,089 | 94.8% |
| at least one country / geographic source | 1,030 | 89.6% |
| at least one genome accession | 1,086 | 94.5% |

Representative record count per source:

| Statistic | Value |
|---|---:|
| minimum | 1 |
| median | 12 |
| mean | 46.09 |
| maximum | 201 |

Unique culture collection numbers per source:

| Statistic | Value |
|---|---:|
| minimum | 1 |
| median | 32 |
| mean | 88.28 |
| maximum | 443 |

## 6. Distribution of available representative records

Representative BacDive record count per source:

| Bucket | Source count |
|---|---:|
| 1 | 186 |
| 2-5 | 233 |
| 6-10 | 123 |
| 11-50 | 296 |
| 51-100 | 117 |
| >100 | 194 |

Unique culture collection number count per source:

| Bucket | Source count |
|---|---:|
| 1 | 25 |
| 2-5 | 158 |
| 6-10 | 91 |
| 11-50 | 412 |
| 51-100 | 146 |
| >100 | 317 |

Interpretation:

- Species-level BacDive hits usually provide more than one representative strain option.
- The median source has 12 representative BacDive records and 32 unique culture collection numbers.
- A small number of well-studied species, such as *Escherichia coli*, *Staphylococcus aureus*, *Salmonella enterica*, *Klebsiella pneumoniae*, and *Listeria monocytogenes*, have very large representative-strain record sets.

## 7. Culture collection interpretation

v2 confirms that species-level BacDive coverage is highly useful for practical strain availability:

```text
1,149 / 1,149 species-level BacDive hits have at least one culture collection number.
```

This does not mean the exact original UniProt source strain is always recoverable. It means:

```text
For every BacDive species-level validated source in this expansion, BacDive provides at least one representative strain record with a culture collection number under that validated species context.
```

Recommended downstream label:

```text
bacdive_species_representative_strain_available = true
```

For exact-strain closure rows, use separate labels such as:

```text
bacdive_exact_strain_main
bacdive_exact_strain_conservative
bacdive_exact_strain_hard
```

## 8. Metadata availability

BacDive also provides useful metadata beyond culture collection numbers:

| Metadata type | Source count | Fraction among 1,149 |
|---|---:|---:|
| culture medium | 1,067 | 92.9% |
| isolation source | 1,089 | 94.8% |
| country | 1,030 | 89.6% |
| genome accession | 1,086 | 94.5% |
| type-strain record | 1,099 | 95.6% |

This supports using BacDive as a provenance and practical-availability layer, not merely as a trait database.

## 9. Audit notes

The v2 summary reports:

```text
audit_notes_count = 0
```

No cache parsing errors were reported during v2 extraction.

Additional sanity checks performed:

- `bacdive_species_representative_source_summary_v2.csv` contains 1,149 rows.
- `bacdive_species_representative_strain_records_v2.csv` contains 52,956 expanded strain-record rows.
- no source has zero representative BacDive records in v2.
- no source lacks culture collection numbers in v2.
- inclusion basis is explicitly recorded per strain record.

## 10. Caveats

1. This is an availability/provenance expansion, not a replacement for MetaTraits.

   BacDive representative strain records provide useful practical information, but they should not become the primary high-dimensional species trait matrix.

2. Species-level representative records are not exact-strain evidence.

   If the original UniProt source cannot be locked to an exact BacDive strain, the representative records should be labeled as species-level availability only.

3. Large species can dominate the expanded strain-record table.

   Species such as *E. coli* may have hundreds of records. For downstream feature construction, use source-level summaries or capped/top-k representative records rather than letting record count inflate model weights.

4. Synonym/subspecies inclusion is intentional but must remain labeled.

   v2 includes records via exact normalized species, subspecies/base-binomial match, closure-validated BacDive IDs, or closure-validated BacDive species labels. These routes should be retained as evidence fields.

## 11. Recommended next step

This v2 expansion is sufficient for the current BacDive availability conclusion. The next integration step should be schema design, not more BacDive querying:

```text
MetaTraits primary species traits
+ BacDive exact-strain evidence
+ BacDive species-level representative strain availability
+ BacDive culture collection numbers
+ BacDive culture medium
+ BacDive isolation source / country
```

Suggested feature / table fields:

| Field | Source | Meaning |
|---|---|---|
| `metatraits_trait_vector_available` | MetaTraits | species-level trait vector availability |
| `bacdive_exact_strain_policy` | BacDive closure | exact strain evidence tier |
| `bacdive_species_representative_available` | BacDive v2 expansion | species-level representative strain available |
| `bacdive_representative_record_count` | BacDive v2 expansion | number of representative BacDive records |
| `bacdive_culture_collection_count` | BacDive v2 expansion | number of unique culture collection numbers |
| `bacdive_has_type_strain_record` | BacDive v2 expansion | whether a type-strain record exists |
| `bacdive_has_culture_medium` | BacDive v2 expansion | culture medium available |
| `bacdive_has_isolation_source` | BacDive v2 expansion | isolation source available |
| `bacdive_has_country` | BacDive v2 expansion | geographic source available |
| `trait_resolution` | integration layer | species-level vs exact-strain evidence |

## 12. Final judgment

The v2 representative strain expansion closes the practical availability question for BacDive species-level hits:

```text
All 1,149 species-level BacDive validated source_signatures have at least one representative BacDive strain record and at least one culture collection number.
```

This result strengthens the hybrid plan:

```text
Use MetaTraits for broad species-level traits.
Use BacDive for exact-strain evidence and species-level representative strain availability/provenance.
```

