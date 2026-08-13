# M4b / C7 TraitFilterLayer Initiation Package

Date: 2026-08-13

Purpose:

```text
Submit the M4b/C7 initiation material requested in the 2026-08-13 teacher
guidance, after C1-C6, MT-TQ-02 and the 2026-08-12 hybrid data-plane package
were marked as ready for the next step.
```

## Main teacher-facing file

```text
M4B_C7_TRAITFILTERLAYER_INITIATION_BLUEPRINT_2026-08-13.md
```

It covers:

```text
TraitFilterLayer v1 implementation scope;
input/output contract;
staged acceptance criteria;
teacher/domain decisions required before implementation.
```

## Audit

```text
audits/
  ENZYMECAGE_M4B_C7_TRAITFILTERLAYER_INITIATION_BLUEPRINT_LOCAL_AUDIT_2026-08-13.md
```

## Current recommendation

Recommended observed/predicted route for teacher review:

```text
B route: observed traits first; predicted soft-fill only for missing core traits.
```

Required boundary:

```text
predicted values do not overwrite observed values;
each trait keeps evidence_type, prediction_used, source_database and provenance;
trait panel still requires senior/domain discussion and teacher decision;
fungal predicted-trait supplement is recommended for evaluation only;
no hard filtering, no uncalibrated confidence float, no production mutation.
```

## Boundary

This package does not claim:

```text
M4b authorization has already been issued;
TraitFilterLayer code has been implemented;
trait panel has been frozen;
B route has been teacher-approved;
fungal prediction route has been finalized;
production organism_uid -> traits routing has been enabled;
hard filtering or irreversible rejection has been enabled.
```

Manifest:

```text
MANIFEST.sha256
DELIVERABLE_SHA256SUMS.txt
```
