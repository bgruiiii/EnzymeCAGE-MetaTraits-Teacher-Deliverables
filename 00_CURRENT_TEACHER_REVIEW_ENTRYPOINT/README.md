# 当前老师审阅入口（MetaTraits / 菌侧）

更新时间：2026-08-20
用途：给老师打开 GitHub 后的第一入口，避免从根目录历史散文件中自行判断最新状态。

## 1. 老师优先看哪些文件

| 优先级 | 内容 | 路径 |
|---|---|---|
| 1 | 2026-08-20 C8 主链路 staged-only 实装证据包：C8-0 至 C8-4 + 固定 30-row bounded rerun 已审计通过；C8-5 小型真实候选表 smoke 尚未完成 | [`../2026-08-20_M4b_C8_Staged_Implementation_Bounded_30_Rerun/`](../2026-08-20_M4b_C8_Staged_Implementation_Bounded_30_Rerun/) |
| 2 | 2026-08-20 C8-P porTraits 受控预检决策包：说明 Chenyu 做到哪里、当前堵塞和 D1-D7 待老师把关事项；未运行预测 | [`../2026-08-20_M4b_C8_P_porTraits_Preflight_Decision_Request/`](../2026-08-20_M4b_C8_P_porTraits_Preflight_Decision_Request/) |
| 3 | 2026-08-19 MetaTraits TSV 落晨羽 + C7-1 long-form mapping 修复包 | [`../2026-08-19_MetaTraits_Bulk_TSV_Landing_and_C7_1_Mapping_Correction/`](../2026-08-19_MetaTraits_Bulk_TSV_Landing_and_C7_1_Mapping_Correction/) |
| 4 | 2026-08-19 C8 TraitFilterLayer 实装方案 / 拆解待审 | [`../2026-08-19_M4b_C8_TraitFilterLayer_Implementation_Plan/`](../2026-08-19_M4b_C8_TraitFilterLayer_Implementation_Plan/) |
| 5 | C8 实装前新增口径问题：补资产来源 delta + porTraits preflight | [`../2026-08-19_M4b_C8_TraitFilterLayer_Implementation_Plan/pending_teacher_decisions/M4B_C8_PENDING_TEACHER_DECISIONS_RESCUED_SOURCES_AND_PORTRAITS_2026-08-19.md`](../2026-08-19_M4b_C8_TraitFilterLayer_Implementation_Plan/pending_teacher_decisions/M4B_C8_PENDING_TEACHER_DECISIONS_RESCUED_SOURCES_AND_PORTRAITS_2026-08-19.md) |
| 6 | 2026-08-19 真菌 observed-trait source exploration closure：解释为什么 C7-2 真菌继续 identity-only | [`../2026-08-19_M4b_C7_2_Fungal_Observed_Trait_Source_Exploration_Closure/`](../2026-08-19_M4b_C7_2_Fungal_Observed_Trait_Source_Exploration_Closure/) |
| 7 | 真菌 observed source 不足时，是否允许用细菌/古菌预测工具预测真菌：需先和师姐讨论 | [`../2026-08-19_M4b_C7_2_Fungal_Observed_Trait_Source_Exploration_Closure/pending_teacher_discussion/M4B_C7_2_FUNGAL_PREDICTION_TOOL_TRANSFER_DISCUSSION_2026-08-19.md`](../2026-08-19_M4b_C7_2_Fungal_Observed_Trait_Source_Exploration_Closure/pending_teacher_discussion/M4B_C7_2_FUNGAL_PREDICTION_TOOL_TRANSFER_DISCUSSION_2026-08-19.md) |
| 8 | 2026-08-18 C7-2 只读 schema/validator bounded 30 交付包 | [`../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/`](../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/) |
| 9 | C7-2 校验报告 | [`../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/TRAIT_FEATURE_ENCODING_VALIDATION_REPORT.md`](../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/TRAIT_FEATURE_ENCODING_VALIDATION_REPORT.md) |
| 10 | C7-2 边界报告 | [`../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/BOUNDARY_VALIDATION_REPORT.md`](../2026-08-18_M4b_C7_2_Schema_Validator_Bounded_30_Environment_Industrial_Bacteria/BOUNDARY_VALIDATION_REPORT.md) |
| 11 | 老师 2026-08-17 已冻结通过的 C7-2 feature encoding 提案 | [`../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/`](../2026-08-16_M4b_C7_2_Feature_Encoding_Proposal/) |
| 12 | 2026-08-14 C7-1 frozen trait panel 证据包 | [`../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/`](../2026-08-14_M4b_C7_1_Trait_Panel_Candidate/) |
| 13 | 2026-08-12 MetaTraits + BacDive 微生物侧性状/可获得性交付包 | [`../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/`](../2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/) |

## 2. 当前状态一句话

截至 2026-08-20，新增 C8 主链路 staged-only 实装证据包：C8-0 输入冻结、
C8-1 lookup index + 137 delta review、C8-2A UID-source expansion harness、
C8-3/C8-4 固定 30-row bounded rerun 均已审计通过。该包不代表 C8-5 已完成；
C8-5 的小型真实上游候选表 smoke 仍需等待上游候选表，不能用 4,681/1,704
harness 或 30 行 bounded 子集冒充真实候选酶。

