# MetaTraits / 菌侧当前状态索引

日期：2026-08-20

## 已完成并准备给老师审阅

| 项 | 状态 | 老师查看路径 |
|---|---|---|
| C8 主链路 staged-only 实装证据 + 固定 30-row bounded rerun | 按老师 2026-08-19 裁定完成 C8-0 输入冻结、C8-1 lookup index + 137 delta review、C8-2A UID-source expansion harness、C8-3/C8-4 固定 30-row bounded rerun；全部 staged-only，未接 production；C8-5 小型真实候选表 smoke 尚未完成 | [`../2026-08-20_M4b_C8_Staged_Implementation_Bounded_30_Rerun/`](../2026-08-20_M4b_C8_Staged_Implementation_Bounded_30_Rerun/) |
| C8-P porTraits 受控预检决策包 | 已完成环境、输入、版本、资产、容器和配额 preflight；未运行 porTraits、未下载 genome FASTA/数据库/容器、未产生 phenotype prediction；提交 D1-D7 请老师裁定 | [`../2026-08-20_M4b_C8_P_porTraits_Preflight_Decision_Request/`](../2026-08-20_M4b_C8_P_porTraits_Preflight_Decision_Request/) |
| MetaTraits TSV 落晨羽 + C7-1 long-form mapping 修复 | 按老师 2026-08-18 P0 要求整理；12/12 bulk summary TSV + 2/2 crosswalk 已在 Chenyu 数据根验证；C7-1 mapping rerun2 15/15 trait rows、8/8 负例断言 PASS；未上传大 TSV 到 GitHub | [`../2026-08-19_MetaTraits_Bulk_TSV_Landing_and_C7_1_Mapping_Correction/`](../2026-08-19_MetaTraits_Bulk_TSV_Landing_and_C7_1_Mapping_Correction/) |
| C8 TraitFilterLayer 实装方案 / 拆解待审 | 按老师 2026-08-18 要求完成方案；以 C7-2 validator 为入口，拆成 C8-0 到 C8-5；仍 staged-only，未接 production；另列补资产来源 delta 与 porTraits preflight 两个待老师裁定问题 | [`../2026-08-19_M4b_C8_TraitFilterLayer_Implementation_Plan/`](../2026-08-19_M4b_C8_TraitFilterLayer_Implementation_Plan/) |
| 真菌 observed-trait source exploration closure | DSMZ/MediaDive/ATCC 可提供少量可审计 observed evidence，但严格合并覆盖不足；建议停止当前轮次深挖，C7-2 真菌继续 identity-only；`575` 仅为探索内部行级分母，不替代老师口径真菌数 `428` | [`../2026-08-19_M4b_C7_2_Fungal_Observed_Trait_Source_Exploration_Closure/`](../2026-08-19_M4b_C7_2_Fungal_Observed_Trait_Source_Exploration_Closure/) |
| 真菌预测工具迁移待讨论 | 如果真菌 observed source 查不到，是否允许用面向细菌/古菌/原核的预测工具预测真菌；当前不默认执行，需先和师姐/领域 reviewer 讨论，再单独请老师裁定 out-of-domain fungal prediction preflight | [`../2026-08-19_M4b_C7_2_Fungal_Observed_Trait_Source_Exploration_Closure/pending_teacher_discussion/M4B_C7_2_FUNGAL_PREDICTION_TOOL_TRANSFER_DISCUSSION_2026-08-19.md`](../2026-08-19_M4b_C7_2_Fungal_Observed_Trait_Source_Exploration_Closure/pending_teacher_discussion/M4B_C7_2_FUNGAL_PREDICTION_TOOL_TRANSFER_DISCUSSION_2026-08-19.md) |
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

Current decision request = teacher-side review of 2026-08-20 C8 staged implementation evidence,
C8-P porTraits preflight decision request, and remaining C8-5 small real upstream candidate-table smoke boundary.
C7-1 F1-F15 panel is already teacher-frozen by the 2026-08-14 second formal裁定.
C7-2 feature encoding proposal is already teacher-frozen by the 2026-08-17 formal裁定.
MetaTraits local TSV landing and C7-1 long-form mapping rerun2 are ready for teacher review.
C8 TraitFilterLayer implementation plan / breakdown was reviewed into staged execution; C8-0 to C8-4 plus 30-row bounded rerun are now packaged as staged-only evidence.
C8-5 still requires a small real upstream candidate table smoke and teacher confirmation before full rollout.
C8 pending teacher decisions now include rescued-asset-linked source delta and porTraits preflight boundary.
Fungal observed-trait source exploration closure is ready for teacher review;
current recommendation remains fungi identity-only in C7-2, with no merge,
no hard filters, and no fungal prediction claims.
If fungal observed sources are insufficient, transferring bacteria/archaea-oriented
prediction tools to fungi is not authorized by default; discuss with senior
student/domain reviewer first, then submit a separate teacher decision if needed.
```

## 仍保持边界/未启动

| 项 | 状态 |
|---|---|
| M4b / M4c production implementation | 未启动 |
| C7-2 feature encoding | 老师 2026-08-17 已冻结通过为设计契约 |
| TraitFilterLayer schema / validator | 8/18 已完成只读 bounded 30 验证包，待老师审阅；不是 production 实装 |
| C8 TraitFilterLayer implementation | C8-0 至 C8-4 staged-only evidence + 固定 30-row bounded rerun 已回包；C8-5 小型真实候选表 smoke 尚未完成 |
| 2,478 source staged status table | 未生成 |
| MetaTraits species-level trait | 不写成 strain-level trait |
| BacDive species representative strain | 不写成原始 UniProt exact strain |
| BacDive exact-strain claims | 需按 main / conservative / hard policy 分层 |
| fungi in BacDive | non-scope，不计为 BacDive failure |
| Prediction-like traits 使用策略 | 只能按老师冻结边界软补齐并显式标注，不写成 production 主特征 |

## 历史已完成项

2026-08-05 以前的 D5、D1-D8、confidence、ID 对齐、污水 soft trait 策略和 Task 7 `not_applicable` contract 仍保留在仓库中作为历史证据。当前审阅以 2026-08-12 新增交付包为准。
