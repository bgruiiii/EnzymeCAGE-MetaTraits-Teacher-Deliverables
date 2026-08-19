# C8 实装前新增口径问题：补资产来源与 porTraits 预测分支

日期：2026-08-19

对象：黄老师审阅；陈浩然侧主线 + 微生物侧

状态：待老师裁定。本文只提出 C8 实装前需要明确的两个口径问题，不主张已经并入新增来源，不主张已经启动 porTraits 预测，不接 production。

## 1. 本文要请老师裁定什么

在整理 C8 TraitFilterLayer staged-only 实装方案时，额外发现两个需要提前说清楚的问题：

1. 4,681 缺 pocket UID 中已有 1,704 个补成 PASS staged 酶资产，这批新可用酶反查到的微生物来源，是否要并入当前 C8 微生物来源名单；
2. 当前本地 MetaTraits 查询表只能覆盖原 2,478 微生物来源中的 1,638 个，剩余未覆盖来源是否需要走 porTraits 基因组性状预测分支。

这两个问题都会影响后续 C8 的 denominator 和 trait evidence 标注方式，因此建议在正式实装前请老师裁定。

## 2. 问题一：补资产后牵出的微生物来源是否并入 C8

### 2.1 已确认事实

当前老师已验收的酶资产结果为：

```text
4,681 UID denominator
1,704 PASS_AFDB_P2RANK_PREDICTED_POCKET_D4_LOADER
1,324 BLOCKED_AFDB_P2RANK_NO_POCKET
1,650 BLOCKED_AFDB_STRUCTURE_FETCH_FAILED
3 BLOCKED_ESM2_3B_EXTRACTION_FAILED
```

原微生物侧已整理的 clean universe 为：

```text
2,478 source_signatures
taxonomy scope = bacteria + archaea + fungi
MetaTraits coverage = 1,638 / 2,478
BacDive species-or-better coverage = 1,746 / 2,478
```

本地重新交叉检查 1,704 PASS UID 与微生物来源映射后，得到：

```text
1,704 PASS UID
962 UID-source mapping rows
500 unique source_signatures
363 source_signatures inside original 2,478 universe
137 source_signatures outside original 2,478 universe
```

137 个 2,478 外来源按 taxonomy group 分布：

```text
bacteria: 88
archaea: 6
fungi: 43
```

按 UID 口径看：

```text
753 PASS UID only map to sources inside original 2,478 universe
209 PASS UID only map to sources outside original 2,478 universe
742 PASS UID have no local uid-to-source mapping in the checked table
```

### 2.2 这说明什么

白话解释：

```text
补资产救回来的是酶资产。
这些酶资产有一部分能反查到微生物来源。
其中大部分可映射来源已经在原 2,478 微生物来源名单里，
但也确实出现了 137 个原 2,478 之外的新 source_signature。
```

因此，不能简单写成：

```text
补资产后所有对应微生物都应自动进入 C8。
```

也不能忽略这 137 个新增来源，因为它们可能影响后续 candidate-to-microbe 覆盖。

### 2.3 建议口径

建议把原 2,478 继续作为当前 C7/C8 已审计的主 universe，不静默改 denominator。

同时新增一个 staged-only delta review：

```text
C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW
```

该表只做清点和标注，不直接并入生产或主训练资产：

```text
source_signature
taxonomy_group
mapped_pass_uid_count
inside_original_2478_universe
metatraits_local_snapshot_covered
bacdive_closure_available_if_checked
recommended_status = PENDING_TEACHER_DECISION
```

### 2.4 需要老师裁定

请老师决定：

1. C8 第一轮 staged rollout 的 denominator 是否保持原 2,478 microbe source universe；
2. 137 个 2,478 外 rescued-asset-linked source_signature 是否先作为 delta review 单独提交；
3. 若老师同意扩入，是否作为 C8 v1.1 staged universe，而不是改写原 2,478 历史口径。

## 3. 问题二：MetaTraits 未覆盖来源是否启动 porTraits 预测

