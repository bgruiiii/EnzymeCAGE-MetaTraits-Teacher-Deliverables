# 当前老师审阅入口（MetaTraits / 菌侧）

更新时间：2026-08-18
用途：给老师打开 GitHub 后的第一入口，避免从根目录历史散文件中自行判断最新状态。

## 1. 老师优先看哪些文件

| 优先级 | 内容 | 路径 |
|---|---|---|
| 1 | 2026-08-18 C7-2 只读 schema/validator bounded 30 交付包 | [`../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/`](../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/) |
| 2 | C7-2 校验报告 | [`../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/TRAIT_FEATURE_ENCODING_VALIDATION_REPORT.md`](../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/TRAIT_FEATURE_ENCODING_VALIDATION_REPORT.md) |
| 3 | C7-2 边界报告 | [`../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/BOUNDARY_VALIDATION_REPORT.md`](../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/BOUNDARY_VALIDATION_REPORT.md) |
| 4 | 老师 2026-08-17 已冻结通过的 C7-2 feature encoding 提案 | [`../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/`](../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/) |
| 5 | 2026-08-14 C7-1 frozen trait panel 证据包 | [`../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/`](../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/) |
| 6 | 2026-08-12 MetaTraits + BacDive 微生物侧性状/可获得性交付包 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/) |

## 2. 当前状态一句话

截至 2026-08-18，老师已在 2026-08-17 裁定中冻结 C7-2 feature encoding
设计契约，并授权下一步只读 schema/validator 实装 + bounded staged 子集。
菌侧本次提交 30 行 bounded 验证包：10 细菌、10 古菌、10 真菌；细菌部分优先
选择环境/工业语境示例；仍为 staged-only，未接 production。

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

C7-2 8/18 bounded 30 中，10 个细菌第一屏五项覆盖：

```text
temperature observed: 10/10
pH observed: 5/10, predicted soft-fill: 5/10
oxygen / anaerobic observed: 10/10
salinity observed: 8/10, predicted soft-fill: 2/10
BacDive culture collection / availability observed: 10/10
```

古菌第一屏结果：BacDive availability 10/10 observed，MetaTraits 四项本地未观察。
真菌第一屏结果：本轮全部 identity-only，不做软补齐。

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
C7-2 feature encoding 已被老师 2026-08-17 冻结为设计契约；
8/18 schema/validator 包是只读 bounded staged 子集验证，仍不代表 production 实装；
2,478 source staged status table 尚未生成；
prediction-like traits 只能按老师冻结边界软补齐并显式标注，不写成 production 主特征。
```

## 5. 为什么根目录仍保留历史文件

根目录中保留了若干历史提交文件，是为了不破坏已经发给老师的旧 GitHub 链接。当前审阅请优先看本文件夹、仓库顶层 README 的 2026-08-12 入口，以及本次新增交付包。
