# porTraits v0.2.1 官方代码、依赖资产、HPC/Apptainer 与输出语义核查

- **核查日期**：2026-08-20
- **核查对象**：`grp-bork/porTraits`
- **重点版本**：官方 GitHub `main` 中标记为 `0.2.1` 的 commit `945795b5a6577f881c451f292eb3a60d94d33eed`
- **对照版本**：GitHub tag `v0.1.7`（2025-08-11）
- **证据优先级**：porTraits 官方 GitHub 代码/README/Tags > 官方 Zenodo/GTDB/metaTraits/Apptainer 文档 > 第三方体量测量
- **重要说明**：截至本次核查，GitHub **没有 `v0.2.1` tag/release**。因此本文中的“porTraits v0.2.1”特指官方 `main` 分支中 `manifest.version = "0.2.1"` 的代码状态，而不是一个已经打 tag 的正式 GitHub release。

---

## 一、最重要的结论先说

### 1. `query_metatraits=none`：官方 v0.2.1 代码明确支持，而且默认就是 `none`

这件事可以明确回答为 **是**。

官方 `nextflow_schema.json` 在 v0.2.1 commit 中把 `query_metatraits` 定义为：

```text
enum = ["none", "NCBI", "GTDB", "both"]
default = "none"
```

官方 `nextflow.config` 同样写着：

```text
query_metatraits = "none"
```

而 `main.nf` 中只有当：

```text
params.query_metatraits && params.query_metatraits != "none"
```

时，才进入 metaTraits reference query 部分。

因此，`query_metatraits=none` 不是我们自己猜出来的 workaround，而是 **v0.2.1 官方代码级支持的合法参数值**。

但是必须同时注意：

> **`query_metatraits=none` 只关闭“向 metaTraits 查询相似/相关参考记录”的步骤，不关闭 porTraits 的本地核心预测流程。**

GTDB-Tk、reCOGnise、GenomeSPOT、eggNOG-mapper、MICROPHERRET、BacDive-AI、Traitar 在当前 `main.nf` 中仍然会执行。

---

### 2. v0.2.1 的版本状态很特殊：代码已经是 0.2.1，但官方还没有 v0.2.1 tag/release/changelog

官方 commit：

```text
945795b5a6577f881c451f292eb3a60d94d33eed
commit message: version -> v0.2.1
```

该 commit 做了两类关键更新：

1. `manifest.version`：`0.2.0 -> 0.2.1`
2. reCOGnise container：切换到 `ghcr.io/grp-bork/recognise:v0.8.0`
3. GenomeSPOT container：切换到 `registry.git.embl.org/schudoma/genomespot-docker:v1.0.1plus`

但官方 Tags 页面截至 2026-08-20 只看到：

- `v0.2.0`
- `v0.1.17`
- `v0.1.7`

**没有 `v0.2.1` tag。**

官方 `CHANGELOG.md` 当前也只写到：

```text
VERSION 0.2.0
```

所以最严谨的表述是：

> porTraits 官方 `main` 分支已经在 2026-05-22 的 commit `945795b...` 中将内部版本升为 `0.2.1`，并明确支持 `query_metatraits=none`；但截至 2026-08-20 尚未发布对应的 `v0.2.1` Git tag/release，CHANGELOG 也尚未增加 0.2.1 条目。

---

## 二、13 个问题逐项核查

---

## 1. porTraits v0.2.1 相比 v0.1.7 新增了哪些必需文件、模块、assets？

这里要区分两层：

- **v0.2.1 相对 v0.2.0 本身**：主要是 reCOGnise 与 GenomeSPOT 容器更新。
- **v0.1.7 → 当前 v0.2.1 代码状态**：中间跨过了 v0.2.0，结构变化明显。

### v0.1.7 根目录

官方 v0.1.7 tag 的根目录主要只有：

```text
bin/
docs/
portraits/modules/
.gitignore
CHANGELOG.md
LICENSE
README.md
main.nf
nextflow.config
nextflow_schema.json
```

### v0.2.1 当前代码新增的重要结构

至少新增：

```text
assets/
config/
.github/workflows/
```

其中真正与运行/结果解释直接相关的是：

```text
assets/
├── traits_harmonized.json
├── traits_info.json
└── versions.json

config/
└── params.yml
```

此外模块侧新增了：

```text
portraits/modules/collate.nf
```

`bin/` 中增加了用于新流程的脚本，包括：

```text
collate_results.py
metatraits_comm.py
```

### 为什么这些 assets 不能随便漏掉？

v0.2.1 的结果汇总 `collate_results` 会读取：

```text
assets/traits_info.json
assets/traits_harmonized.json
assets/versions.json
```

它们分别承担：

- **traits_info.json**：给统一 trait 添加 category / group / ontology 等元数据；
- **traits_harmonized.json**：把各预测工具自己的 trait 名称映射到统一 trait；
- **versions.json**：记录模型来源版本，当前官方文件中包括：
  - BacDive-AI：`a1bef3e`
  - GenomeSPOT：`1.0.1`
  - MICROPHERRET：`fd21931`
  - Traitar：`8bd7d86`

