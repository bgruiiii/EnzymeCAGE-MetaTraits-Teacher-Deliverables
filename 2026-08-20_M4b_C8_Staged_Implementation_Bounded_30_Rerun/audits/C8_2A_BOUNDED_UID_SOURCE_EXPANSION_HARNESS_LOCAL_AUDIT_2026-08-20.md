# C8-2A Bounded UID Source Expansion Harness Local Audit

Date: 2026-08-20

Audited archive:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/enzymecage_m4b_c8_2a_bounded_uid_source_expansion_harness_20260820.tar.gz
```

Identity sidecar:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/enzymecage_m4b_c8_2a_bounded_uid_source_expansion_harness_20260820.tar.gz.identity.txt
```

## Verdict

```text
LOCAL_AUDIT_VERDICT = PASS_TEACHER_READY_C8_2A_BOUNDED_HARNESS
```

The returned package satisfies the C8-2A bounded/staged implementation harness
contract:

```text
enzyme_uid candidate table -> microbe source_signature expansion
```

It is suitable as staged evidence that the C8-2 join/schema/boundary logic works
on the teacher-accepted M4 E2 4,681-row status table.

Important scope boundary:

```text
This is not the final all-enzyme candidate pool.
This is not the future full-library enzyme source.
This package must not be used to limit later C8 coverage.
The P2Rank status names here are specific to the M4 E2 fallback harness only.
Future full-library C8 must accept the upstream candidate table through the same
schema and may consume other valid asset families, including the existing main
AlphaFill-derived pocket assets where applicable.
```

## Archive And Identity

| Check | Result |
|---|---|
| archive exists | PASS |
| identity sidecar exists | PASS |
| archive bytes | 333,276 |
| computed archive SHA256 | `d2d9ba4ba94a830cd268355588ce6d8041ed2cd3eb66e615891a5313c9a70c79` |
| identity archive SHA256 | `d2d9ba4ba94a830cd268355588ce6d8041ed2cd3eb66e615891a5313c9a70c79` |
| SHA256 match | PASS |
| single root | `enzymecage_m4b_c8_2a_bounded_uid_source_expansion_harness_20260820` |
| tar member count | 12 |
| `MANIFEST.files` present | PASS |
| `MANIFEST.sha256` present | PASS |
| `sha256sum -c MANIFEST.sha256` | PASS |
| final status | `C8_2A_BOUNDED_UID_SOURCE_EXPANSION_HARNESS_COMPLETE` |

Note:

```text
identity manifest_file_count = 12
MANIFEST.files lines = 10
```

This is acceptable for this package because the tar contains 12 files total,
while `MANIFEST.files` lists the 10 primary output files. `MANIFEST.sha256`
also covers `MANIFEST.files`, and the independent SHA256 check passed.

## Returned Files

The archive contains the expected C8-2A outputs:

```text
C8_BOUNDARY_VALIDATION_REPORT.md
C8_INPUT_CANDIDATE_TABLE.csv
C8_INPUT_PATH_RESOLUTION_TABLE.csv
C8_UID_SOURCE_EXPANSION_REPORT.md
C8_UID_SOURCE_EXPANSION_SUMMARY.csv
C8_UID_SOURCE_EXPANSION_TABLE.csv
C8_UID_SOURCE_EXPANSION_VALIDATION_REPORT.json
C8_UID_SOURCE_EXPANSION_VALIDATION_REPORT.md
COMMAND_LOG.txt
FINAL_STATUS.txt
MANIFEST.files
MANIFEST.sha256
```

No final `trait_annotation.jsonl` was generated, as required for C8-2A.

## Independent Row Count Checks

Independent CSV checks reproduced the returned counts:

| Metric | Observed | Expected | Result |
|---|---:|---:|---|
| `C8_INPUT_CANDIDATE_TABLE.csv` data rows | 4,681 | 4,681 | PASS |
| unique candidate enzyme UID | 4,681 | 4,681 | PASS |
| `C8_UID_SOURCE_EXPANSION_TABLE.csv` data rows | 4,681 | 4,681 | PASS |
| unique expansion enzyme UID | 4,681 | 4,681 | PASS |
| consumable PASS assets | 1,704 | 1,704 | PASS |
| blocked / non-consumable assets | 2,977 | 2,977 | PASS |
| C8-3 eligible main rows | 753 | 753 | PASS |
| delta review rows | 209 | 209 | PASS |
| mapped outside main and delta | 0 | 0 | PASS |

Candidate input status:

```text
C8_CANDIDATE_ASSET_AVAILABLE = 1,704
ASSET_NOT_AVAILABLE = 2,977
```

Expansion status:

```text
READY_FOR_C8_3_TRAIT_ANNOTATION = 753
DELTA_REVIEW_ONLY_NOT_MAIN_C8 = 209
NOT_MAPPED = 742
ASSET_NOT_AVAILABLE = 2,977
```

Source-universe class:

```text
MAIN_2478 = 753
DELTA_137_PENDING_TEACHER_DECISION = 209
NOT_MAPPED = 742
NOT_APPLICABLE_ASSET_NOT_AVAILABLE = 2,977
```

## Main And Delta Taxonomy Counts

Rows eligible for main C8-3 trait annotation:

```text
MAIN_2478 total = 753
target_bacteria = 495
target_archaea = 73
target_fungi = 185
```

Delta rows kept out of main C8 pending teacher decision:

```text
DELTA_137_PENDING_TEACHER_DECISION total = 209
target_bacteria = 116
target_archaea = 8
target_fungi = 85
```

Boundary checks:

```text
delta rows marked C8-3 eligible = 0
non-main rows marked C8-3 eligible = 0
main rows not marked C8-3 eligible = 0
```

This preserves the teacher 2026-08-19 rule that the 137 rescued outside-universe
sources remain delta review only and are not silently merged into the original
2,478 main denominator.

## Boundary And Red-Line Checks

The returned boundary report marks PASS for:

```text
staged-only
no production D4 mutation
no production pool mutation
no formal asset mutation
no MetaTraits API call
no BacDive API call
no porTraits run
no raw MetaTraits TSV read
no trait_annotation generated
no trait values generated
main denominator preserved at 2,478
137 delta not merged
no hard rejection
no trait_score
no uncalibrated confidence
```

Independent checks support these claims:

```text
production/formal mutation rows = 0
validation errors = []
validation warnings = []
overall_pass = true
```

## Scope Wording Review

The report explicitly states:

```text
C8-2A used FULL_4681 as a bounded/staged implementation harness because no
upstream pollutant/reaction enzyme candidate table is frozen yet.
This is not the final all-enzyme candidate pool and must not limit later
full-library C8 use.
```

This wording is important and correct. It prevents the 4,681 M4 E2 fallback
harness from being mistaken for the final enzyme universe.

No problematic report-level generalization was found that would make P2Rank the
only valid future asset source. P2Rank appears through the current M4 E2 harness
status labels, which is acceptable for this bounded test.

## Conclusion

This package can be accepted as C8-2A bounded/staged UID-to-source expansion
evidence.

Recommended internal status:

```text
C8-2A bounded UID source expansion harness: PASS.
Ready to feed C8-3/C8-4 bounded harness generation for the 753 MAIN_2478
eligible rows only.
Delta rows remain review-only.
Not-mapped PASS UIDs and asset-blocked UIDs do not proceed to C8-3 in this
bounded harness.
```

