# M3-D4 污水相关 Trait 证据与 hard/soft 策略：刘老师详细选择卡

日期：2026-07-26  
用途：刘老师会前阅读并在 T1/T2/T3 中选择 D4 生物学策略  
状态：**V1 SOFT DEFAULT ALREADY DECIDED / EXPERT UPGRADE SELECTION PENDING / M4B NOT AUTHORIZED**

## 1. 这次真正需要刘老师选择什么

这项选择不是判断“metaTraits 有没有某个字段”，而是判断：

> 当系统为候选微生物取得氧需求、温度、pH、盐度等 Trait 证据后，这些证据只能作为
> 推荐理由和不确定性提示，还是允许在未来证据链闭合后自动、不可逆地剔除微生物？

需要在以下三种策略中选择一项：

```text
T1:
  当前和 v1 均全部 soft，不进行自动不可逆剔除。

T2:
  当前仍全部 soft；
  未来正式数据门通过后，仅 strict oxygen conflict 可 hard reject。

T3:
  当前仍全部 soft；
  未来正式数据门通过后，strict oxygen conflict 以及
  temperature / pH / salinity 区间无交集均可 hard reject。
```

刘老师只需判断哪套生物学风险边界可接受，不需要现场编写代码、查询数据库、设计
schema 或重新计算 D5。

## 2. 为什么这个选择重要

在后续菌层中，Trait 证据可能进入：

```text
候选微生物
  -> MicrobeTraitTool
  -> TraitFilterLayer
  -> trait_score / hard rejection
  -> MicrobeSelectionAgent
  -> 最终候选菌与理由
```

两类决策的后果不同：

| 角色 | 系统行为 | 风险 |
|---|---|---|
| soft evidence | 调整解释、提示匹配度、添加 uncertainty，不删除候选 | 保守；可能保留不理想候选 |
| hard constraint | 一旦确定冲突，候选菌自动被过滤，后续 LLM 不得恢复 | 更有选择力；证据错误时可能错杀正确菌 |

因此，“有记录”“有多数标签”或“看起来不匹配”都不足以自动变成 hard rejection。

## 3. 权威层级：哪些已经由黄老师决定，哪些仍待刘老师审核

### 3.1 黄老师已经决定的 v1 默认

黄老师在 `MT-D5 验收通过 & MT-D1–D8 逐项裁定` 中对 MT-D4 已明确：

| Trait | v1 已定角色 | 已定理由 |
|---|---|---|
| temperature | soft | D5 覆盖 5/5，但污水工艺分级标准未验证 |
| pH | soft | 同上 |
| salinity | soft | 同上 |
| oxygen_preference | soft | 同上 |
| biofilm | 不使用，统一 unknown | D5 覆盖 0/5 |
| safety/pathogenicity | soft + 人工复核标记 | 数据不完整且安全责任重大 |

共同边界：

```text
irreversible exclusion:
  disabled
uncertainty_flag:
  required
LLM bypass of hard constraints:
  forbidden
```

这意味着在刘老师和黄老师完成新的升级裁定前，实际生效状态始终等同 T1。

### 3.2 2026-07-24 新任务要求补什么

黄老师要求学生补：

```text
污水 Trait 硬约束清单:
  好氧/厌氧、盐度、温度、pH 分级标准
问题:
  污水领域是否有可直接采用的现成分级标准
若没有:
  学生先出草案供 review
```

当前证据包没有验证出一套可以覆盖所有污水工艺、直接作为自动 hard threshold 的统一
标准。这个结论只表示“本项目当前尚未验证”，不声称全球不存在任何行业或工艺标准。

### 3.3 本文件中哪些属于学生提案

以下不是黄老师已经批准的生产规则，而是为刘老师选择准备的学生侧未来升级提案：

- H1–H7 hard-evidence 资格门；
- strict oxygen conflict 的精确定义；
- temperature/pH/salinity 的区间无交集算法；
- W1/W2 演示场景；
- T2/T3 的未来激活范围。

选择 T2/T3 表示刘老师生物学上接受对应未来路径；仍须黄老师写入最终合同并另行授权，
才可能实施。

## 4. 真实 D5 证据来自哪里

新合同版 D5 的证据链是：

