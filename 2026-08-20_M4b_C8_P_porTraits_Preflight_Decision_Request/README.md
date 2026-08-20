# 2026-08-20 M4b C8-P porTraits Preflight Decision Request

本目录是给黄老师审阅的 C8-P porTraits 受控预检总结包。

## 老师优先阅读

1. 主决策说明：
   [`M4B_C8_P_PORTRAITS_PREFLIGHT_DECISION_REQUEST_2026-08-20.md`](M4B_C8_P_PORTRAITS_PREFLIGHT_DECISION_REQUEST_2026-08-20.md)
2. D1-D7 待裁定清单：
   [`pending_teacher_decisions/C8_P_TEACHER_DECISION_CHECKLIST_D1_D7_2026-08-20.md`](pending_teacher_decisions/C8_P_TEACHER_DECISION_CHECKLIST_D1_D7_2026-08-20.md)
3. 证据索引：
   [`evidence_index/C8_P_PORTRAITS_PREFLIGHT_EVIDENCE_INDEX_2026-08-20.md`](evidence_index/C8_P_PORTRAITS_PREFLIGHT_EVIDENCE_INDEX_2026-08-20.md)

## 一句话结论

我们已按老师 2026-08-19 裁定，把 C8-P porTraits 单独拆成受控 preflight 路线。
目前只完成环境、输入、版本、资产、容器和配额预检；**没有运行 porTraits，没有
运行 Nextflow workflow，没有下载 genome FASTA / 数据库 / 容器，没有产生任何
phenotype prediction，也没有写入 production**。

当前 C8-P 数据侧可行，执行侧未就绪：

```text
目标范围：MetaTraits 未覆盖 bacteria 322 + archaea 90 = 412
真菌：428，继续 identity-only，不进入 porTraits v1
assembly_accession：412/412 present
本地 genome FASTA：0/412
Nextflow：已装 user-space 24.10.5
porTraits：官方 main commit 945795b / manifest 0.2.1 支持 query_metatraits=none
容器运行时：Singularity / Apptainer / Docker / module 均缺失
porTraits 资产：0/10 本地可复用
资产 URL 元数据：3/7 confirmed，4/7 eggNOG server failed
空间：/usrdata 159 TB available，估算需要约 294 GB 解压后空间
```

## 目前请求老师把关

请老师审定是否允许进入下一阶段的受控准备，而不是默认启动预测：

```text
D1 是否允许使用 porTraits 官方 main commit 945795b / manifest 0.2.1
D2 Singularity / Apptainer 由管理员安装、HPC module 提供，还是暂缓
D3 是否允许下载或转移 porTraits-DB / reCOGnise / GTDB-Tk r220 / eggNOG 5.0.2 / PFAM assets
D4 是否允许准备 10 个 OCI-to-SIF 容器镜像
D5 是否允许后续只下载极小 bacteria/archaea genome FASTA smoke 输入
D6 是否确认资产目录建议为 /usrdata/EnzymeCAGE_data/databases/portraits/v0.2.1/
D7 是否再次确认 fungi identity-only、无 production、无 hard rejection、无 trait_score、无 F5 prediction
```

## 包内结构

```text
authority_reference/       老师 08-19 裁定、C8-P 路径契约、porTraits 官方依赖审计
audits/                    三轮 prompt / Chenyu 回包的本地审计
evidence_index/            本包证据路径索引
hpc_archives/              三轮 Chenyu 小回包 tar.gz
hpc_identity/              三轮 Chenyu 回包 identity.txt
pending_teacher_decisions/ D1-D7 待裁定清单
prompts/                   三轮 Chenyu executor-only prompt
checksums/                 本交付包文件清单与 SHA256
```

## 当前边界

```text
staged-only preflight
不接 production
不改 production D4
不改 production pool
不写 trait_annotation
不做全量 rollout
不做真菌 porTraits v1
不预测 F5
不输出 trait_score / hard rejection / 未校准 confidence
不把 predicted evidence 写成 observed experimental fact
```
