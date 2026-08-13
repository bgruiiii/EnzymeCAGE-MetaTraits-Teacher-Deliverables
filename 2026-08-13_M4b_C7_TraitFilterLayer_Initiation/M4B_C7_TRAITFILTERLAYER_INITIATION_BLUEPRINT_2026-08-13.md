# M4b / C7 TraitFilterLayer 立项蓝图草案

日期：2026-08-13

状态：本地立项材料草案，供提交黄老师前复核；尚未启动 M4b 实装，尚未冻结 trait panel，尚未提交 feature encoding 方案，尚未接入 production 运行链。

依据：

```text
00_Authority_Teacher_Plan/
TEACHER_REPLY_PROJECT_NEXT_STEPS_GUIDANCE_2026-08-13.md
```

老师 2026-08-13 要求：

```text
提交 M4b 立项材料（C7）。
前置已满足：C1-C6 全闭 + MT-TQ-02 闭 + hybrid 数据面全齐
+ 08-12 裁定 5 项。
材料要素：TraitFilterLayer 实装范围 / 输入输出契约 / 验收标准。
```

## 0. 边界说明

本材料只请求 M4b/C7 立项裁定，不声称 M4b 已经开始。

本材料不包含：

```text
TraitFilterLayer 活代码；
MicrobeTraitTool 活代码；
trait panel 最终冻结；
feature encoding 最终方案；
MicrobeSelectionAgent 完整形态；
production organism_uid -> traits 通路；
hard filtering / irreversible rejection；
observed 与 predicted 性状混成同一证据等级；
真菌性状生产补齐已完成。
```

若黄老师授权 M4b，建议仍按老师 2026-08-13 给出的顺序推进：

```text
M4b 授权
-> trait panel 冻结
-> feature encoding 提案
-> TraitFilterLayer 实装
-> staged 验收
-> 再决定是否进入 production 链
```

## 1. 已满足的前置条件

### 1.1 C1-C6 / MT-TQ-02 状态

老师 2026-08-13 已明确写明：

```text
C1-C6 全闭（08-07）
MT-TQ-02 闭
hybrid 数据面全齐（08-12 交付包复核通过）
08-12 裁定 5 项
```

历史边界仍延续：

```text
MT-TQ-02 通过不等于自动授权 M4b；
TraitValue / MicrobeTraitTool / TraitFilterLayer 活代码属于 M4b；
M4b 需要单独立项授权。
```

### 1.2 08-12 hybrid 数据面

8.12 交付包已在菌侧 teacher deliverables 仓库：

```text
repo:
git@github.com:bgruiiii/EnzymeCAGE-MetaTraits-Teacher-Deliverables.git

current local mirror used for 08-12 package:
custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/

package:
2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/

remote main HEAD checked locally:
c4ac2087fc7c29a8414e34ca30d28c42244f1588
```

核心数据面结论：

| 项 | 结果 | 解释 |
|---|---:|---|
| source_signature universe | 2,478 | final clean microbe source universe |
| enzyme-source rows | 145,607 | row-weighted universe |
| MetaTraits coverage | 1,638 / 2,478 = 66.1% | species-level trait matrix 主来源 |
| MetaTraits row-weighted coverage | 114,325 / 145,607 = 78.5% | 按训练行加权 |
| BacDive validated species-or-better | 1,746 / 2,478 = 70.5% | 身份、可获得性、培养/来源补充 |
| BacDive row-weighted coverage | 121,243 / 145,607 = 83.3% | 按训练行加权 |
| both covered | 1,508 | 两库都覆盖 |
| BacDive only | 238 | BacDive 补 MetaTraits 缺口 |
| MetaTraits only | 130 | MetaTraits 补 BacDive 缺口 |
| neither | 602 | 当前数据面主要缺口 |
| BacDive species representative sources | 1,149 | species-level validated 可展开代表菌株 |
| representative strain records | 52,956 | BacDive representative strain expansion v2 |

推荐分工：

