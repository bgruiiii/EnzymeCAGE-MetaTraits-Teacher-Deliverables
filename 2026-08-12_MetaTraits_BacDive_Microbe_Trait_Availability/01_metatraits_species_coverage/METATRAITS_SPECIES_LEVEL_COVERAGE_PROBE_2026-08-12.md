# MetaTraits species-level coverage probe against EnzymeCAGE microbe-side host tables

Date: 2026-08-12  
Scope: local read-only availability probe.  
Question: if MetaTraits cannot reliably resolve strain-level traits, how much of our microbe-side host set can be covered at species level?

## 1. Inputs used

### EnzymeCAGE microbe-side source tables

Early taxonomy-filtered source catalog:

```text
data/processed/rhea/2026-01-21/microbe/taxonomy_filter_2026-04-28/source_signature_catalog_keep_bacteria_fungi_archaea.csv
```

This is the table produced after UniProt/Rhea enzyme hosts were mapped to organism metadata and filtered to keep only:

```text
Bacteria + Fungi + Archaea
```

Companion UID-level table:

```text
data/processed/rhea/2026-01-21/microbe/taxonomy_filter_2026-04-28/uid_to_source_keep_bacteria_fungi_archaea.csv
```

Final clean training package source table:

```text
custom/github_upload/reaction_enzyme_microbe_training_clean_2026-06-01/tables/enzyme_to_microbe_source.csv
```

### MetaTraits local snapshot

```text
data/metatraits/ncbi_species_summary_all.tsv.gz
data/metatraits/ncbi_species_summary_no_predictions.tsv.gz
data/metatraits/NCBI2GTDB.tsv.gz
data/metatraits/GTDB2NCBI.tsv.gz
data/metatraits/gtdb_species_summary_no_predictions.tsv.gz
```

Main trait tables used for this probe:

```text
ncbi_species_summary_all.tsv.gz
ncbi_species_summary_no_predictions.tsv.gz
```

Both are species-level summary tables, not strain-level observation tables.

## 2. Matching policy

Because our UniProt `TaxID` can often be strain-level while MetaTraits NCBI summary is species-level, three matching signals were checked:

1. Direct `TaxID` match.
2. Species name extracted from UniProt lineage, e.g. the lineage part ending in `(species)`.
3. Parentheses-stripped organism name fallback, e.g. removing `(strain ...)`, synonym, or common-name parentheticals.

The main reported coverage uses the union of these signals.

Important caveat:

> Direct TaxID matching alone underestimates species-level availability, because many UniProt TaxIDs are strain TaxIDs while MetaTraits stores species TaxIDs.

## 3. Early taxonomy-filtered source catalog coverage

Denominator:

```text
source_signature rows = 3,234
UID-weighted enzyme hosts = 168,335
taxonomy groups:
  target_bacteria = 2,481 source signatures
  target_fungi    =   575 source signatures
  target_archaea  =   178 source signatures
```

MetaTraits NCBI species summary availability:

| Match mode | Source-signature coverage | UID-weighted coverage |
|---|---:|---:|
| Direct TaxID only | 799/3,234 = 24.7% | 5,962/168,335 = 3.5% |
| Lineage species name | 1,925/3,234 = 59.5% | 131,629/168,335 = 78.2% |
| Organism stripped name | 1,587/3,234 = 49.1% | 89,517/168,335 = 53.2% |
| Union | 1,956/3,234 = 60.5% | 132,001/168,335 = 78.4% |

By taxonomy group, the union-matched set is:

```text
target_bacteria = 1,886
target_archaea  =    70
target_fungi    =     0
```

Missing set:

```text
target_bacteria = 595
target_archaea  = 108
target_fungi    = 575
```

Interpretation:

> At species level, MetaTraits covers a majority of bacterial source signatures and a smaller subset of archaeal source signatures, but this local MetaTraits snapshot effectively does not cover the fungal source signatures.

## 4. Final clean training table coverage

Denominator from final clean package:

```text
unique source_signatures = 2,478
example rows = 145,607
taxonomy groups:
  target_bacteria = 1,897 source signatures
  target_fungi    =   428 source signatures
  target_archaea  =   153 source signatures
```

MetaTraits NCBI species summary availability:

```text
matched source_signatures = 1,638 / 2,478 = 66.1%
matched example rows      = 114,325 / 145,607 = 78.5%
```

Matched taxonomy groups:

```text
target_bacteria = 1,575
target_archaea  =    63
target_fungi    =     0
```

Unique species-name denominator in the final clean table:

```text
unique species guesses = 1,722
matched species        = 1,070 / 1,722 = 62.1%
row-weighted matched   = 114,367 / 145,607 = 78.5%
```

## 5. Trait richness among matched source signatures

For matched early source signatures against `ncbi_species_summary_all.tsv.gz`:

```text
matched source signatures = 1,956
minimum trait rows        = 1
median trait rows         = 154
maximum trait rows        = 219
```

Trait-count bins:

```text
>100 traits  = 1,861 source signatures
51-100       =    43
11-50        =    24
1-10         =    28
```

Interpretation:

> Once a bacterial/archaeal species is present in MetaTraits, it usually has a rich species-level trait profile, not just one or two fields.

## 6. Main conclusion

The species-level MetaTraits route is useful, but bounded.

Recommended framing:

> MetaTraits cannot close strain-level exact trait assignment for our enzyme hosts, but a species-level enrichment route is feasible. On the early bacteria/fungi/archaea source catalog it covers about 60.5% of source signatures and 78.4% of UID-weighted enzyme hosts. On the final clean training table it covers about 66.1% of source signatures and 78.5% of example rows. Coverage is concentrated in bacteria and some archaea; fungi are essentially not covered by the local MetaTraits species snapshot.

Therefore, this should be treated as:

```text
species-level contextual microbe trait enrichment
```

not:

```text
strain-level exact host trait evidence
```

## 7. Outputs generated by this probe

Machine-readable summary:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/16_MetaTraits_Integration_Research_2026-07-15/metatraits_species_coverage_probe_2026-08-12/coverage_summary.json
```

Per-source coverage table:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/16_MetaTraits_Integration_Research_2026-07-15/metatraits_species_coverage_probe_2026-08-12/source_signature_metatraits_coverage.csv
```

