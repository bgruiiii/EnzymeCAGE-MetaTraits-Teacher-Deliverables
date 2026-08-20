# M4b / C8 TraitFilterLayer 实装方案与拆解待审

日期：2026-08-19

对象：黄老师审阅；陈浩然侧主线 + 微生物侧。

状态：**方案 / 拆解待审**。本文不声称 C8 已实装，不接 production，不改
production D4，不改 production pool。

## 1. 本文要回答什么

黄老师 2026-08-18 任务单要求陈浩然侧在 08-20 前提交：

```text
C8 实装方案 / 拆解待审
```

本方案回答四个问题：

1. C8 TraitFilterLayer 从哪些已经验收或冻结的材料开始；
2. C8 要读入什么、生成什么、怎样校验；
3. 哪些步骤可以先做成 staged-only，只读验证；
4. 哪些事情仍需黄老师审定后才能进入真正联调或 production。

## 2. 老师已给出的边界

### 2.1 2026-08-14 裁定

已经通过：

```text
full 4,681 staged status table 第二里程碑验收通过；
1,704 套 PASS staged 资产可被下游消费；
C7-1 trait panel F1-F15 逐项冻结；
全部产出 staged-only，不构成 production D4 merge；
mutation checks 全 False。
```

C7-1 冻结的关键规则：

```text
第一屏 5 项：F1 oxygen_tolerance, F2 temperature, F3 pH, F4 salinity,
F5 bacdive_availability。

追问展开 10 项：F6-F15。

observed 永远优先；
predicted 不覆盖 observed；
F1-F4/F6-F8 允许 predicted soft-fill，但必须显式标注；
F5 禁止预测，只能来自 BacDive / culture collection evidence；
F8 只能作 broad degradation context，不能声称可降解用户输入污染物；
F15 只能作低覆盖生态背景，不参与排序/评分/推荐；
真菌本轮 identity-only，不启用 predicted soft-fill；
无 hard rejection、无 trait_score、无未校准 confidence。
```

### 2.2 2026-08-17 裁定

已经通过：

```text
C7-2 feature encoding 提案冻结通过；
下一步仅限只读 schema/validator 实装 + bounded staged 子集；
仍 staged-only，不构成 TraitFilterLayer production 实装或生产授权。
```

### 2.3 2026-08-18 任务单

老师进一步授权：

```text
C8 TraitFilterLayer 实装授权；
边界：产物严格 staged-only，不接 production；
入口：C7-2 已验收只读 schema/validator + C7-1 frozen trait panel；
落地：以 C7-2 validator 为入口起草 TraitFilterLayer 消费契约，
并与弓赛 fallback 引擎产出的酶候选做上下游联调。
```

同一任务单还要求：

```text
MetaTraits bulk TSV 落晨羽；
回报路径 + 文件清单 + SHA256；
明确 TSV 字段与 C7-1 trait panel 的映射口径；
MetaTraits 走本地 TSV，不依赖失效 API。
```

该 TSV 落地与 C7-1 映射口径已在 2026-08-19 整理为前置证据。

## 3. 当前可用证据

### 3.1 酶资产侧

老师 2026-08-14 已验收：

```text
4,681 UID denominator；
1,704 UID PASS staged assets；
1,324 AFDB_P2RANK_NO_POCKET；
1,650 AFDB_STRUCTURE_FETCH_FAILED；
3 ESM2_3B_EXTRACTION_FAILED；
STAGED_ASSET_MANIFEST = 1,704 UID * 6 assets = 10,224 files；
formal_assets_mutated / production_pool_mutated / production_d4_mutated 全 False。
```

C8 只允许消费 staged PASS 资产，不允许把 blocker 当作可用资产。

### 3.2 微生物来源侧

2026-08-12 已整理并上传的微生物侧证据：

```text
final clean microbe source universe = 2,478 source_signatures；
enzyme-source rows = 145,607；
MetaTraits local snapshot coverage = 1,638 / 2,478；
BacDive validated species-or-better = 1,746 / 2,478；
BacDive exact_strain_main = 597 / 2,478；
BacDive hard exact strain = 555 / 2,478；
BacDive + MetaTraits both covered = 1,508；
BacDive only = 238；
MetaTraits only = 130；
neither = 602。
```

这些数值作为 C8 覆盖率汇总口径，但不能写成所有 2,478 都有完整 trait。