因此，如果只拿 v0.1.7 风格的几个 `.nf` 和模型目录去拼 v0.2.1，很容易在最后的 harmonization/collation 阶段缺资产。

### v0.2.0 changelog 已明确记录的结构性变化

官方 CHANGELOG 对 v0.2.0 写明：

- fixed NCBI-based metaTraits reference queries
- fixed output bug in PFAM2Traitar
- made GTDB-Tk `--mash_db` optional internally
- process outputs prefixed with genome ID
- cleaned/limited outputs
- added metaTraits GTDB queries
- **added result collation**
- **added reference data files to repo**
- **added toggle for metaTraits reference queries**
- updated documentation

所以，v0.1.7 到 v0.2.1 的大部分“新必需结构”实际上是在 v0.2.0 阶段加入的，v0.2.1 再更新容器版本。

**结论：不能把 v0.2.1 当成 v0.1.7 的简单版本号升级；运行包需要同时带上新的 `assets/`、`config/params.yml`、collation 模块和相关脚本。**

---

## 2. 官方推荐运行方式是 Docker、Singularity 还是 Apptainer？HPC 是否有官方说明？

官方 README 原文语义非常明确：

> porTraits requires a docker/singularity installation as all dependencies are served via Docker containers.

因此官方明确写到的是：

- **Docker**
- **Singularity**

没有在当前 porTraits README/参数文档中看到官方直接使用 **Apptainer** 这个名称。

### 当前默认配置实际偏向 Docker

`nextflow.config` 当前写着：

```text
docker {
    enabled = true
}
```

并且各 process 使用的是：

- `ghcr.io/...`
- `quay.io/...`
- `registry.git.embl.org/...`

等 Docker/OCI registry 镜像。

所以：

> **porTraits 官方发布形态本质上是 OCI/Docker 容器；Singularity 是官方认可的运行时，但官方仓库并没有给出一套独立的 `.sif` 发布包。**

### 官方有没有专门 HPC 教程？

本次核查没有在官方仓库中找到：

- Slurm profile
- PBS profile
- HPC-specific config
- Apptainer profile
- 集群作业提交示例
- 官方 HPC deployment guide

官方提供的运行入口主要是：

1. CloWM 云端 GUI
2. Nextflow CLI

因此，“HPC 能不能跑”答案是 **能，Nextflow + Singularity/Apptainer 本身非常适合 HPC**，但这是运行时生态能力；**porTraits 项目本身目前没有一份专门的 HPC 运维说明。**

---

## 3. porTraits 所需 `metatraits_models` 官方下载地址、体量、目录结构是什么？

### 官方下载地址

官方 `config/params.yml` 明确给出：

```text
https://zenodo.org/records/16818976/files/porTraits-DB.tar.gz
```

官方 README 对应的 porTraits database Zenodo DOI 为：

```text
10.5281/zenodo.16818976
```

### 官方要求的目录结构

`params.yml` 直接给了模板：

```text
/path/to/metatraits_models
├── Bacdive-AI
│   └── models
├── GenomeSPOT
│   └── models
├── MICROPHERRET
└── Traitar
```

然后：

```yaml
metatraits_models: "/path/to/metatraits_models"
```

### 主流程实际访问的路径

`main.nf` 中分别使用：

```text
${metatraits_models}/GenomeSPOT/models
${metatraits_models}/MICROPHERRET
${metatraits_models}/BacDive-AI/models
${metatraits_models}/Traitar/
```

### ⚠️ HPC 部署必须注意：BacDive-AI 目录大小写存在官方文件间不一致

官方 `config/params.yml` 的目录示例写成：

```text
Bacdive-AI/models
```

但 v0.2.1 `main.nf` 的实际运行路径写成：

```text
BacDive-AI/models
```

Linux/HPC 文件系统通常区分大小写，因此如果严格照 `params.yml` 建成 `Bacdive-AI/`，运行到 BacDive-AI process 时可能出现路径不存在。**执行端应以 `main.nf` 实际消费路径 `BacDive-AI/models` 为准**；若已经按示例解压成 `Bacdive-AI/`，应在 smoke 前统一重命名或建立受控软链接，并记录该兼容处理。

### 体量

本次能够从 porTraits 官方 GitHub 确认下载文件和 Zenodo record，但 **GitHub README/params.yml 本身没有标注 `porTraits-DB.tar.gz` 文件大小**；当前网页索引也没有可靠返回该 Zenodo record 的文件 size metadata。

因此这里不能凭空写一个 GB 数。

**严谨结论：**

- 下载地址：已官方确认；
- 目录结构：已官方确认；
- 精确压缩包体量：**本次未从可检索的官方页面独立核实，不建议把非官方猜测写进部署预算。**

