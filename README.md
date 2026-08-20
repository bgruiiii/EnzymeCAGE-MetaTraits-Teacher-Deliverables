# MetaTraits Teacher Deliverables

## 老师当前优先审阅入口 — 2026-08-20

本次新增 C8-P porTraits 受控预检决策包：

- [`2026-08-20_M4b_C8_P_porTraits_Preflight_Decision_Request/`](2026-08-20_M4b_C8_P_porTraits_Preflight_Decision_Request/)

该包对应老师 2026-08-19 裁定中“MetaTraits 未覆盖 bacteria / archaea 如需
porTraits，先交 C8-P preflight 方案、老师审定后再启动”的要求。我们已完成
C8-P0 路径契约、C8-P1 Chenyu 环境/输入预检、C8-P2A runtime/version resolver、
C8-P2B asset/container/quota metadata-only preflight，并逐包本地审计。当前只
完成受控预检，未运行 porTraits、未运行 Nextflow workflow、未下载 genome
FASTA / 数据库 / 容器、未产生 phenotype prediction、未写 production。核心
结论是：目标集合清楚（322 bacteria + 90 archaea = 412，428 fungi 继续
identity-only），Nextflow 与 porTraits v0.2.1 路线已找到，但实际 smoke 仍
卡在 Singularity/Apptainer、porTraits 资产、eggNOG 来源、SIF 镜像、tiny FASTA
授权和老师 D1-D7 裁定。

## 老师当前优先审阅入口 — 2026-08-20

请优先打开当前入口和本次 2026-08-20 新增两项：

- [`00_CURRENT_TEACHER_REVIEW_ENTRYPOINT/`](00_CURRENT_TEACHER_REVIEW_ENTRYPOINT/)
- [`2026-08-20_M4b_C8_Staged_Implementation_Bounded_30_Rerun/`](2026-08-20_M4b_C8_Staged_Implementation_Bounded_30_Rerun/)
- [`2026-08-20_M4b_C8_P_porTraits_Preflight_Decision_Request/`](2026-08-20_M4b_C8_P_porTraits_Preflight_Decision_Request/)

本次 C8 主链路包对应老师 2026-08-19 对陈浩然侧 C8 的 staged-only
推进要求：C8-0 输入冻结、C8-1 lookup index + 137 delta review、C8-2A
UID-source expansion harness、C8-3/C8-4 固定 30-row bounded rerun 均已整理
并审计通过。该包不声明 C8-5 已完成；C8-5 的小型真实上游候选表 smoke 仍需
等待上游候选表，不能用 4,681/1,704 harness 或 30 行 bounded 子集冒充真实
候选酶。

本次 C8-P porTraits 包是受控 preflight decision request：只完成环境、输入、
版本、资产、容器和配额预检；没有运行 porTraits workflow，没有 phenotype
prediction，没有下载 genome FASTA / 数据库 / 容器，没有写 production。该包
请求老师裁定 D1-D7 后，才决定是否进入下一阶段准备。

## 老师当前优先审阅入口 — 2026-08-19

请优先打开当前入口和本次新增两项：MetaTraits TSV 落晨羽 + C7-1 映射修复，
以及 C8 TraitFilterLayer 实装方案 / 拆解待审：

- [`00_CURRENT_TEACHER_REVIEW_ENTRYPOINT/`](00_CURRENT_TEACHER_REVIEW_ENTRYPOINT/)
- [`2026-08-19_MetaTraits_Bulk_TSV_Landing_and_C7_1_Mapping_Correction/`](2026-08-19_MetaTraits_Bulk_TSV_Landing_and_C7_1_Mapping_Correction/)
- [`2026-08-19_M4b_C8_TraitFilterLayer_Implementation_Plan/`](2026-08-19_M4b_C8_TraitFilterLayer_Implementation_Plan/)
- [`2026-08-19_M4b_C7_2_Fungal_Observed_Trait_Source_Exploration_Closure/`](2026-08-19_M4b_C7_2_Fungal_Observed_Trait_Source_Exploration_Closure/)
- [`2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/`](2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/)
- [`2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/`](2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/)
- [`2026-08-14_M4b_C7_1_Trait_Panel_Candidate/`](2026-08-14_M4b_C7_1_Trait_Panel_Candidate/)
- [`2026-08-13_M4b_C7_TraitFilterLayer_Initiation/`](2026-08-13_M4b_C7_TraitFilterLayer_Initiation/)

