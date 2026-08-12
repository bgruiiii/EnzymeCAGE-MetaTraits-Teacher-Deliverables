# MetaTraits / 菌侧当前状态索引

日期：2026-08-12

## 已完成并准备给老师审阅

| 项 | 状态 | 老师查看路径 |
|---|---|---|
| MetaTraits 物种级覆盖检查 | 完成 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/01_metatraits_species_coverage/`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/01_metatraits_species_coverage/) |
| BacDive 全量 2,478 source closure | 完成 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/02_bacdive_full_closure/`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/02_bacdive_full_closure/) |
| BacDive vs MetaTraits 性状数量/类别对比 | 完成 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/03_bacdive_vs_metatraits_trait_comparison/`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/03_bacdive_vs_metatraits_trait_comparison/) |
| BacDive species-level representative strain / 保藏编号 v2 展开 | 完成 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/04_bacdive_species_representative_strain_expansion/`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/04_bacdive_species_representative_strain_expansion/) |
| SHA256 manifest | 完成 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/DELIVERABLE_SHA256SUMS.txt`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/DELIVERABLE_SHA256SUMS.txt) |

## 当前推荐设计

```text
MetaTraits = primary species-level trait matrix
BacDive = exact-strain evidence + species-level representative strain availability + culture collection numbers + culture medium + isolation/source metadata
```

## 仍保持边界/未启动

| 项 | 状态 |
|---|---|
| M4b / M4c production implementation | 未启动 |
| MetaTraits species-level trait | 不写成 strain-level trait |
| BacDive species representative strain | 不写成原始 UniProt exact strain |
| BacDive exact-strain claims | 需按 main / conservative / hard policy 分层 |
| fungi in BacDive | non-scope，不计为 BacDive failure |

## 历史已完成项

2026-08-05 以前的 D5、D1-D8、confidence、ID 对齐、污水 soft trait 策略和 Task 7 `not_applicable` contract 仍保留在仓库中作为历史证据。当前审阅以 2026-08-12 新增交付包为准。
