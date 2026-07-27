# MT-D5 New-Contract Reaudit and Resubmission

Date: 2026-07-24

Status: student resubmission; teacher acceptance not yet claimed

## Teacher entry points

- [`metatraits_probe_report.md`](metatraits_probe_report.md): current
  new-contract report and bounded usefulness decision.
- [`P0_TOP_MRR_ENZYME_TO_HOST_METATRAITS_CROSSWALK.csv`](P0_TOP_MRR_ENZYME_TO_HOST_METATRAITS_CROSSWALK.csv):
  frozen positive labels, exact UniProt target-RHEA references and ranks for
  ten P0 enzymes, ten UniProt hosts, the five metaTraits samples and all ten
  documented TaxID API outcomes, including the explicit
  `exact_strain`/`exact_species`/`no_exact_match_established` result class.
- [`ORGANISM_ID_ALIGNMENT_EXPLICIT_TRISTATE_SUPPLEMENT_2026-07-26.md`](ORGANISM_ID_ALIGNMENT_EXPLICIT_TRISTATE_SUPPLEMENT_2026-07-26.md):
  three-class definitions, ten-row result, aggregate counts and the
  species/strain non-inheritance boundary.
- [`audits/METATRAITS_D5_NEW_CONTRACT_INDEPENDENT_REAUDIT_2026-07-24.md`](audits/METATRAITS_D5_NEW_CONTRACT_INDEPENDENT_REAUDIT_2026-07-24.md):
  requirement-by-requirement audit.
- [`audits/METATRAITS_ORGANISM_ID_ALIGNMENT_EXPLICIT_TRISTATE_SUPPLEMENT_INDEPENDENT_AUDIT_2026-07-26.md`](audits/METATRAITS_ORGANISM_ID_ALIGNMENT_EXPLICIT_TRISTATE_SUPPLEMENT_INDEPENDENT_AUDIT_2026-07-26.md):
  independent mechanical and semantic audit of the explicit ID classes.
- [`DELIVERABLE_SHA256SUMS.txt`](DELIVERABLE_SHA256SUMS.txt): identities for
  this report, crosswalk, supplements, audits, the combined P0 index and the
  five original JSON bodies.

## Original JSON bodies

The five original HTTP response bodies remain directly visible at their
byte-preserving paths:

```text
../2026-07-24_MT_D5_Accepted_Evidence_Resubmission/raw/metatraits/samples/
```

They are included by path and SHA256 in this resubmission manifest. They were
not downloaded again or rewritten.

## Preservation boundary

The repository-root historical `metatraits_probe_report.md` remains the
byte-identical 2026-07-16 accepted report. This dated report is the current
2026-07-24 new-contract interpretation. No historical commit or evidence body
was overwritten.
