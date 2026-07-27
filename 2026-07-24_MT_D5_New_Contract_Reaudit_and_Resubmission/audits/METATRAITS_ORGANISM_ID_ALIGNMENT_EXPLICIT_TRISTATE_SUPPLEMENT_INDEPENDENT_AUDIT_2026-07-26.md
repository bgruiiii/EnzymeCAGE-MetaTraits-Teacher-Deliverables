# MetaTraits Organism-ID Explicit Tri-State Supplement Independent Audit

Audit date: 2026-07-26  
Audited objects:

```text
ORGANISM_ID_ALIGNMENT_EXPLICIT_TRISTATE_SUPPLEMENT_2026-07-26.md
P0_TOP_MRR_ENZYME_TO_HOST_METATRAITS_CROSSWALK.csv
metatraits_probe_report.md
```

Verdict:

```text
TEN_ROWS_PARSED_PASS
THREE_ALLOWED_CLASSES_EXPLICIT_PASS
EXACT_STRAIN_COUNT_0_PASS
EXACT_SPECIES_COUNT_0_PASS
NO_EXACT_MATCH_ESTABLISHED_COUNT_10_PASS
SPECIES_NAME_CONTEXTUAL_COUNT_5_PASS
NO_SUMMARY_COUNT_5_PASS
ALL_DOCUMENTED_TAXID_STATUS_404_PASS
STRAIN_SPECIES_NONINHERITANCE_PASS
NO_DATABASE_ABSENCE_CLAIM_PASS
ORIGINAL_JSON_IDENTITIES_UNCHANGED_PASS
NO_NEW_NETWORK_OR_HPC_PASS
```

## 1. Why this supplement was required

The previous crosswalk correctly retained:

```text
taxid_api_404_species_name_summary_only
taxid_api_404_no_delivered_summary
```

but did not expose the teacher-facing three-class field directly. The
underlying direct-query work was complete; the missing part was explicit
classification, not a missing network probe.

## 2. Mechanical recomputation

The CSV was parsed as a strict header plus ten data rows. The allowed values
for `metatraits_exact_id_alignment_class` are:

```text
exact_strain
exact_species
no_exact_match_established
```

Recomputed counts:

```text
rows:
  10

documented_taxid_api_status == 404:
  10

metatraits_exact_id_alignment_class:
  exact_strain                    0
  exact_species                   0
  no_exact_match_established     10

metatraits_id_alignment_state:
  taxid_api_404_species_name_summary_only     5
  taxid_api_404_no_delivered_summary          5

metatraits_summary_included:
  yes     5
  no      5
```

No row was classified from organism-name text alone.

## 3. Semantic audit

The supplement defines an exact class only by equality between the queried
UniProt NCBI TaxID and a returned metaTraits record TaxID at the corresponding
taxon rank. It expressly forbids species-to-strain and strain-to-species
inheritance.

Because:

- all ten documented direct TaxID calls returned HTTP 404;
- the five working summaries were species-name queries;
- summary objects have no `tax_id`;

the current evidence establishes zero exact-strain matches and zero
exact-species matches.

`no_exact_match_established` is correctly defined as an evidence-chain result,
not proof that metaTraits lacks the organism or trait.

## 4. Source separation

The audit confirmed that:

```text
enzyme_to_host_mapping_state:
  concerns UniProt/KEGG host mapping

metatraits_id_alignment_state:
  records the bounded query outcome

metatraits_exact_id_alignment_class:
  records the normalized exact-ID conclusion
```

The nine `exact` enzyme-to-host mapping states were not misrepresented as
exact metaTraits trait alignment. The disclosed `P29931`
`MAPPING_DRIFT_OR_CONFLICT` state remains unchanged.

## 5. Preservation audit

The five accepted original metaTraits JSON bodies retain these SHA256
identities:

```text
Q8EFP8       0d0eeecd9b5cd6314d71e680119b5fd155fac2980f59581436501ed2f42d0604
Q12WS1      c3da972bb5214ef65f9631b48882dbd8eec96e2ebe0edb38901856ae96ec9e6b
A0A0H3C8X0  99ca0fb51622ba9d30eba9befabe6e90f96750eac96f1af31f8638807479a0e5
Q6BQK1      28b4e749f70dafba8ad5ccf5c1948ce9ce8623709959687c4ebfd718ca1f8735
P71875      414606627724f0ada3dcbc5be618291d94378fa60b0756e9dd62741fd4faa202
```

No original HTTP response, request ledger, UniProt evidence or teacher
authority file was rewritten.

## 6. Execution boundary

This correction used only deterministic local parsing of delivered files. It
did not perform:

```text
network request
HPC/GPU execution
model inference
M4b/M4c implementation
trait assignment
hard filtering
GitHub push
```

## 7. Final conclusion

The ID-alignment work is now explicit at both row and aggregate level:

```text
exact strain:
  0
exact species:
  0
no exact match established:
  10
```

The result remains a completed negative finding, not a working production
`organism_uid -> traits` path.
