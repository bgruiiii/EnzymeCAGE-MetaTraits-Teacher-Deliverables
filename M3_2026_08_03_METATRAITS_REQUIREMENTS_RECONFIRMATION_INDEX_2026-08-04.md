# M3 2026-08-03 MetaTraits / 菌层要求再确认索引

日期：2026-08-04  
状态：本地索引，待统一 GitHub push。  
目的：回应黄老师 2026-08-03 清单中菌层下半链、D5、D1-D8、confidence、Task 7 等要求，明确哪些内容已经完成、证据在哪里、哪些仍是未闭合边界。

## 1. 本轮新增入口

本轮新增再确认包：

```text
2026-08-04_M3_Bacteria_Layer_D1_D8_Confidence_and_Task7_Reconfirmation/
```

包内关键文件：

```text
README.md
audits/M3_BACTERIA_LAYER_D1_D8_AND_CONFIDENCE_REQUIREMENTS_REAUDIT_2026-08-04.md
audits/M3_TASK7_TRAITVALUE_NOT_APPLICABLE_2026_08_03_RECONFIRMATION_AUDIT_2026-08-04.md
DELIVERABLE_SHA256SUMS.txt
```

## 2. D5 新合同预调研

D5 已完成新合同版，不是只沿用旧文件名。

D5 新合同版交付：

```text
2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/
```

本轮 D5 再确认索引：

```text
METATRAITS_D5_2026_08_03_TEACHER_LIST_RECONFIRMATION_INDEX_2026-08-04.md
```

关键覆盖：

```text
P0 Top-MRR 正确酶 -> host mapping；
10 个 P0-derived host mappings；
5 个 raw summary JSON；
API stability；
wastewater trait coverage；
no_robust_majority；
rate limit；
ID alignment；
exact strain / exact species / no exact match 三分类。
```

## 3. ⑤⑥⑦ / D1-D8 / confidence

本轮再确认：

```text
2026-08-04_M3_Bacteria_Layer_D1_D8_Confidence_and_Task7_Reconfirmation/
audits/M3_BACTERIA_LAYER_D1_D8_AND_CONFIDENCE_REQUIREMENTS_REAUDIT_2026-08-04.md
```

关键结论：

```text
D1-D8 已由 2026-07-18 老师文件正式裁定；
D3 tie-break 后续修正为 supporting-enzyme count descending + numeric NCBI taxon ID ascending；
D4 继续 soft-only，不自动删除候选菌；
D2 / confidence 不输出伪精确 organism_confidence float；
如未来必须 numeric confidence，需要另写 CONFIDENCE_MAPPING_PROPOSAL.md；
official versioned MetaTraits snapshot 尚未取得；
sampled exact strain/species ID alignment 未建立精确匹配。
```

## 4. Task 7

既有 contract：

```text
TRAIT_VALUE_NOT_APPLICABLE_SCHEMA_CONTRACT.md
2026-07-24_Task7_TraitValue_Not_Applicable_Contract/
```

本轮再确认：

```text
2026-08-04_M3_Bacteria_Layer_D1_D8_Confidence_and_Task7_Reconfirmation/
audits/M3_TASK7_TRAITVALUE_NOT_APPLICABLE_2026_08_03_RECONFIRMATION_AUDIT_2026-08-04.md
```

结论：

```text
Task 7 内容已完成；
contract-only；
不落 Pydantic 活代码；
不启动 M4b/M4c。
```

## 5. D4 soft 生物学决定

既有决定记录：

```text
2026-07-27_M3_D4_Wastewater_Trait_Soft_Policy_Decision/
```

结论：

```text
污水相关性状保留为参考、建议、解释和不确定性提示；
不自动删除候选菌；
不执行 hard rejection；
不做 species/strain 相互继承。
```

## 6. 不能过度声称

不能说：

```text
MetaTraits exact TaxID -> trait production 通路已打通；
official versioned snapshot 已取得；
organism_confidence 0-1 数值已经实现；
污水 trait 已作为 hard filter 自动删除候选菌；
M4b / M4c 已启动。
```