```text
P0 Top-MRR 正确酶:
  EnzymeCAGE v1 冻结测试表

酶 UID -> 宿主:
  reviewed UniProt 主证据
  KEGG 独立补充

宿主 -> Trait:
  metaTraits website /taxon/download species summary
```

宿主菌不是从 metaTraits 中任意挑选的。先从 P0 冻结测试集中选择反应组内
`positive_rank=1` 且 `Label=1` 的酶，再反查 reviewed UniProt 宿主，最后才查询
metaTraits。

新合同版 D5 已复核：

```text
P0 frozen test rows recomputed:
  70,815
selected enzyme UIDs:
  10
selected-source rows:
  10 UIDs x 5 seeds = 50
Label=1:
  50/50
positive_rank=1:
  10/10 selected UIDs
reviewed UniProt exact primary accession:
  10/10
target RHEA referenced by saved UniProt evidence:
  10/10
successful metaTraits sample hosts:
  5
```

`Label=1` 是冻结测试集 ground truth，不表示 D5 新做了生化实验。

## 5. 五个真实宿主样本

| 酶 UID | reviewed UniProt 宿主 | UniProt tax ID | metaTraits 查询层级 | summary records |
|---|---|---:|---|---:|
| `Q8EFP8` | *Shewanella oneidensis* MR-1 | 211586 | species name | 146 |
| `Q12WS1` | *Methanococcoides burtonii* ACE-M | 259564 | species name | 134 |
| `A0A0H3C8X0` | *Caulobacter vibrioides* NA1000 | 565050 | species name | 161 |
| `Q6BQK1` | *Debaryomyces hansenii* CBS 767 | 284592 | species name | 9 |
| `P71875` | *Mycobacterium tuberculosis* H37Rv | 83332 | species name | 147 |

五份原始 JSON 合计 597 条记录，并保留原始响应字节和 SHA256。

“宿主”只表示该 reviewed UniProt 蛋白条目直接标注的 organism/taxon。它不自动证明该
微生物能在实际污水工艺中完成目标转化。

## 6. 污水相关 Trait 的真实覆盖度

| 类别 | 有匹配记录的样本 | 匹配记录数 | 当前可支持的结论 |
|---|---:|---:|---|
| oxygen/atmosphere | 5/5 | 30 | 可作 bounded soft evidence |
| temperature | 5/5 | 25 | 可作 bounded soft evidence |
| pH | 5/5 | 13 | 可作 bounded soft evidence |
| salinity | 5/5 | 19 | 可作 bounded soft evidence |
| biofilm | 0/5 | 0 | 当前不可用于过滤 |
| safety/pathogenicity | 4/5 | 7 | 不完整，只能人工复核 |
| wastewater metabolism | 4/5 | 158 | 有用但不完整，不直接等于目标反应能力 |

这里的“5/5 覆盖”只表示五份 summary 中存在相关记录，不表示：

```text
exact strain attribution:
  已建立
non-AI evidence:
  5/5
robust consensus:
  5/5
统一单位和完整上下界:
  5/5
适合具体污水工艺:
  已证明
可用于 hard rejection:
  已证明
```

## 7. 当前证据为什么还不能直接 hard filtering

### 7.1 exact tax-ID 链没有闭合

```text
documented NCBI tax-ID API query:
  10/10 HTTP 404
documented /api/v1 logical probes:
  16/16 HTTP 404
working summary route:
  species-name query
summary tax_id field:
  absent
exact strain-level attribution:
  not established
```

species summary 可以包含有用的背景证据，但不能冒充 exact strain 证据，也不能从
species 静默继承到 strain。

### 7.2 官方生产数据面尚未取得

```text
official versioned snapshot:
  尚未取得
website summary downloads:
  5/5 HTTP 200，bounded usable with retry
successful repeat bodies:
  3/3 byte-identical
transient TLS timeout:
  1
HTTP 429 observed:
  0
published numeric rate limit:
  UNKNOWN
```

这证明网站面在有界探测中可用，不证明有 SLA、稳定生产 API 或无限访问频率。

### 7.3 `is_ai` 与 `majority_label` 是独立维度

黄老师已经废止把 evidence 压成三状态的旧设计。Trait 记录必须分别保留：

```text
value
is_ai
majority_label
source_database
source_url
tax_id
```

`is_ai=false` 不自动代表多数共识稳健；`No robust majority` 也不等同 AI 预测。

