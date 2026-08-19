# 2026-08-19 MetaTraits Bulk TSV Landing And C7-1 Mapping Correction

本目录对应黄老师 2026-08-18 任务单中陈浩然侧 P0 项：

```text
metaTraits TSV 落晨羽（回报路径 + 清单 + SHA256），DDL 08-19
交付：全部 TSV 落晨羽；回报路径 + 文件清单；SHA256 校验 + 版本日期追溯；
明确 TSV 字段与 C7-1 trait panel 的映射口径。
```

## 结论

**本项可作为 08-19 MetaTraits TSV 落晨羽 + C7-1 TSV 字段映射口径的审阅材料。**

已完成：

```text
MetaTraits bulk TSV landing: PASS
C7-1 long-form mapping rerun2: PASS
```

边界：

```text
未调用 MetaTraits API
未调用 BacDive API
未运行基因组在线预测
未激活 active_snapshot.json
未接 production
未修改 EnzymeCAGE formal assets
未把 230MB 级原始 TSV gzip 文件上传到 GitHub
```

## 老师优先阅读

1. 数据落晨羽与 SHA256：
   [`metatraits_landing_metadata/VALIDATION_REPORT.md`](metatraits_landing_metadata/VALIDATION_REPORT.md)
2. 已落地 TSV 文件清单：
   [`metatraits_landing_metadata/METATRAITS_BULK_TSV_FILE_MANIFEST.csv`](metatraits_landing_metadata/METATRAITS_BULK_TSV_FILE_MANIFEST.csv)
3. C7-1 trait panel 与 MetaTraits long-form 字段映射：
   [`c7_1_mapping_rerun2/C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_RERUN2.md`](c7_1_mapping_rerun2/C7_1_TRAIT_PANEL_METATRAITS_LONG_FORM_MAPPING_RERUN2.md)
4. C7-1 映射负例断言：
   [`c7_1_mapping_rerun2/METATRAITS_C7_1_NEGATIVE_ASSERTIONS_RERUN2.csv`](c7_1_mapping_rerun2/METATRAITS_C7_1_NEGATIVE_ASSERTIONS_RERUN2.csv)
5. 本地审计：
   [`audits/METATRAITS_BULK_TSV_LANDED_CHENYU_RETURN_LOCAL_AUDIT_2026-08-18.md`](audits/METATRAITS_BULK_TSV_LANDED_CHENYU_RETURN_LOCAL_AUDIT_2026-08-18.md)
   和
   [`audits/METATRAITS_C7_1_LONG_FORM_MAPPING_RERUN2_FALSE_POSITIVE_FIX_RETURN_LOCAL_AUDIT_2026-08-19.md`](audits/METATRAITS_C7_1_LONG_FORM_MAPPING_RERUN2_FALSE_POSITIVE_FIX_RETURN_LOCAL_AUDIT_2026-08-19.md)

## Chenyu 数据路径

MetaTraits bulk TSV 已落在 Chenyu：

```text
/usrdata/EnzymeCAGE_data/data/metatraits/incoming/metatraits_bulk_tsv_snapshot_20260818
```

对应 Chenyu metadata 回包：

```text
/usrdata/EnzymeCAGE_data/EnzymeCAGE-master/HPC_Returned_Result_Summaries/metatraits_bulk_tsv_landed_chenyu_20260818.tar.gz
/usrdata/EnzymeCAGE_data/EnzymeCAGE-master/HPC_Returned_Result_Summaries/metatraits_bulk_tsv_landed_chenyu_20260818.tar.gz.identity.txt
```

C7-1 long-form mapping rerun2 回包：

```text
/usrdata/EnzymeCAGE_data/EnzymeCAGE-master/HPC_Returned_Result_Summaries/metatraits_c7_1_long_form_mapping_rerun2_false_positive_fix_20260819.tar.gz
/usrdata/EnzymeCAGE_data/EnzymeCAGE-master/HPC_Returned_Result_Summaries/metatraits_c7_1_long_form_mapping_rerun2_false_positive_fix_20260819.tar.gz.identity.txt
```

## 数据落地摘要

Landing final status:

```text
METATRAITS_BULK_TSV_LANDED_CHENYU_COMPLETE
required_summary_validated_count=12/12
companion_crosswalk_validated_count=2/2
```

文件范围：

```text
12 个 bulk summary TSV gzip:
  NCBI / GTDB
  family / genus / species
  all / no_predictions

2 个 companion crosswalk:
  GTDB2NCBI.tsv.gz
  NCBI2GTDB.tsv.gz
```

所有 14 个 `.tsv.gz` 均通过 gzip 校验和 SHA256 记录。官方 index 中 14 个
文件的 last modified 均记录为：

```text
2026-06-10 10:23
```

## C7-1 映射修复摘要

Rerun2 final status:

```text
METATRAITS_C7_1_LONG_FORM_MAPPING_RERUN2_FALSE_POSITIVE_FIX_COMPLETE
trait_panel_rows_written=15/15
negative_assertions_passed=8/8
```

MetaTraits bulk TSV 是 long-form 表；映射使用行级字段：

```text
trait_name
unit
consensus_value
minimum
median
mean
maximum
discrete_values
databases
group_1
group_2
ontology_ids
```

不是只按表头关键词匹配。

本次 rerun2 修正了两个假阳性问题：

```text
F3 pH: 不再把 Atmosphere / Morphology / Cell morphology / Cell size phenotype 误映射为 pH
F12 Gram: 不再把 produces: gramicidin 误映射为 Gram/cell-envelope
```

机器可读负例断言全部通过：

```text
ASSERT_F3_NO_ATMOSPHERE_ROWS = PASS
ASSERT_F3_NO_MORPHOLOGY_ROWS = PASS
ASSERT_F3_NO_CELL_MORPHOLOGY_ROWS = PASS
ASSERT_F3_NO_CELL_SIZE_PHENOTYPE_ROWS = PASS
ASSERT_F3_NO_AEROTOLERANT_ROWS = PASS
ASSERT_F3_NO_CAPNOPHILIC_ROWS = PASS
ASSERT_F3_NO_CELL_SHAPE_OR_CELL_SIZE_ROWS = PASS
ASSERT_F12_NO_GRAMICIDIN_ROWS = PASS
```

## 归档与身份

小型 metadata archive 已随本目录保留，便于校验：

```text
hpc_archives/metatraits_bulk_tsv_landed_chenyu_20260818.tar.gz
hpc_archives/metatraits_c7_1_long_form_mapping_rerun2_false_positive_fix_20260819.tar.gz
hpc_identity/metatraits_bulk_tsv_landed_chenyu_20260818.tar.gz.identity.txt
hpc_identity/metatraits_c7_1_long_form_mapping_rerun2_false_positive_fix_20260819.tar.gz.identity.txt
```

archive SHA256:

```text
metatraits_bulk_tsv_landed_chenyu_20260818.tar.gz
cbe9bb3b5372e8a703bdf7387fbf98d4a663d25a45a615b4db84a85e7665fa1b

metatraits_c7_1_long_form_mapping_rerun2_false_positive_fix_20260819.tar.gz
61940833695160553983d05e722af0ee1d10c7ce3d8f3bfbef79c0c567f30db9
```

## 与 C8 的关系

本目录完成的是 C8 前置数据条件之一：MetaTraits TSV 已在 Chenyu 稳定落地，
且 C7-1 字段映射口径已修正。它不是 C8 production 实装，也不代表
TraitFilterLayer 已接入正式链路。