本次 2026-08-19 新增 MetaTraits 包对应老师 2026-08-18 P0 要求：
MetaTraits 12 个 bulk TSV 已落 Chenyu，回报路径、文件清单、SHA256、
官方日期追溯已整理；C7-1 TSV 字段映射已按 long-form row-level route 修正，
rerun2 负例断言 8/8 PASS，pH 不再误匹配 Atmosphere/Morphology，Gram 不再
误匹配 gramicidin。原始大 TSV 不上传 GitHub，仅保留 Chenyu 路径和 metadata
回包。

本次 2026-08-19 新增 C8 包对应老师 2026-08-18 要求：
C8 TraitFilterLayer 实装方案 / 拆解待审。该方案以 C7-2 validator 为入口，
引用已冻结 C7-1 F1-F15、C7-2 encoding contract 和 MetaTraits long-form
rerun2 映射口径，提出 C8-0 至 C8-5 staged-only 实装拆分。它不是 C8 实装
结果，也不接 production。C8 包内另列两个实装前待老师裁定问题：补资产后
牵出的 137 个 2,478 外 source_signature 是否扩入 staged universe，以及
MetaTraits 未覆盖 bacteria/archaea 是否另行授权 porTraits genome prediction
preflight；详细见
[`2026-08-19_M4b_C8_TraitFilterLayer_Implementation_Plan/pending_teacher_decisions/M4B_C8_PENDING_TEACHER_DECISIONS_RESCUED_SOURCES_AND_PORTRAITS_2026-08-19.md`](2026-08-19_M4b_C8_TraitFilterLayer_Implementation_Plan/pending_teacher_decisions/M4B_C8_PENDING_TEACHER_DECISIONS_RESCUED_SOURCES_AND_PORTRAITS_2026-08-19.md)。

本次 2026-08-19 新增真菌 observed-trait source exploration closure 包用于
说明为什么当前 C7-2 真菌仍保持 identity-only。DSMZ/MediaDive/ATCC 能提供
少量可审计 observed evidence，但严格合并覆盖只有 any evidence `78/575`，
temperature `75/575`，pH `12/575`，salinity `0/575`，oxygen `68/575`，
culture collection accession `78/575`；`575` 只是探索内部 source_signature
行级分母，不替代 C7-2 老师口径真菌数 `428`。结论是停止当前轮次真菌
observed-source 深挖，不合并到 C7-2，不做 hard filter，不使用真菌预测声明。
若后续考虑用面向细菌/古菌/原核的预测工具补真菌性状，本包新增待讨论项：
先和师姐/领域 reviewer 讨论工具迁移和 out-of-domain 边界，再单独请老师裁定；
当前不默认执行。

2026-08-18 C7-2 包对应老师 2026-08-17 裁定后的下一步：C7-2
只读 schema/validator 实装 + bounded staged 子集。包内包含
`POLICY_MANIFEST.json`、`TRAIN_SET_MANIFEST.csv`、`trait_annotation.jsonl`、
校验报告、边界报告、`MANIFEST.sha256` 和 `FINAL_STATUS.txt`。30 行子集来自
`2,478` 微生物主库与老师接受的 `1,704` staged PASS 酶资产交集，其中细菌
部分优先选取环境/工业语境示例；当前仍 staged-only，未接 production。

老师 2026-08-17 已裁定 2026-08-16 C7-2 feature encoding 提案作为设计契约
冻结通过；8/18 包是按该冻结契约做的只读小样例验证，不构成
TraitFilterLayer production 实装。

当前微生物侧主数据库为 2,478 个 source_signature；MetaTraits 本地快照覆盖
1,638/2,478。未覆盖部分本轮不做在线基因组预测扩展，只按 C7-2 冻结边界标注
为未观察/缺失；真菌在本轮保持 identity-only，预测路线单独评估。

C7-1 冻结面板口径：第一屏展示温度、pH、耗氧/厌氧、盐度和 BacDive 保藏
编号；其他保留性状按追问展开。biosafety level 不进入 C7-1/C7-2 trait
panel；真菌本轮 identity-only，预测路线单独评估、单独裁定。