### 3.3 C7-2 bounded validator

2026-08-18 已完成只读 bounded 30 验证：

```text
30 rows = 10 bacteria + 10 archaea + 10 fungi；
all rows come from teacher-accepted 1,704 staged PASS assets；
P0DXV0 excluded，保持 1,704 与 1,705 口径分开；
POLICY_MANIFEST.json / TRAIN_SET_MANIFEST.csv / trait_annotation.jsonl /
TRAIT_FEATURE_ENCODING_VALIDATION_REPORT.md / BOUNDARY_VALIDATION_REPORT.md
均已生成；
overall_pass=True；
validation errors=0；
无 production / formal asset mutation。
```

这说明 C7-2 的 schema 和 validator 可以作为 C8 的起点。

### 3.4 MetaTraits TSV 与 C7-1 字段映射

2026-08-18/19 已完成：

```text
MetaTraits 12 个 bulk summary TSV gzip 已落 Chenyu；
2 个 crosswalk 已落 Chenyu；
14/14 gzip test PASS；
14/14 SHA256 recorded；
official index last modified = 2026-06-10 10:23；
DATA_DIR=/usrdata/EnzymeCAGE_data/data/metatraits/incoming/metatraits_bulk_tsv_snapshot_20260818。
```

2026-08-19 rerun2 修正后：

```text
C7-1 long-form mapping trait_panel_rows_written=15/15；
negative_assertions_passed=8/8；
F3 pH 不再误匹配 Atmosphere / Morphology；
F12 Gram 不再误匹配 gramicidin；
未下载、未 API、未预测、未 production mutation、未 snapshot activation。
```

C8 应直接引用 rerun2 映射口径，不能回退到早期 header-only 映射。

## 4. C8 的工作定位

C8 不是重新训练模型，也不是新找菌，也不是改变 C7-1/C7-2 规则。

C8 应该做的是：

```text
把 upstream 酶候选表中的 UID，接到已有 staged 酶资产和微生物来源；
对每个候选菌按 F1-F15 读取本地 trait 证据；
按 C7-2 已冻结规则生成 trait_annotation；
做只读校验；
输出可供后续 TraitFilterLayer 过滤/展示使用的 staged 包。
```

白话说：前面 C7-1/C7-2 已经规定了“哪些性状能用、怎么标注”；C8 要设计
“正式干活时这一层怎么接线、怎么查表、怎么输出、怎么防错”。

## 5. 输入契约

### 5.1 上游酶候选输入

最小字段：

```text
query_id
pollutant_name_or_smiles
reaction_candidate_id
reaction_source
enzyme_uid
enzyme_candidate_rank_or_order
enzyme_candidate_source
```

说明：

```text
reaction_source 可来自主路线或 fallback，但 C8 不负责判断反应预测器是否达标；
enzyme_uid 必须能在 staged PASS 资产或受控测试输入中找到；
若 enzyme_uid 没有 staged PASS 资产，应记录为 ASSET_NOT_AVAILABLE，不继续生成 trait。
```

### 5.2 酶资产输入

来自老师已验收的 staged assets：

```text
FULL_4681_STAGED_STATUS_TABLE.csv
STAGED_ASSET_MANIFEST.csv
per-UID validation reports
```

必须保留字段：

```text
UniprotID
sequence_sha256
esm_shape
p2rank_pocket_residue_count
p2rank_top_pocket_score
same_pocket_for_esm_node_and_gvp
loader_validation_status
dataset0_constructed
evidence_tier
formal_assets_mutated
production_pool_mutated
production_d4_mutated
```

硬规则：

```text
只允许 PASS_AFDB_P2RANK_PREDICTED_POCKET_D4_LOADER；
sequence_sha256 必须一致；
esm_node_feature_shape[0] == p2rank_pocket_residue_count；
same_pocket_for_esm_node_and_gvp == True；
loader_validation_status == PASS；
mutation 三列必须 False。
```

### 5.3 UID 到微生物来源输入

来自已审计的 2,478 source universe 与 UID-to-source 映射。

必须保留：

```text
uid
source_signature
TaxID
organism_name
taxonomy_group = bacteria | archaea | fungi
mapping_source
mapping_method
mapping_resolution
strain_name_or_null
```

禁止：

```text
不得把 species-level trait 写成 strain-level trait；
不得把 BacDive species representative 写成原始 UniProt exact strain；
不得对 source_signature / species / strain 做静默继承。
```

