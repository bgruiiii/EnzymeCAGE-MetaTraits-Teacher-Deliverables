# M3-D4 污水 Trait 证据与 hard/soft 详细选择卡本地独立审计

审计日期：2026-07-26（Asia/Shanghai）  
审计对象：
`M3_D4_WASTEWATER_TRAIT_POLICY_BIOLOGICAL_SELECTION_CARD_2026-07-26.md`  
对象 SHA256：
`75f5ee05f8c48c52ec5f3ff375576c458a417f70f99f94c62acfd9d049ba0ad0`  
结论：**PASS FOR LIU-TEACHER T1/T2/T3 SELECTION / AUTHORITY LAYERS SEPARATED / NO HARD FILTER ACTIVATED**

## 1. 审计目标

本次重审不只检查 T1/T2/T3 是否存在，还检查：

1. 黄老师已裁定 v1 与学生未来提案是否分层；
2. D5 新合同版真实样本数字是否一致；
3. coverage 是否被误写成 hard-ready；
4. `is_ai`、`No robust majority`、`unknown`、`not_applicable` 是否混淆；
5. H1–H7、W1/W2 是否诚实标成学生提案；
6. T2/T3 当前是否仍保持 T1 行为；
7. 刘老师是否只需做选择；
8. 选择后、黄老师授权前是否保持 M4b/M4c 锁定。

## 2. 权威层级一致性

### 2.1 黄老师已经决定

选择卡正确保留 MT-D4 既有裁定：

```text
temperature:
  soft
pH:
  soft
salinity:
  soft
oxygen_preference:
  soft
biofilm:
  unused / unknown
safety/pathogenicity:
  soft + manual review
irreversible exclusion:
  disabled
```

该部分没有被写成仍待刘老师重新决定的空白。

### 2.2 刘老师当前需要决定

选择卡将专家选择限定为：

```text
T1:
  不预先开放 future hard threshold
T2:
  未来只开放 strict obligate oxygen conflict
T3:
  未来开放 strict oxygen + 三项数值区间无交集
```

T2/T3 只决定未来生物学范围，仍依赖数据门和黄老师授权。

### 2.3 学生提案身份

选择卡明确以下均为学生侧 proposal：

```text
H1–H7 hard-evidence gate
strict oxygen conflict implementation
numeric interval non-overlap algorithm
W1/W2 demo ranges
T2/T3 future activation scope
```

没有把它们冒充黄老师已批准的生产阈值或行业标准。

## 3. D5 P0→酶→宿主链审计

详细卡列出的来源链与新合同版 D5 一致：

```text
P0 rank/correctness:
  frozen EnzymeCAGE v1 test tables
enzyme -> host:
  reviewed UniProt primary, KEGG supplemental
host -> traits:
  metaTraits website species summary
```

关键数字复核：

```text
P0 rows recomputed:
  70,815
selected UIDs:
  10
selected source rows:
  50
Label=1:
  50/50
positive_rank=1:
  10/10
reviewed UniProt exact primary accession:
  10/10
saved UniProt target-RHEA reference:
  10/10
successful metaTraits hosts:
  5
```

选择卡明确 `Label=1` 是冻结测试集 ground truth，不宣称 D5 进行了新生化实验。

## 4. 五个真实宿主样本审计

| UID | Host | Tax ID | Records | 审计 |
|---|---|---:|---:|---|
| Q8EFP8 | *Shewanella oneidensis* MR-1 | 211586 | 146 | PASS |
| Q12WS1 | *Methanococcoides burtonii* ACE-M | 259564 | 134 | PASS |
| A0A0H3C8X0 | *Caulobacter vibrioides* NA1000 | 565050 | 161 | PASS |
| Q6BQK1 | *Debaryomyces hansenii* CBS 767 | 284592 | 9 | PASS |
| P71875 | *Mycobacterium tuberculosis* H37Rv | 83332 | 147 | PASS |

合计 `146+134+161+9+147=597`。选择卡明确 metaTraits 查询是 species-name summary，
没有把 UniProt strain annotation 改写成 exact strain-level Trait 归属。

## 5. Trait 覆盖度审计

| Category | Samples | Records | 卡中角色 | 审计 |
|---|---:|---:|---|---|
| oxygen/atmosphere | 5/5 | 30 | bounded soft | PASS |
| temperature | 5/5 | 25 | bounded soft | PASS |
| pH | 5/5 | 13 | bounded soft | PASS |
| salinity | 5/5 | 19 | bounded soft | PASS |
| biofilm | 0/5 | 0 | unused/unknown | PASS |
| safety/pathogenicity | 4/5 | 7 | soft + manual | PASS |
| wastewater metabolism | 4/5 | 158 | contextual soft only | PASS |

选择卡没有把字段存在写成：

- exact-ID 闭合；
- non-AI 证据充分；
- 适合目标污水工艺；
- 能完成当前目标反应；
- 可自动 hard reject。

## 6. `No robust majority` 审计

| UID | Total | NRM | Percentage |
|---|---:|---:|---:|
| Q8EFP8 | 146 | 12 | 8.219178% |
| Q12WS1 | 134 | 2 | 1.492537% |
| A0A0H3C8X0 | 161 | 24 | 14.906832% |
| Q6BQK1 | 9 | 0 | 0.000000% |
| P71875 | 147 | 5 | 3.401361% |
| aggregate | 597 | 43 | 7.202680% |

逐项和合计均与 D5 报告一致。选择卡明确这是五样本记录比例，不是全库率；
`No robust majority` 进入 uncertainty，不作负证据。

## 7. 数据面与 ID 边界审计

选择卡所列：