实际部署时应在能访问 Zenodo 的节点上先读取 Content-Length / Zenodo API metadata，再决定 scratch/quota。

---

## 4. `metatraits_models` 里是否包含 BacDive-AI、GenomeSPOT、MICROPHERRET、Traitar 全部模型？

**是。官方 `params.yml` 明确要求这 4 套目录全部放在 `metatraits_models` 根目录下。**

即：

| predictor | 官方期望位置 |
|---|---|
| BacDive-AI | `Bacdive-AI/models` |
| GenomeSPOT | `GenomeSPOT/models` |
| MICROPHERRET | `MICROPHERRET` |
| Traitar | `Traitar` |

这里容易产生一个误区：

README 说 **GenomeSPOT is run from scratch**，这不等于“GenomeSPOT 不需要模型资产”。

当前 `main.nf` 仍把：

```text
${metatraits_models}/GenomeSPOT/models
```

显式传给 GenomeSPOT process。

所以针对 v0.2.1 的部署，四套资产都应准备。

---

## 5. reCOGnise marker genes 官方下载地址、体量、版本要求是什么？

### 官方下载

porTraits `params.yml` 指向：

```text
https://zenodo.org/records/17916463/files/recognise_markers.tar.gz
```

### Zenodo 官方记录

- Dataset：**reCOGnise specI identification marker gene database**
- Version：**v1**
- 文件：`recognise_markers.tar.gz`
- 文件大小：**1.0 GB**
- DOI：`10.5281/zenodo.17916463`

### porTraits v0.2.1 使用的 reCOGnise 软件版本

v0.2.1 commit 把容器明确改成：

```text
ghcr.io/grp-bork/recognise:v0.8.0
```

因此最稳妥的配套写法是：

```text
reCOGnise software container: v0.8.0
marker database: Zenodo Version v1
```

本次没有找到官方声明“marker DB v1 仅能与 reCOGnise v0.8.0 使用”的更严格版本锁定说明，所以不要把它写成强制一一绑定关系；只能说这是 v0.2.1 官方当前组合。

---

## 6. GTDB-Tk 数据库需要哪个 release？v0.2.1 默认还是 release220 吗？体量多少？

### 是，v0.2.1 仍明确使用 release220

有三重证据：

1. README：
   ```text
   GTDB (r220)
   ```
2. `nextflow_schema.json`：
   ```text
   gtdbtk_data default = "GTDB/release220"
   ```
3. 当前 porTraits 容器：
   ```text
   gtdbtk:2.4.1
   ```

所以虽然截至 2026 年 GTDB 已经有更新 release，**porTraits v0.2.1 官方工作流仍固定围绕 r220。**

### 官方 r220 GTDB-Tk 数据包大小

GTDB 官方下载目录显示：

```text
gtdbtk_r220_data.tar.gz
101.04G
```

因此 HPC 上至少要按 **约 101 GB 压缩下载体量**来预算。

GTDB-Tk 官方文档通常还会提示解压后的实际数据库空间更大；因此建议不要只按 101 GB 给 quota。

### 是否可以擅自换 release226 / release232？

GTDB-Tk 2.4.1 本身可能兼容比 r220 更新的版本，但 **porTraits 自己的 metaTraits taxonomy mapping/context 与官方文档仍围绕 r220**。

所以如果目标是“严格复现 porTraits v0.2.1”，应使用：

```text
GTDB release220
```

而不是因为 GTDB 有新版本就直接替换。

---

## 7. eggNOG-mapper 数据库需要哪个版本？默认路径里的 5.0.2 是否仍适用于 v0.2.1？体量多少？

### v0.2.1 官方 README 仍然明确写 `emapperdb-5.0.2`

当前 README 给出的下载项是：

```text
http://eggnog6.embl.de/download/emapperdb-5.0.2/eggnog.db.gz
http://eggnog6.embl.de/download/emapperdb-5.0.2/eggnog_proteins.dmnd.gz
http://eggnog6.embl.de/download/emapperdb-5.0.2/eggnog.taxa.tar.gz
http://eggnog6.embl.de/download/emapperdb-5.0.2/pfam.tar.gz
```

当前容器则是：

```text
quay.io/biocontainers/eggnog-mapper:2.1.12--pyhdfd78af_2
```

因此：

> **对于 porTraits v0.2.1，`emapperdb-5.0.2` 仍然是官方 README 指定的数据库目录版本。**

### 体量

porTraits 官方 README 没有给这几个文件标 size。

一个 2026 年的独立复现实验给出的实测量级约为：

- `eggnog.db.gz`：约 **6.3 GB** 压缩，约 **39 GB** 解压
- `eggnog_proteins.dmnd.gz`：约 **4.8 GB** 压缩，约 **8.7 GB** 解压
- `eggnog.taxa.tar.gz`：约 **71 MB**
- 三者解压总磁盘约 **48 GB**
- **尚未计入 PFAM archive**

