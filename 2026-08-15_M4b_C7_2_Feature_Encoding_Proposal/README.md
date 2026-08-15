# M4b / C7-2 Feature Encoding Proposal Package

Date: 2026-08-15

Status: proposal submitted for Huang teacher review; not implemented; not production.

## Purpose

This package submits the Chen Haoran-side M4b/C7 C7-2 feature encoding proposal after Huang teacher's 2026-08-14 C7-1 item-by-item freeze.

The proposal maps the frozen F1-F15 trait panel into an auditable encoding design and aligns it with Huang teacher's 7.2 loader contract and 7.3 microbe feature consumption interface.

## Teacher-Facing Files

Main proposal:

```text
M4B_C7_2_FEATURE_ENCODING_PROPOSAL_2026-08-15.md
```

Local audit:

```text
audits/M4B_C7_2_FEATURE_ENCODING_PROPOSAL_LOCAL_AUDIT_2026-08-15.md
```

Integrity files:

```text
MANIFEST.files
MANIFEST.sha256
DELIVERABLE_SHA256SUMS.txt
```

## Authority Alignment

Primary authority:

```text
TEACHER_REPLY_FULL_4681_ACCEPTANCE_AND_C7_1_FREEZE_2026-08-14.md
```

Teacher-required C7-2 content covered:

```text
F1-F15 frozen trait IDs are referenced explicitly.
Fungi remain identity-only.
TRAIN_SET_MANIFEST.csv design follows the teacher 7.2 loader contract.
trait_annotation.jsonl design follows the teacher 7.3 microbe feature consumption interface.
observed and predicted fields remain separate with provenance.
predicted soft fill is allowed only for teacher-authorized categories.
```

## Main Boundaries

This package does not claim:

```text
TraitFilterLayer has been implemented;
C7-2 has been frozen by Huang teacher;
the 2,478-source staged status table has been generated;
any train/validation/test split has been frozen;
any microbe has been automatically accepted or rejected;
any trait_score or uncalibrated confidence score is available;
any exact pollutant degradation fact is inferred from broad traits;
any fungal trait prediction has entered this round;
any production D4 or production pool has been modified.
```

## Numbering Note

The 2026-08-13 initiation blueprint used an earlier split in which C7-2 was route/fungal-policy review and C7-3 was feature encoding. Huang teacher's latest 2026-08-14裁定 names the next Chen Haoran task as C7-2 feature encoding proposal. This package follows the latest teacher authority.