## Current 2026-08-12 hybrid data-plane package

- [`2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/`](2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/)

该交付包汇总了 EnzymeCAGE 微生物侧 MetaTraits 与 BacDive 的最新探索结果：MetaTraits 作为物种级主性状矩阵来源，BacDive 作为菌株身份、代表菌株可获得性、保藏编号、培养基和分离来源补充来源。

核心结果：

- final clean microbe source universe: 2,478 source_signatures / 145,607 enzyme-source rows；
- MetaTraits 覆盖 1,638 / 2,478 source_signatures = 66.1%，confirmed covered source 平均约 156.8 个 unique trait_name；
- BacDive closure 后 validated species-or-better 覆盖 1,746 / 2,478 = 70.5%，row-weighted 83.3%；
- BacDive exact_strain_main 覆盖 597 / 2,478 = 24.1%，hard exact 覆盖 555 / 2,478 = 22.4%；
- BacDive 与 MetaTraits main-policy overlap: both covered 1,508，BacDive only 238，MetaTraits only 130，neither 602；
- BacDive species-level representative strain expansion v2: 1,149 / 1,149 species-level BacDive hits 均有至少一个 representative strain record 和至少一个 culture collection number。
- MetaTraits observed-only 与 all snapshot 对比显示：source 覆盖均为 1,638 / 2,478，但 all snapshot 的 covered source 平均 unique trait_name 约 156.8，no_predictions 为 47.7；因此 prediction-like 信息主要补充性状密度，不增加当前本地 source 覆盖。
- 新增待讨论项：先定义污染物降解微生物核心性状面板，再裁定 observed 缺失时是否允许 MetaTraits predicted traits 作为 soft feature 补齐；真菌需单独策略。

建议阅读顺序：

1. [`2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/README.md`](2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/README.md)
2. [`03_bacdive_vs_metatraits_trait_comparison/BACDIVE_VS_METATRAITS_TRAIT_AVAILABILITY_COMPARISON_2026-08-12.md`](2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/03_bacdive_vs_metatraits_trait_comparison/BACDIVE_VS_METATRAITS_TRAIT_AVAILABILITY_COMPARISON_2026-08-12.md)
3. [`02_bacdive_full_closure/CODEX_LOCAL_AUDIT_BACDIVE_FULL_CLOSURE_2478_2026-08-12.md`](2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/02_bacdive_full_closure/CODEX_LOCAL_AUDIT_BACDIVE_FULL_CLOSURE_2478_2026-08-12.md)
4. [`04_bacdive_species_representative_strain_expansion/CODEX_AUDIT_BACDIVE_SPECIES_REPRESENTATIVE_STRAIN_EXPANSION_V2_2026-08-12.md`](2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/04_bacdive_species_representative_strain_expansion/CODEX_AUDIT_BACDIVE_SPECIES_REPRESENTATIVE_STRAIN_EXPANSION_V2_2026-08-12.md)
5. [`05_next_discussion_trait_panel_and_prediction_policy/TRAIT_PANEL_AND_PREDICTION_POLICY_DISCUSSION_REQUEST_2026-08-12.md`](2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/05_next_discussion_trait_panel_and_prediction_policy/TRAIT_PANEL_AND_PREDICTION_POLICY_DISCUSSION_REQUEST_2026-08-12.md)

解释边界：MetaTraits 是 species-level trait source，不写成 strain-level trait；BacDive species-level representative strain records 不写成原始 UniProt exact strain；exact-strain evidence 按 main/conservative/hard policy 分层；prediction-like traits 尚未裁定为 production 主特征。历史文件保留用于追溯，当前审阅以本 2026-08-12 入口为准。


## 老师当前优先审阅入口 — 2026-08-05

请优先打开：

- [`00_CURRENT_TEACHER_REVIEW_ENTRYPOINT/`](00_CURRENT_TEACHER_REVIEW_ENTRYPOINT/)

该文件夹汇总了当前最新回应、已完成证据路径、仍保持锁定的 M4b/M4c 边界，以及仍需老师或外部维护方闭合的问题。根目录中保留历史文件是为了不破坏此前已经发给老师的旧 GitHub 链接；当前审阅请以本入口和下方最新回应为准。

