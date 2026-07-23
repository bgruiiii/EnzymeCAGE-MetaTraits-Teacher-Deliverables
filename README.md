# MetaTraits Teacher Deliverables

## P0 current delivery: D5 new-contract reaudit — 2026-07-24

The current teacher-facing D5 report does not rely on filename identity or
earlier acceptance. It explicitly audits the P0 Top-MRR enzyme-to-host chain,
five original metaTraits JSON bodies, four required real-sample checks and the
TaxID direct-query result:

- [`2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/metatraits_probe_report.md`](2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/metatraits_probe_report.md)
- [dated path index, ten-row crosswalk, independent audit and manifest](2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/)

Bounded decision: the data support soft-trait prototyping on the five sampled
hosts, but not hard filtering, exact strain attribution or production. The
documented TaxID API returned 404 for all ten P0-derived host tax IDs, so a
working production `organism_uid -> traits` path remains unresolved.

## Current Task 7 contract delivery — 2026-07-24

The teacher-authorized contract-only Task 7 delivery is placed directly at
repository root:

- [`TRAIT_VALUE_NOT_APPLICABLE_SCHEMA_CONTRACT.md`](TRAIT_VALUE_NOT_APPLICABLE_SCHEMA_CONTRACT.md)
- dated path index, independent audit, and SHA256 manifest:
  [`2026-07-24_Task7_TraitValue_Not_Applicable_Contract/`](2026-07-24_Task7_TraitValue_Not_Applicable_Contract/)

Status: student delivery; teacher acceptance not yet claimed. It defines the
`reason`/`note` contract and required `not_applicable` example without adding
Pydantic code, tests, `MicrobeTraitTool`, or M4b/M4c implementation.

## Current prerequisite resubmission — 2026-07-24

The P0 MT-D5 evidence requested by the 2026-07-24 supplement was originally
completed and independently audited on 2026-07-16, then accepted in
`TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md`.
It was not rerun. The accepted files are resubmitted byte-for-byte:

- report at repository root:
  [`metatraits_probe_report.md`](metatraits_probe_report.md);
- five raw sample JSON bodies, accepted package, source paths and audit:
  [`2026-07-24_MT_D5_Accepted_Evidence_Resubmission/`](2026-07-24_MT_D5_Accepted_Evidence_Resubmission/).

The dated folder README is the teacher-facing path index. Its hash manifest
proves that the report, five JSON bodies, deterministic tar, tar identity,
2026-07-16 audit and authority reference retain their original bytes.

## Current submission — 2026-07-23

Teacher-requested files are placed directly in the repository root:

- P0 Task 4: [`SNAPSHOT_CONTRACT_DRAFT.md`](SNAPSHOT_CONTRACT_DRAFT.md)
- Task 6 corrected unsent inquiry:
  [`METATRAITS_API_INQUIRY_EMAIL_DRAFT.md`](METATRAITS_API_INQUIRY_EMAIL_DRAFT.md)
- Delivery status and Task 7 decision request:
  [`METATRAITS_TASKS_4_6_AND_TASK7_DECISION_REQUEST_2026-07-23.md`](METATRAITS_TASKS_4_6_AND_TASK7_DECISION_REQUEST_2026-07-23.md)

Individual task audits and the final pre-submission audit are under
[`2026-07-23_MetaTraits_Tasks_4_6_and_Task7_Decision_Request/audits/`](2026-07-23_MetaTraits_Tasks_4_6_and_Task7_Decision_Request/audits/).
The submission hash manifest is
[`2026-07-23_MetaTraits_Tasks_4_6_and_Task7_Decision_Request/DELIVERABLE_SHA256SUMS.txt`](2026-07-23_MetaTraits_Tasks_4_6_and_Task7_Decision_Request/DELIVERABLE_SHA256SUMS.txt).

Tasks 4 and 6 were subsequently accepted by the teacher on 2026-07-23.
Task 7 was adjudicated as contract-only: the schema contract and example remain
an upcoming student delivery, while live code and tests are deferred to a
future separately authorized M4b. M4b and M4c remain unauthorized.

The 2026-07-21 folder and commit are retained unchanged as historical
evidence. Its nested snapshot has the same bytes as the current root
resubmission, but its email predates the project-name decision. Use the
root-level files as the current submission.