```text
MetaTraits = 主性状矩阵；
BacDive = exact-strain evidence / representative strain availability /
          culture collection / culture medium / isolation source / country。
```

## 2. 仍需黄老师或领域侧裁定的问题

### 2.1 核心 trait panel 尚未冻结

哪些性状对污水污染物降解任务最重要，需要师姐 / 领域老师讨论后确认，再请黄老师裁定冻结。

当前只能列候选面板，不应写成最终 production panel：

| 候选模块 | 示例 | 当前建议角色 |
|---|---|---|
| oxygen / atmosphere | aerobic, anaerobic, facultative, aerotolerant | 高优先级 soft feature |
| temperature | min / max / optimum / preference | 高优先级 soft feature |
| pH | min / max / optimum / preference | 高优先级 soft feature |
| salinity | tolerance / optimum / maximum | 中高优先级 soft feature |
| catabolic / degradation traits | aromatic compound, hydrocarbon, lignin, plastic, cellulose | 高优先级 contextual feature |
| substrate / carbon utilization | carbon source, metabolite utilization | 高优先级 contextual feature |
| respiration / electron acceptor | nitrate, nitrite, sulfate, iron, sulfur | 高优先级 contextual feature |
| enzyme activity | oxidase, catalase, hydrolase and related groups | 中高优先级 side evidence |
| biosafety | biosafety level / pathogenicity flags | soft warning + manual review |
| BacDive availability | culture collection, type strain, medium, source | 实验追溯与可获得性层 |

### 2.2 observed / predicted 使用路线建议

08-12 讨论材料给出三个路线。结合当前目标，建议向黄老师提交 B 路线作为首选方案，但仍等待老师裁定后再实装。

| 方案 | 含义 | 优点 | 风险 / 代价 |
|---|---|---|---|
| A | 只用 observed traits | 最保守、可解释性强 | 性状少，部分污水生态代谢性状缺失，真菌问题仍无法解决 |
| B（建议） | 核心性状 observed 优先；observed 缺失时 predicted 软补齐 | 保留核心性状覆盖，避免因局部缺失弃用 source；只要 provenance / evidence_type 完整保留，仍可追溯每条性状是实验来源还是预测来源 | 需要先冻结核心面板和可预测补齐类别；prediction 只能作为 soft feature |
| C | observed 与 predicted 分开编码 | 审计最清楚，模型可区分证据等级 | schema 和特征维度更复杂 |

B 路线的建议口径：

```text
已有 observed trait 时优先采用 observed；
核心 trait 缺失时允许 predicted 软补齐；
predicted 不覆盖 observed；
每条 trait 必须保留 evidence_type、prediction_used、source_database、
record_id/source_file/provenance 信息；
下游可追溯每条性状是实验来源、数据库来源还是预测来源；
prediction 不用于 hard rejection。
```

工程底座仍建议保留 C-compatible 审计字段：

```text
trait_value_observed
trait_value_predicted
trait_observed_available
trait_predicted_available
trait_evidence_type = observed | predicted | missing
```

这样黄老师最终若选择：

```text
A：只读取 observed 字段；
B：observed 优先，缺失时读取 predicted 字段并保留 prediction flag；
C：observed / predicted 分开进入 feature encoding。
```

该底座不把 B 路线写死进数据结构，只保证老师最终裁定后，observed / predicted 证据等级仍能被清楚实现和审计。

### 2.3 真菌 source 需要单独策略

当前 2,478 source_signature 中有 428 个真菌来源。8.12 数据面显示：

```text
target_fungi = 428
MetaTraits all coverage = 0
MetaTraits no_predictions coverage = 0
BacDive = prokaryote-oriented, fungi marked non-scope
```

因此真菌不能写成 BacDive 查询失败，也不能把 bacteria/archaea 的 species-level trait 规则静默套用到真菌。

建议提交黄老师裁定的稳妥口径：

