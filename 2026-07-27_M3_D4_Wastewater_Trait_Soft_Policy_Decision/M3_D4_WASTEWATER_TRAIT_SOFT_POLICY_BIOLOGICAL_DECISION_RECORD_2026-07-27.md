# M3-D4 污水相关 Trait soft 策略生物学决定记录

日期：2026-07-27  
决定来源：生物学侧会议结论（师姐建议，经项目侧确认）  
对应前置材料：`M3_D4_WASTEWATER_TRAIT_POLICY_BIOLOGICAL_SELECTION_CARD_2026-07-26.md`  
状态：**T1 SELECTED / POLICY FROZEN / M4B AND M4C NOT AUTHORIZED**

## 1. 决定

采用选择卡中的 **T1：所有污水相关 Trait 保持 soft**。

Trait 信息保留给用户，用于：

- 提供参考和候选菌使用建议；
- 解释候选菌与用户场景可能相符或冲突的地方；
- 披露证据来源、证据强度、冲突和不确定性；
- 提醒需要人工复核的生物安全或工艺适配问题。

Trait 信息不得用于：

- 自动、不可逆地删除候选菌；
- 因单条、AI 推断、无稳健多数或 ID 未对齐记录执行 hard rejection；
- 让 LLM 把 soft 提示改写成确定的生物学结论；
- 从 species 向 strain 或从 strain 向 species 继承性状。

## 2. 与黄老师既有 MT-D4 裁定的关系

本决定确认并继续沿用黄老师已经冻结的 v1 最小保守策略，不是另起一套规则：

| Trait | 当前角色 | 当前处理 |
|---|---|---|
| oxygen preference | soft | 参考、建议、冲突提示和 uncertainty |
| temperature | soft | 参考和工艺适配提示 |
| pH | soft | 参考和工艺适配提示 |
| salinity | soft | 参考和工艺适配提示 |
| wastewater metabolism | contextual soft | 不替代反应—酶证据链 |
| safety/pathogenicity | soft warning + manual review | 不自动代替安全专家决定 |
| biofilm | unknown / unused | 当前 D5 覆盖 0/5，不参与过滤 |

因此，选择卡中 T2/T3 所描述的未来 hard 升级路径本轮均不采用。

## 3. 当前数据边界

本决定不改变 D5 和 ID 对齐探测已经披露的事实：

```text
official versioned MetaTraits snapshot:
  尚未取得

documented API:
  16/16 HTTP 404

NCBI tax-ID direct query:
  10/10 HTTP 404

exact alignment:
  exact_strain = 0
  exact_species = 0
  no_exact_match_established = 10

species-name summary:
  只能作为 attribution_unresolved 的 contextual evidence
```

在 exact ID 和正式数据面未闭合时，species-name summary：

- 可以在报告中单独展示；
- 必须标记 `tax_id absent`、`attribution_unresolved` 和 provenance；
- 不参与 hard rejection；
- 不得冒充 exact strain/species 证据；
- 当前不参与自动 `trait_score`、排序或过滤。

## 4. 对实现边界的影响

本决定只冻结 D4 生物学政策，不自动授权实现。

```text
Task 7 contract:
  保持 contract-only

MicrobeTraitTool / TraitFilterLayer:
  未启动

M4b:
  未授权

MicrobeSelectionAgent 完整形态 / M4c:
  未授权
```

如果黄老师后续授权最小 M4b 启动包，实现也只能验证：

- soft-only；
- unknown / not_applicable；
- provenance；
- uncertainty；
- 不执行 hard rejection。

## 5. 给黄老师的准确表述

> 生物学侧已选择继续采用全 soft 策略。污水相关性状保留为用户参考、候选菌使用建议、
> 解释信息和不确定性提示，不用于自动删除候选菌。该选择确认黄老师既有 v1 保守口径，
> 不构成 M4b/M4c 启动授权，也不把当前 species-name summary 升格为 exact strain/species
> 证据。