### 5.4 Trait 来源输入

MetaTraits：

```text
只读本地 TSV snapshot；
不调用 MetaTraits API；
不运行在线 genome prediction；
使用 C7-1 long-form rerun2 mapping 口径；
observed/no_predictions 与 all scope 分开记录。
```

BacDive：

```text
只读此前已审计的 BacDive closure/cache 表；
不新调用 BacDive API；
F5 availability / culture collection number 只从 BacDive/保藏证据读取；
species representative 必须显式标注。
```

## 6. 输出契约

C8 staged package 建议输出以下文件。

### 6.1 POLICY_MANIFEST.json

说明本轮采用哪一版规则。

必含：

```text
trait_panel_id = M4B_C7_PANEL_FROZEN_2026_08_14
feature_encoding_contract = M4B_C7_2_FEATURE_ENCODING_PROPOSAL_2026-08-15
metatraits_mapping_contract = C7_1_LONG_FORM_MAPPING_RERUN2_FALSE_POSITIVE_FIX_2026-08-19
teacher_authorization_id = TEACHER_REPLY_NEXT_ACTIONS_2026-08-18
route = observed_first_predicted_soft_fill_for_allowed_categories
allowed_predicted_soft_fill = F1,F2,F3,F4,F6,F7,F8
forbidden_predicted_soft_fill = F5,F9,F10,F11,F12,F13,F14,F15
fungal_trait_policy = identity_only
hard_rejection_enabled = false
trait_score_enabled = false
uncalibrated_confidence_enabled = false
production_integration_enabled = false
```

### 6.2 C8_INPUT_CANDIDATE_TABLE.csv

说明 C8 读入的上游候选是什么。

必含：

```text
query_id
pollutant_name_or_smiles
reaction_candidate_id
reaction_source
enzyme_uid
enzyme_candidate_source
enzyme_candidate_rank_or_order
input_status
input_exclusion_reason
```

### 6.3 TRAIN_SET_MANIFEST.csv

沿用 C7-2 7.2 loader 契约，记录可消费 staged enzyme assets。

必含：

```text
UniprotID
sequence_sha256
sequence_length
esm_shape
p2rank_pocket_residue_count
p2rank_top_pocket_score
gvp_available
same_pocket_for_esm_node_and_gvp
loader_validation_status
dataset0_constructed
evidence_tier
formal_assets_mutated
production_pool_mutated
production_d4_mutated
deduplication_status
split
inclusion_status
exclusion_reason
source_status_table
source_asset_manifest
```

### 6.4 trait_annotation.jsonl

一行对应一个 enzyme_uid 到一个 microbe source 的候选关系。

必含四段：

```text
asset: 酶资产状态；
mapping: uid -> source_signature / organism / taxonomy 信息；
traits: F1-F15 每项显式保留；
row_policy: hard_rejection / trait_score / production 等红线状态。
```

每个 F trait 必须统一保留：

```text
trait_id
trait_name
display_layer
observed_value
predicted_value
resolved_display_value
value_status
evidence_type
prediction_used
observed_available
predicted_available
source_database
source_resolution
provenance
missing_reason
warnings
```

### 6.5 C8_TRAITFILTERLAYER_CONSUMPTION_CONTRACT.md

给后续代码或联调用的接口说明。

必须写清：

```text
上游候选表如何接入；
候选 UID 没有 staged asset 时如何 fail closed；
一个 UID 对多个 source_signature 时如何保留多行；
第一屏 5 项如何展示；
追问展开 10 项如何保留；
observed / predicted / missing / fungi identity-only 如何标注；
哪些字段不得参与排序或硬过滤。
```

### 6.6 C8_VALIDATION_REPORT.md / json

校验结果。

建议分四层：

```text
asset validation
mapping validation
trait policy validation
boundary validation
```

### 6.7 C8_BOUNDARY_VALIDATION_REPORT.md

专门给老师看红线是否没越过。

### 6.8 MANIFEST.files / MANIFEST.sha256 / FINAL_STATUS.txt

用于归档和复核。

## 7. 处理规则

### 7.1 候选接入规则

