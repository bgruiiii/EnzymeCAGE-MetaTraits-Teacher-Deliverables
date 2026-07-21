# MetaTraits M4a Current Teacher Review And Decision Request Draft

Date: 2026-07-21

Status: `DRAFT_NOT_SENT_M4A_EXECUTABLE_EVIDENCE_READY_FOR_TEACHER_REVIEW`

Scope: working scaffold for the later consolidated teacher submission. Current
M4a executable implementation, offline tests and M4a-4 benchmark evidence have
been locally audited. Full closure is still teacher-dependent for the explicit
review/decision items below. M4b and M4c authorization is not presumed.

## Suggested Message To Teacher

黄老师您好。按照您对 MT-D5 和 MT-D1-D8 的裁定，我们已完成并严格审计
M4a 当前可执行的 `Enzyme2OrganismTool`、`OrganismAggregator`、离线测试
和 M4a-4 联调补测证据：
10 个 UID、UniProt reviewed 主证据、KEGG 0/1/N 独立补充、稀疏样本保留、
无 confidence float、默认按支持酶数量降序和 NCBI taxon ID 升序排序均已
通过；100 次 warm、2/4 并发和 EnzymeCAGE-in-ADRMATS 进程显存证据已
完成并通过本地审计；M4b/M4c 尚未启动。结合后续预检和我们主动进行的
数据粒度复核，拟请您审阅或裁定以下事项：

1. 请明确 M4a smoke 中 A、B、C 三种 `OrganismAggregator` 对照列各自的
   完整公式、输入字段和稳定 tie-break。早期框架与最新回复对 B/C 名称的
   含义不一致，且早期 A 依赖当前已废止的 confidence float，因此我们没有
   自行补写公式。当前 v1 默认排序保持不变。

   需要特别向您披露并请您确认：您在 MT-D3 原文中写的是
   "supporting-enzyme 数量降序 + UID 升序 tie-break"。我们在已验收实现中
   将这里的候选 UID 操作化为生产主键 `NCBI taxon ID`，因此当前
   `OrganismAggregator` 实际是按 supporting-enzyme 数量降序，再按 numeric
   NCBI taxon ID 升序排序。这样做的依据是您同时裁定 "生产主键：NCBI
   taxon ID"；但如果您这里的 UID 指的是 enzyme UID、另一种 organism
   candidate UID 字符串，或需要别的 tie-break，请您明确，我们会按您的裁定
   修正实现和 smoke 对照表。
2. M4a-4P 对固定 ADRMATS commit 和晨宇部署的静态核查均只发现远程
   DashScope 模型，没有发现其他本地 ADRMATS GPU checkpoint 或加载入口。
   请确认原要求中“与 ADRMATS 其他模型共存时的显存峰值”如何闭环：是将
   “不存在额外本地模型”作为 unavailable/not-applicable 边界，并仅报告
   EnzymeCAGE-in-ADRMATS 进程显存，还是由您指定一个确切的本地模型集合、
   checkpoint 和加载方式。我们不会把零额外模型写成共存 PASS。
3. 我们在复核 UniProt 宿主与 metaTraits 性状数据粒度时主动发现一个口径问题。
   这不是本次运行任务的报错，也不表示现有 M4a 宿主映射错误。UniProt reviewed
   UID 可能对应具体菌株，例如 Q8EFP8 对应 *Shewanella oneidensis* MR-1、
   NCBI taxon `211586`；但按 species name 查询 metaTraits 时，实际返回了
   `211586` 和 species taxon `70863` 两种粒度。不同菌株的性状和目标酶存在性
   都不能假定一致，因此请确认后续规则：

   当前已验收的 M4a 结构化输出只保留 reviewed UniProt 的 organism name、NCBI
   taxon ID、lineage、annotation score、protein existence 和原始响应 hash；原始
   UniProt fixture 中虽可追溯 Proteomes/RefSeq 等 cross-reference，但
   proteome/assembly 尚未进入当前输出 schema。M4a 也未运行 porTraits，且按当前
   授权不得运行。我们不会把这些可考虑的后续增强误写成已实现能力。

   - 是否只有与 UniProt 宿主 NCBI taxon ID 精确相同的记录才能作为该候选的
     直接性状证据；
   - exact taxon 无记录时，species 汇总和同物种其他菌株记录是否只能作为
     背景证据并标记 `taxonomy_scope_mismatch/unknown`，不得直接过滤或排序；
   - 若要把同物种其他菌株作为新候选，是否必须先对该具体菌株独立证明目标酶
     存在，再使用其对应性状，而不能仅因性状更合适就替换原菌株。

   我们建议采用上述保守方案：exact-tax-ID 优先；无精确记录则保留原产酶宿主、
   性状记为不确定；不在未经酶存在性验证的菌株之间做选择。
