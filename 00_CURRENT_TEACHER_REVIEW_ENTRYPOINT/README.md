# 当前老师审阅入口（MetaTraits / 菌侧）

更新时间：2026-08-13  
用途：给老师打开 GitHub 后的第一入口，避免从根目录历史散文件中自行判断最新状态。

## 1. 老师优先看哪些文件

| 优先级 | 内容 | 路径 |
|---|---|---|
| 1 | 2026-08-13 M4b/C7 TraitFilterLayer 立项材料 | [`../2026-08-13_M4b_C7_TraitFilterLayer_Initiation/`](../2026-08-13_M4b_C7_TraitFilterLayer_Initiation/) |
| 2 | C7 TraitFilterLayer 立项蓝图 | [`../2026-08-13_M4b_C7_TraitFilterLayer_Initiation/M4B_C7_TRAITFILTERLAYER_INITIATION_BLUEPRINT_2026-08-13.md`](../2026-08-13_M4b_C7_TraitFilterLayer_Initiation/M4B_C7_TRAITFILTERLAYER_INITIATION_BLUEPRINT_2026-08-13.md) |
| 3 | 2026-08-12 MetaTraits + BacDive 微生物侧性状/可获得性交付包 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/) |
| 4 | BacDive vs MetaTraits 性状可获得性对比报告 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/03_bacdive_vs_metatraits_trait_comparison/BACDIVE_VS_METATRAITS_TRAIT_AVAILABILITY_COMPARISON_2026-08-12.md`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/03_bacdive_vs_metatraits_trait_comparison/BACDIVE_VS_METATRAITS_TRAIT_AVAILABILITY_COMPARISON_2026-08-12.md) |
| 5 | 性状面板与 prediction 使用策略待讨论清单 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/05_next_discussion_trait_panel_and_prediction_policy/TRAIT_PANEL_AND_PREDICTION_POLICY_DISCUSSION_REQUEST_2026-08-12.md`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/05_next_discussion_trait_panel_and_prediction_policy/TRAIT_PANEL_AND_PREDICTION_POLICY_DISCUSSION_REQUEST_2026-08-12.md) |

## 2. 当前状态一句话

截至 2026-08-13，菌侧已在 08-12 hybrid 数据面基础上提交 M4b/C7
TraitFilterLayer 立项蓝图。建议 B 路线：observed traits 优先，核心
trait 缺失时 predicted soft-fill，并保留 evidence/provenance；该路线仍需
老师裁定后才能实装。

## 3. 本次关键结果

```text
Final clean microbe source universe: 2,478 source_signatures / 145,607 enzyme-source rows
MetaTraits coverage: 1,638 / 2,478 = 66.1%
BacDive validated species-or-better: 1,746 / 2,478 = 70.5%
BacDive exact_strain_main: 597 / 2,478 = 24.1%
BacDive hard exact strain: 555 / 2,478 = 22.4%
BacDive + MetaTraits both covered: 1,508 source_signatures
BacDive only: 238 source_signatures
MetaTraits only: 130 source_signatures
BacDive species-level representative expansion v2: 1,149 / 1,149 have at least one representative strain record and at least one culture collection number
MetaTraits all vs no_predictions: source coverage both 1,638 / 2,478; mean unique traits per covered source 156.8 vs 47.7
```

## 4. 当前不能误写成完成的内容

```text
MetaTraits species-level trait 不等于 strain-level trait；
BacDive species-level representative strain record 不等于原始 UniProt exact strain；
BacDive exact-strain evidence 需要按 main / conservative / hard policy 分层；
真菌属于 BacDive non-scope，不应计为 BacDive 查询失败；
当前结果支持 schema 设计与后续实现，但不代表 M4b/M4c production pipeline 已经启动。
M4b/C7 尚未获授权实装；
B 路线只是提交给老师审阅的建议，不写成已裁定；
prediction-like traits 的使用策略尚需裁定；当前建议是先定义核心性状面板，再决定 observed 缺失时是否允许 predicted soft fill。
```

## 5. 为什么根目录仍保留历史文件

根目录中保留了若干历史提交文件，是为了不破坏已经发给老师的旧 GitHub 链接。当前审阅请优先看本文件夹、仓库顶层 README 的 2026-08-12 入口，以及本次新增交付包。
