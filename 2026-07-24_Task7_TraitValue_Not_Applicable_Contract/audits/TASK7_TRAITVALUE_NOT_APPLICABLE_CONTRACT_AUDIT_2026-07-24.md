# Task 7 TraitValue `not_applicable` Contract Audit

Date: 2026-07-24
Audited object: repository-root
`TRAIT_VALUE_NOT_APPLICABLE_SCHEMA_CONTRACT.md`
Verdict: PASS at contract-delivery level; teacher acceptance not yet claimed

## 1. Authority scope

The controlling 2026-07-23 adjudication authorizes only:

```text
TraitValue schema revision contract
+ reason/note field definitions
+ one not_applicable example
```

It explicitly defers Pydantic runtime code, field-validation tests,
`MicrobeTraitTool`, and M4b integration. The 2026-07-24 supplement repeats
that boundary and does not supersede it.

## 2. Requirement-by-requirement audit

| Check | Result | Contract evidence |
|---|---|---|
| Contract status is explicit | PASS | Header states `CONTRACT_ONLY_APPROVED / CODE_DEFERRED_TO_M4B`. |
| `trait_name` is defined | PASS | Section 2 defines a required non-empty string. |
| `value` and `not_applicable` are defined | PASS | Section 2 defines the sentinel as an evidence boundary, not biological absence. |
| `reason` is defined | PASS | Section 2 makes it conditionally required and requires an evidence-chain explanation. |
| `note` is defined | PASS | Section 2 makes it conditionally required and fixes the required limiting sentence. |
| Conditional schema rule is present | PASS | Section 2 includes a language-neutral `if value / then required` schema block. |
| Teacher-specified example is present | PASS | Section 4 contains all four requested lines. |
| Exact-tax-ID semantics are retained | PASS | Section 3 forbids species/strain cross-inheritance. |
| Example reason is not overgeneralized | PASS | Section 3 permits the species/strain wording only after both checks were actually established. |
| Accepted schema v1.1 remains intact | PASS | Sections 1 and 5 keep source/provenance, `is_ai`, and `majority_label` independent. |
| Retired three-state `evidence` is not restored | PASS | Sections 1 and 5 explicitly reject it. |
| No unapproved confidence float is added | PASS | Section 5 explicitly excludes `confidence` and `organism_confidence`. |
| No runtime implementation is claimed | PASS | Section 6 lists all deferred implementation work. |

## 3. Boundary audit

The dated Task 7 delivery contains Markdown and a checksum manifest only.
It adds no `.py` source file and no test file. No query, filtering, model, HPC,
M4b, or M4c execution was performed for this task.

The contract's YAML snippets are documentation examples only; they are not
runtime schemas or executable code.

## 4. Semantic audit

The following statements were checked together:

```text
not_applicable = current evidence chain cannot assign the trait
not_applicable != the organism biologically lacks the trait
species tax_id != strain tax_id
related-taxon provenance != permission to inherit
No robust majority != not_applicable
is_ai != majority_label
```

No contradiction was found among the Task 7 contract, MT-TQ-06, MT-TQ-07,
the accepted schema v1.1 patch, or the MT-D2 no-confidence decision.

## 5. Audit conclusion

Task 7 is complete only at the teacher-authorized contract layer. Runtime code
and tests remain `CODE_DEFERRED_TO_M4B`; this audit does not claim M4b start,
M4c start, or teacher acceptance of this new delivery.
