# 仍需后续裁定的问题（MetaTraits / 菌侧）

日期：2026-08-13  
说明：本文件只列“尚未正式裁定或尚未进入 production 实现”的事项，避免把探索结果写成已经批准或已经上线。

## 0. 2026-08-13 C7 立项待裁定

| 问题 | 当前证据 | 需要裁定/确认 |
|---|---|---|
| M4b/C7 是否授权 | C1-C6、MT-TQ-02、08-12 hybrid 数据面均已满足前置；C7 蓝图已提交 | 是否授权进入 M4b/C7 立项流程 |
| TraitFilterLayer v1 范围 | 蓝图建议只做 staged soft trait layer，不做 hard filtering / production mutation | 是否接受该 v1 范围 |
| observed/predicted 路线 | 建议 B：observed 优先，核心缺失 trait predicted soft-fill，并保留 evidence/provenance | 是否接受 B 路线 |
| 核心 trait panel | 候选面板已列出，但需师姐/领域侧讨论 | 是否先由领域侧确认后再冻结 |
| 真菌策略 | 当前 MetaTraits/BacDive 对真菌不形成普通 observed 覆盖；建议评估预测补充或真菌专用资源 | 是否按单独路线处理真菌 |

## 1. 本次 2026-08-12 结果后的建议裁定点

| 问题 | 当前证据 | 需要裁定/确认 |
|---|---|---|
| 微生物侧主性状来源 | MetaTraits 覆盖 1,638 / 2,478，confirmed covered source 平均约 156.8 个 unique trait_name | 是否采用 MetaTraits 作为 primary species-level trait matrix |
| BacDive 的角色 | BacDive validated species-or-better 1,746 / 2,478；species-level representative expansion v2 中 1,149 / 1,149 有 representative strain record 和 culture collection number | 是否采用 BacDive 作为 exact-strain / representative strain availability / culture collection / provenance layer |
| species-level trait 边界 | MetaTraits 只能作为 species-level trait，不等于 strain-level trait | 是否接受 species-level trait_resolution 标注进入后续 schema |
| species-level representative strain 边界 | BacDive representative records 不等于原始 UniProt exact strain | 是否接受 representative strain availability 作为可获得性证据，而非 exact-strain claim |
| 后续 production schema | 当前已形成 schema 建议，但尚未进入 M4b/M4c production implementation | 是否授权后续实现/集成 |
| 污染物降解核心性状面板 | MetaTraits 可提供 environmental preferences、metabolism、physiology、genome、enzymes、safety 等类别；不同类别 observed 覆盖差异很大 | 请裁定哪些性状应作为污水污染物降解微生物的核心面板 |
| Prediction-like traits 使用策略 | all 与 no_predictions 的 source 覆盖同为 1,638 / 2,478，但 covered source 平均 unique trait_name 为 156.8 vs 47.7 | 是否允许对核心性状中 observed 缺失的项目使用 predicted soft feature，并保留 evidence_type |
| 真菌 trait 策略 | 当前 428 个 target_fungi 在本地 MetaTraits NCBI summary 中未覆盖，BacDive 又属于 prokaryote-focused non-scope | 是否暂不加入真菌性状、寻找真菌专用资源，或允许预测性状单独标注进入 |

## 2. 仍不能误写成完成的内容

```text
M4b / M4c production pipeline 尚未启动；
MetaTraits species-level trait 不能冒充 strain-level trait；
BacDive species-level representative strain 不能冒充原始 UniProt exact strain；
BacDive exact-strain evidence 需要保留 main / conservative / hard policy 分层；
fungi 属于 BacDive non-scope，不计为 BacDive 查询失败；
prediction-like traits 尚未裁定为 production 主特征，若使用应保留 evidence_type 与 missing/observed/predicted 标记。
```

## 3. 建议汇报口径

```text
菌侧已完成 MetaTraits 与 BacDive 的全量可获得性探索和对比。结果支持使用 MetaTraits 作为物种级主性状矩阵，并使用 BacDive 补充 exact-strain evidence、species-level representative strain availability、保藏编号、培养基和分离来源。下一步建议先裁定污染物降解核心性状面板，以及 observed 缺失时 predicted trait 是否可作为 soft feature 补齐；后续是否进入 production schema / M4b/M4c 实现仍需正式授权。
```
