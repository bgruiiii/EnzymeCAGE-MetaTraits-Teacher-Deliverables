# MetaTraits D5 对 2026-08-03 老师清单的逐条复核索引

日期：2026-08-04  
状态：复核索引；不新增网络请求、不新增 HPC 运行、不启动 M4b。  
目的：回应黄老师 2026-08-03 合并反馈中再次列为 P0 的 D5 metaTraits 预调研要求，明确哪些内容已经在 2026-07-24/2026-07-26 新合同版交付中完成，证据在哪里。

## 1. 总体结论

D5 新合同版预调研已经完成过，不是仅凭文件名沿用旧报告。

主要交付位置：

```text
2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/
```

核心入口：

```text
2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/metatraits_probe_report.md
2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/P0_TOP_MRR_ENZYME_TO_HOST_METATRAITS_CROSSWALK.csv
2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/ORGANISM_ID_ALIGNMENT_EXPLICIT_TRISTATE_SUPPLEMENT_2026-07-26.md
2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/audits/METATRAITS_D5_NEW_CONTRACT_INDEPENDENT_REAUDIT_2026-07-24.md
```

5 个原始 metaTraits JSON 未重写，按字节保留在：

```text
2026-07-24_MT_D5_Accepted_Evidence_Resubmission/raw/metatraits/samples/
```

## 2. 对老师 2026-08-03 D5 要求逐条回应

| 老师要求 | 当前状态 | 证据位置 |
|---|---|---|
| 用 P0 test set Top MRR 的酶反查 5–10 个宿主菌 | 已完成。选择 10 个 P0 Top-MRR 酶，5 个成功 metaTraits 样本来自这 10 个宿主中的固定子集。 | `metatraits_probe_report.md` §3–§4；`P0_TOP_MRR_ENZYME_TO_HOST_METATRAITS_CROSSWALK.csv` |
| 确认不是“排名最前”而是“排名最前的正确酶” | 已完成。crosswalk 区分 `positive_rank=1`、`frozen_test_label=1`、`candidate_source=positive_deduplicated_step4`，并有 UniProt 目标 RHEA 参考。 | `metatraits_probe_report.md` §3；`audits/METATRAITS_D5_NEW_CONTRACT_INDEPENDENT_REAUDIT_2026-07-24.md` §2 |
| 5–10 个真实宿主微生物 | 已完成。10 个 UniProt-reviewed host/taxon 映射；其中 5 个有 metaTraits summary JSON。 | `metatraits_probe_report.md` §4；crosswalk columns `uniprot_tax_id`, `uniprot_organism` |
| 附 5 个 sample 菌原始 JSON | 已完成。5 个 HTTP response bodies 按字节保留，未重构。 | `../2026-07-24_MT_D5_Accepted_Evidence_Resubmission/raw/metatraits/samples/*/summary.json` |
| 接口稳定性 | 已完成。API 16/16 HTTP 404；website summary 5/5 HTTP 200；observation 2/2 HTTP 200；Shewanella repeat 3/3 byte-identical；1 次 TLS timeout。 | `metatraits_probe_report.md` §6.1 |
| 污水相关性状覆盖度 | 已完成。oxygen/temperature/pH/salinity 5/5；wastewater metabolism 4/5；safety/pathogenicity 4/5；biofilm 0/5。 | `metatraits_probe_report.md` §6.2 |
| `no_robust_majority` 比例 | 已完成。五样本合计 43/597 = 7.202680%。 | `metatraits_probe_report.md` §6.3 |
| rate limit | 已完成。15 个完成 HTTP responses 中 0 个 429；published threshold UNKNOWN；不主张无限制。 | `metatraits_probe_report.md` §6.4 |
| ID 对齐初测 | 已完成且为负结果。10/10 TaxID API 404；5 个 species-name summary 只能作为 soft contextual evidence。 | `metatraits_probe_report.md` §7；`ORGANISM_ID_ALIGNMENT_EXPLICIT_TRISTATE_SUPPLEMENT_2026-07-26.md` |
| 区分 exact strain / exact species / no exact match | 已完成。`exact_strain=0`，`exact_species=0`，`no_exact_match_established=10`。 | `ORGANISM_ID_ALIGNMENT_EXPLICIT_TRISTATE_SUPPLEMENT_2026-07-26.md` §3；crosswalk column `metatraits_exact_id_alignment_class` |
| strain 和 species 不能互相继承性状 | 已显式写入。species-name summary 不得升级为 exact strain/species。 | `ORGANISM_ID_ALIGNMENT_EXPLICIT_TRISTATE_SUPPLEMENT_2026-07-26.md` §4 |

## 3. 当前 D5 边界

当前 D5 结论仍然是：

```text
可用于 bounded soft-trait prototyping；
不可用于 hard filtering；
不可用于 production；
不可声称 exact TaxID → trait 通路已打通；
不可启动 M4b。
```

如果老师要求的是“在 2026-08-04 重新联网刷新 metaTraits 数据”，那需要另行授权一次 fresh probe；但按 2026-08-03 清单的文字要求，现有 2026-07-24/07-26 新合同版交付已经逐条覆盖。