```text
真菌在当前本地 MetaTraits/BacDive 数据面中不作为普通 missing 处理；
推荐评估真菌预测性状补充路线，或寻找真菌专用 trait 资源；
该建议不是当前 C7 阶段的既定实施路线，需经师姐 / 领域侧讨论和黄老师裁定；
若后续采用预测补充，必须单独标注 taxonomy_group=fungi、
trait_evidence_type=predicted、prediction_source、missing/uncertainty reason，
不得冒充 observed trait 或 BacDive / MetaTraits species-summary 覆盖。
```

### 2.4 hard filtering 继续关闭

沿用 2026-07-27 生物学 soft policy：

```text
所有污水相关 trait 当前保持 soft；
不执行自动、不可逆剔除；
unknown / not_applicable / No robust majority 不得解释成生物学不存在；
safety/pathogenicity 只做 warning + manual review；
biofilm 当前保持 unknown / unused。
```

M4b Phase 1 的 TraitFilterLayer 虽然保留 `filter` 名称，但建议实际语义是：

```text
trait evidence assembler + soft compatibility annotator
```

不建议在 C7 直接申请 hard rejection。

## 3. TraitFilterLayer 建议实装范围

### 3.1 建议纳入范围

授权后，TraitFilterLayer v1 只做 staged soft trait layer：

```text
1. 读取 M4a organism/source candidates；
2. 读取 08-12 hybrid 数据面产生的 MetaTraits / BacDive source-level tables；
3. 按冻结后的 trait panel 提取 trait features；
4. 按黄老师裁定的 observed-first / predicted-soft-fill 路线处理 observed / predicted；
5. 对真菌、not covered、not_applicable、unknown、predicted-only 情况显式留痕；
6. 输出 source-level trait feature table、provenance table、soft warning table；
7. 生成 staged validation report；
8. 不修改 production pool，不直接接入最终模型 ranking。
```

TraitFilterLayer v1 的最低行为：

```text
输入一个 source_signature / organism candidate；
返回该 source 的 trait evidence 状态、可编码字段、证据等级、缺失原因和软提示；
任何情况下不得静默删除候选菌。
```

### 3.2 明确不纳入范围

M4b C7 首轮不建议纳入：

```text
hard rejection；
LLM 选择候选菌；
production model retraining；
numeric organism_confidence float；
未校准 trait_score；
species -> strain 或 strain -> species trait inheritance；
把 representative strain traits 写成原始 UniProt exact strain traits；
真菌预测资源的无审计批量接入；
在线 API / website fallback 作为唯一生产依赖；
MetaTraits observed 与 predicted 混写为一个普通 value。
```

若黄老师要求 `trait_score`，建议作为 feature encoding proposal 的单独小任务提交：

```text
先冻结 trait panel 和 observed-first / predicted-soft-fill 路线；
再定义 deterministic feature encoding；
再决定是否产生 numeric score；
不得在 C7 立项材料中直接承诺未校准 trait_score。
```

## 4. 输入契约草案

### 4.1 organism/source candidate input

来源：M4a `Enzyme2OrganismTool` / `OrganismAggregator` 输出或其冻结导出表。

最低字段：

```text
source_signature
organism_uid
taxonomy_group
source_resolution_level
species_name
strain_name_or_null
uniprot_tax_id_or_null
gtdb_id_or_null
enzyme_uid
rhea_id_or_reaction_id
organism_source
organism_evidence_fields
```

边界：

```text
v1 不输出 organism_confidence float；
reviewed/unreviewed、annotation score、protein existence、KEGG multiplicity 等
原始证据维度保持分列，不折叠成未校准数值。
```

### 4.2 MetaTraits trait input

来源：08-12 MetaTraits species-level coverage / trait comparison tables。

最低字段：

```text
source_signature
species_name
metatraits_species_match_status
trait_name
trait_group_1
trait_group_2
trait_value_observed
trait_value_predicted
trait_observed_available
trait_predicted_available
trait_evidence_type
trait_resolution = species
is_ai
majority_label
source_database
source_url_or_record_id
tax_id_or_null
missing_reason
provenance_sha256_or_snapshot_id
```

关键限制：

