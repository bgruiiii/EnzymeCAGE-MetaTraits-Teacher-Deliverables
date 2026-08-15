# 仍需后续裁定的问题（MetaTraits / 菌侧）

日期：2026-08-15
说明：本文件只列“尚未正式裁定或尚未进入 production 实现”的事项，避免把探索结果写成已经批准或已经上线。

## 0. 2026-08-15 C7-2 提交后仍待裁定

| 问题 | 当前证据 | 需要裁定/确认 |
|---|---|---|
| C7-2 feature encoding proposal | 2026-08-15 已提交提案，引用老师冻结的 F1-F15、7.2 loader 契约和 7.3 菌层消费接口 | 请老师审阅并冻结/要求修改 C7-2 编码方案 |
| TraitFilterLayer implementation | 当前只有 C7-2 提案，没有代码/schema/validator/smoke | C7-2 freeze 后是否授权进入只读 schema/validator 小任务 |
| 2,478 source staged status table | 当前尚未生成 C7 staged status table | 需等 schema/validator 和 staged subset smoke 后再启动 |
| Production integration | 当前仍为 staged soft layer 候选流程 | 是否在后续 staged 验收后另行授权 production，当前不请求 |

## 1. 本次 2026-08-12 结果后的建议裁定点

| 问题 | 当前证据 | 需要裁定/确认 |
|---|---|---|
| 微生物侧主性状来源 | MetaTraits 覆盖 1,638 / 2,478，confirmed covered source 平均约 156.8 个 unique trait_name | 是否采用 MetaTraits 作为 primary species-level trait matrix |
| BacDive 的角色 | BacDive validated species-or-better 1,746 / 2,478；species-level representative expansion v2 中 1,149 / 1,149 有 representative strain record 和 culture collection number | 是否采用 BacDive 作为 exact-strain / representative strain availability / culture collection / provenance layer |
| species-level trait 边界 | MetaTraits 只能作为 species-level trait，不等于 strain-level trait | 是否接受 species-level trait_resolution 标注进入后续 schema |
| species-level representative strain 边界 | BacDive representative records 不等于原始 UniProt exact strain | 是否接受 representative strain availability 作为可获得性证据，而非 exact-strain claim |
| 后续 production schema | 当前已形成 schema 建议，但尚未进入 M4b/M4c production implementation | 是否授权后续实现/集成 |
| 污染物降解核心性状面板 | 老师 2026-08-14 第二份裁定已冻结 C7-1 F1-F15 | C7-2 只请求编码方案冻结，不再请求扩项 |
| Prediction-like traits 使用策略 | 老师冻结 observed 优先、允许类别 predicted 软补齐、预测必须标注 | 后续实现需按 C7-2 编码方案逐项落字段并审计 |
| 真菌 trait 策略 | 老师冻结真菌 428 株 identity-only，不启用 predicted 软补齐 | 后续真菌预测工具评估若启动，应作为单独支线另请裁定 |

## 2. 仍不能误写成完成的内容

```text
C7-2 feature encoding 尚未被老师冻结；
TraitFilterLayer schema/validator 尚未实装；
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
菌侧已按老师 2026-08-14 第二份正式裁定完成 C7-2 feature encoding 提案回包。提案引用已冻结的 F1-F15 trait panel，保持真菌 identity-only，按 7.2 loader 契约设计 TRAIN_SET_MANIFEST.csv，按 7.3 菌层接口设计 trait_annotation.jsonl；当前仍是 staged proposal，未实装、未接 production。请老师审阅并裁定 C7-2 编码方案。
```