## Current 2026-08-03 teacher-requirement reconfirmation — 2026-08-04

The latest MetaTraits / bacteria-layer reconfirmation package has been pushed
and is placed at repository root so completed work is visible from the GitHub
homepage:

- [`M3_2026_08_03_METATRAITS_REQUIREMENTS_RECONFIRMATION_INDEX_2026-08-04.md`](M3_2026_08_03_METATRAITS_REQUIREMENTS_RECONFIRMATION_INDEX_2026-08-04.md)
- [`2026-08-04_M3_Bacteria_Layer_D1_D8_Confidence_and_Task7_Reconfirmation/`](2026-08-04_M3_Bacteria_Layer_D1_D8_Confidence_and_Task7_Reconfirmation/)

Status: D5, D1--D8, enzyme-to-organism confidence, organism-ID alignment,
wastewater soft-trait policy, and Task 7 `not_applicable` contract have been
reconfirmed with explicit evidence paths. M4b/M4c remain locked unless Huang
laoshi separately authorizes implementation.

## Final 07-23/07-24 response and D4 soft decision — 2026-07-27

The complete item-by-item response is placed directly at repository root so
earlier completed work is not missed:

- [`M3_2026_07_23_24_TEACHER_TASK_LIST_FINAL_RESPONSE_2026-07-27.md`](M3_2026_07_23_24_TEACHER_TASK_LIST_FINAL_RESPONSE_2026-07-27.md)
- [`M3_NEXT_ROUND_HUANG_TEACHER_ADJUDICATION_REQUEST_AFTER_BIOLOGICAL_DECISIONS_2026-07-27.md`](M3_NEXT_ROUND_HUANG_TEACHER_ADJUDICATION_REQUEST_AFTER_BIOLOGICAL_DECISIONS_2026-07-27.md)

The biological meeting selected T1: retain all wastewater-relevant traits as
soft evidence for reference, advice, explanation and uncertainty. Traits do
not automatically delete microorganisms, and species/strain inheritance
remains forbidden.

- decision record, audit and hashes:
  [`2026-07-27_M3_D4_Wastewater_Trait_Soft_Policy_Decision/`](2026-07-27_M3_D4_Wastewater_Trait_Soft_Policy_Decision/)

The cross-side response is duplicated byte-for-byte in the enzyme
teacher-deliverables repository. Enzyme and microbe evidence assets remain
separated by repository. M4b and M4c remain locked.

## Historical pre-decision D4 material — 2026-07-27

The detailed T1/T2/T3 biological selection card, visual meeting version and
independent audits are retained as the evidence reviewed before the
2026-07-27 meeting:

- [`2026-07-27_M3_D4_Wastewater_Trait_Biological_Selection_Pending/`](2026-07-27_M3_D4_Wastewater_Trait_Biological_Selection_Pending/)

Status at the time of that package: T1/T2/T3 selection was pending. The current
T1 decision is recorded in the newer package above. Effective v1 behavior
remains all-soft and M4b/M4c remain locked.

## Current prerequisite status closure — 2026-07-26

The 2026-07-23 and 2026-07-24 teacher lists are closed item by item without
replacing earlier adjudications:

- teacher-facing status matrix:
  [`M3_P1_MICROBE_PREREQUISITES_EXISTING_DECISIONS_AND_STATUS_CLOSURE_2026-07-26.md`](M3_P1_MICROBE_PREREQUISITES_EXISTING_DECISIONS_AND_STATUS_CLOSURE_2026-07-26.md)
- byte-identical authority copies, local audit and SHA256 manifest:
  [`2026-07-26_M3_P1_Microbe_Prerequisites_Status_Closure/`](2026-07-26_M3_P1_Microbe_Prerequisites_Status_Closure/)

The resubmitted decisions show that v1 does not create an
`organism_confidence` float, D1--D8 are not wholly undecided, and only the D4
expert upgrade remains for the biological meeting. M4b/M4c remain locked.

## P0 current delivery: D5 new-contract reaudit — 2026-07-24

Combined index for the two teacher-defined P0 items (D5 and the original
2026-07-22 clarification bytes):

- [`M3_P0_PREREQUISITES_COMPLETION_INDEX_2026-07-24.md`](M3_P0_PREREQUISITES_COMPLETION_INDEX_2026-07-24.md)