### 7.4 `No robust majority` 不是负证据

五份 summary：

| UID | total records | No robust majority | 比例 |
|---|---:|---:|---:|
| `Q8EFP8` | 146 | 12 | 8.219178% |
| `Q12WS1` | 134 | 2 | 1.492537% |
| `A0A0H3C8X0` | 161 | 24 | 14.906832% |
| `Q6BQK1` | 9 | 0 | 0.000000% |
| `P71875` | 147 | 5 | 3.401361% |
| **合计** | **597** | **43** | **7.202680%** |

这是当前五样本记录比例，不是 metaTraits 全库冲突率。`No robust majority` 表示当前
来源间没有形成稳健多数，必须进入 `uncertainty_flags`，不能解释成“不具备该 Trait”。

### 7.5 数值字段存在不等于有可靠生长区间

五样本中 temperature/pH/salinity 有相关记录，但审计发现：

- 多个数值边界记录主要是 `is_ai=true`；
- 稀疏样本 `Q6BQK1` 只有 growth-point 值，没有完整 min/max 区间记录；
- 单一中位数不能冒充完整生长范围；
- 单位、记录类型和上下界必须成对验证。

因此当前不能仅凭一个 median 或一条 AI 预测记录自动剔除候选菌。

## 8. 所有策略当前共同遵守的证据语义

### 8.1 `unknown`

表示数据缺失、ID 未对齐、证据不足或冲突未解。`unknown`：

```text
does not mean:
  biologically absent
hard rejection:
  forbidden
soft explanation:
  可说明证据不足
```

### 8.2 `not_applicable`

Task 7 已冻结的语义：

```text
not_applicable:
  当前证据链下无法将该 Trait 归属给该 taxon
not_applicable !=:
  该微生物在生物学上不存在此性状
```

### 8.3 `No robust majority`

```text
meaning:
  聚合来源没有形成稳健多数
handling:
  uncertainty_flag
hard rejection:
  forbidden
```

### 8.4 AI-derived records

```text
current v1:
  可作为带标记的 soft/contextual evidence
future proposed hard use:
  forbidden
```

### 8.5 safety/pathogenicity

```text
all T1/T2/T3:
  soft warning + mandatory manual review
automatic safety rejection:
  disabled
```

即使记录中出现 biosafety level 2/3，也不能由当前 TraitFilterLayer 自动代替安全专家
作最终决定。

### 8.6 biofilm

```text
current five-sample coverage:
  0/5
all T1/T2/T3:
  unused / unknown
if user requires biofilm:
  insufficient_evidence + 人工查文献
```

### 8.7 wastewater metabolism

```text
current five-sample coverage:
  4/5
all T1/T2/T3:
  contextual soft evidence only
hard rejection:
  disabled
```

metaTraits 中广义污水代谢相关记录不能证明该菌能够催化当前目标反应，也不能替代
EnzymeCAGE 的反应—酶证据链。

## 9. T2/T3 未来升级前的两级总闸

选择 T2/T3 不是批准现在 hard filtering。至少要先同时通过以下两级总闸。

### 9.1 数据面总闸 G1–G6

```text
G1 official data:
  取得 official versioned snapshot，或黄老师另行批准的稳定生产数据面

G2 exact ID:
  organism_uid 与 Trait record 的 NCBI tax ID 精确一致

G3 no silent inheritance:
  禁止 species -> strain、strain -> species 或 related taxon 静默继承

G4 schema:
  schema v1.1 保留 is_ai / majority_label / source / tax_id 独立维度

G5 provenance:
  snapshot version、record identity、source URL、hash 可追溯

G6 authority:
  刘老师选择已写入最终方案，且黄老师明确授权 M4b / hard policy
```

任一 G 门失败，系统继续等同 T1。

### 9.2 单条 hard evidence 资格门 H1–H7

以下是学生侧为未来 T2/T3 提出的保守资格门，需随刘老师选择一起提交黄老师确认：

```text
H1 exact taxon:
  record tax_id == queried NCBI taxon ID

H2 no inheritance:
  没有跨 species/strain 或 related taxon 继承

H3 non-AI:
  is_ai == false

H4 robust:
  majority_label != "No robust majority"

H5 independent corroboration:
  num_observations >= 2
  unique_databases >= 2

H6 traceable provenance:
  每条关键证据有 source_database + source_url/record identity

H7 valid schema and units:
  trait、value/interval、unit 均通过冻结 validator
```