这些只能作为 **部署预算参考**，不是 porTraits 官方声明的 size。

### 一个现实风险：下载域名可能变化

近年的 eggNOG-mapper 社区 issue 中出现过旧下载 host 失效/迁移的问题，因此：

- “数据库版本仍是 5.0.2”与
- “README 中某个具体 hostname 今天一定可下载”

不是同一件事。

应优先保持 **DB release=5.0.2**，下载 host 如有 404 再核对 eggNOG 官方当前镜像，不要自行换数据库大版本。

---

## 8. PFAM clan/map 文件包含在 eggNOG DB 里，还是需要单独下载？

答案要精确区分：

### 它不在 `eggnog.db` 这个单一文件里面

porTraits README 把 PFAM 作为一个单独 archive 下载：

```text
pfam.tar.gz
```

因此不能只下载：

```text
eggnog.db.gz
eggnog_proteins.dmnd.gz
eggnog.taxa.tar.gz
```

就认为 PFAM 准备完了。

### 但它可以放在同一个 eggNOG database 根目录中

porTraits 默认要求：

```text
${eggnog_db}/pfam/Pfam-A.clans.tsv.gz
```

官方 `params.yml` 还明确提示：

- 在 `eggnog_db` 下准备 `pfam/`
- 下载 `Pfam-A.clans.tsv.gz`
- 或者通过 `pfam_clade_map` 指向已有 copy

所以最准确的说法是：

> **PFAM 数据属于 porTraits eggNOG/PFAM 功能注释资源的一部分，但它是独立文件/独立 archive，不是包含在主 `eggnog.db` 文件内部。**

部署时必须确认最终存在：

```text
/path/to/eggnog_db/pfam/Pfam-A.clans.tsv.gz
```

---

## 9. porTraits 官方容器镜像列表有哪些？是否提供 `.sif`/Singularity 镜像，还是只能从 Docker/OCI 拉？

v0.2.1 `nextflow.config` 中可以整理出 **8 个不同的 OCI image reference**：

| 用途 | 官方当前 image |
|---|---|
| reCOGnise | `ghcr.io/grp-bork/recognise:v0.8.0` |
| GTDB-Tk | `quay.io/biocontainers/gtdbtk:2.4.1--pyhdfd78af_1` |
| GenomeSPOT | `registry.git.embl.org/schudoma/genomespot-docker:v1.0.1plus` |
| eggNOG-mapper | `quay.io/biocontainers/eggnog-mapper:2.1.12--pyhdfd78af_2` |
| emapper2matrix / MICROPHERRET | `registry.git.embl.org/schudoma/portrait_sklearn:v1.2.2_micropherret` |
| BacDive-AI / Traitar | `registry.git.embl.org/schudoma/portrait_sklearn:v.1.4.0_traitar_bacdive` |
| metaTraits NCBI/GTDB query | `registry.git.embl.org/schudoma/portraits_metatraits:latest` |
| result collator | `registry.git.embl.org/schudoma/portraits_metatraits:with_pandas` |

### 是否有官方 `.sif`？

当前 v0.2.1 配置中：

- 没有 `.sif` 路径；
- 没有 `.sif` release assets；
- 没有列出一套专门 Singularity image 下载表；
- 实际引用的是 GHCR / Quay / EMBL registry 的 OCI/Docker images。

值得注意的是，在 v0.2.1 commit 中 reCOGnise 原先有一条 `oras://...recognise-singularity...` 被注释掉，改成了 GHCR OCI image。

因此当前官方方向很清楚：

> **上游发布 OCI/Docker image；Singularity/Apptainer 需要从 OCI registry 拉取并转换/缓存为 SIF。**

---

## 10. Apptainer 无 root 环境能否直接拉并运行这些镜像？是否需要管理员开启 user namespace / setuid？

### 通常可以，无需用户 root

Apptainer 官方文档明确支持：

```bash
apptainer pull docker://...
apptainer run docker://...
```

而且会把 OCI layers 转换为 SIF。

例如：

```bash
apptainer pull recognise_v0.8.0.sif \
  docker://ghcr.io/grp-bork/recognise:v0.8.0
```

以及：

```bash
apptainer pull gtdbtk_2.4.1.sif \
  docker://quay.io/biocontainers/gtdbtk:2.4.1--pyhdfd78af_1
```

普通用户一般不需要 Docker daemon，也不需要 root。

### 但是“无 root”不等于“完全不依赖管理员配置”

现代 Apptainer 的非 setuid 模式依赖 Linux **unprivileged user namespaces**。

因此有两种典型 HPC 情形：

#### 情形 A：集群允许 unprivileged user namespace

普通用户可以正常使用系统安装好的 Apptainer：

```text
pull OCI -> SIF
run SIF
```

通常不需要额外 root 权限。

#### 情形 B：集群禁用了 unprivileged user namespace

那非-setuid Apptainer 无法正常完成某些容器操作。

