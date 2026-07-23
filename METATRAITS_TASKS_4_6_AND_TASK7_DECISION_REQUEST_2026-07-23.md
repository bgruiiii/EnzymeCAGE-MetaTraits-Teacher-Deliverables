# MetaTraits Tasks 4、6 交付与 Task 7 边界裁定请求

日期：2026-07-23

状态：`TASK4_AND_TASK6_SUBMITTED_TASK7_PENDING_TEACHER_SCOPE_DECISION`

权威依据：

```text
TEACHER_REPLY_M3_P1_UNLOCK_CASE1_REBOUND_AND_METATRAITS_M4A_ADJUDICATION_2026-07-21.md
SHA256 57699b8a92ba6b555c96c0216c3961af0e80299d150b21979cb4fa7a19a18d57
```

## 1. 老师从哪里开始看

| 老师任务 | 根目录交付文件 | 当前状态 |
|---|---|---|
| Task 4：Snapshot 契约草案 | `SNAPSHOT_CONTRACT_DRAFT.md` | 本地审计通过，等待老师单独裁定 |
| Task 6：移除对外项目名 | `METATRAITS_API_INQUIRY_EMAIL_DRAFT.md` | 本地审计通过；邮件仍未发送 |
| Task 7：not_applicable schema | 本文第 4 节 | 未实施，等待老师确认实施边界 |

逐任务审计及提交前总审计位于：

```text
2026-07-23_MetaTraits_Tasks_4_6_and_Task7_Decision_Request/audits/
```

## 2. Task 4：SNAPSHOT_CONTRACT_DRAFT.md

老师要求的六项均在根目录草案中：

1. 版本字段；
2. 更新频率；
3. 许可展示；
4. 本地存储路径；
5. hash 校验方式；
6. 与在线 fallback 的切换条件。

草案另明确：

```text
production default = snapshot_only
TTL cache = 24 hours
minimum request spacing >= 2 seconds
three consecutive failures open the circuit breaker
bulk observation scraping = prohibited
complete online provenance required
M4b remains unauthorized
```

说明：完全相同字节的草案曾存在于旧 commit
`65bbd2d459591f068340467740e972a4a689a42d` 的嵌套路径
`2026-07-21_MetaTraits_M4a_Teacher_Review_Decision_Request/planning/`，
但旧仓库首页只要求老师进入日期目录后再找文件，没有把它标成当前
两项主要交付之一。这次不改写历史 commit，而是把同一审计通过的
文件重新放在仓库根目录，并在首页第一屏直接链接。

本次提交仍只是请求老师对 MT-TQ-02 单独裁定，不声称草案已经得到
老师批准，也不据此启动 M4b。

## 3. Task 6：去除对外项目名

根目录当前邮件草案：

```text
METATRAITS_API_INQUIRY_EMAIL_DRAFT.md
status = UNSENT_GENERIC_INQUIRY_DRAFT_PENDING_RECIPIENT_AND_SIGNATURE_REVIEW
```

邮件对外身份已改为：

```text
On behalf of an academic bioinformatics enzyme-to-microorganism mapping study
```

当前邮件中不含大小写不敏感的上游项目名。收件人地址、老师姓名和
单位仍等待老师核验，邮件没有发送，也没有声称已经联系维护方。

已验收 M4a 源码中的第三方请求身份本来就是通用的：

```text
USER_AGENT = ADRMATS-MicrobeCrew-Enzyme2Organism/1.0
```

`Enzyme2OrganismTool` 与 `OrganismAggregator` 两个文件中没有项目名，
也没有额外 logger/print 对外披露，因此无需改算法、改查询参数、
重跑 HPC 或篡改已验收返回包。旧日期目录中的旧邮件作为历史证据
保留；当前应使用根目录的新版本。

## 4. Task 7：需要老师确认的最小实施边界

老师要求的目标输出为：

```yaml
trait_name: oxygen_preference
value: not_applicable
reason: taxon-level record absent (species/strain 均无对应观测)
note: not_applicable 表示“当前证据链下无法归属”，不等于“生物学上不存在此性状”
```

当前已验收的 M4a 只包含 `Enzyme2OrganismTool` 和
`OrganismAggregator`，它们不产生 trait 输出。包含 `TraitValue`
和 `MicrobeTraitTool` 的性状层属于尚未授权的 M4b。直接把字段实现
到 `MicrobeTraitTool` 会越过“Task 4 Snapshot 契约裁定前不启动
M4b”的边界，因此本轮没有擅自实现或伪称 Task 7 已完成。

请老师确认：

> 黄老师，任务 7 要求在 not_applicable 输出 schema 中增加 `reason`
> 和 `note`。当前已验收的 M4a 只包含 Enzyme2OrganismTool 和
> OrganismAggregator，不产生 trait 输出；包含 TraitValue 的
> MicrobeTraitTool 属于尚未授权的 M4b。这里本轮是只提交 TraitValue
> schema 修订契约和示例，不实现 MicrobeTraitTool；还是授权新增独立
> 的 Pydantic TraitValue schema 与字段校验测试，但仍不查询性状、
> 不实现过滤和 M4b 调用链？

老师回复前，Task 7 状态保持：

```text
NOT_IMPLEMENTED_PENDING_TEACHER_SCOPE_DECISION
M4B_NOT_STARTED
M4C_NOT_STARTED
```

## 5. 本次状态边界

Task 4 和 Task 6 已完成本地内容审计并提交 GitHub，仍等待老师验收。
Task 7 只有边界问题，没有实现。旧提交没有 force-push、rebase 或
覆盖；已验收 HPC 返回包没有修改。
