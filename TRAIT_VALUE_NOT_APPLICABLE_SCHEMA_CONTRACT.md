# TraitValue `not_applicable` Schema Revision Contract

Date: 2026-07-24
Status: `CONTRACT_ONLY_APPROVED / CODE_DEFERRED_TO_M4B`
Scope: Task 7 contract-layer delivery only

## 1. Authority and purpose

This document supplies the Task 7 deliverable authorized in
`TEACHER_REPLY_M3_TASKS_1_7_ACCEPTANCE_AND_TASK7_SCOPE_AND_SNAPSHOT_MTTQ02_2026-07-23.md`:
a `TraitValue` schema revision contract defining `reason` and `note`, plus one
`not_applicable` output example.

This is an additive contract-layer clarification of the accepted schema v1.1
`TraitRecord` decision. It does not restore the retired three-state `evidence`
field and does not merge the independent `is_ai`, `majority_label`,
`source_database`, `source_url`, `tax_id`, or source-value dimensions.

## 2. Normative field contract

The keywords MUST, MUST NOT, REQUIRED, and OPTIONAL are normative.

| Field | Contract type | Requirement |
|---|---|---|
| `trait_name` | non-empty string | REQUIRED. Identifies the queried trait, for example `oxygen_preference`. |
| `value` | source-native scalar/value, or the exact string `not_applicable` | REQUIRED. `not_applicable` is an evidence-boundary sentinel; it is not a biological absence assertion. |
| `reason` | non-empty string | REQUIRED when `value: not_applicable`. It MUST state the evidence-chain condition that prevents assignment to the exact queried taxon. It MUST NOT claim that the organism biologically lacks the trait. This Task 7 contract does not impose a new requirement on ordinary observed values. |
| `note` | non-empty string | REQUIRED when `value: not_applicable`, with the exact value `not_applicable 表示"当前证据链下无法归属"，不等于"生物学上不存在此性状"`. This Task 7 contract does not impose a new requirement on ordinary observed values. |

The conditional rule is:

```yaml
if:
  value: not_applicable
then:
  required:
    - reason
    - note
  note_must_equal: 'not_applicable 表示"当前证据链下无法归属"，不等于"生物学上不存在此性状"'
```

This YAML block is a language-neutral schema statement. It is not executable
Pydantic code.

## 3. Exact-tax-ID attribution rule

Trait attribution MUST use the exact queried taxon ID. A strain-level tax ID
and a species-level tax ID MUST NOT inherit trait records from one another.

The `reason` text MUST match the checks actually performed:

- `taxon-level record absent (species/strain 均无对应观测)` may be used only
  when the evidence lookup has established that neither the relevant species
  record nor the relevant strain record contains a corresponding observation;
- a record found only at a related species or strain may be disclosed as
  provenance, but MUST NOT be assigned to the exact queried tax ID;
- `not_applicable` records an inability to assign the trait under the current
  evidence chain. It MUST NOT be consumed as proof that the trait is
  biologically nonexistent.

## 4. Required output example

```yaml
trait_name: oxygen_preference
value: not_applicable
reason: taxon-level record absent (species/strain 均无对应观测)
note: not_applicable 表示"当前证据链下无法归属"，不等于"生物学上不存在此性状"
```

## 5. Compatibility boundaries

This revision is limited to the `not_applicable` representation:

1. `is_ai` and `majority_label` remain independent dimensions and MUST NOT be
   collapsed into `value`, `reason`, or `note`.
2. `source_database`, `source_url`, `tax_id`, and source-value provenance
   remain independently traceable.
3. The retired
   `evidence: experimental | predicted | no_robust_majority` design MUST NOT
   be reintroduced.
4. No `confidence` or `organism_confidence` float is introduced by this
   contract.
5. This contract does not define new semantics for ordinary observed values,
   `No robust majority`, missing source provenance, or source conflict.

## 6. Explicit non-implementation boundary

This delivery contains no Pydantic implementation, field-validation test,
`MicrobeTraitTool` implementation, trait query, filtering behavior, model
call, M4b call-chain integration, or M4c work. Runtime implementation and
field-validation tests remain deferred until M4b is separately authorized.