需要管理员选择受支持的部署方式，例如：

- 配置/启用 user namespaces；或
- 安装/启用 Apptainer 的 setuid-root 组件。

### 是否必须使用 `--fakeroot`？

**跑 porTraits 并不天然需要 `--fakeroot`。**

如果只是拉取并运行公开 OCI image，正常的非 root Apptainer 流程即可。

所以给 HPC 管理员的问题应该是：

```text
1. 集群是否已经安装 Apptainer？
2. 是否允许普通用户运行 SIF？
3. 是否启用了 unprivileged user namespaces，或采用了 setuid Apptainer？
4. 计算节点能否访问 ghcr.io / quay.io / registry.git.embl.org？
5. 如果不能联网，是否允许登录节点预拉 SIF 后复制到共享文件系统？
```

---

## 11. v0.2.1 能否只跑极小 FASTA smoke，并跳过 GTDB-Tk / eggNOG 等重型模块？

### 输入层面：可以给很小的 FASTA 文件

porTraits 接受：

```text
fna
fasta
fa
fna.gz
fasta.gz
fa.gz
```

所以“极小 FASTA”在文件类型上不是问题。

### 流程层面：官方没有提供跳过 GTDB-Tk / eggNOG 的开关

这是最关键的地方。

当前 `main.nf` 按顺序直接调用：

```text
GTDB-Tk
reCOGnise
GenomeSPOT
eggNOG-mapper
emapper2matrix
MICROPHERRET
BacDive-AI
Traitar
collate_results
```

只有：

```text
metaTraits reference query
```

被 `query_metatraits` 包在条件分支里。

当前 schema 中没有找到类似：

```text
skip_gtdbtk
skip_eggnog
skip_genomespot
skip_prediction
light_mode
smoke_mode
```

这样的官方参数。

### 所以结论是

> **v0.2.1 没有官方“轻量 smoke 模式”。`query_metatraits=none` 不是跳重型模块开关。**

如果不准备 GTDB r220 / eggNOG / reCOGnise / model assets，完整 workflow 依然会因为核心 process 缺数据库而失败。

### 推荐怎么做 smoke？

如果目标是“验证 HPC 环境能否真的跑 porTraits”，最可靠的 smoke 不是造一个十几 bp 的假 FASTA，而是：

- 取一个**很小但真实、完整度足够的细菌基因组 FASTA**；
- `query_metatraits=none`，避免依赖 metaTraits 在线查询；
- 仍把全部本地数据库/模型/容器准备好；
- 用单 genome 验证端到端流程。

如果只是想先验证某一个 container 能不能启动，应独立做 container-level smoke；这属于部署测试，不是 porTraits 官方 workflow 的“skip 模式”。

---

## 12. porTraits 输出中哪些文件对应我们关心的 F1-F4/F6-F8，字段语义是什么？

### 首先说明：porTraits 官方没有名为 `F1`、`F2` … `F8` 的字段

这些 F 编号显然是我们项目内部的 trait 编码，不是 porTraits 原生 schema。

因此不能在没有项目 F-code 定义表的情况下，凭直觉把：

```text
F1 -> temperature
F2 -> pH
...
```

硬写死。

正确做法应该是根据 porTraits 的标准化 `feature` 名称建立 crosswalk。

### v0.2.1 最重要的统一结果文件

```text
collated/portraits_results.tsv.gz
```

这是四个 genome-based predictor 的 harmonized 结果汇总。

如果启用 metaTraits context query，还可能有：

```text
collated/metatraits_gtdb.tsv.gz
collated/metatraits_ncbi.tsv.gz
```

如果：

```text
query_metatraits=none
```

那么后两类 metaTraits context 表不要求产生；核心本地预测结果仍是：

```text
portraits_results.tsv.gz
```

### `portraits_results.tsv.gz` 的核心字段

从官方 `collate_results.py` 可以确认统一字段包括：

| 字段 | 含义 |
|---|---|
| `feature` | harmonized 后的标准 trait 名，是我们做 F-code 映射最重要的键 |
| `category` | trait 大类 |
| `group1` | 一级分组 |
| `group2` | 二级分组 |
| `ontology` | 对应 ontology 信息 |
| `trait_link` | metaTraits 中该 trait 的链接 |
| `tool` | 产生该预测的工具，如 `genomespot`、BacDive-AI、MICROPHERRET、Traitar |
| `tool_version` | 工具/模型版本 |
| `tool_feature` | 原预测工具自己的 trait 名 |
| `genome` | 输入 genome ID |
| `value_probability` | 预测得分/概率或 GenomeSPOT 的连续输出值 |
| `value_binary` | 二值结果；是否存在要看具体工具/trait |
| `gtdb` | 汇总时可合并的 GTDB lineage |
| `speci` | reCOGnise/specI taxonomy 结果 |

### 不同 predictor 的 `value_probability/value_binary` 不能完全按同一个统计含义理解