```text
对于每个上游 enzyme_uid：
1. 查 staged PASS asset；
2. 若没有 PASS asset，记录 ASSET_NOT_AVAILABLE，不生成 trait；
3. 若有 PASS asset，查 uid -> source_signature；
4. 若一个 UID 对多个 source_signature，逐个 source_signature 展开，不合并；
5. 对每个 source_signature 查 MetaTraits / BacDive 本地证据；
6. 按 F1-F15 输出 trait_annotation；
7. 全部过程只读。
```

### 7.2 Trait 取值规则

```text
如果 taxonomy_group == fungi：
    F1-F15 value_status = FUNGI_IDENTITY_ONLY；
    prediction_used = false；
    missing_reason = fungi_no_local_trait_source。

如果有 observed/no_predictions 证据：
    使用 observed；
    predicted_value 可记录为 available，但 prediction_used=false。

如果没有 observed，但 all scope 有值，且 trait_id 属于 F1-F4/F6-F8：
    使用 predicted soft-fill；
    prediction_used=true；
    必须标注 source_database / source_file / source_file_sha256 / databases。

如果没有 observed，或该 trait 禁止 predicted：
    value_status = NOT_OBSERVED 或 NOT_APPLICABLE；
    不得把缺失解释为生物学不存在。
```

### 7.3 第一屏展示规则

第一屏只展示：

```text
F2 temperature
F3 pH
F1 oxygen_tolerance
F4 salinity
F5 bacdive_availability / culture collection number
```

展示时必须带状态：

```text
observed
predicted soft-fill
not observed
fungi identity-only
species representative
exact strain
```

### 7.4 追问展开规则

F6-F15 保留在 `traits` 字段中，默认不作为第一屏主要展示。用户追问某个菌时，
再展开这些信息。

### 7.5 禁止规则

```text
不 hard reject 微生物；
不输出 trait_score；
不输出未校准 confidence；
不把 F8 broad degradation 写成对目标污染物的直接降解事实；
不把 F15 用于排序、评分、推荐；
不预测 F5 保藏编号；
不对真菌做 predicted soft-fill；
不把 species representative 写成 exact strain；
不合并掉 F1-F15 ID。
```

## 8. Validator 必须检查什么

### 8.1 Asset checks

```text
只消费 PASS_AFDB_P2RANK_PREDICTED_POCKET_D4_LOADER；
asset manifest 中 6 件套存在；
sequence_sha256 与 manifest 一致；
esm_shape[0] == p2rank_pocket_residue_count；
same_pocket_for_esm_node_and_gvp == True；
loader_validation_status == PASS；
formal_assets_mutated == False；
production_pool_mutated == False；
production_d4_mutated == False。
```

### 8.2 Mapping checks

```text
uid -> source_signature 不得空写；
TaxID / organism_name / taxonomy_group 必须可追溯；
多 source_signature 不得静默合并；
species-level / strain-level / species representative 必须显式标注；
真菌必须走 identity-only。
```

### 8.3 Trait checks

```text
每行必须恰好有 F1-F15；
没有未冻结 trait ID；
F5 prediction_used 永远 false；
F9-F15 prediction_used 永远 false；
F1-F4/F6-F8 只有 observed 缺失时才可 predicted soft-fill；
observed 和 predicted 不得混在同一个字段里；
missing 不得写成 biological absence；
F3 不得混入 Atmosphere/Morphology；
F12 不得混入 gramicidin。
```

### 8.4 Boundary checks

```text
no MetaTraits API；
no BacDive API；
no online genome prediction；
no asset generation；
no production D4 mutation；
no production pool mutation；
no active_snapshot activation；
no UID replacement；
no hard rejection；
no trait_score；
no uncalibrated confidence。
```

## 9. 建议拆分任务

### C8-0：输入冻结与路径预检

目的：确认 C8 消费的输入都存在，且是老师已验收/冻结版本。

输出：

```text
C8_INPUT_SOURCE_AUDIT.md
C8_INPUT_SOURCE_AUDIT.json
```

必须检查：

```text
1,704 staged PASS package identity；
C7-2 bounded validator package identity；
MetaTraits TSV landing identity；
C7-1 long-form rerun2 mapping identity；
BacDive prior closure/cache source identity；
teacher authority file identity。
```

### C8-1：构建只读 trait lookup index

目的：从本地 MetaTraits TSV 和 BacDive cache 中抽取 F1-F15 所需字段，生成
staged lookup，便于后续按 TaxID/source_signature 查。

输出：

