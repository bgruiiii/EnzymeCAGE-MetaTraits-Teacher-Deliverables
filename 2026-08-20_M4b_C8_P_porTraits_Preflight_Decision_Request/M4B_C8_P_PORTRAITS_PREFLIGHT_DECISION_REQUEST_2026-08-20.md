# M4b C8-P porTraits Preflight Decision Request

Date: 2026-08-20

Status:

```text
TEACHER_DECISION_REQUEST
C8-P_PREFLIGHT_COMPLETED_AS_METADATA_AND_ENVIRONMENT_EXPLORATION
NO_PORTRAITS_PREDICTION_EXECUTED
NO_PRODUCTION_MUTATION
```

## 1. 这件事为什么出现

C8 v1 的主路线已经由老师 2026-08-19 批准为 staged-only 实装：observed-first，
优先使用本地 MetaTraits TSV lookup；BacDive 只补身份 / 保藏编号 / 可获得性；
允许的 predicted soft-fill 仍受 C7-2 冻结边界限制；真菌本轮 identity-only。

在 C8 方案审查中，老师同时裁定：

```text
C8 v1 不自动启动 porTraits。
如需推进 MetaTraits 未覆盖 bacteria / archaea，先交 C8-P porTraits Genome Prediction Preflight 方案。
porTraits 输出如后续被授权，只能作为 staged-only prediction evidence。
source_type = porTraits_genome_prediction。
不写 production，不替换 observed，不把 predicted 写成实验事实。
真菌 428 株继续 identity-only，不使用 porTraits v1。
```

因此我们没有把 porTraits 混入 C8 主线，而是单独开了 C8-P 受控预检分支。

## 2. C8-P 问的窄问题

C8-P 只问一个窄问题：

```text
对原 2,478 微生物主 universe 中，本地 MetaTraits 未覆盖的 bacteria / archaea，
是否具备后续用 porTraits 做 staged-only genome prediction evidence 的条件？
```

C8-P 不问：

```text
是否现在全量补齐所有微生物性状；
是否对真菌做 porTraits v1 预测；
是否用 prediction 替代 observed evidence；
是否把 prediction 写进 production；
是否产生 hard filter / trait_score / 未校准 confidence；
是否预测 F5 culture collection number。
```

## 3. 数据分母和目标集合

沿用已审计主分母：

```text
original C8 microbe universe = 2,478 source_signatures
target_bacteria = 1,897
target_archaea = 153
target_fungi = 428
MetaTraits covered = 1,638 / 2,478
```

C8-P 目标只取 MetaTraits 未覆盖的原核微生物：

```text
bacteria uncovered = 322 / 1,897
archaea uncovered = 90 / 153
C8-P bacteria/archaea targets = 412
fungi excluded identity-only = 428
```

Chenyu C8-P1 回包和本地审计确认：

```text
412 / 412 have assembly_accession
0 duplicate target source_signature
0 fungal target rows
0 / 412 local genome FASTA found
```

解释：

```text
数据侧目标集合是清楚的；如果老师后续批准 tiny smoke，输入可以从 assembly_accession
出发下载或转移极小 genome FASTA 样本。但当前没有下载 FASTA，也没有运行预测。
```

## 4. 我们按顺序做了什么

### C8-P0：路径契约和任务拆解

我们先写了 C8-P path contract，明确：

```text
只做 bacteria / archaea；
真菌 identity-only；
保持 2,478 主分母；
不静默改 denominator；
不运行 full prediction；
不接 production；
每个 Chenyu 回包必须先本地审计再进入下一步。
```

### C8-P1：Chenyu 环境和输入预检

目的：

```text
检查 Chenyu 是否具备 porTraits 代码、Nextflow、容器、资产、目标集合、genome FASTA 条件。
```

结果：

```text
数据目标集合 PASS：322 bacteria + 90 archaea = 412
真菌排除 PASS：428 identity-only
assembly_accession PASS：412/412
本地 genome FASTA：0/412
Nextflow：缺失
容器运行时：缺失
porTraits 资产：10/10 categories missing
本地 v0.1.7：不支持 query_metatraits=none
```

