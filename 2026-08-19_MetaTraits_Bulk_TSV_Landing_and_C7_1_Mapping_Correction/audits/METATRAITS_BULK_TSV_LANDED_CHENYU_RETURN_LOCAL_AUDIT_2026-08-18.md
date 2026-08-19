# MetaTraits Bulk TSV Landed On Chenyu Return Local Audit

Date: 2026-08-18

Audited package:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/metatraits_bulk_tsv_landed_chenyu_20260818.tar.gz
```

Identity sidecar:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/metatraits_bulk_tsv_landed_chenyu_20260818.tar.gz.identity.txt
```

## Verdict

**DATA LANDING / VALIDATION: PASS.**

The returned package supports the claim that the 12 required MetaTraits bulk
summary TSV gzip files plus 2 companion crosswalk files were present under the
Chenyu data root and validated by gzip test and SHA256.

**C7-1 FIELD MAPPING: NEEDS SUPPLEMENTAL MAPPING-ONLY FIX.**

The returned `C7_1_TRAIT_PANEL_FIELD_MAPPING_DRAFT.csv` used a header-keyword
match and marked almost all C7-1 traits as
`NOT_MAPPED_FROM_METATRAITS_TSV`. This is too mechanical for MetaTraits bulk
summary TSVs, because the files are long-form tables: the semantic trait labels
live in `trait_name`, `group_1` and `group_2` rows, not in wide columns such as
`temperature` or `pH`.

No large TSV data need to be re-uploaded for the fix. A small mapping-only
rerun against the already landed `DATA_DIR` is sufficient.

## Teacher Requirement Check

Teacher's 2026-08-18 requirement for Chen Haoran side:

```text
metaTraits TSV 落晨羽（回报路径 + 清单 + SHA256），DDL 08-19
交付：全部 TSV 落晨羽；回报路径 + 文件清单；SHA256 校验 + 版本日期追溯；
明确 TSV 字段与 C7-1 trait panel 的映射口径。
```

Audit outcome:

| Requirement | Status | Evidence |
|---|---|---|
| Chenyu path reported | PASS | `FINAL_STATUS.txt`, identity sidecar |
| 12 required bulk TSV files present | PASS | `required_summary_validated_count=12/12` |
| 2 companion crosswalks present | PASS | `companion_crosswalk_validated_count=2/2` |
| SHA256 computed | PASS | `SHA256SUMS.txt`; matches local prefetch SHA256 for all 14 files |
| gzip integrity checked | PASS | `GZIP_TEST_REPORT.csv`; 14/14 PASS |
| version/date traceability | PASS | `OFFICIAL_SOURCE_INDEX_PARSED.csv`; all 14 last modified `2026-06-10 10:23` |
| metadata-only archive | PASS | archive size 7.1K; no `.tsv.gz` files included |
| no API / no prediction / no production mutation | PASS BY REPORT | `VALIDATION_REPORT.json` and log state these boundaries |
| C7-1 mapping口径 | PARTIAL | draft exists, but content-level trait mapping is incomplete |

## Core Evidence

Final status:

```text
final_status=METATRAITS_BULK_TSV_LANDED_CHENYU_COMPLETE
DATA_DIR=/usrdata/EnzymeCAGE_data/data/metatraits/incoming/metatraits_bulk_tsv_snapshot_20260818
RETURN_DIR=/usrdata/EnzymeCAGE_data/EnzymeCAGE-master/HPC_Returned_Result_Summaries/metatraits_bulk_tsv_landed_chenyu_20260818
required_summary_validated_count=12/12
companion_crosswalk_validated_count=2/2
```

Archive identity:

```text
archive_size_bytes=7179
archive_sha256=cbe9bb3b5372e8a703bdf7387fbf98d4a663d25a45a615b4db84a85e7665fa1b
```

Local hash of returned archive matched the identity sidecar:

```text
cbe9bb3b5372e8a703bdf7387fbf98d4a663d25a45a615b4db84a85e7665fa1b
```

The Chenyu TSV SHA256 table matched the local prefetch
`C:\Users\Melo\Desktop\临时工作\metatraits_bulk_tsv_20260818\SHA256SUMS.txt`
for all 14 files. Total landed TSV bytes from manifest matched local prefetch:

