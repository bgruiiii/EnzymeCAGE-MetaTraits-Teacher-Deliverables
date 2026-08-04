# M3 bacteria-layer D1-D8 and organism-confidence requirements reaudit

Date: 2026-08-04  
Scope: local read-only review of teacher requirements in
`TEACHER_REPLY_M3_COMBINED_THREE_QUESTIONS_AND_NEXT_STEPS_2026-08-03.md`;
no code change; no GitHub sync.

## 1. Question being answered

The 2026-08-03 teacher file again lists bacteria-layer prerequisites:

- D5 MetaTraits probe;
- data-plane access path;
- organism ID alignment;
- wastewater trait hard/soft policy;
- D1-D8 positions;
- enzyme-to-organism confidence source / OrganismAggregator prerequisite.

This audit checks whether these were already completed in earlier files and
what still needs a fresh pointer or decision in the final combined response.

## 2. Authority files checked

Primary teacher authority:

```text
00_Authority_Teacher_Plan/
TEACHER_REPLY_M3_COMBINED_THREE_QUESTIONS_AND_NEXT_STEPS_2026-08-03.md

00_Authority_Teacher_Plan/
TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md

00_Authority_Teacher_Plan/
TEACHER_REPLY_M3_P1_UNLOCK_CASE1_REBOUND_AND_METATRAITS_M4A_ADJUDICATION_2026-07-21.md

00_Authority_Teacher_Plan/
STUDENT_REPLY_MTD3_TIEBREAK_CONFLICT_VERIFIED_2026-07-28.md
```

Student request / evidence package:

```text
15_Teacher_Formal_Training_Final_Report_2026-07-13/
ENZYMECAGE_METATRAITS_MT_D5_RESULTS_AND_D1_D8_TEACHER_DECISION_REQUEST_2026-07-16.md

/home/a/EnzymeCAGE-MetaTraits-Teacher-Deliverables/
2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/

/home/a/EnzymeCAGE-MetaTraits-Teacher-Deliverables/
METATRAITS_D5_2026_08_03_TEACHER_LIST_RECONFIRMATION_INDEX_2026-08-04.md
```

## 3. D1-D8 state

The 2026-07-18 teacher reply explicitly says:

```text
MT-D5 验收通过 / MT-D1–D8 裁定完成 / M4a 授权启动
```

Therefore, the correct final-response posture is not “we newly decide D1-D8
now”, but:

> D1-D8 had already been formally adjudicated in the 2026-07-18 teacher file.
> In the 2026-08-04 final response, we should re-point the teacher to that
> adjudication and disclose the later MT-D3 tie-break clarification.

### D1

Teacher decision: B+.

```text
UniProt reviewed organism/taxon ID = primary evidence;
KEGG Organism = independent supplement / cross-evidence, preserving
0/1/N multiplicity;
TrEMBL unreviewed = not included by default in v1.
```

Status: completed by teacher adjudication; no new decision needed unless M4
expands source policy.

### D2

Teacher decision: revised C.

```text
v1 does not output organism_confidence float.
Deterministic code passes through raw evidence dimensions:
reviewed status, annotation score, protein existence and KEGG multiplicity.
LLM may explain existing evidence grades but may not invent a numeric
confidence.
```

Important for the 2026-08-03 “路线甲/路线乙” item:

- The current accepted route is neither a student-hosted numeric-confidence
  `Enzyme2OrganismTool` contract nor an uncalibrated live UniProt float.
- The accepted v1 route is “no pseudo-precise float; preserve raw evidence
  dimensions”.
- If a later schema strictly requires a `confidence` field, teacher requires a
  separate `CONFIDENCE_MAPPING_PROPOSAL.md`.

Status: completed by 2026-07-18 teacher adjudication. In the final response,
we should explicitly point this out because the 2026-08-03 combined checklist
repeats the confidence concern.

### D3

Original 2026-07-18 decision:

```text
v1 default = supporting-enzyme count descending + UID ascending tie-break.
```

Later correction:

- 2026-07-21 follow-up adjudication accepted current implementation:
  supporting-enzyme count descending + numeric NCBI taxon ID ascending.
- 2026-07-28 verified student reply documented the discrepancy and provided
  implementation/test evidence.

Current status:

```text
supporting-enzyme count descending
+ numeric NCBI taxon ID ascending tie-break
```

Status: completed, but final response must cite the corrected 07-21/07-28
version rather than the older UID wording.

### D4

Teacher 2026-07-18 decision: all v1 traits are soft + uncertainty_flag; no
irreversible deletion.