H5 是学生侧为不可逆剔除提出的保守门，不应冒充黄老师此前已经批准的 hard threshold。
黄老师此前 MT-D6 的“每个正向推荐至少 2 条可追溯 evidence”是 LLM 推荐证据要求；
本文件建议未来 hard rejection 至少采用同等或更严格的独立支持门。

任一 H 门失败：

```text
hard rejection:
  forbidden
result:
  unknown 或带 uncertainty 的 soft evidence
```

## 10. 未来可选的 fixed Trait 判定规则

本节只在选择 T2/T3、G1–G6 和 H1–H7 全部通过、黄老师另行授权后才可能生效。

### 10.1 Oxygen：只允许 strict obligate conflict

| 污水场景 | 未来可 hard reject 的严格冲突 | 不允许 hard reject |
|---|---|---|
| aerobic | exact、non-AI、robust 的 `obligate anaerobic` | facultative；普通 anaerobic；缺失；AI；冲突 |
| anaerobic | exact、non-AI、robust 的 `obligate aerobic` | facultative；普通 aerobic；缺失；AI；冲突 |
| anoxic | 暂无自动 hard rule | 全部 soft/unknown |
| unspecified | 无 | 全部 soft/unknown |

普通 `aerobic` / `anaerobic` 不等于 `obligate`，不得扩大解释。

### 10.2 Temperature / pH / salinity：只允许完整区间无交集

只有同一 exact taxon 同时存在通过 H1–H7 的 minimum 和 maximum 记录时，才构造：

```text
organism_interval:
  [median(valid minimum records), median(valid maximum records)]

scenario_interval:
  [scenario_min, scenario_max]
```

判断：

```text
no overlap:
  future hard incompatible
overlap:
  compatible for this single dimension
only growth median:
  soft only
missing one bound:
  unknown / soft only
invalid or mixed unit:
  fail-closed, no hard rejection
```

冻结单位提案：

```text
temperature:
  Celsius
pH:
  pH
salinity:
  % NaCl (w/v)
silent conversion:
  forbidden
```

“某一维相容”不等于该微生物整体适合该污水工艺，最终仍需综合其他证据。

## 11. W1/W2 场景是什么，不是什么

T3 需要明确的场景区间才能执行。学生侧预先给出两个演示草案：

| 演示场景 | oxygen | temperature | pH | salinity |
|---|---|---:|---:|---:|
| W1 conventional aerobic demo | aerobic | 15–35 °C | 6.5–8.5 | 0–1.0% NaCl (w/v) |
| W2 mesophilic anaerobic demo | anaerobic | 30–40 °C | 6.8–7.8 | 0–1.0% NaCl (w/v) |

必须明确：

```text
status:
  学生侧演示默认值，等待生物学专家 review
not:
  国际统一污水标准
not:
  覆盖全部工艺的阈值
not:
  已在当前五样本上验证可安全 hard filtering
```

如果实际项目提供已确认的运行范围，应使用真实项目范围替代 W1/W2；没有项目范围时，
系统不得自行猜测。即使使用真实范围，仍必须通过 G/H 门和区间规则。

## 12. T1：全 soft，维持黄老师当前 v1

### 12.1 规则

```text
hard traits:
  none
oxygen / temperature / pH / salinity:
  soft evidence + uncertainty
biofilm:
  unknown / unused
safety/pathogenicity:
  soft warning + manual review
missing / AI / conflict:
  unknown or labelled soft evidence, never reject
```

### 12.2 优点

- 与黄老师已经裁定的 v1 完全一致；
- 适合当前 exact-ID、正式 snapshot 和阈值标准均未闭合的证据状态；
- 错杀风险最低；
- 保留全部候选，便于后续人工复核和收集更多证据；
- 不需要现在承诺尚未验证的 W1/W2 hard threshold。

### 12.3 代价

- 明显不适合某场景的微生物可能仍保留在候选列表；
- 系统只能提示风险，无法自动缩小候选范围；
- 后续如果证据链成熟，需要再做一次专家升级裁定。

### 12.4 选择 T1 的准确含义

```text
current:
  all soft
future automatic upgrade:
  none
review trigger:
  official snapshot + exact-ID + sufficient evidence + new expert review
```

