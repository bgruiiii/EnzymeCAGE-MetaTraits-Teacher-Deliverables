# 当前老师审阅入口（MetaTraits / 菌侧）

更新时间：2026-08-16
用途：给老师打开 GitHub 后的第一入口，避免从根目录历史散文件中自行判断最新状态。

## 1. 老师优先看哪些文件

| 优先级 | 内容 | 路径 |
|---|---|---|
| 1 | 2026-08-16 C7-2 feature encoding 提案 | [`../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/`](../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/) |
| 2 | C7-2 主提案 | [`../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/M4B_C7_2_FEATURE_ENCODING_PROPOSAL_2026-08-15.md`](../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/M4B_C7_2_FEATURE_ENCODING_PROPOSAL_2026-08-15.md) |
| 3 | C7-2 本地审计 | [`../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/audits/M4B_C7_2_FEATURE_ENCODING_PROPOSAL_LOCAL_AUDIT_2026-08-15.md`](../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/audits/M4B_C7_2_FEATURE_ENCODING_PROPOSAL_LOCAL_AUDIT_2026-08-15.md) |
| 4 | 2026-08-14 C7-1 frozen trait panel 证据包 | [`../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/`](../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/) |
| 5 | 2026-08-13 M4b/C7 TraitFilterLayer 立项材料 | [`../2026-08-13_M4b_C7_TraitFilterLayer_Initiation/`](../2026-08-13_M4b_C7_TraitFilterLayer_Initiation/) |
| 6 | 2026-08-12 MetaTraits + BacDive 微生物侧性状/可获得性交付包 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/) |

## 2. 当前状态一句话

截至 2026-08-16，老师已在 2026-08-14 第二份正式裁定中逐项冻结 C7-1
F1-F15 trait panel。菌侧本次提交 C7-2 feature encoding 提案，按冻结的
F1-F15 条目、真菌 identity-only 边界、7.2 loader 契约和 7.3 菌层消费接口
设计后续 staged 编码方案；尚未实装、尚未接 production。

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

C7-1 冻结面板第一屏展示：

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
C7-1 已被老师逐项冻结，但 C7-2 feature encoding 仍是提交给老师审阅的提案；
C7-2 尚未被老师冻结；
TraitFilterLayer schema/validator 尚未实装；
2,478 source staged status table 尚未生成；
prediction-like traits 只能按老师冻结边界软补齐并显式标注，不写成 production 主特征。
```

## 5. 为什么根目录仍保留历史文件

根目录中保留了若干历史提交文件，是为了不破坏已经发给老师的旧 GitHub 链接。当前审阅请优先看本文件夹、仓库顶层 README 的 2026-08-12 入口，以及本次新增交付包。
