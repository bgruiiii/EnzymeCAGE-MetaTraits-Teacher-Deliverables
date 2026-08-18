# MetaTraits / 菌侧当前状态索引

日期：2026-08-18

## 已完成并准备给老师审阅

| 项 | 状态 | 老师查看路径 |
|---|---|---|
| C7-2 schema/validator bounded 30 | 按老师 2026-08-17 裁定完成只读 schema/validator + bounded staged 子集；提交老师审阅；未接 production | [`../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/`](../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/) |
| C7-2 feature encoding 提案 | 老师 2026-08-17 已冻结通过为设计契约；作为本次 schema/validator 的冻结依据 | [`../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/`](../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/) |
| C7-1 trait panel | 老师 2026-08-14 第二份裁定已逐项冻结 F1-F15；本包保留冻结前候选表证据 | [`../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/`](../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/) |
| M4b/C7 TraitFilterLayer 立项材料 | 老师已授权立项流程；作为 C7-2 的历史蓝图证据 | [`../2026-08-13_M4b_C7_TraitFilterLayer_Initiation/`](../2026-08-13_M4b_C7_TraitFilterLayer_Initiation/) |
| C7 observed/predicted 路线和真菌策略 | 老师最新裁定已纳入 C7-2 约束：observed 优先、允许类别 predicted 软补齐、真菌 identity-only | [`../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/M4B_C7_2_FEATURE_ENCODING_PROPOSAL_2026-08-15.md`](../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/M4B_C7_2_FEATURE_ENCODING_PROPOSAL_2026-08-15.md) |
| MetaTraits 物种级覆盖检查 | 完成 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/01_metatraits_species_coverage/`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/01_metatraits_species_coverage/) |
| BacDive 全量 2,478 source closure | 完成 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/02_bacdive_full_closure/`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/02_bacdive_full_closure/) |
| BacDive vs MetaTraits 性状数量/类别对比 | 完成 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/03_bacdive_vs_metatraits_trait_comparison/`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/03_bacdive_vs_metatraits_trait_comparison/) |
| BacDive species-level representative strain / 保藏编号 v2 展开 | 完成 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/04_bacdive_species_representative_strain_expansion/`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/04_bacdive_species_representative_strain_expansion/) |
| 性状面板与 prediction 使用策略讨论材料 | 完成，待老师/领域 reviewer 裁定 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/05_next_discussion_trait_panel_and_prediction_policy/`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/05_next_discussion_trait_panel_and_prediction_policy/) |
| SHA256 manifest | 完成 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/DELIVERABLE_SHA256SUMS.txt`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/DELIVERABLE_SHA256SUMS.txt) |

## 当前推荐设计

```text
MetaTraits = primary species-level trait matrix
BacDive = exact-strain evidence + species-level representative strain availability + culture collection numbers + culture medium + isolation/source metadata

Current decision request = teacher-side review of C7-2 read-only schema/validator bounded 30 package.
C7-1 F1-F15 panel is already teacher-frozen by the 2026-08-14 second formal裁定.
C7-2 feature encoding proposal is already teacher-frozen by the 2026-08-17 formal裁定.
```

## 仍保持边界/未启动

| 项 | 状态 |
|---|---|
| M4b / M4c production implementation | 未启动 |
| C7-2 feature encoding | 老师 2026-08-17 已冻结通过为设计契约 |
| TraitFilterLayer schema / validator | 8/18 已完成只读 bounded 30 验证包，待老师审阅；不是 production 实装 |
| 2,478 source staged status table | 未生成 |
| MetaTraits species-level trait | 不写成 strain-level trait |
| BacDive species representative strain | 不写成原始 UniProt exact strain |
| BacDive exact-strain claims | 需按 main / conservative / hard policy 分层 |
| fungi in BacDive | non-scope，不计为 BacDive failure |
| Prediction-like traits 使用策略 | 只能按老师冻结边界软补齐并显式标注，不写成 production 主特征 |

## 历史已完成项

2026-08-05 以前的 D5、D1-D8、confidence、ID 对齐、污水 soft trait 策略和 Task 7 `not_applicable` contract 仍保留在仓库中作为历史证据。当前审阅以 2026-08-12 新增交付包为准。