## 13. T2：分阶段，仅 strict oxygen 可 hard

### 13.1 当前阶段

```text
G/H gates incomplete:
  与 T1 完全相同，全部 soft
current five samples auto-rejected:
  0
```

### 13.2 未来阶段

只有 G1–G6、H1–H7 全部通过且黄老师授权后：

```text
oxygen:
  strict obligate conflict may hard reject
temperature / pH / salinity:
  soft only
biofilm:
  unused / unknown
safety:
  soft + manual review
```

### 13.3 优点

- 只对生物学语义最明确的 `obligate` 氧条件冲突开放 hard；
- 不把普通 aerobic/anaerobic 或 facultative 扩大解释；
- 比 T3 更少依赖数值阈值和单位；
- 在保守前提下给未来自动过滤留出第一步。

### 13.4 风险与代价

- oxygen 标签仍可能受来源冲突和 taxon 粒度影响；
- anoxic 场景没有自动 hard 规则；
- 温度、pH、盐度即使明显不匹配仍只能 soft；
- 选择 T2 等于预先接受一条未来 hard 路径，必须严格依赖 G/H 门。

### 13.5 选择 T2 的准确含义

```text
current:
  all soft
future pre-approved biological scope:
  strict obligate oxygen conflict only
implementation:
  still requires Huang-teacher authorization
```

## 14. T3：分阶段，oxygen + 三个数值区间可 hard

### 14.1 当前阶段

```text
G/H gates incomplete:
  与 T1 完全相同，全部 soft
current five samples auto-rejected:
  0
```

### 14.2 未来阶段

只有 G1–G6、H1–H7 全部通过且黄老师授权后：

```text
oxygen:
  strict obligate conflict rule
temperature / pH / salinity:
  complete valid interval vs confirmed scenario interval
  no overlap -> hard incompatible
biofilm:
  unused / unknown
safety:
  soft + manual review
```

### 14.3 优点

- 对实际运行条件的表达最完整；
- 能在证据充分时较强地缩小候选菌范围；
- 区间无交集算法确定、可解释、可测试；
- 真实项目提供运行范围时可替代演示默认值。

### 14.4 风险与代价

- 错杀风险三项中最高；
- min/max、单位、AI 标志和 exact taxon 任一错误都会影响不可逆决策；
- 当前数值证据尚不足以证明 W1/W2 可安全作为 universal hard threshold；
- 不同污水工艺条件差异大，演示默认值不能覆盖全部场景；
- 需要更多 validator、mutation tests 和专家审查。

### 14.5 选择 T3 的准确含义

```text
current:
  all soft
future pre-approved biological scope:
  strict oxygen + temperature/pH/salinity interval non-overlap
scenario:
  actual confirmed project range preferred
  W1/W2 only if separately accepted as demo defaults
implementation:
  still requires Huang-teacher authorization
```

## 15. T1/T2/T3 横向比较

| 维度 | T1 全 soft | T2 oxygen-only staged hard | T3 four-trait staged hard |
|---|---|---|---|
| 当前是否 hard | 否 | 否 | 否 |
| 当前五样本自动剔除 | 0 | 0 | 0 |
| exact-ID 未闭时是否 hard | 否 | 否 | 否 |
| 未来 hard 范围 | 无 | strict obligate oxygen conflict | oxygen + 三个数值区间无交集 |
| 是否依赖 W1/W2 | 否 | 否 | 可能；真实项目范围优先 |
| 当前证据直接支持度 | 最高 | 仅支持未来保守提案 | 最低，需更多验证 |
| 自动过滤能力 | 最低 | 中 | 最高 |
| 错杀风险 | 最低 | 低到中 | 最高 |
| 与黄老师 v1 默认一致 | 完全一致 | 当前一致，未来升级 | 当前一致，未来升级 |

## 16. 学生侧建议

以下是学生侧建议，不是刘老师已经同意：

```text
推荐:
  T1

理由:
  official versioned snapshot 尚未取得；
  exact tax-ID -> Trait 路径未闭合；
  working summaries 是 species-name aggregates；
  biofilm 0/5；
  safety 4/5 且必须人工复核；
  多个数值边界记录主要是 AI-derived；
  W1/W2 尚未作为通用 hard threshold 获得专家验证。
```