```text
temperature         soft
pH                  soft
salinity            soft
oxygen_preference   soft
biofilm             not used / unknown due D5 coverage 0/5
safety/pathogenicity soft + manual review flag
```

Later biological-side meeting with Liu teacher/senior sister confirms the same
direction: retain soft trait evidence as reference/advice/explanation and
uncertainty, not automatic deletion.

Status: completed and confirmed. Final response should not propose a new hard
filter.

### D5

Teacher 2026-07-18 decision: D5 probe closed.

2026-08-04 local reconfirmation additionally points to the new-contract D5
resubmission package and index:

```text
/home/a/EnzymeCAGE-MetaTraits-Teacher-Deliverables/
2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/

/home/a/EnzymeCAGE-MetaTraits-Teacher-Deliverables/
METATRAITS_D5_2026_08_03_TEACHER_LIST_RECONFIRMATION_INDEX_2026-08-04.md
```

Status: completed; final response must re-list location and not assume the
teacher remembers earlier upload.

### D6

Teacher decision: adopt enhanced prompt constraints.

```text
Do not bypass TraitFilterLayer hard constraints;
each positive recommendation needs at least 2 traceable evidence items;
if insufficient, return insufficient_evidence/unknown;
No robust majority and source conflict enter uncertainty_flags.
```

Status: decision completed; implementation belongs to later M4c.

### D7

Teacher decision: independent `MicrobeCrew`.

Status: completed.

### D8

Teacher decision: default M4a = preload at startup, final loading strategy
after M4a latency/concurrency/GPU tests.

Status: v1 default exists; final production strategy deferred by teacher, not
a student omission.

## 4. ⑤⑥⑦ bacteria-layer prerequisites

### ⑤ MetaTraits data-plane access

Already adjudicated in 2026-07-18:

- production main path = official versioned snapshot;
- contact maintainers in parallel;
- website endpoint only experimental fallback with TTL cache, interval,
  provenance and circuit breaker;
- do not launch M4b without snapshot.

Status: decision completed at contract level; final response should point to
`SNAPSHOT_CONTRACT_DRAFT.md` and the D5/D5A2 evidence.

### ⑥ organism ID alignment

Already included in D5 new-contract resubmission and 2026-08-04 D5
reconfirmation:

- UniProt/taxon direct documented API path returned 404 in the D5 probe;
- current delivered result is no exact ID match established for the sampled
  P0-derived hosts;
- 2026-07-26 supplement explicitly separates `exact_strain`,
  `exact_species` and `no_exact_match_established`.

Status: completed for the required initial probe. Final response must make the
negative result explicit, not bury it as a “name lookup failed” detail.

### ⑦ wastewater trait hard constraint list

Teacher 2026-07-18 D4 already locks v1 as soft-only:

- no irreversible deletion in v1;
- biofilm not used because D5 coverage was 0/5;
- safety/pathogenicity only soft + manual review flag.

Later Liu-side biological discussion confirmed retaining soft traits as
reference/advice/explanation.

Status: completed for v1 policy. If a later hard allowlist is desired, it is a
future expert-review upgrade, not an unresolved current v1 requirement.

## 5. Current answer to the 2026-08-03 repeated confidence question

The teacher’s 2026-08-03 checklist asks whether enzyme-to-organism confidence
uses:

```text
路线甲：student-provided Enzyme2OrganismTool with confidence;
路线乙：teacher side derives confidence from UniProt entry type.
```

The earlier binding 2026-07-18 answer was:

```text
v1 does not output organism_confidence float.
Pass through raw evidence dimensions only.
If a confidence field becomes mandatory, write a separate deterministic
CONFIDENCE_MAPPING_PROPOSAL.md before implementation.
```

Therefore the final response should say:

> This item was already adjudicated as “no pseudo numeric confidence in v1”.
> We will not provide only organism name/taxon ID silently; we will provide
> reviewed status, annotation score, protein existence and KEGG multiplicity as
> raw evidence dimensions. A numeric confidence mapping is a future separate
> proposal if required.

## 6. Verdict

Content-level status:

- D1-D8: completed by 2026-07-18 teacher adjudication, with D3 tie-break later
  corrected by 2026-07-21/07-28.
- D5: completed; 2026-08-04 reconfirmation index prepared.
- ⑤⑥⑦: covered by D5/D1-D8 decisions and D5 new-contract resubmission.
- 2.2 confidence: covered by D2; no numeric confidence in v1.

Remaining action:

- Add this status to the stepwise tracker.
- Later, during final combined GitHub delivery, expose these locations in the
  final index so the teacher will not miss earlier completed work.