```text
MetaTraits species-level trait 不能冒充 strain-level trait；
is_ai 与 majority_label 必须保持独立；
No robust majority 进入 uncertainty，不作为负证据；
predicted 只能按黄老师裁定的路线进入 soft feature。
```

### 4.3 BacDive availability / provenance input

来源：08-12 BacDive full closure / representative strain expansion v2。

最低字段：

```text
source_signature
bacdive_closure_status
bacdive_exact_strain_policy
bacdive_designation_confidence
bacdive_species_representative_available
representative_record_count
culture_collection_count
has_type_strain_record
has_culture_medium
has_isolation_source
has_country
has_genome_accession
bacdive_record_inclusion_basis
bacdive_resolution
bacdive_provenance_record_id
```

关键限制：

```text
BacDive species representative strain 不等于 UniProt 原始 exact strain；
exact-strain evidence 必须按 main / conservative / hard policy 分层；
fungi 在 BacDive 中是 non-scope，不计作普通 BacDive failure。
```

### 4.4 policy input

M4b 实装前必须冻结一个 policy manifest：

```text
trait_panel_id
trait_panel_version
domain_review_status
teacher_authorization_id
observed_predicted_route = A | B | C
allowed_predicted_trait_categories
fungal_trait_policy
hard_rejection_enabled = false
biofilm_policy = unknown_unused
safety_policy = soft_warning_manual_review
missing_value_policy
not_applicable_policy
provenance_required = true
```

若 `observed_predicted_route`、`trait_panel_id` 或 `teacher_authorization_id` 缺失，TraitFilterLayer 应 fail closed，不生成生产可用结果。

## 5. 输出契约草案

### 5.1 source-level trait feature output

建议输出：

```text
TRAIT_FEATURE_MATRIX_STAGED.csv
```

最低字段：

```text
source_signature
organism_uid
taxonomy_group
trait_panel_id
trait_name
trait_category
trait_value_for_encoding
trait_value_observed
trait_value_predicted
trait_evidence_type
trait_resolution
trait_available
prediction_used
missing_reason
uncertainty_flags
hard_rejection_applied = false
soft_warning
provenance_row_id
```

### 5.2 provenance output

建议输出：

```text
TRAIT_PROVENANCE_TABLE.csv
```

最低字段：

```text
provenance_row_id
source_signature
database
database_snapshot_or_package
record_id_or_url
trait_name
trait_value
evidence_type
resolution
is_ai
majority_label
tax_id
source_file
source_file_sha256
parser_version
created_at_utc
```

### 5.3 soft filter / compatibility output

建议输出：

```text
TRAITFILTERLAYER_SOFT_RESULT.jsonl
```

每行最低结构：

```json
{
  "source_signature": "<id>",
  "organism_uid": "<id>",
  "trait_panel_id": "<id>",
  "route": "A|B|C",
  "hard_rejection_applied": false,
  "soft_warnings": [],
  "uncertainty_flags": [],
  "trait_rows_emitted": 0,
  "provenance_rows_emitted": 0,
  "final_status": "PASS_SOFT_TRAIT_LAYER|BLOCKED_POLICY_NOT_FROZEN|BLOCKED_INPUT_MISSING|PASS_WITH_MISSING_TRAITS"
}
```

### 5.4 report / manifest output

M4b staged 验收包至少包含：

```text
TRAIT_PANEL_DECISION_RECORD.md
TRAITFILTERLAYER_IMPLEMENTATION_SCOPE.md
TRAITFILTERLAYER_IO_CONTRACT.md
TRAIT_FEATURE_MATRIX_STAGED.csv
TRAIT_PROVENANCE_TABLE.csv
TRAITFILTERLAYER_SOFT_RESULT.jsonl
FUNGAL_TRAIT_POLICY_REVIEW_TABLE.csv
OBSERVED_PREDICTED_ROUTE_REPORT.md
SCHEMA_VALIDATION_REPORT.md
BOUNDARY_VALIDATION_REPORT.md
MANIFEST.sha256
FINAL_STATUS.txt
```

## 6. 验收标准草案