本地审计结论：

```text
C8_P1_COMPLETE_BUT_NOT_READY_FOR_PORTRAITS_SMOKE
```

### C8-P2A：能先解决的运行时和版本问题

目的：

```text
在不跑 porTraits、不下载数据库、不下载 genome FASTA、不拉容器的前提下，
尝试解决 Nextflow 和 query_metatraits=none 版本路线。
```

结果：

```text
Nextflow resolved: user-space 24.10.5 build 5935
porTraits official main commit 945795b / manifest 0.2.1 found
v0.2.1 supports query_metatraits=none and default is none
container runtime still missing
porTraits assets still 0/10
genome FASTA still absent
teacher approval still needed for v0.1.7 -> v0.2.1
```

本地审计结论：

```text
C8_P2A_PARTIAL_PASS_NEXTFLOW_AND_VERSION_RESOLVED_NOT_READY_FOR_SMOKE
```

### C8-P2B：资产、容器、配额准备预检

目的：

```text
只做 metadata-only 部署计划：官方资产 URL、大小、配额、拟议目录、容器镜像清单、
管理员问题和老师决策清单。
```

结果：

```text
porTraits-DB: confirmed, 1.32 GB, Zenodo MD5
reCOGnise markers: confirmed, 974 MB, Zenodo MD5
GTDB-Tk r220: confirmed, 101 GB compressed
eggNOG 5.0.2 / PFAM: 4 URLs metadata failed, server empty reply
estimated compressed downloads: ~152 GB
estimated decompressed/on-disk: ~294 GB
/usrdata available: 159 TB
container image refs: 10 unique images identified from v0.2.1 code
local reusable assets: 0/10 found
container runtime: still absent
```

本地审计结论：

```text
PASS_AS_METADATA_ONLY_PREFLIGHT_PACKAGE
NOT_READY_FOR_PORTRAITS_SMOKE
```

## 5. 当前哪些事情已经清楚

### 已经清楚 1：目标集合可以定义

C8-P 不再是模糊的“缺多少补多少”。它有明确分母和边界：

```text
只针对 412 个 MetaTraits-uncovered bacteria / archaea。
不包含 428 fungi。
不改变 2,478 主 universe 历史口径。
```

### 已经清楚 2：v0.1.7 不适合当前路线

本地旧快照 v0.1.7 不支持 `query_metatraits=none`，并且会调用 MetaTraits 在线
API；这不符合我们本轮“不依赖在线 MetaTraits API”的要求。

### 已经清楚 3：v0.2.1 是可行版本路线，但需要老师批准

官方 main commit `945795b5a6577f881c451f292eb3a60d94d33eed` 的 manifest version
为 `0.2.1`，代码中支持 `query_metatraits=none`，默认也是 `none`。

但截至本次审计：

```text
GitHub 没有 v0.2.1 tag/release；
CHANGELOG 尚未写到 v0.2.1；
因此不能擅自把它当作已冻结 release 使用。
```

建议老师把它作为单独版本选择裁定。

### 已经清楚 4：空间不是主要瓶颈

`/usrdata` 有 159 TB 可用，估算 porTraits assets + SIF 约 294 GB 解压后空间。
因此主要问题不是配额，而是授权、下载源、容器运行时和资产准备。

## 6. 当前主要堵塞

### B1. 容器运行时缺失

```text
singularity: not found
apptainer: not found
docker: not found
module: not found
```

porTraits 依赖容器运行各个 process。没有 Singularity/Apptainer 或可用 HPC
module 时，不能进入 workflow smoke。

### B2. porTraits 必需资产缺失

本机搜索结果：

```text
metatraits_models: not found
BacDive-AI models: not found
GenomeSPOT models: not found
MICROPHERRET: not found
Traitar: not found
reCOGnise marker genes: not found
GTDB-Tk database: not found
eggNOG database: not found
PFAM mapping: not found
container SIF images: not found
```

