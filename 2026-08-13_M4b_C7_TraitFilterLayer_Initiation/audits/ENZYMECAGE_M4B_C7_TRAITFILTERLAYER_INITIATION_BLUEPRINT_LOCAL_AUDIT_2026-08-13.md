# Local audit: M4b / C7 TraitFilterLayer initiation blueprint

Date: 2026-08-13

Audited draft:

```text
01_Path_Contract_Objective/
M4b_C7_TraitFilterLayer_Initiation_Blueprint_2026-08-13/
M4B_C7_TRAITFILTERLAYER_INITIATION_BLUEPRINT_2026-08-13.md
```

Authority:

```text
00_Authority_Teacher_Plan/
TEACHER_REPLY_PROJECT_NEXT_STEPS_GUIDANCE_2026-08-13.md
```

## 1. Verdict

Verdict:

```text
LOCAL_AUDIT_PASS_FOR_USER_REVIEW_BEFORE_TEACHER_SUBMISSION
```

The draft covers the teacher-required C7 elements:

```text
TraitFilterLayer implementation scope;
input/output contract;
acceptance criteria.
```

It does not claim that M4b, TraitFilterLayer implementation, trait panel
freezing, feature encoding, production trait routing, or hard filtering has
already started.

## 2. Teacher requirement coverage

Teacher 2026-08-13 required:

| Requirement | Draft coverage |
|---|---|
| C7 / M4b initiation material | Sections 0, 8 |
| TraitFilterLayer implementation scope | Section 3 |
| Input/output contract | Sections 4 and 5 |
| Acceptance criteria | Section 6 |
| Preconditions | Section 1 |
| Respect future sequence | Section 0 lists authorization -> panel freeze -> encoding -> implementation |

## 3. Evidence basis

The draft uses the following evidence:

| Evidence | Located source |
|---|---|
| 2026-08-13 teacher C7 requirement | `TEACHER_REPLY_PROJECT_NEXT_STEPS_GUIDANCE_2026-08-13.md` |
| C1-C6 closed and MT-TQ-02 closed | 2026-08-13 teacher guidance; 2026-08-07 teacher reply for C1-C6 closure |
| Historical M4b code boundary | 2026-07-23 teacher Task 7 / MT-TQ-02 reply and 2026-08-04 Task 7 reconfirmation audit |
| MetaTraits coverage 1,638 / 2,478 | 08-12 MetaTraits species-level coverage report |
| BacDive coverage 1,746 / 2,478 | 08-12 BacDive full closure audit |
| BacDive / MetaTraits overlap | 08-12 BacDive full closure audit and deliverable README |
| Representative strain expansion 1,149 / 52,956 | 08-12 hybrid deliverable README |
| observed vs predicted A/B/C routes | 08-12 trait panel and prediction policy discussion material |
| soft-only wastewater policy | 2026-07-27 wastewater trait soft policy decision record |

## 4. Repository visibility check

The current 08-12 microbe-side deliverable was checked in:

```text
custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/
```

Remote:

```text
git@github.com:bgruiiii/EnzymeCAGE-MetaTraits-Teacher-Deliverables.git
```

Local check showed:

```text
remote main HEAD = c4ac2087fc7c29a8414e34ca30d28c42244f1588
```

The older local clone:

```text
/home/a/EnzymeCAGE-MetaTraits-Teacher-Deliverables
```

is behind and should not be used as the source of truth for the 08-12 package
unless it is synchronized first.

## 5. Boundary audit

No-overclaim checks:

| Check | Result |
|---|---|
| Claims M4b already authorized | PASS: says authorization is requested and separate |
| Claims TraitFilterLayer already implemented | PASS: says no active code |
| Claims trait panel frozen | PASS: says panel needs domain review and teacher decision |
| Claims A/B/C route selected as teacher-approved | PASS: recommends B for teacher review, but does not claim teacher has裁定 |
| Claims fungi will definitely be predicted | PASS: wording is "recommend/evaluate predicted supplement route"; not a finalized implementation decision |
| Claims MetaTraits species-level trait as strain-level | PASS: explicitly forbids |
| Claims BacDive representative strains equal UniProt exact strains | PASS: explicitly forbids |
| Claims hard filtering | PASS: hard filtering remains disabled |
| Claims confidence float | PASS: no organism_confidence float; no uncalibrated trait_score |
| Claims production mutation | PASS: production mutation excluded and acceptance requires false |

## 6. Deliberate design choice

The draft recommends a C-compatible schema foundation:

```text
observed and predicted kept in separate fields
```

Reason:

```text
The draft recommends route B for teacher review: observed traits first, predicted
soft-fill only for missing core traits, with full evidence/provenance flags.
It does not claim route B is teacher-approved. The schema still preserves
observed and predicted fields separately, so evidence tiers are not mixed.
```

## 7. Residual decisions for user/teacher

The following are intentionally not resolved by the draft:

```text
1. final pollutant-degradation trait panel;
2. whether teacher accepts recommended observed-first / predicted-soft-fill route B;
3. exact allowed predicted trait categories;
4. fungal prediction supplement route/resource and evidence tier;
5. whether any numeric trait_score is later needed after feature encoding.
```

These should remain visible in the teacher-facing blueprint rather than being
silently decided locally.

## 8. Submission steps

Before teacher submission:

```text
1. User reviews the C7 wording.
2. If approved, include it in the correct microbe-side teacher deliverables
   repository, not the enzyme-side deliverables repository.
3. Update the current teacher review entrypoint / README so the teacher can
   find the 08-13 C7 material.
4. Do not upload private chat-message drafts.
```

Do not start M4b implementation until teacher authorization is received.