#### BacDive-AI / MICROPHERRET / Traitar

官方 collator 会读取：

```text
*.prob.tsv.gz
*.binary.tsv.gz
```

并写入：

```text
value_probability
value_binary
```

所以它们明确同时保留连续预测得分和二值预测。

#### GenomeSPOT

GenomeSPOT 原始输出结构不同。

porTraits 会把 GenomeSPOT 的值统一放进：

```text
value_probability
```

但这里并不意味着所有 GenomeSPOT 数值都严格等价于 sklearn classifier 的 probability。

其中 oxygen 被官方代码做了特殊处理，并基于 0.5 得到 `value_binary`；其他连续生理性状可能没有对应的 binary。

### 如何映射 F1-F4/F6-F8？

建议项目内建立一张显式 mapping：

```text
project_feature_code | portraits_feature | accepted_tool | value_type | unit/meaning
```

例如：

```text
F? | <exact porTraits feature name> | BacDive-AI/GenomeSPOT/... | probability/binary/continuous | ...
```

**不要按输出行号映射，也不要按 predictor 自己的 `tool_feature` 直接硬编码；应优先用 harmonized `feature`。**

> 本次网页核查无法恢复你们内部 F1-F4/F6-F8 的具体定义，因此本文不虚构 F-code 对应关系。只要把内部 F-code 定义表交给执行端，就可以基于 `feature` 精确建立 crosswalk。

---

## 13. porTraits 预测结果是否有概率/二值输出？能否标 `source_type=porTraits_genome_prediction`，不当 observed 用？

### 有概率/得分，也有二值输出

对于 BacDive-AI、MICROPHERRET、Traitar：

```text
*.prob.tsv.gz
*.binary.tsv.gz
```

会被官方汇总为：

```text
value_probability
value_binary
```

GenomeSPOT 也会进入统一 `value_probability` 字段，但其连续变量语义需要按 GenomeSPOT trait 本身解释；oxygen 另有 binary 转换。

### 可以，而且应该明确标成 prediction

metaTraits 官方自己就明确把数据源分成：

```text
Culture-based
Prediction-based
```

Prediction-based 部分明确列出：

- BacDive-AI
- GenomeSPOT
- MICROPHERRET
- Traitar

metaTraits 文档还说明：

- AI/prediction data 与实验观测必须能区分；
- taxonomy summary 中的 percentage 是记录/预测的比例，**不是 confidence score**；
- individual record view 保留 source provenance 和 prediction context。

所以在我们自己的数据模型中增加：

```text
source_type = porTraits_genome_prediction
```

是非常合理且必要的。

甚至建议进一步保留：

```text
source_type = porTraits_genome_prediction
prediction_tool = BacDive-AI | GenomeSPOT | MICROPHERRET | Traitar
prediction_tool_version = ...
prediction_value = ...
prediction_binary = ...
observed = false
```

### 注意：`source_type` 不是 porTraits 官方原生字段

porTraits 自己输出的是：

```text
tool
tool_version
value_probability
value_binary
```

所以：

```text
source_type=porTraits_genome_prediction
```

属于我们下游数据治理新增的 provenance 字段。

但是它完全符合官方对 **prediction-based vs culture-based** 的分类原则。

### 最关键的数据治理规则

建议明确规定：

```text
porTraits genome prediction != observed phenotype
```

因此：

- 不得把 porTraits prediction 填入实验观测值字段；
- 不得在 downstream ranking 中标为 `observed=true`；
- 如果 observed 数据和 prediction 同时存在，应保留两条来源或明确 source priority；
- probability/score 也不能直接解释成“实验可信度”。

---

# 三、HPC 部署时真正需要准备的资产清单

## A. 工作流代码

建议锁定：

```text
repo: https://github.com/grp-bork/porTraits
commit: 945795b5a6577f881c451f292eb3a60d94d33eed
manifest version: 0.2.1
```

不要只写“latest”，否则后续 main 改动会破坏复现。

---

## B. porTraits predictor models

```text
https://zenodo.org/records/16818976/files/porTraits-DB.tar.gz
```

最终目录：

```text
metatraits_models/
├── Bacdive-AI/
│   └── models/
├── GenomeSPOT/
│   └── models/
├── MICROPHERRET/
└── Traitar/
```

---

## C. reCOGnise marker DB

```text
https://zenodo.org/records/17916463/files/recognise_markers.tar.gz
```

官方 Zenodo 文件：

```text
Version: v1
Size: 1.0 GB
```

---

## D. GTDB-Tk database

严格复现 porTraits v0.2.1：

```text
GTDB release220
gtdbtk_r220_data.tar.gz
compressed size: 101.04G
```

---

## E. eggNOG-mapper 5.0.2

官方 README 要求：

```text
eggnog.db.gz
eggnog_proteins.dmnd.gz
eggnog.taxa.tar.gz
pfam.tar.gz
```

并确保：

