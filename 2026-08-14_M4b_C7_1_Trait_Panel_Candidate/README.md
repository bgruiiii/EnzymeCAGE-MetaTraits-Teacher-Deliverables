# M4b / C7-1 Trait Panel Candidate Package

Date: 2026-08-14

Status: candidate, pending teacher-side item-by-item freeze.

## Purpose

This package submits the C7-1 candidate trait panel requested by Huang teacher
on 2026-08-14 for the Chen Haoran microbe-side M4b/C7 TraitFilterLayer line.

It is a staged soft trait-layer candidate package only. It does not implement
TraitFilterLayer code, does not enable production routing, and does not define
hard rejection rules.

## Teacher-Facing Files

Main report:

```text
M4B_C7_1_TRAIT_PANEL_CANDIDATE_REPORT_2026-08-14.md
```

Machine-readable candidate table:

```text
C7_1_TRAIT_PANEL_CANDIDATE_TABLE_2026-08-14.csv
```

Local audit:

```text
audits/M4B_C7_1_TRAIT_PANEL_CANDIDATE_LOCAL_AUDIT_2026-08-14.md
```

## Key Candidate Panel Result

First-screen display fields recommended by senior discussion:

```text
oxygen / anaerobic status
temperature
pH
salinity
BacDive culture collection number / availability provenance
```

Detailed-on-request fields retained as candidate soft context:

```text
respiration / electron acceptor
carbon and substrate utilization
broad catabolic / degradation context
enzyme activity
motility
cell morphology
cell envelope / Gram context
sporulation
genome background
habitat generalism
```

Explicit exclusion:

```text
biosafety level is deleted from the C7-1 trait panel.
```

Fungal boundary:

```text
fungi remain identity-only in this round;
missing_reason = fungi_no_local_trait_source;
fungal prediction tool testing is separate feasibility work and is not merged into C7-1.
```

## Boundary

This package does not claim:

```text
teacher-side trait freeze has completed;
production authorization;
automatic strain selection;
automatic candidate deletion;
exact pollutant degradation proof from broad traits;
culture availability prediction;
biosafety judgment inside TraitFilterLayer;
fungal trait prediction included in this round.
```

## Manifest

```text
MANIFEST.files
MANIFEST.sha256
DELIVERABLE_SHA256SUMS.txt
```