截至 2026-08-20，新增 C8-P porTraits 受控预检决策包。该包不代表 porTraits
已经启动预测；目前只完成环境、输入、版本、资产、容器和配额预检。核心状态：
412 个 MetaTraits 未覆盖 bacteria/archaea 目标集合已确认且都有 assembly_accession；
428 真菌继续 identity-only；Nextflow 已安装，porTraits v0.2.1 路线支持
query_metatraits=none；但 Singularity/Apptainer、porTraits assets、eggNOG 来源、
SIF 镜像、tiny FASTA 授权和老师 D1-D7 裁定仍未闭合。

截至 2026-08-19，MetaTraits 12 个 bulk TSV 已落 Chenyu 并完成路径、清单、
SHA256、官方日期追溯；C7-1 与 MetaTraits long-form 字段映射已通过 rerun2
修正，8/8 负例断言 PASS。C8 TraitFilterLayer 已整理为实装方案 / 拆解待审，
仍为 staged-only，未接 production。

C8 实装前新增发现两个需老师裁定的问题：1,704 PASS 酶资产反查后出现 137 个
原 2,478 外 source_signature，建议先做 delta review、不静默扩库；MetaTraits
本地 TSV 对原 2,478 覆盖为 1,638/2,478，未覆盖 bacteria/archaea 如需预测，
建议另行授权 porTraits genome prediction preflight，fungi 本轮仍 identity-only。

真菌 observed-trait source exploration closure 已单独整理为本次新增包。当前
可审计来源 DSMZ/MediaDive/ATCC 只能覆盖少量探索行：any strict evidence
`78/575`，temperature `75/575`，pH `12/575`，salinity `0/575`，oxygen
`68/575`，culture collection accession `78/575`。因此本轮建议停止真菌
observed-source 深挖，继续保持 C7-2 真菌 identity-only；`575` 只是探索内部
行级分母，不替代 C7-2 老师口径真菌数 `428`。

如果后续想用面向细菌/古菌/原核的预测工具去补真菌性状，当前不建议直接执行。
这需要先和师姐/领域 reviewer 讨论工具训练域、out-of-domain 标注、是否只作
exploratory fallback，再单独请老师裁定；当前 C7-2 不使用此类真菌预测。

## 3. 本次关键结果

```text
MetaTraits Chenyu DATA_DIR: /usrdata/EnzymeCAGE_data/data/metatraits/incoming/metatraits_bulk_tsv_snapshot_20260818
MetaTraits required summary TSV: 12/12 present + gzip PASS
MetaTraits companion crosswalk: 2/2 present
MetaTraits official index last modified: 2026-06-10 10:23
C7-1 long-form mapping rerun2: trait_panel_rows_written=15/15
C7-1 false-positive assertions: 8/8 PASS
F3 pH false positives cleared: no Atmosphere / Morphology rows
F12 Gram false positives cleared: no gramicidin rows
Final clean microbe source universe: 2,478 source_signatures / 145,607 enzyme-source rows
MetaTraits coverage: 1,638 / 2,478 = 66.1%
BacDive validated species-or-better: 1,746 / 2,478 = 70.5%
BacDive exact_strain_main: 597 / 2,478 = 24.1%
BacDive hard exact strain: 555 / 2,478 = 22.4%
BacDive + MetaTraits both covered: 1,508 source_signatures
BacDive only: 238 source_signatures
MetaTraits only: 130 source_signatures
BacDive species-level representative expansion v2: 1,149 / 1,149 have at least one representative strain record and at least one culture collection number
MetaTraits all vs no_predictions: source coverage both 1,638 / 2,478; mean unique traits per covered source 156.8 vs 47.7
```

C8 方案拆分：

```text
C8-0 输入冻结与路径预检
C8-1 构建只读 trait lookup index
C8-2 候选 UID 到微生物来源展开
C8-3 生成 trait_annotation.jsonl
C8-4 validator 与边界报告
C8-5 bounded-to-full staged rollout
```

C7-1 冻结面板第一屏展示：

```text
temperature / pH / oxygen-anaerobic status / salinity / BacDive culture collection number
```

C7-2 8/18 bounded 30 中，10 个细菌第一屏五项覆盖：

```text
temperature observed: 10/10
pH observed: 5/10, predicted soft-fill: 5/10
oxygen / anaerobic observed: 10/10
salinity observed: 8/10, predicted soft-fill: 2/10
BacDive culture collection / availability observed: 10/10
```

古菌第一屏结果：BacDive availability 10/10 observed，MetaTraits 四项本地未观察。
真菌第一屏结果：本轮全部 identity-only，不做软补齐。

C7-1 明确删除：

```text
biosafety level 不进入 trait panel
```

## 4. 当前不能误写成完成的内容

```text
MetaTraits species-level trait 不等于 strain-level trait；
BacDive species-level representative strain record 不等于原始 UniProt exact strain；
BacDive exact-strain evidence 需要按 main / conservative / hard policy 分层；
真菌属于 BacDive non-scope，不应计为 BacDive 查询失败；
当前结果支持 schema 设计与后续实现，但不代表 M4b/M4c production pipeline 已经启动。
C7-2 feature encoding 已被老师 2026-08-17 冻结为设计契约；
8/18 schema/validator 包是只读 bounded staged 子集验证，仍不代表 production 实装；
C8 目前是方案 / 拆解待审，不代表已经实装；
2,478 source staged status table 尚未生成；
prediction-like traits 只能按老师冻结边界软补齐并显式标注，不写成 production 主特征。
```

## 5. 为什么根目录仍保留历史文件

根目录中保留了若干历史提交文件，是为了不破坏已经发给老师的旧 GitHub 链接。当前审阅请优先看本文件夹、仓库顶层 README 的 2026-08-12 入口，以及本次新增交付包。