```text
${eggnog_db}/pfam/Pfam-A.clans.tsv.gz
```

存在。

---

## F. 容器

至少准备当前 `nextflow.config` 中引用的 8 个 OCI image references。

如果 HPC compute node 不能访问公网，建议在允许联网的登录节点/数据传输节点一次性：

```text
OCI -> SIF
```

再把 SIF 放到共享只读 container cache。

---

# 四、推荐的 v0.2.1 “离线预测、不查 metaTraits”参数原则

核心逻辑：

```yaml
query_metatraits: "none"

metatraits_models: "/shared/db/portraits/metatraits_models"
recognise_marker_genes: "/shared/db/portraits/recognise_markers"
gtdbtk_data: "/shared/db/GTDB/release220"
eggnog_db: "/shared/db/eggnog/emapperdb-5.0.2"
```

并确保：

```text
pfam_clade_map =
/shared/db/eggnog/emapperdb-5.0.2/pfam/Pfam-A.clans.tsv.gz
```

### 这套配置能跳过什么？

能跳过：

```text
metaTraits NCBI/GTDB online/reference query
```

### 不能跳过什么？

仍会跑：

```text
GTDB-Tk
reCOGnise
GenomeSPOT
eggNOG-mapper
MICROPHERRET
BacDive-AI
Traitar
collate_results
```

因此它应该被称为：

> **no-metaTraits-reference-query mode**

而不是：

> lightweight mode / minimal mode / no-database mode

---

# 五、资源预算：哪些数字是官方，哪些不是

| 资源 | 版本 | 体量 | 证据等级 |
|---|---|---:|---|
| reCOGnise marker DB | v1 | **1.0 GB** | Zenodo 官方 |
| GTDB-Tk data | r220 | **101.04 GB 压缩包** | GTDB 官方 |
| eggNOG `eggnog.db.gz` | 5.0.2 | ~6.3 GB 压缩 | 2026 第三方复现实测，非 porTraits 官方 |
| eggNOG proteins | 5.0.2 | ~4.8 GB 压缩 | 2026 第三方复现实测，非 porTraits 官方 |
| eggNOG taxonomy | 5.0.2 | ~71 MB | 2026 第三方复现实测，非 porTraits 官方 |
| eggNOG 三项解压 | 5.0.2 | ~48 GB | 第三方实测，未计 PFAM |
| porTraits-DB | Zenodo 16818976 | **本次未从官方索引核实** | 不应猜测 |
| PFAM archive | 5.0.2 | **本次未核实** | 不应猜测 |

**部署时的最大资产明显是 GTDB r220；即便只有一个 genome smoke，也必须能访问这套数据库，因为官方流程没有 skip GTDB-Tk。**

---

# 六、对我们当前落地最有价值的判断

## 1. `query_metatraits=none` 可以放心用

它是官方 schema 的合法值，且默认就是 none。

因此如果 metaTraits API/网页当前不可用，**porTraits 的本地 genome trait prediction 路线本身仍然有官方代码路径**，并不要求必须成功访问 metaTraits reference query。

但前提是本地重型数据库和四类模型全部到位。

## 2. 当前真正的 HPC 瓶颈不是 metaTraits API，而是本地资源准备

主要是：

```text
GTDB r220
eggNOG 5.0.2 + PFAM
reCOGnise markers
porTraits-DB
8 类 OCI image references
```

## 3. Apptainer 是合理的 HPC 运行方案，但不是 porTraits README 明写的第三种官方模式

最严谨表述：

> porTraits 官方写 Docker/Singularity；Apptainer 作为 Singularity 社区后继、HPC 常用 OCI/SIF runtime，可以按照 Apptainer 官方机制拉取这些 Docker/OCI images，但这属于运行环境适配，不是 porTraits 仓库提供的专门 Apptainer profile。

## 4. porTraits 的结果必须保留“预测”身份

建议我们自己的最终数据表显式增加：

```text
source_type=porTraits_genome_prediction
observed=false
```

并保留：

```text
tool
tool_version
value_probability
value_binary
```

这样就不会和 BacDive / DSMZ / CBS 等实验观测数据混在一起。

---

# 七、推荐给 Codex/HPC 执行端的检查清单

- [ ] checkout 固定 commit `945795b5a6577f881c451f292eb3a60d94d33eed`
- [ ] 确认 `nextflow.config` manifest version 为 `0.2.1`
- [ ] 确认 schema 中 `query_metatraits` enum 包含 `none`
- [ ] 使用 `query_metatraits=none`
- [ ] 不把 `none` 误认为 skip GTDB/eggNOG
- [ ] 准备 porTraits-DB 四套模型目录
- [ ] 准备 reCOGnise marker DB v1
- [ ] 准备 GTDB r220
- [ ] 准备 eggNOG `emapperdb-5.0.2`
- [ ] 确认 `pfam/Pfam-A.clans.tsv.gz` 存在
- [ ] 将 8 个 OCI image references 逐一做 `apptainer pull` 测试
- [ ] HPC 禁止公网时预拉 `.sif`
- [ ] 用一个真实的小型细菌 genome 做端到端 smoke
- [ ] 检查 `collated/portraits_results.tsv.gz`
- [ ] 检查 `value_probability` / `value_binary`
- [ ] 下游增加 `source_type=porTraits_genome_prediction`
- [ ] 下游增加 `observed=false`
- [ ] 用 `feature` 字段与项目 F1-F4/F6-F8 做显式 crosswalk，不按行号映射

