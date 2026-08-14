# 当前老师审阅入口（MetaTraits / 菌侧）

更新时间：2026-08-14  
用途：给老师打开 GitHub 后的第一入口，避免从根目录历史散文件中自行判断最新状态。

## 1. 老师优先看哪些文件

| 优先级 | 内容 | 路径 |
|---|---|---|
| 1 | 2026-08-14 C7-1 trait panel 候选表 | [`../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/`](../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/) |
| 2 | C7-1 正式说明 | [`../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/M4B_C7_1_TRAIT_PANEL_CANDIDATE_REPORT_2026-08-14.md`](../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/M4B_C7_1_TRAIT_PANEL_CANDIDATE_REPORT_2026-08-14.md) |
| 3 | C7-1 候选表 CSV | [`../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/C7_1_TRAIT_PANEL_CANDIDATE_TABLE_2026-08-14.csv`](../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/C7_1_TRAIT_PANEL_CANDIDATE_TABLE_2026-08-14.csv) |
| 4 | 2026-08-13 M4b/C7 TraitFilterLayer 立项材料 | [`../2026-08-13_M4b_C7_TraitFilterLayer_Initiation/`](../2026-08-13_M4b_C7_TraitFilterLayer_Initiation/) |
| 5 | 2026-08-12 MetaTraits + BacDive 微生物侧性状/可获得性交付包 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/) |

## 2. 当前状态一句话

截至 2026-08-14，菌侧已提交 C7-1 trait panel 候选表。该表按老师要求
附来源库、证据级别、soft role、允许/禁止类别引用、数据覆盖率和师姐讨论
意见栏，等待老师逐项冻结；未实装、未接 production。

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

C7-1 候选面板第一屏展示：

```text
temperature / pH / oxygen-anaerobic status / salinity / BacDive culture collection number
```

C7-1 明确删除：

```text
biosafety level 不进入 trait panel
```

## 4. 当前不能误写成完成的内容

```text
MetaTraits species-level trait 不等于 strain-level trait；
BacDive species-level representative strain record 不等于原始 UniProt exact strain；
BacDive exact-strain evidence 需要按 main / conservative / hard policy 分层；
真菌属于 BacDive non-scope，不应计为 BacDive 查询失败；
当前结果支持 schema 设计与后续实现，但不代表 M4b/M4c production pipeline 已经启动。
M4b/C7 C7-1 仍是候选表，等待老师逐项冻结；
B 路线和真菌策略将在 C7-2 中按老师授权单独裁定；
prediction-like traits 的使用只作为候选口径，不写成 production 主特征。
```

## 5. 为什么根目录仍保留历史文件

根目录中保留了若干历史提交文件，是为了不破坏已经发给老师的旧 GitHub 链接。当前审阅请优先看本文件夹、仓库顶层 README 的 2026-08-12 入口，以及本次新增交付包。
