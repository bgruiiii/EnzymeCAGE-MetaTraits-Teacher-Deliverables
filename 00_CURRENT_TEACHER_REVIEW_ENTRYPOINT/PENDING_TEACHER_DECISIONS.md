# 仍需后续裁定的问题（MetaTraits / 菌侧）

日期：2026-08-18
说明：本文件只列“尚未正式裁定或尚未进入 production 实现”的事项，避免把探索结果写成已经批准或已经上线。

## 0. 2026-08-18 C7-2 schema/validator 提交后仍待裁定

| 问题 | 当前证据 | 需要裁定/确认 |
|---|---|---|
| C7-2 read-only schema/validator bounded 30 | 2026-08-18 已按老师 2026-08-17 裁定提交 `POLICY_MANIFEST` / `TRAIN_SET_MANIFEST` / `trait_annotation.jsonl` / 校验报告；仍 staged-only | 请老师审阅本次只读 schema/validator bounded 子集是否通过 |
| C7-2 feature encoding proposal | 老师 2026-08-17 已冻结通过为设计契约 | 不再请求冻结；仅作为本次 schema/validator 的冻结依据 |
| TraitFilterLayer implementation | 当前仅完成只读 bounded 30 schema/validator 验证包，未接 production | 后续是否授权 2,478 source staged status table 或 production integration，需另行裁定 |
| 2,478 source staged status table | 当前尚未生成 C7 staged status table | 需等 schema/validator 和 staged subset smoke 后再启动 |
| Production integration | 当前仍为 staged soft layer 候选流程 | 是否在后续 staged 验收后另行授权 production，当前不请求 |
| P18173 / P80550 accession clarification | 老师 2026-08-17 要求单独澄清 P18173 的 Q8SXV0 vs U3PT72 选择规则、P80550 original 38aa 来源 | 这是独立 table-only 小任务，不属于本次 C7-2 schema/validator 包 |

## 1. 本次 2026-08-12 结果后的建议裁定点

| 问题 | 当前证据 | 需要裁定/确认 |
|---|---|---|
| 微生物侧主性状来源 | MetaTraits 覆盖 1,638 / 2,478，confirmed covered source 平均约 156.8 个 unique trait_name | 是否采用 MetaTraits 作为 primary species-level trait matrix |
| BacDive 的角色 | BacDive validated species-or-better 1,746 / 2,478；species-level representative expansion v2 中 1,149 / 1,149 有 representative strain record 和 culture collection number | 是否采用 BacDive 作为 exact-strain / representative strain availability / culture collection / provenance layer |
| species-level trait 边界 | MetaTraits 只能作为 species-level trait，不等于 strain-level trait | 是否接受 species-level trait_resolution 标注进入后续 schema |
| species-level representative strain 边界 | BacDive representative records 不等于原始 UniProt exact strain | 是否接受 representative strain availability 作为可获得性证据，而非 exact-strain claim |
| 后续 production schema | 当前已形成 schema/validator bounded 30 只读验证包，但尚未进入 M4b/M4c production implementation | 是否授权后续实现/集成 |
| 污染物降解核心性状面板 | 老师 2026-08-14 第二份裁定已冻结 C7-1 F1-F15 | C7-2 只请求编码方案冻结，不再请求扩项 |
| Prediction-like traits 使用策略 | 老师冻结 observed 优先、允许类别 predicted 软补齐、预测必须标注 | 后续实现需按 C7-2 编码方案逐项落字段并审计 |
| 真菌 trait 策略 | 老师冻结真菌 428 株 identity-only，不启用 predicted 软补齐 | 后续真菌预测工具评估若启动，应作为单独支线另请裁定 |

## 2. 仍不能误写成完成的内容

```text
C7-2 feature encoding 已被老师 2026-08-17 冻结为设计契约；
TraitFilterLayer schema/validator 仅完成 8/18 只读 bounded 30 验证包；
2,478 source staged status table 尚未生成；
M4b / M4c production pipeline 尚未启动；
MetaTraits species-level trait 不能冒充 strain-level trait；
BacDive species-level representative strain 不能冒充原始 UniProt exact strain；
BacDive exact-strain evidence 需要保留 main / conservative / hard policy 分层；
fungi 属于 BacDive non-scope，不计为 BacDive 查询失败；
biosafety level 已从 C7-1 trait panel 删除，不作为本轮性状；
prediction-like traits 只能按老师冻结边界软补齐并显式标注，不写成 production 主特征。
```

## 3. 建议汇报口径

```text
菌侧已按老师 2026-08-17 裁定完成 C7-2 只读 schema/validator bounded 30 回包。包内包含 POLICY_MANIFEST、TRAIN_SET_MANIFEST、trait_annotation.jsonl、校验报告、边界报告和 MANIFEST；当前仍 staged-only，未接 production。请老师审阅本次 bounded schema/validator 结果。
```
