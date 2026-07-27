# M3-D4 污水 Trait 策略老师展示版 HTML 本地独立审计

审计日期：2026-07-26（Asia/Shanghai）  
审计对象：
`M3_D4_WASTEWATER_TRAIT_POLICY_TEACHER_PRESENTATION_2026-07-26.html`  
对象 SHA256：
`f95209ae3957ecf194eaed7ade256e4a5a216637f14cf2cb62cd9e70702f15b5`  
结论：**PASS FOR OFFLINE TEACHER PRESENTATION / FACTS CONSISTENT /
BIOLOGICAL SELECTION PENDING / NO M4B AUTHORIZATION**

## 1. 文件定位与用途

HTML 与详细 Markdown 选择卡同目录，作为刘老师会前的可视化展示层：

```text
01_Path_Contract_Objective/M3_P1_PreTeacher_Adjudication_2026-07-26/
M3_D4_WASTEWATER_TRAIT_POLICY_TEACHER_PRESENTATION_2026-07-26.html
```

详细证据与正式文字边界仍以以下文件为准：

```text
M3_D4_WASTEWATER_TRAIT_POLICY_BIOLOGICAL_SELECTION_CARD_2026-07-26.md
ENZYMECAGE_M3_D4_WASTEWATER_TRAIT_POLICY_BIOLOGICAL_SELECTION_CARD_LOCAL_AUDIT_2026-07-26.md
```

HTML 只改变信息展示方式，没有修改 MetaTraits 原始响应、P0 ground truth、D5
机器审计、老师既有裁定或任何生产代码。

## 2. 正式选择框架审计

页面把刘老师的正式选择严格限制为：

```text
T1:
  当前和 v1 均全 soft

T2:
  当前全 soft；
  未来证据与授权总闸全部通过后，仅 strict obligate oxygen conflict 可 hard

T3:
  当前全 soft；
  未来总闸通过后，可允许 oxygen 及 temperature/pH/salinity 完整区间无交集 hard
```

三项当前自动剔除均为 0。页面没有把“选择 T2/T3”写成当前启用 hard filtering，
也没有把学生推荐 T1 写成刘老师已经选择。

## 3. 权威层级与权限边界

页面分别标明：

```text
黄老师已裁定的 v1:
  当前所有 Trait 均不作不可逆剔除

学生未来提案:
  G1–G6、H1–H7、strict oxygen、区间无交集、W1/W2

刘老师待选择:
  T1/T2/T3 生物学风险边界

黄老师待授权:
  最终合同、M4b 或 hard policy 最小启动范围
```

以下禁止事项均在页面中披露：

- 黄老师未授权前不实现 M4b，不自动剔除真实候选菌；
- `No robust majority` 不作负证据；
- AI-derived record 不触发 hard rejection；
- species summary 不继承到 exact strain；
- W1/W2 不冒充统一行业标准；
- D5 新合同版等待老师验收，不借旧验收冒充新验收。

结果：`AUTHORITY_AND_PROPOSAL_SEPARATION = PASS`。

## 4. 真实证据链与关键数字

### 4.1 P0 到真实宿主

页面披露：

```text
P0 rows recomputed:
  70,815
selected source rows Label=1:
  50/50
reviewed UniProt exact primary accession:
  10/10
displayed successful MetaTraits hosts:
  5
original JSON records:
  597
```

五个展示宿主及 taxon ID、query key、记录数与详细 Markdown 一致。页面明确
`Label=1` 是冻结测试集 ground truth，不是 D5 新增实验；UniProt 宿主标注也不自动
证明该菌能在实际污水条件下完成目标转化。

### 4.2 Trait 覆盖度

| Trait 类别 | 宿主覆盖 | 记录数 | 页面角色 |
|---|---:|---:|---|
| oxygen/atmosphere | 5/5 | 30 | bounded soft |
| temperature | 5/5 | 25 | bounded soft |
| pH | 5/5 | 13 | bounded soft |
| salinity | 5/5 | 19 | bounded soft |
| biofilm | 0/5 | 0 | unused/unknown |
| safety/pathogenicity | 4/5 | 7 | manual review |
| wastewater metabolism | 4/5 | 158 | contextual soft |

页面明确“有记录不等于 hard-ready”，没有把字段覆盖度冒充 exact-strain、non-AI、
稳健共识或工艺适配证据。

### 4.3 接口、稳定性、冲突和限流

