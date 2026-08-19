# M4b C8 TraitFilterLayer Implementation Plan Local Audit

Date: 2026-08-19

Audited document:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/01_Path_Contract_Objective/M4b_C8_TraitFilterLayer_Implementation_Plan_2026-08-19/M4B_C8_TRAITFILTERLAYER_IMPLEMENTATION_PLAN_AND_TASK_BREAKDOWN_2026-08-19.md
```

## Verdict

**PASS for teacher-facing C8 implementation plan / task breakdown review.**

The document answers the 2026-08-18 teacher requirement:

```text
08-20 前：提交 C8 实装方案 / 拆解待审
```

It does not claim that C8 has already been implemented. It keeps the C8 route
staged-only and preserves all active C7-1/C7-2 boundaries.

## Authority Alignment

Checked against:

```text
TEACHER_REPLY_FULL_4681_ACCEPTANCE_AND_C7_1_FREEZE_2026-08-14.md
TEACHER_REPLY_C7_2_FREEZE_AND_1650_ACCESSION_REVIEW_2026-08-17.md
TEACHER_REPLY_NEXT_ACTIONS_2026-08-18.md
M4B_C7_2_FEATURE_ENCODING_PROPOSAL_2026-08-15.md
C7_2_SCHEMA_VALIDATOR_BOUNDED_30_ENVIRONMENT_INDUSTRIAL_BACTERIA_STAGED_ONLY_2026-08-18
MetaTraits TSV landing and C7-1 mapping rerun2 audit packages
```

## Requirement Checks

| Requirement | Status | Audit note |
|---|---|---|
| C8 implementation plan / breakdown | PASS | Document splits C8 into C8-0 through C8-5 |
| Use C7-2 validator as entry point | PASS | Sections 3.3, 4, 8 and 9 cite C7-2 validator and reuse its schema |
| Use C7-1 frozen F1-F15 | PASS | Sections 2.1, 6 and 7 preserve all F1-F15 IDs |
| Staged-only | PASS | Repeated in status, boundary checks, non-claims and rollout |
| No production mutation | PASS | Explicitly forbidden in status, inputs, validator and non-claims |
| No API reliance | PASS | MetaTraits API and BacDive API are both forbidden for C8 inputs |
| Local MetaTraits TSV route | PASS | Uses Chenyu local TSV snapshot and rerun2 long-form mapping |
| Fungi identity-only | PASS | Explicit in policy, trait rules, validator and non-claims |
| F5 not predicted | PASS | F5 availability/culture collection observed-only |
| F8 boundary | PASS | Broad degradation context only; no exact pollutant degradation claim |
| F15 boundary | PASS | Low-coverage ecological background only; not ranking/scoring/recommendation |
| No hard rejection / trait_score / uncalibrated confidence | PASS | Explicitly disabled and validator-enforced |
| Gong Sai line separation | PASS | C8 consumes structured upstream candidate tables only; does not judge or implement fallback engine |

## Evidence Preservation

The plan correctly carries forward:

```text
4,681 UID denominator
1,704 PASS staged assets
1,324 no-pocket blockers
1,650 structure-fetch blockers
3 ESM2 failures
2,478 microbe source_signatures
1,638 / 2,478 MetaTraits local snapshot coverage
1,746 / 2,478 BacDive species-or-better coverage
30-row C7-2 bounded validator PASS
MetaTraits C7-1 long-form rerun2 mapping PASS with 8/8 negative assertions
```

## Boundary Wording Review

Forbidden or risky terms appear only in explicit negative contexts:

```text
production backfill: not used
全量补齐: not used
UID replacement: used only as "no UID replacement"
hard filter / hard rejection: used only as disabled/forbidden
trait_score: used only as disabled/forbidden
production-ready: used only as non-claim
```

## Residual Teacher Decisions

The plan correctly leaves the following as teacher-review questions instead of
silently deciding them:

```text
whether C8-1 read-only lookup index may be generated as staged derivative;
whether first full staged denominator should be 1,704 PASS assets only or also list
2,478 source-universe rows not reached by current enzyme candidates;
whether fallback integration should start with a small candidate-table interface smoke;
whether C8 continues as display/explanation/coverage only with no hard filtering or trait_score.
```

## Final Audit Conclusion

The C8 plan is ready to place in the microbe-side teacher deliverables repo
together with the 2026-08-19 MetaTraits TSV landing and corrected C7-1 mapping
evidence. It should still be described as a plan awaiting teacher review, not
as an implementation result.
