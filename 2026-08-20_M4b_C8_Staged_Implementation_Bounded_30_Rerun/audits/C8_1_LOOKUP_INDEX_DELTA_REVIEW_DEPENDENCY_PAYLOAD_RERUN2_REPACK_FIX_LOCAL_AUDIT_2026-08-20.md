# C8-1 Lookup Index + Delta Review Rerun2 Repack-Fix Local Audit

Date: 2026-08-20

Audited archive:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820.tar.gz
```

Identity sidecar:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820.tar.gz.identity.txt
```

## Verdict

```text
LOCAL_AUDIT_VERDICT = PASS_TEACHER_READY_C8_1_STAGED_ONLY_CANDIDATE
```

The rerun2 package fixes the two rerun1 audit defects:

```text
1. MANIFEST.files and MANIFEST.sha256 are now present and validate.
2. All 428 fungal F5 rows in C8_METATRAITS_LOOKUP_INDEX.jsonl now use
   value_status_preview = FUNGI_IDENTITY_ONLY.
```

The package preserves the teacher-required C8 boundaries:

```text
staged-only
main denominator = original 2,478 source_signature universe
137 rescued-asset-linked outside-universe sources = delta review only
no API calls
no porTraits
no production mutation
no final trait_annotation.jsonl
no hard rejection / trait_score / uncalibrated confidence
F5 not predicted
F8 not written as direct target-pollutant degradation fact
F15 not used for ranking
fungi identity-only in the MetaTraits lookup
```

## Archive And Identity

| Check | Result |
|---|---|
| archive exists | PASS |
| identity sidecar exists | PASS |
| archive bytes | 1,302,070 |
| computed archive SHA256 | `ebae0d9ffbf1cb3cec666bba0d7a8b5562d59d0a140fe3ab06c6e1da6f094b33` |
| identity archive SHA256 | `ebae0d9ffbf1cb3cec666bba0d7a8b5562d59d0a140fe3ab06c6e1da6f094b33` |
| SHA256 match | PASS |
| single root | `enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820` |
| unsafe absolute / `..` paths | PASS |
| forbidden files (`__pycache__`, `.pyc`, payload tarballs, raw TSV gzip, `trait_annotation.jsonl`) | PASS: none |
| `MANIFEST.files` present | PASS |
| `MANIFEST.sha256` present | PASS |
| `sha256sum -c MANIFEST.sha256` | PASS |
| final status | `C8_1_LOOKUP_INDEX_AND_DELTA_REVIEW_RERUN2_REPACK_FIX_COMPLETE` |

## Core Row Counts

Independent row-count checks:

| File | Expected | Observed |
|---|---:|---:|
| `C8_METATRAITS_LOOKUP_INDEX.jsonl` | 37,170 JSONL rows | 37,170 |
| `C8_BACDIVE_AVAILABILITY_LOOKUP.csv` | 2,478 data rows + header | 2,479 lines |
| `C8_LOOKUP_SOURCE_UNIVERSE.csv` | 2,478 data rows + header | 2,479 lines |
| `C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW.csv` | 137 data rows + header | 138 lines |
| `C8_METATRAITS_LOOKUP_INDEX_SUMMARY.csv` | 15 data rows + header | 16 lines |

Trait row counts:

```text
F1-F15 each have exactly 2,478 lookup rows.
Every main source_signature has exactly 15 lookup rows.
```

## Main Universe And Delta Separation

Independent set checks:

```text
main unique source_signature count = 2,478
BacDive lookup unique source_signature count = 2,478
MetaTraits lookup unique source_signature count = 2,478
delta unique source_signature count = 137
delta ∩ main = 0
```

Delta checks:

```text
target_bacteria = 88
target_archaea = 6
target_fungi = 43
recommended_status = PENDING_TEACHER_DECISION for all 137 rows
inside_original_2478_universe = false for all 137 rows
```

This passes the teacher 2026-08-19 rule that the 137 outside-universe sources
must remain a separate delta review and must not be merged into the 2,478 main
denominator.

## Fungal F5 Fix

Rerun2 fixed the rerun1 localized defect:

```text
target_fungi + F5 rows = 428
fungal F5 rows with value_status_preview = FUNGI_IDENTITY_ONLY = 428
fungal F5 rows with source_type_preview = identity_only = 428
fungal F5 rows with mapping_status = FUNGI_IDENTITY_ONLY = 428
all fungal MetaTraits lookup rows are identity-only = true
```

F5 summary row after fix:

```text
trait_id = F5
main_universe_rows = 2478
observed_available_count = 0
predicted_soft_fill_candidate_count = 0
not_observed_count = 0
fungi_identity_only_count = 428
not_metatraits_source_count = 2050
prediction_allowed_for_trait = False
first_screen = observed_evidence_only
```

This is now consistent with the teacher boundary: fungi remain identity-only,
and F5 remains observed-only / non-predicted.

## Trait Red Lines

Independent red-line checks:

```text
F5 predicted rows = 0
F8 target-pollutant direct degradation wording = 0 detected
F15 predicted rows = 0
final trait_annotation.jsonl in returned root = absent
```

## Report Consistency

Rerun2 reports now explicitly distinguish:

```text
metatraits_gzip_files_validated = 14
metatraits_bulk_summary_tsv_files_streamed = 12
metatraits_crosswalk_gzip_files_validated_not_streamed = 2
```

This resolves the rerun1 report inconsistency.

Returned validation report includes:

```text
overall_pass = true
fungal_f5_patch_count = 428
fungal_f5_identity_only_rows = 428
all_fungi_metatraits_lookup_identity_only = true
manifest_files_present = true
manifest_sha256_present = true
pycache_excluded = true
```

Returned boundary report marks PASS for:

```text
staged-only
no production D4 mutation
no production pool mutation
no formal asset mutation
no hard rejection
no trait_score
no uncalibrated confidence
no MetaTraits API call
no BacDive API call
no porTraits run
no final trait_annotation generated
main denominator preserved at 2,478
137 delta sources not merged
fungi identity-only
F5 not predicted
F8 no direct target-pollutant degradation claim
F15 not used for ranking
dependency payload verified
manifest_files_present
manifest_sha256_present
pycache_excluded
```

Independent checks support these claims.

## Conclusion

This package can be treated as the corrected C8-1 staged-only lookup-index and
delta rescued-source review candidate.

Recommended internal status:

```text
C8-1 lookup index + C8 delta review: PASS after rerun2 repack-fix.
Teacher-ready as staged-only evidence, pending packaging into the next
microbe-side GitHub delivery batch.
```

Important scope note:

```text
This is not production activation.
This does not generate final C8 trait_annotation.jsonl.
This does not merge the 137 outside-universe rescued sources into the main
2,478 denominator.
```