```text
documented /api/v1 probes:
  16/16 HTTP 404
tax-ID API:
  10/10 HTTP 404
website summary:
  5/5 HTTP 200
repeat response bodies:
  3/3 byte-identical
transient TLS timeout:
  1
HTTP 429 observed:
  0
published numeric rate limit:
  UNKNOWN
No robust majority:
  43/597 = 7.202680%
```

页面没有把 0 个 HTTP 429 解释成无限频率，也没有把五样本比例写成 MetaTraits 全库率。

结果：`NUMERIC_AND_EVIDENCE_CHAIN_CONSISTENCY = PASS`。

## 5. 未来证据门和判定规则

页面完整展示：

- G1–G6 数据面、exact ID、provenance、validator、反向测试和授权总闸；
- H1–H7 单条证据的 exact taxon、禁止继承、非 AI、稳健多数、双独立支持、
  字段完整、类型/单位有效要求；
- oxygen 仅允许 strict obligate conflict；
- temperature/pH/salinity 仅允许同一 exact taxon 的完整有效区间与确认工艺区间
  无交集；
- 缺 min/max、单位不明、AI、冲突或 ID 未闭合时都继续 soft/unknown。

页面明确 G/H 门是学生提案，不是黄老师既有批准规则；黄老师此前的“正向推荐至少
2 条 evidence”也没有被偷换成 hard threshold。

结果：`FUTURE_RULE_SCOPE_AND_NONAUTHORIZATION = PASS`。

## 6. W1/W2 场景边界

页面展示的演示值与详细 Markdown 一致：

```text
W1 conventional aerobic:
  aerobic / 15–35 °C / pH 6.5–8.5 / 0–1.0% NaCl (w/v)

W2 mesophilic anaerobic:
  anaerobic / 30–40 °C / pH 6.8–7.8 / 0–1.0% NaCl (w/v)
```

同时明确：

- W1/W2 是学生演示默认；
- 不是国际统一标准；
- 不覆盖所有污水工艺；
- 未在当前五样本上证明可安全 hard filtering；
- 真实项目确认范围优先。

结果：`DEMO_RANGE_BOUNDARY = PASS`。

## 7. HTML 技术结构审计

```text
doctype:
  html5
charset:
  utf-8
viewport:
  present
external JavaScript:
  none
external stylesheet:
  none
external image/font dependency:
  none
responsive breakpoints:
  930px / 640px
print stylesheet:
  A4
```

使用 `lxml.etree.HTMLParser(recover=False)` 解析：

```text
root:
  html
parser errors:
  0
all ids:
  13
unique ids:
  13
section ids:
  13
unique section ids:
  13
navigation links:
  11
missing navigation targets:
  0
tables:
  2
details blocks:
  1
CSS opening/closing braces:
  157 / 157
```

当前环境没有发现 Chromium、Firefox、wkhtmltoimage 或 WeasyPrint，因此未生成像素级
截图；DOM、导航目标、响应式/打印规则和离线依赖已静态核验。正式投屏前仍建议在实际
展示浏览器中快速目视一次字号和分页。

结果：`OFFLINE_HTML_STRUCTURE = PASS`。

## 8. 索引与哈希

HTML 已登记到：

```text
FILE_INDEX.md
M3_NEXT_ROUND_PRETEACHER_MASTER_INDEX_AND_DECISION_STATUS_2026-07-26.md
PRETEACHER_SELECTION_PACKAGE_SHA256SUMS.txt
```

最终选择包必须在对象目录执行：

```text
sha256sum -c PRETEACHER_SELECTION_PACKAGE_SHA256SUMS.txt
```

并包含本 HTML 的 `OK`。

## 9. 未执行事项

本项未执行：

```text
GitHub push
external email
HPC/GPU
model inference
MetaTraits network query
original JSON mutation
production code
M4b/M4c
hard filtering
```

结果：`NO_UNAUTHORIZED_ACTION = PASS`。

## 10. 最终结论

```text
T1/T2/T3 fidelity:
  PASS
numeric consistency:
  PASS
authority/proposal separation:
  PASS
unknown/no-majority/AI semantics:
  PASS
W1/W2 boundary:
  PASS
offline self-contained structure:
  PASS
HTML parser:
  PASS, 0 errors
current hard filtering:
  NO
M4b authorization:
  NO
```

该 HTML 可以作为刘老师会议中的第二项选择展示入口。正式裁定和科学证据仍以详细
Markdown、D5 原始资产及其独立审计为准。