---

# 八、官方与高优先级来源

## porTraits 官方

1. Repository  
   https://github.com/grp-bork/porTraits

2. v0.2.1 version bump commit  
   https://github.com/grp-bork/porTraits/commit/945795b5a6577f881c451f292eb3a60d94d33eed

3. v0.2.1 `nextflow.config`  
   https://github.com/grp-bork/porTraits/blob/945795b5a6577f881c451f292eb3a60d94d33eed/nextflow.config

4. v0.2.1 `nextflow_schema.json`  
   https://github.com/grp-bork/porTraits/blob/945795b5a6577f881c451f292eb3a60d94d33eed/nextflow_schema.json

5. v0.2.1 `main.nf`  
   https://github.com/grp-bork/porTraits/blob/945795b5a6577f881c451f292eb3a60d94d33eed/main.nf

6. v0.2.1 `config/params.yml`  
   https://github.com/grp-bork/porTraits/blob/945795b5a6577f881c451f292eb3a60d94d33eed/config/params.yml

7. v0.2.1 `collate_results.py`  
   https://github.com/grp-bork/porTraits/blob/945795b5a6577f881c451f292eb3a60d94d33eed/bin/collate_results.py

8. v0.2.1 `collate.nf`  
   https://github.com/grp-bork/porTraits/blob/945795b5a6577f881c451f292eb3a60d94d33eed/portraits/modules/collate.nf

9. Tags  
   https://github.com/grp-bork/porTraits/tags

10. CHANGELOG  
    https://github.com/grp-bork/porTraits/blob/945795b5a6577f881c451f292eb3a60d94d33eed/CHANGELOG.md

11. v0.1.7 tree  
    https://github.com/grp-bork/porTraits/tree/v0.1.7

## porTraits / reCOGnise databases

12. porTraits model archive  
    https://zenodo.org/records/16818976/files/porTraits-DB.tar.gz

13. reCOGnise marker database  
    https://zenodo.org/records/17916463

## GTDB

14. GTDB release220 GTDB-Tk full package  
    https://data.gtdb.ecogenomic.org/releases/release220/220.0/auxillary_files/gtdbtk_package/full_package/

15. GTDB releases  
    https://data.gtdb.ecogenomic.org/releases/

## metaTraits

16. metaTraits documentation  
    https://metatraits.embl.de/documentation

17. metaTraits paper / workflow description  
    https://pmc.ncbi.nlm.nih.gov/articles/PMC12807735/

## Apptainer

18. Docker/OCI support  
    https://apptainer.org/docs/user/latest/docker_and_oci.html

19. User namespaces / rootless deployment  
    https://apptainer.org/docs/admin/main/user_namespace.html

20. `apptainer pull`  
    https://apptainer.org/docs/user/main/cli/apptainer_pull.html

---

# 九、最终裁定表

| 问题 | 裁定 |
|---|---|
| v0.2.1 支持 `query_metatraits=none`？ | **是，代码明确支持，且默认 none** |
| 有正式 v0.2.1 tag/release？ | **截至 2026-08-20 没有** |
| changelog 写到 v0.2.1？ | **没有，只写到 0.2.0** |
| none 会跳过 metaTraits 在线 query？ | **是** |
| none 会跳过 GTDB-Tk？ | **不会** |
| none 会跳过 eggNOG？ | **不会** |
| none 会跳过四类 phenotype predictor？ | **不会** |
| `metatraits_models` 含四个 predictor？ | **是，官方 params.yml 明确列四个目录** |
| GTDB 默认 r220？ | **是** |
| eggNOG DB 仍是 5.0.2？ | **是，当前 v0.2.1 README 仍指定** |
| PFAM 是否只靠 eggnog.db 即可？ | **否，需单独 PFAM archive/file，并放到 eggNOG DB 树中** |
| 官方有预制 `.sif` 列表？ | **未发现；当前配置引用 OCI/Docker registry images** |
| Apptainer 普通用户可拉 OCI？ | **可以，前提是集群 Apptainer/user namespace或setuid配置允许** |
| 有官方 skip-heavy smoke mode？ | **没有发现** |
| 结果有 probability/binary？ | **有，具体语义按 predictor 区分** |
| 可标 `porTraits_genome_prediction`？ | **可以且推荐，但这是我们新增 provenance 字段** |
| 可当 observed phenotype？ | **不应当** |