### B3. eggNOG 5.0.2 来源还没闭合

porTraits v0.2.1 README 仍指向 eggNOG `emapperdb-5.0.2`。P2B 对 4 个 eggNOG /
PFAM URL 做 HEAD 元数据检查时均得到 empty reply。

这可能是：

```text
服务器临时不可用；
服务器不支持 HEAD；
下载 host 已迁移；
需要使用镜像或改用受控下载命令验证。
```

在老师未批准下载前，我们没有尝试真正下载。

### B4. 容器镜像尚未准备

P2B 从 v0.2.1 代码识别出 10 个唯一镜像，涉及 `ghcr.io`、`quay.io` 和
`registry.git.embl.org`。其中 EMBL registry 可能需要认证；GHCR registry API
可能需要 token；实际 SIF pull/build 仍需 Singularity/Apptainer。

### B5. Tiny genome FASTA smoke 尚未授权

C8-P1 已证明 412/412 有 assembly_accession，但本地 0/412 FASTA。后续如果要
smoke，只建议极小 bacteria/archaea 样本，并需老师或用户明确授权下载/转移。

## 7. 现在能不能推进下一步

不能直接进入 porTraits smoke 或 phenotype prediction。

可以推进的是：

```text
C8-P3: 请老师审定 D1-D7 后，再决定是否进入资产/容器准备和 tiny smoke。
```

如果老师批准 D1-D7，下一步才是受控执行：

```text
1. 管理员/HPC 提供 Singularity 或 Apptainer；
2. 下载或转移 porTraits-DB、reCOGnise markers、GTDB-Tk r220、eggNOG 5.0.2、PFAM；
3. 准备 10 个 SIF；
4. 只下载极小 bacteria/archaea FASTA smoke 输入；
5. 运行 C8-P4 tiny smoke；
6. smoke 通过后，再另行请老师决定是否做小样本 phenotype prediction。
```

如果老师不批准 v0.2.1 或资产下载，则 C8-P 暂停或关闭；C8 v1 继续按 observed-first
本地 MetaTraits TSV + BacDive identity/availability 路线推进。

## 8. 请求老师裁定

请老师重点把关：

```text
D1 是否允许使用 porTraits official main commit 945795b / manifest 0.2.1；
D2 是否由管理员/HPC 提供 Singularity 或 Apptainer；
D3 是否允许下载或转移 porTraits-DB / reCOGnise / GTDB-Tk r220 / eggNOG 5.0.2 / PFAM；
D4 是否允许准备 10 个 OCI-to-SIF 容器；
D5 是否允许后续 tiny bacteria/archaea FASTA smoke；
D6 是否确认资产目录 /usrdata/EnzymeCAGE_data/databases/portraits/v0.2.1/；
D7 是否确认所有红线继续有效：真菌 identity-only、不接 production、不替代 observed、
   不 hard reject、不输出 trait_score、不输出未校准 confidence、不预测 F5。
```

学生侧建议：

```text
若老师认可 C8-P 继续探索，建议先批准 D1-D4 + D6，用于受控资产/容器准备；
D5 tiny FASTA smoke 可作为单独开关，等运行时和核心资产准备完成后再执行；
D7 作为 C8-P 全程红线确认。
```

## 9. 本包不包含什么

```text
不包含 genome FASTA；
不包含 GTDB / eggNOG / PFAM / porTraits-DB / reCOGnise 大数据库；
不包含 container SIF 或 OCI layers；
不包含 phenotype prediction 结果；
不包含 production D4 / production pool / formal asset mutation；
不包含真菌预测。
```

## 10. 结论

C8-P 已完成“能不能准备 porTraits”的受控预检：数据侧目标集合明确，Nextflow 与
v0.2.1 版本路线已有解决方案，空间足够；但实际运行前仍缺容器运行时、资产下载、
eggNOG 来源闭合、SIF 准备和 tiny FASTA 授权。

因此本次提交不是预测结果，而是请求老师决定是否允许进入下一阶段受控准备。