```text
C8_METATRAITS_LOOKUP_INDEX.csv 或 jsonl
C8_BACDIVE_AVAILABILITY_LOOKUP.csv
C8_LOOKUP_INDEX_BUILD_REPORT.md
```

边界：

```text
不下载；
不 API；
不预测；
不激活为 production snapshot。
```

### C8-2：候选 UID 到微生物来源展开

目的：把上游 enzyme_uid 候选展开成 UID-source_signature 行。

输出：

```text
C8_UID_SOURCE_EXPANSION_TABLE.csv
C8_UID_SOURCE_EXPANSION_REPORT.md
```

规则：

```text
一 UID 多来源则多行保留；
找不到 source_signature 则记录 NOT_MAPPED；
找不到 staged PASS asset 则记录 ASSET_NOT_AVAILABLE。
```

### C8-3：生成 trait_annotation.jsonl

目的：按 C7-2 冻结 schema 生成每行 F1-F15 注解。

输出：

```text
trait_annotation.jsonl
TRAIN_SET_MANIFEST.csv
```

规则：

```text
observed first；
predicted soft-fill only for F1-F4/F6-F8；
F5 observed only；
fungi identity-only；
保留 provenance。
```

### C8-4：validator 与边界报告

目的：自动检查 C8 是否违反 C7-1/C7-2/老师红线。

输出：

```text
C8_VALIDATION_REPORT.json
C8_VALIDATION_REPORT.md
C8_BOUNDARY_VALIDATION_REPORT.md
```

COMPLETE 条件：

```text
asset checks PASS；
mapping checks PASS；
trait checks PASS；
boundary checks PASS；
0 hard error。
```

### C8-5：bounded-to-full staged rollout

建议顺序：

```text
第一步：使用 30-row bounded 子集复跑，确认与 2026-08-18 C7-2 validator 结果一致；
第二步：使用一个小型真实 upstream enzyme candidate table 做联调样例；
第三步：老师同意后，再扩展到完整 staged PASS intersection / 2,478 source universe；
第四步：仍只输出 staged report，不接 production。
```

## 10. 与弓赛 fallback 引擎的接口

C8 不接管弓赛的 reaction fallback 质量判断，也不替弓赛生成候选反应。

C8 只要求上游给出一个结构化候选表：

```text
pollutant/query
reaction candidate
reaction source
enzyme UID
enzyme candidate source
```

C8 返回：

```text
每个 enzyme UID 对应的微生物候选；
每个微生物候选的 F1-F15 trait evidence；
第一屏五项展示状态；
缺失/预测/真菌 identity-only 标注；
不做 hard rejection 的解释信息。
```

如果上游暂时没有稳定 fallback 结果，C8 可以先用此前已验收的 bounded staged
UID 列表做 schema smoke，不影响 C8 自身接口定义。

## 11. 建议给老师审定的问题

当前不需要新增生物专家决定才能写本方案，因为 C7-1 和 C7-2 的关键生物口径
已经冻结。仍建议请黄老师确认以下工程推进点：

1. C8-1 只读 lookup index 是否可作为 staged 派生物生成；
2. C8 首轮 full staged rollout 的 denominator 是仅限 1,704 PASS assets，
   还是同时列出 2,478 source universe 中未被当前 enzyme candidates 命中的来源；
3. 与弓赛 fallback 联调时，是否先用小型候选表做接口验收，再等待其效果整改后全量联调；
4. C8 输出是否只做展示/解释/覆盖统计，继续禁止任何 hard filtering 和 trait_score。

## 12. 非主张

本文不主张：

```text
C8 已经实装；
TraitFilterLayer 已 production-ready；
已经生成 full 2,478 trait_annotation；
已经接入弓赛 fallback 真实批跑；
已经启用任何 hard filter；
已经给微生物打 trait_score；
已经对真菌做性状预测；
已经把 MetaTraits snapshot 激活到 production；
已经修改 production D4 或 production pool。
```

## 13. 建议交付包结构

```text
2026-08-19_M4b_C8_TraitFilterLayer_Implementation_Plan/
  README.md
  M4B_C8_TRAITFILTERLAYER_IMPLEMENTATION_PLAN_AND_TASK_BREAKDOWN_2026-08-19.md
  authority_reference/
  evidence_index/
  audits/
  MANIFEST.files
  MANIFEST.sha256
```

老师审定本方案后，再启动 C8 executor-only 实装提示词与 staged-only 回包。
