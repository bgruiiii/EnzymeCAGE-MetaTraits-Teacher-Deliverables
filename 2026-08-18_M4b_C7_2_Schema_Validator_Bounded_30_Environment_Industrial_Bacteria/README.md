# C7-2 Schema/Validator Bounded 30 Staged-Only Package

Date: 2026-08-18

This package is a read-only schema/validator proof against a 30-row bounded staged subset.
It follows Huang teacher's 2026-08-17 authorization and the frozen C7-2 proposal §9.

Contents:

- `POLICY_MANIFEST.json`
- `TRAIN_SET_MANIFEST.csv`
- `trait_annotation.jsonl`
- `TRAIT_FEATURE_ENCODING_VALIDATION_REPORT.md`
- `BOUNDARY_VALIDATION_REPORT.md`
- `FINAL_STATUS.txt`
- `LOCAL_AUDIT_C7_2_SCHEMA_VALIDATOR_BOUNDED_30_2026-08-18.md`
- `scripts/build_c7_2_schema_validator_bounded_30.py`
- `MANIFEST.sha256`

Scope notes:

- 30 rows = 10 bacteria + 10 archaea + 10 fungi.
- The bacteria rows are selected from the real staged PASS intersection with preference for environmental/industrial-facing examples.
- Rows come only from the teacher-accepted 1,704 staged PASS package.
- P0DXV0 is excluded to keep 1,704 and 1,705 effective口径 distinct.
- MetaTraits values come only from local downloaded snapshots.
- BacDive values come only from prior audited local closure/cache tables.
- No online genome prediction, no new BacDive API query, no asset generation, and no production mutation were performed.