### 6.1 立项材料验收

本 C7 材料本身建议按以下标准由老师裁定：

| 要求 | 验收标准 |
|---|---|
| TraitFilterLayer 实装范围 | 明确纳入 staged soft trait layer，明确排除 hard filtering、production merge、未校准 trait_score |
| 输入输出契约 | 覆盖 organism/source、MetaTraits、BacDive、policy manifest、feature/provenance/soft result 输出 |
| 验收标准 | 明确后续 staged 验收文件、schema、边界与 no-overclaim 检查 |
| 待裁定项 | 明确 trait panel、B 路线建议、真菌预测补充路线仍需老师/领域侧确认 |
| 证据边界 | 不把 species-level trait 写成 strain-level，不把 predicted 写成 observed，不把 fungi 写成 BacDive failure |

### 6.2 M4b 实装后 staged 验收

若黄老师授权 M4b，建议首轮实装验收只要求 staged 小规模闭环：

```text
1. 冻结一个 trait_panel_id 和 policy manifest；
2. 明确黄老师选择的 observed/predicted 路线 A/B/C；
3. 在冻结 source subset 上生成 trait feature matrix、provenance table 和 soft result；
4. subset 必须覆盖 bacteria、archaea、fungi、MetaTraits-covered、BacDive-only、
   MetaTraits-only、neither-covered 等关键分层；
5. schema validation 全部 PASS；
6. provenance rows 可回到 08-12 package 文件和 SHA256；
7. hard_rejection_applied 全部 false；
8. no confidence float；
9. no species/strain silent inheritance；
10. fungi 单独进入 fungal policy table；
11. observed / predicted / missing 可分开统计；
12. production mutation check 为 false。
```

建议最低审计计数：

```text
trait_panel fields emitted count；
observed rows / predicted rows / missing rows；
taxonomy_group counts；
MetaTraits covered / BacDive covered / neither covered counts；
fungi rows and fungal policy status；
soft warning counts；
uncertainty flag counts；
schema error count = 0；
production mutation flags = false。
```

## 7. 建议拆分为小任务

授权前只提交 C7，不开工。

授权后建议每次只做一个小任务：

| 小任务 | 目标 | 输出 |
|---|---|---|
| C7-1 | 冻结 trait panel 决策表 | `TRAIT_PANEL_DECISION_RECORD.md` + panel CSV |
| C7-2 | 冻结 B 路线裁定与真菌策略 | `OBSERVED_PREDICTED_ROUTE_REPORT.md` + `FUNGAL_TRAIT_POLICY_REVIEW_TABLE.csv` |
| C7-3 | 写 feature encoding 提案 | `TRAIT_FEATURE_ENCODING_PROPOSAL.md` |
| C7-4 | 实装只读 TraitFilterLayer schema / validator | code + schema tests |
| C7-5 | staged subset smoke | staged output package + audit |
| C7-6 | 扩展到 2,478 source staged status table | full staged feature/provenance/status package |

每一步均需本地审计后再决定是否提交老师，不跳步。

## 8. 给黄老师的最小请求

建议本轮向黄老师请求：

```text
请黄老师审阅 M4b / C7 立项蓝图，确认是否授权进入 M4b 立项流程。

若授权，下一步不直接写 production 代码，而是先冻结：
1) trait panel；
2) 是否接受 B 路线：observed 优先，核心缺失 trait 由 predicted 软补齐，并保留完整 evidence/provenance；
3) 真菌 source 的预测补充评估路线；
4) feature encoding 提案；
之后再实装 TraitFilterLayer staged soft layer。
```

需要黄老师裁定的最小项：

```text
1. 是否接受 TraitFilterLayer v1 只做 staged soft trait layer；
2. 是否接受 B 路线，并同意底层 schema 保留 observed/predicted 分开审计字段；
3. trait panel 是否先由师姐/领域侧确认后再冻结；
4. 真菌是否按单独路线处理，并评估预测性状补充；
5. 是否继续禁止 hard filtering、未校准 confidence float 和 production mutation。
```
