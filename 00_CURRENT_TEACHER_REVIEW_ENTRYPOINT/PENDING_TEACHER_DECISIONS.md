# 仍需后续裁定的问题（MetaTraits / 菌侧）

日期：2026-08-14  
说明：本文件只列“尚未正式裁定或尚未进入 production 实现”的事项，避免把探索结果写成已经批准或已经上线。

## 0. 2026-08-14 C7-1 提交后仍待裁定

| 问题 | 当前证据 | 需要裁定/确认 |
|---|---|---|
| C7-1 trait panel | 2026-08-14 已提交候选表，含来源库、证据级别、soft role、允许/禁止类别引用、覆盖率和师姐讨论意见 | 请老师逐项冻结或要求修改 |
| C7-2 observed/predicted route | C7-1 中仅记录候选口径：observed 优先，允许类别可 predicted soft-fill；预测必须标注 | 是否进入 C7-2 并裁定正式路线 |
| C7-2 真菌策略 | C7-1 报告按老师边界写为 identity-only；师姐建议另测真菌基因组性状预测工具 | 是否保持 identity-only；是否授权单独真菌预测可行性评估 |
| TraitFilterLayer implementation | 当前只有 C7-1 候选表，没有代码/schema/validator/smoke | C7-1 freeze 后是否进入 C7-2/C7-3 |
| Production integration | 当前仍为 staged soft layer 候选流程 | 是否在后续 staged 验收后另行授权 production，当前不请求 |

## 1. 本次 2026-08-12 结果后的建议裁定点

| 问题 | 当前证据 | 需要裁定/确认 |
|---|---|---|
| 微生物侧主性状来源 | MetaTraits 覆盖 1,638 / 2,478，confirmed covered source 平均约 156.8 个 unique trait_name | 是否采用 MetaTraits 作为 primary species-level trait matrix |
| BacDive 的角色 | BacDive validated species-or-better 1,746 / 2,478；species-level representative expansion v2 中 1,149 / 1,149 有 representative strain record 和 culture collection number | 是否采用 BacDive 作为 exact-strain / representative strain availability / culture collection / provenance layer |
| species-level trait 边界 | MetaTraits 只能作为 species-level trait，不等于 strain-level trait | 是否接受 species-level trait_resolution 标注进入后续 schema |
| species-level representative strain 边界 | BacDive representative records 不等于原始 UniProt exact strain | 是否接受 representative strain availability 作为可获得性证据，而非 exact-strain claim |
| 后续 production schema | 当前已形成 schema 建议，但尚未进入 M4b/M4c production implementation | 是否授权后续实现/集成 |
| 污染物降解核心性状面板 | C7-1 已提交候选面板；第一屏候选为温度、pH、耗氧/厌氧、盐度、BacDive 保藏编号；其他性状追问展开 | 请老师逐项冻结、删改或要求补充 |
| Prediction-like traits 使用策略 | all 与 no_predictions 的 source 覆盖同为 1,638 / 2,478，但 covered source 平均 unique trait_name 为 156.8 vs 47.7 | C7-2 是否允许对核心性状中 observed 缺失的项目使用 predicted soft feature，并保留 evidence_type |
| 真菌 trait 策略 | 当前 428 个 target_fungi 在本地 MetaTraits NCBI summary 中未覆盖，BacDive 又属于 prokaryote-focused non-scope | 是否暂不加入真菌性状、寻找真菌专用资源，或允许预测性状单独标注进入 |

## 2. 仍不能误写成完成的内容

```text
C7-1 trait panel 尚未被老师逐项冻结；
C7-2 route/fungal policy 尚未启动；
M4b / M4c production pipeline 尚未启动；
MetaTraits species-level trait 不能冒充 strain-level trait；
BacDive species-level representative strain 不能冒充原始 UniProt exact strain；
BacDive exact-strain evidence 需要保留 main / conservative / hard policy 分层；
fungi 属于 BacDive non-scope，不计为 BacDive 查询失败；
biosafety level 已从 C7-1 trait panel 删除，不作为本轮性状；
prediction-like traits 尚未裁定为 production 主特征，若使用应保留 evidence_type 与 missing/observed/predicted 标记。
```

## 3. 建议汇报口径

```text
菌侧已完成 C7-1 trait panel 候选表。结果建议第一屏展示温度、pH、耗氧/厌氧、盐度和 BacDive 保藏编号；其他保留性状按追问展开；biosafety level 不进入 C7-1 trait panel；真菌本轮 identity-only。下一步请老师逐项冻结 C7-1 panel，之后再进入 C7-2 observed/predicted 路线和真菌策略裁定。
```