4. 请审阅并批准或修改 `SNAPSHOT_CONTRACT_DRAFT.md`，重点包括官方版本字段、
   更新频率、许可展示、本地路径、hash 校验和 experimental fallback 切换条件。
5. 请审阅 `METATRAITS_API_INQUIRY_EMAIL_DRAFT.md`，确认收件人、署名、是否保留
   EnzymeCAGE 项目名及问题措辞；当前邮件尚未发送，也未声称已联系维护方。
6. M4a-4BAAAA 已提供并通过本地审计：100 次 warm、concurrency 2/4、
   305 条调用行和 6917 条显存采样均可重算，且继承的科学证据未改字节。
   请基于该证据裁定最终 checkpoint 加载策略；在您裁定前，我们仍只按您
   先前指定的 A，即启动时预加载，作为当前默认。

我们已对老师原文要求与当前验收实现再做一轮反向核对。除上述 MT-D3
"UID 升序"具体字段需您确认外，暂未发现其他把老师要求操作化为另一种
实现口径的情况；其余未闭环项均按 teacher-review、teacher-decision 或
future-not-authorized 边界保留，没有写成已通过。

## Files For Review

```text
16_MetaTraits_Integration_Research_2026-07-15/02_Planning/
SNAPSHOT_CONTRACT_DRAFT.md

16_MetaTraits_Integration_Research_2026-07-15/02_Planning/
METATRAITS_API_INQUIRY_EMAIL_DRAFT.md

03_HPC_Returned_Result_Summaries/
metatraits_m4a3a_portable_validator_transport_final_correction_20260720/
source/microbe_crew/M4A_SMOKE_REPORT.md

04_Local_Review_Audits/
ENZYMECAGE_METATRAITS_M4A3A_PORTABLE_VALIDATOR_AND_TRANSPORT_FINAL_CORRECTION_LOCAL_AUDIT_2026-07-20.md

04_Local_Review_Audits/
ENZYMECAGE_METATRAITS_M4A4BAAAA_FINAL_TRANSPORT_AND_TEACHER_REQUIREMENT_CROSSCHECK_2026-07-21.md
```

## Reply Contract

Please preserve each answer separately:

```text
MT-TQ-01: explicit A/B/C formulas, source fields and deterministic tie-breaks,
          including whether MT-D3 "UID ascending" means numeric NCBI taxon ID
          ascending as currently implemented, or another exact UID field;
          or explicit permission to omit a non-executable comparison column
MT-TQ-02: snapshot contract approved, or exact amendments
MT-TQ-03: maintainer email recipient/signature/project-name/wording decision and,
          after sending, sent-date evidence
MT-TQ-04: final checkpoint-loading strategy after audited M4a-4 benchmark evidence
MT-TQ-06: zero-additional-local-model coexistence interpretation, or an exact
          teacher-specified local model/checkpoint/load contract
MT-TQ-07: exact-taxon versus species/sibling-strain trait attribution policy,
          fallback semantics and enzyme-proof requirement for strain expansion
```

Not requested yet:

```text
MT-TQ-05 M4b allowlist/thresholds/authorization: future separate gate
M4c authorization: future separate gate after M4b
```