### 3.1 已确认事实

原 2,478 微生物来源中，MetaTraits 本地 snapshot 覆盖为：

```text
1,638 / 2,478 = 66.1%
```

按 taxonomy group 看：

```text
bacteria: 1,575 / 1,897
archaea: 63 / 153
fungi: 0 / 428
```

MetaTraits `all` 表包含 prediction-like 信息，`no_predictions` 表排除 prediction-like 信息。前期审计显示：

```text
ncbi_species_summary_all.tsv.gz: covered 1,638 / 2,478
ncbi_species_summary_no_predictions.tsv.gz: covered 1,638 / 2,478
```

也就是说，prediction-like 记录主要增加已覆盖物种的 trait 数量，没有把 2,478 中未覆盖的来源变成已覆盖。

### 3.2 porTraits 是什么

porTraits 不是我们新引入的一条自创路线，也不是简单调用 MetaTraits 在线 API。
给老师汇报时建议表述为：MetaTraits 官方体系里的 porTraits genome prediction
branch，而不是 EnzymeCAGE 另找的新工具。

更准确地说：

```text
porTraits 是 MetaTraits 官方生态中的 genome annotation / phenotype prediction workflow。
它用微生物基因组 FASTA 或 MAG FASTA 作为输入，
通过多个 genome-based predictors 预测微生物表型性状。
```

官方 porTraits 集成的主要预测器包括：

```text
BacDive-AI
GenomeSPOT
Traitar
MICROPHERRET
```

因此它和当前 C8 的本地 MetaTraits TSV 查询不是同一层：

```text
MetaTraits local TSV lookup
= 查已有数据库记录

porTraits genome-based prediction
= 用基因组重新预测性状
```

### 3.3 porTraits 与 MetaTraits API 的关系

前期核查显示，porTraits 的核心预测流程可以和 MetaTraits 在线 context query 分开。

关键点：

```text
porTraits 的 query_metatraits 参数默认值为 none。
当 query_metatraits = none 时，workflow 不依赖在线 MetaTraits context query 才能运行核心预测。
```

也就是说：

```text
MetaTraits API 不稳定
不等于 porTraits genome-based prediction 一定不能跑。
```

但这也不表示 C8 当前已经可以直接启用 porTraits，因为 porTraits 需要另行准备计算环境和输入资产。

### 3.4 porTraits 需要什么输入和环境

porTraits 不能只靠 UniProt ID、TaxID 或 species name 预测。

它需要：

```text
genome FASTA / MAG FASTA
```

本地或 HPC 运行还需要：

```text
Nextflow
Docker 或 Singularity
BacDive-AI models
GenomeSPOT models
MICROPHERRET assets
Traitar assets
reCOGnise marker genes
GTDB-Tk database
eggNOG database
PFAM assets
```

因此如果要对 MetaTraits 未覆盖来源使用 porTraits，需要先确认：

```text
1. 对应 bacteria / archaea 是否有可用 genome FASTA；
2. Chenyu 或本地是否已有 porTraits workflow 与模型数据库；
3. query_metatraits=none 的最小 smoke test 是否能产生四类 predictor 输出；
4. 输出是否能写入 C7/C8 允许的 trait schema，并标注为 predicted。
```

### 3.5 真菌边界

当前 porTraits v1 官方描述面向 prokaryotic genomes。

因此本轮不能把 fungi 直接放入 porTraits v1：

```text
bacteria / archaea:
可在老师授权后做 porTraits prediction preflight

fungi:
本轮仍保持 identity-only
不使用 porTraits v1 预测
```

这与 C7-1 / C7-2 中“真菌本轮 identity-only”的老师冻结口径一致。

### 3.6 建议口径

建议 C8 v1 不自动启动 porTraits。

C8 v1 先按已冻结规则执行：

```text
observed first
本地 MetaTraits TSV lookup
BacDive 只补身份 / 保藏编号 / 可获得性相关证据
允许 predicted soft-fill 的字段只在已有授权范围内标注
真菌 identity-only
staged-only
```