```text
documented API:
  16/16 HTTP 404
documented tax-ID query:
  10/10 HTTP 404
website summaries:
  5/5 HTTP 200
repeat bodies:
  3/3 byte-identical
TLS timeout:
  1
HTTP 429:
  0
published numeric rate limit:
  UNKNOWN
summary tax_id:
  absent
```

与 D5 新合同版报告一致。卡中结论仅为 website surface 有界可用，不宣称 production
稳定性、可用 TaxID API 或 unlimited rate。

## 8. 证据语义审计

选择卡分别处理：

```text
is_ai:
  prediction-origin boolean
majority_label:
  independent consensus label
No robust majority:
  consensus conflict/insufficiency state
unknown:
  missing, unresolved or insufficient evidence
not_applicable:
  current evidence chain cannot assign the trait
```

没有恢复老师已废止的三状态 `evidence` 字段，也没有新增 confidence float。

Task 7 的关键等式保持：

```text
not_applicable != biologically absent
No robust majority != not_applicable
is_ai != majority_label
```

## 9. G1–G6 总闸审计

T2/T3 在 future hard 生效前要求：

```text
official/stable authorized data plane
exact NCBI tax ID
no species/strain inheritance
schema v1.1
full provenance
Liu selection + Huang authorization
```

任一未通过时，系统行为继续等同 T1。当前已知 official snapshot 和 exact-ID path 均未
闭合，所以详细卡没有提前激活 hard filtering。

## 10. H1–H7 单记录资格门审计

H1–H7 被明确标为学生侧未来提案：

```text
exact taxon
no inheritance
non-AI
robust majority
>=2 observations
>=2 independent databases
traceable source
valid schema/unit
```

卡中专门区分：

- 黄老师 MT-D6 的“正向推荐至少 2 条 evidence”是 LLM recommendation 规则；
- H5 是学生为不可逆 hard rejection 提出的同等或更严格门；
- H5 尚不是老师已批准的 hard threshold。

该分层修复了旧短卡可能给人“H1–H7 已获权威批准”的误解。

## 11. Oxygen 规则审计

选择卡只允许未来排除 strict obligate conflict：

```text
aerobic scenario:
  obligate anaerobic may reject
anaerobic scenario:
  obligate aerobic may reject
facultative:
  never rejected by oxygen rule
plain aerobic / anaerobic:
  not promoted to obligate
anoxic / unspecified:
  no hard rule
```

该规则不扩大普通标签语义。

## 12. Temperature/pH/salinity 规则审计

选择卡要求同一 exact taxon 的合格 minimum/maximum 记录成对存在，才可构造 organism
interval；单个 growth median、缺一侧边界、混合单位或非法记录均不得 hard reject。

未来判定仅为：

```text
organism interval ∩ confirmed scenario interval == empty:
  hard incompatible
otherwise:
  not hard incompatible on this dimension
```

“单维相容”没有被写成“整体污水适用”。

## 13. W1/W2 审计

选择卡给出：

```text
W1:
  aerobic, 15–35 °C, pH 6.5–8.5, salinity 0–1.0%
W2:
  anaerobic, 30–40 °C, pH 6.8–7.8, salinity 0–1.0%
```

并明确它们是学生演示默认、等待专家 review，不是国际统一标准，不覆盖全部污水工艺，
当前五样本也没有验证其 hard-filter 安全性。真实项目确认范围优先。

## 14. T1/T2/T3 后果审计

| 项目 | T1 | T2 | T3 |
|---|---|---|---|
| 当前 hard | no | no | no |
| 当前自动剔除 | 0 | 0 | 0 |
| future hard | none | strict oxygen | oxygen + 3 intervals |
| 当前与 v1 一致 | yes | yes | yes |
| 错杀风险 | lowest | low–medium | highest |

选择卡推荐 T1，并说明若希望预先保留最保守升级方向，T2 比 T3 稳妥。推荐没有写成
刘老师已经选择。

## 15. “老师只做选择”审计

正式勾选区只有：

```text
T1
T2
T3
```

每一项均给出：

- 当前行为；
- 未来可开放范围；
- G/H 前提；
- 是否依赖 W1/W2；
- 优点；
- 风险；
- 选择的准确含义。

刘老师无需现场提供代码、数据库接口、单位转换、missing policy 或阈值算法。

## 16. 选择后流程审计

详细卡按用户要求冻结了会后顺序：

```text
记录 A/B/C + T1/T2/T3 专家选择
-> 写两份专家选择后冻结合同
-> 写最终方案
-> 填黄老师裁定卡
-> 酶/微生物分仓更新 GitHub
-> 补充 07-23/07-24 任务单逐项回复
-> SHA256 + 独立审计
-> 推送
-> 给黄老师结果定位消息
```

这只是未来工作流，不冒充已经发生的专家裁定、GitHub 推送或黄老师反馈。

## 17. 禁止动作审计

本次只重写 Markdown 选择材料与审计。未执行：

```text
MetaTraits network query
HPC/GPU job
TraitFilterLayer code
hard rejection
candidate removal
M4b/M4c implementation
GitHub push
external teacher message
```

## 18. 最终结论

```text
teacher v1 authority preserved:
  PASS
student proposal identity disclosed:
  PASS
D5 evidence numbers:
  PASS
coverage/hard-readiness boundary:
  PASS
evidence semantics:
  PASS
T1/T2/T3 fixed-choice completeness:
  PASS
current hard filter:
  DISABLED
expert selection:
  STILL REQUIRED
Huang authorization:
  STILL REQUIRED
```

该详细选择卡可以交刘老师阅读并只勾选 T1/T2/T3；不能作为 M4b、M4c、production
MetaTraits 数据面或真实候选菌自动剔除的授权。