```text
276513632 bytes
```

## File Manifest Check

`METATRAITS_BULK_TSV_FILE_MANIFEST.csv` has 14 data rows:

| Field | Observed counts |
|---|---|
| role | `bulk_summary=12`, `companion_crosswalk=2` |
| required_summary_12 | `true=12`, `false=2` |
| taxonomy_namespace | `gtdb=6`, `ncbi=6`, `crosswalk=2` |
| taxonomic_rank | `family=4`, `genus=4`, `species=4`, `mapping=2` |
| prediction_scope | `all=6`, `no_predictions=6`, `mapping=2` |
| gzip_test_status | `PASS=14` |
| validation_status | `PASS=14` |
| row_count_status | `COUNTED=14` |

All `chenyu_path` values are under:

```text
/usrdata/EnzymeCAGE_data/data/metatraits/incoming/metatraits_bulk_tsv_snapshot_20260818/
```

## Minor Packaging Notes

These are not blockers for the data landing claim:

1. The package contains `DOWNLOAD_COMMAND_LOG.txt` instead of the later revised
   `TRANSFER_AND_VALIDATION_LOG.txt`. Its contents explicitly say no data
   download commands were issued and only local validation was performed.
2. `VALIDATION_REPORT.json` and the file manifest still use
   `downloaded_count` / `download_status` wording from the earlier prompt
   version. The log and paths show the operation was validate-only over the
   uploaded `DATA_DIR`.
3. `MANIFEST.files` and `MANIFEST.sha256` omit `MANIFEST.files` and
   `MANIFEST.sha256` themselves. The listed file hashes pass
   `sha256sum -c MANIFEST.sha256`; this is acceptable as a common self-manifest
   convention, but should be described if teacher asks.

## C7-1 Mapping Issue

The returned mapping table is not enough as the final answer to teacher's
"TSV fields -> C7-1 trait panel" request.

Observed MetaTraits TSV header structure:

```text
taxon_id
taxon_name
trait_name
unit
database_count
total_observations
consensus_value
consensus_count
consensus_percentage
minimum
median
mean
maximum
discrete_values
databases
group_1
group_2
ontology_ids
taxon_lineage
```

Local spot-check of `ncbi_species_summary_all.tsv.gz` and
`ncbi_species_summary_no_predictions.tsv.gz` found C7-relevant trait labels in
row values, for example:

```text
acidophilic    Environmental preferences    pH
aerobic growth: acetate    Metabolism    Aerobic growth
anaerobic growth: nitrate  Metabolism    Anaerobic growth
assimilation: D-glucose    Metabolism    Assimilation
```

Therefore the mapping should use columns like:

```text
trait_name
group_1
group_2
consensus_value
minimum / median / mean / maximum
discrete_values
databases
ontology_ids
```

and then list C7-1 candidate `trait_name` / `group_2` patterns for each trait.
It should not rely only on column names.

## Recommended Next Action

Run a **mapping-only correction** on Chenyu or locally against the already
landed files:

```text
DATA_DIR=/usrdata/EnzymeCAGE_data/data/metatraits/incoming/metatraits_bulk_tsv_snapshot_20260818
```

Required output should be a small report/table only, with no TSV re-upload and
no production activation:

```text
C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_CORRECTION.csv
C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_CORRECTION.md
```

The correction should explicitly state:

1. MetaTraits summary TSVs are long-form trait tables.
2. `no_predictions` files represent observed/no-prediction evidence.
3. `all` files include prediction-like soft-fill candidates where allowed by
   the frozen C7-1 policy.
4. F5 remains BacDive/local culture-collection evidence only.
5. F15 remains ecological background only and not ranking input.
6. Fungi remain identity-only in the current bounded route.

## Final Audit Conclusion

This package can be used to report that the MetaTraits bulk TSV snapshot has
landed on Chenyu with verified path, manifest, gzip integrity, SHA256 and
upstream date. It should not be uploaded/reported as the complete 08-18 task
until the C7-1 long-form mapping correction is added.