对 MetaTraits 未覆盖的 bacteria / archaea，建议另开一个受控 preflight：

```text
C8-P / porTraits Genome Prediction Preflight
```

该 preflight 只做：

```text
只读环境核查
只读 genome FASTA 可获得性核查
query_metatraits=none smoke test
小样本 phenotype prediction
输出 staged-only prediction evidence
不写 production
不替换 observed
不把 predicted 写成实验事实
```

### 3.7 需要老师裁定

请老师决定：

1. 当前 C8 是否先保持 local MetaTraits TSV + BacDive closure 的只读查询路线；
2. 对 MetaTraits 未覆盖的 bacteria / archaea，是否授权单独启动 porTraits preflight；
3. porTraits 预测输出是否仅作为 `source_type=porTraits_genome_prediction` 的 staged predicted evidence；
4. fungi 是否继续保持 identity-only，等待另行 fungal-specific evidence branch。

## 4. 建议写入给老师的简短反馈

建议向老师说明：

```text
另有两个 C8 实装前需要请老师裁定的口径问题：

第一，4,681 缺 pocket UID 经 P2Rank/AFDB staged 流程救回 1,704 个 PASS 酶资产后，
反查当前本地 uid-to-source 映射，得到 500 个唯一 source_signature，其中 363 个
落在原 2,478 微生物 universe 内，另有 137 个在原 2,478 外。我们建议不静默改写
原 2,478 口径，而是先生成 rescued-asset-linked source delta review，请老师裁定
是否扩入 C8 staged universe。

第二，MetaTraits 本地 TSV 对原 2,478 source_signature 的覆盖仍为 1,638/2,478。
MetaTraits all 表中的 prediction-like 信息增加的是已覆盖来源的 trait 密度，
没有扩大 source 覆盖。对剩余未覆盖的 bacteria/archaea，如老师同意，建议另开
porTraits genome prediction preflight。porTraits 属于 MetaTraits 官方生态中的
genome annotation / phenotype prediction workflow，不是我们自创新路线；它以
genome/MAG FASTA 为输入，可设置 query_metatraits=none 与在线 MetaTraits context
query 解耦。但本轮不建议自动启用，且 fungi 仍保持 identity-only。
```

## 5. 本文不主张的内容

本文不主张：

```text
已经把 137 个新增 source_signature 并入 C8；
已经改变原 2,478 微生物 universe 的历史统计口径；
已经启动 porTraits；
已经对 MetaTraits 未覆盖来源完成预测；
已经对真菌做 porTraits 预测；
已经把 predicted 当成 observed；
已经接 production；
已经修改 production D4 或 production pool。
```

## 6. 证据来源

本地证据文件：

```text
custom/github_upload/EnzymeCAGE-Teacher-Deliverables/
  2026-08-14_M4_E2_Full_4681_Staged_Status_Table/
    tables/FULL_4681_STAGED_STATUS_TABLE.csv

data/processed/rhea/2026-01-21/microbe/
  taxonomy_filter_2026-04-28/
    uid_to_source_keep_bacteria_fungi_archaea.csv

custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/
  2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/
    01_metatraits_species_coverage/source_signature_metatraits_coverage.csv
    02_bacdive_full_closure/bacdive_metatraits_overlap_by_source_signature.csv

custom/docs/enzyme_feature_expansion/
  ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/
    00_Authority_Teacher_Plan/
      PORTRAITS_OFFICIAL_WORKFLOW_API_DECOUPLING_CODEX_CORRECTION_2026-08-18.md
      TEACHER_REPLY_FULL_4681_ACCEPTANCE_AND_C7_1_FREEZE_2026-08-14.md
      TEACHER_REPLY_C7_2_FREEZE_AND_1650_ACCESSION_REVIEW_2026-08-17.md
      TEACHER_REPLY_NEXT_ACTIONS_2026-08-18.md
```