如果刘老师希望现在就给未来升级留一个最保守的预授权方向，T2 比 T3 更稳妥；但当前
实际行为仍必须等同 T1。

## 17. 刘老师正式选择区

请选择一项：

```text
[ ] T1（学生侧推荐）
    当前和 v1 全部 soft；
    不预先批准任何 future hard threshold；
    等正式数据面、exact-ID 和更多证据形成后再做专家 review。

[ ] T2
    当前全部 soft；
    未来 G1–G6、H1–H7 通过且黄老师授权后，
    仅 strict obligate oxygen conflict 可 hard reject。

[ ] T3
    当前全部 soft；
    未来 G1–G6、H1–H7 通过且黄老师授权后，
    oxygen 以及 temperature/pH/salinity 区间无交集可 hard reject；
    真实项目范围优先，W1/W2 仅为待审核演示默认。
```

如果对未来 hard 路径尚无把握，应选择 T1；不需要另写一套临时方案。

## 18. 刘老师选择后怎样形成最终方案

收到刘老师选择后，学生侧按以下顺序执行：

```text
Step 1:
  原样记录刘老师 T1/T2/T3 选择，不回填成学生推荐。

Step 2:
  与反应预测 A/B/C 选择一起写两份“专家选择后冻结合同”。

Step 3:
  写最终实施方案，明确：
    current policy
    future policy
    G1–G6
    H1–H7
    trait allowlist
    thresholds/scenario
    unknown/not_applicable semantics
    prohibited actions

Step 4:
  写入黄老师固定裁定卡，请黄老师确认是否授权相应最小 pilot/M4b 范围。

Step 5:
  分仓更新 teacher-deliverables：
    反应预测内容 -> 酶侧仓库
    D4/MetaTraits 内容 -> 微生物侧仓库

Step 6:
  补充 2026-07-23 和 2026-07-24 两份任务单的逐项作业回复，
  为每一项写明完成状态、结果、GitHub 路径、commit 和仍需裁定项。

Step 7:
  重新计算 SHA256、独立审计、推送 GitHub，再向黄老师发送简短结果定位消息。
```

刘老师选择本身不授权：

- M4b 活代码；
- `TraitFilterLayer` hard filtering；
- production MetaTraits 数据面；
- 自动剔除任何真实候选菌；
- M4c LLM 选菌。

## 19. 证据位置

### 19.1 新合同版 D5

```text
GitHub:
  https://github.com/bgruiiii/EnzymeCAGE-MetaTraits-Teacher-Deliverables/tree/main/
  2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission

report:
  metatraits_probe_report.md

independent audit:
  audits/METATRAITS_D5_NEW_CONTRACT_INDEPENDENT_REAUDIT_2026-07-24.md

commit:
  48c6e80be60cca285540c65acc5dd337762ede94

status:
  student resubmission complete / teacher acceptance pending
```

### 19.2 已有 MT-D4 权威裁定

```text
authority:
  TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md

decision:
  v1 all soft + uncertainty
  biofilm unused/unknown
  safety soft + manual review
  irreversible exclusion disabled
```

### 19.3 既有决策状态闭合

```text
GitHub:
  https://github.com/bgruiiii/EnzymeCAGE-MetaTraits-Teacher-Deliverables/blob/main/
  M3_P1_MICROBE_PREREQUISITES_EXISTING_DECISIONS_AND_STATUS_CLOSURE_2026-07-26.md

commit:
  47aaa2a0a0af1d45fe0629244e7d22ed795c2ded
```

## 20. 选择前保持锁定

```text
[x] 当前全部 Trait 继续 soft
[x] biofilm 继续 unused / unknown
[x] safety/pathogenicity 继续 manual review
[x] exact-ID 未闭时禁止 hard rejection
[x] official snapshot 未取得时禁止 production
[x] No robust majority 不作负证据
[x] AI record 不触发 hard rejection
[x] species summary 不继承到 exact strain
[x] W1/W2 不冒充统一行业标准
[x] 刘老师选择后仍需黄老师授权
[x] 不提前编写 M4b/M4c 活代码
```

本文件用于让刘老师做固定生物学选择，不构成对 MetaTraits 数据完整性、任一候选菌真实
污水适应性、任何 hard threshold 或 M4b/M4c 实施的老师验收声明。