The current teacher-facing D5 report does not rely on filename identity or
earlier acceptance. It explicitly audits the P0 Top-MRR enzyme-to-host chain,
five original metaTraits JSON bodies, four required real-sample checks and the
TaxID direct-query result:

- [`2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/metatraits_probe_report.md`](2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/metatraits_probe_report.md)
- [dated path index, ten-row crosswalk, independent audit and manifest](2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/)

Bounded decision: the data support soft-trait prototyping on the five sampled
hosts, but not hard filtering, exact strain attribution or production. The
documented TaxID API returned 404 for all ten P0-derived host tax IDs, so a
working production `organism_uid -> traits` path remains unresolved. The
explicit normalized result is `exact_strain=0`, `exact_species=0`,
`no_exact_match_established=10`; five rows retain species-name summaries only
as contextual soft evidence.

## Current Task 7 contract delivery — 2026-07-24

The teacher-authorized contract-only Task 7 delivery is placed directly at
repository root:

- [`TRAIT_VALUE_NOT_APPLICABLE_SCHEMA_CONTRACT.md`](TRAIT_VALUE_NOT_APPLICABLE_SCHEMA_CONTRACT.md)
- dated path index, independent audit, and SHA256 manifest:
  [`2026-07-24_Task7_TraitValue_Not_Applicable_Contract/`](2026-07-24_Task7_TraitValue_Not_Applicable_Contract/)

Status: student delivery; teacher acceptance not yet claimed. It defines the
`reason`/`note` contract and required `not_applicable` example without adding
Pydantic code, tests, `MicrobeTraitTool`, or M4b/M4c implementation.

## Current prerequisite resubmission — 2026-07-24

The P0 MT-D5 evidence requested by the 2026-07-24 supplement was originally
completed and independently audited on 2026-07-16, then accepted in
`TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md`.
It was not rerun. The accepted files are resubmitted byte-for-byte:

- report at repository root:
  [`metatraits_probe_report.md`](metatraits_probe_report.md);
- five raw sample JSON bodies, accepted package, source paths and audit:
  [`2026-07-24_MT_D5_Accepted_Evidence_Resubmission/`](2026-07-24_MT_D5_Accepted_Evidence_Resubmission/).

The dated folder README is the teacher-facing path index. Its hash manifest
proves that the report, five JSON bodies, deterministic tar, tar identity,
2026-07-16 audit and authority reference retain their original bytes.

## Current submission — 2026-07-23

Teacher-requested files are placed directly in the repository root:

- P0 Task 4: [`SNAPSHOT_CONTRACT_DRAFT.md`](SNAPSHOT_CONTRACT_DRAFT.md)
- Task 6 corrected unsent inquiry:
  [`METATRAITS_API_INQUIRY_EMAIL_DRAFT.md`](METATRAITS_API_INQUIRY_EMAIL_DRAFT.md)
- Delivery status and Task 7 decision request:
  [`METATRAITS_TASKS_4_6_AND_TASK7_DECISION_REQUEST_2026-07-23.md`](METATRAITS_TASKS_4_6_AND_TASK7_DECISION_REQUEST_2026-07-23.md)

Individual task audits and the final pre-submission audit are under
[`2026-07-23_MetaTraits_Tasks_4_6_and_Task7_Decision_Request/audits/`](2026-07-23_MetaTraits_Tasks_4_6_and_Task7_Decision_Request/audits/).
The submission hash manifest is
[`2026-07-23_MetaTraits_Tasks_4_6_and_Task7_Decision_Request/DELIVERABLE_SHA256SUMS.txt`](2026-07-23_MetaTraits_Tasks_4_6_and_Task7_Decision_Request/DELIVERABLE_SHA256SUMS.txt).

Tasks 4 and 6 were subsequently accepted by the teacher on 2026-07-23.
Task 7 was adjudicated as contract-only and was delivered on 2026-07-24 at
the root path listed above; live code and tests remain deferred to a future
separately authorized M4b. M4b and M4c remain unauthorized.

The 2026-07-21 folder and commit are retained unchanged as historical
evidence. Its nested snapshot has the same bytes as the current root
resubmission, but its email predates the project-name decision. Use the
root-level files as the current submission.
