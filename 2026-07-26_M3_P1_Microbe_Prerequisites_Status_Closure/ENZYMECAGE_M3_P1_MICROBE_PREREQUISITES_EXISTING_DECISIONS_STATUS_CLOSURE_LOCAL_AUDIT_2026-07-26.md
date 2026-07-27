# M3 P1 微生物侧前置输入既有裁定与状态闭合本地审计

审计日期：2026-07-26（Asia/Shanghai）  
审计对象：
`M3_P1_MICROBE_PREREQUISITES_EXISTING_DECISIONS_AND_STATUS_CLOSURE_2026-07-26.md`  
结论：**PASS FOR STATUS-CLOSURE SUBMISSION / NO M4b OR M4c AUTHORIZATION**

## 1. 权威文件完整性

本次状态闭合同时读取并逐项交叉核对：

```text
TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md
TEACHER_REPLY_M3_P1_UNLOCK_CASE1_REBOUND_AND_METATRAITS_M4A_ADJUDICATION_2026-07-21.md
TEACHER_REPLY_M3_TASKS_1_7_ACCEPTANCE_AND_TASK7_SCOPE_AND_SNAPSHOT_MTTQ02_2026-07-23(1).md
TEACHER_REPLY_M3_NEXT_ROUND_STUDENT_PREREQUISITES_SUPPLEMENT_2026-07-24(1).md
```

四份原件进入 teacher-deliverables 包时均保持字节不变。特别保留 07-18 文件名
与文内 `日期：2026-07-16` 的差异，没有静默改写。

## 2. “已有裁定”判定依据

```text
07-18:
  状态明确写 MT-D1–D8 裁定完成
  D2 明确 v1 不输出 organism_confidence float
  D3 给出 v1 默认 supporting-enzyme count
  D8 给出联调前默认 A

07-21:
  MT-TQ-01 最终裁定 NCBI taxon ID 数字升序 tie-break
  MT-TQ-04 最终继续 A 启动预加载
  §七明确“不改动 MT-D1–D8 既有裁定”

07-23:
  SNAPSHOT 草案 PASS
  M4b 仍不启动
  Task 7 走 contract-only (a)

07-24:
  自身定位为补充件，不改动上一轮裁定
```

因此本审计拒绝重新创造一套 D1–D8 立场，也拒绝为满足 07-24 §2.2 而擅自增加
confidence float。

## 3. 既有 Git 交付核验

下列提交均能在对应本地 teacher-deliverables 仓库解析，且工作树中存在所声明文件：

```text
07-22 original enzyme clarification:
  cf06bf6e63b19c1d7cb486ba954e9a42d151da27

M4a teacher review package:
  65bbd2d459591f068340467740e972a4a689a42d

Task 7 contract:
  20f55d0c4769d85b7f90caaeb7e76d1a596b1ff7

D5 new-contract reaudit:
  48c6e80be60cca285540c65acc5dd337762ede94

P0 clarification/index:
  324a19e820a7780bbb929ab025f90eccaac4eb5f

reaction predictor adjudication package:
  601d0d384825e4e0fca1e2790de37db7a664c96a
```

## 4. 2.2 实现一致性抽查

M4a teacher-review 包内实现抽查：

```text
enzyme2organism_tool.py:
  reviewed UniProt primary
  KEGG independent supplement
  rejects unreviewed/unsupported entries

organism_aggregator.py:
  supporting_enzyme_count present
  sort = count descending, NCBI taxon ID ascending

organism_confidence:
  no runtime field or scoring multiplier found
```

该实现与 MT-D1、D2、D3 和 07-21 MT-TQ-01 一致。

## 5. D5 新合同要求复核

`2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/metatraits_probe_report.md`
已明确披露：

```text
P0 frozen-label positive evidence:
  50/50 source rows Label=1
positive rank:
  rank 1 within each reaction candidate group
reviewed UniProt reaction support:
  10/10
host mappings:
  10
successful metaTraits samples:
  5
original JSON:
  5
interface / coverage / no_robust_majority / rate limit:
  all reported
NCBI tax-ID direct-query initial test:
  complete negative result, 10/10 HTTP 404
explicit exact-ID classes:
  exact_strain = 0
  exact_species = 0
  no_exact_match_established = 10
contextual fallback:
  species-name summary only = 5
  no delivered summary = 5
```

显式分类由 crosswalk 的 `metatraits_exact_id_alignment_class` 逐行重算，并由
`METATRAITS_ORGANISM_ID_ALIGNMENT_EXPLICIT_TRISTATE_SUPPLEMENT_INDEPENDENT_AUDIT_2026-07-26.md`
单独审计。报告没有把 species-name summary 冒充 exact species/strain path，也没有把
`no_exact_match_established` 冒充数据库缺失声明，或把 0 个 429 冒充 unlimited。

## 6. 真正未闭合项

```text
reaction predictor final route:
  biological / teacher adjudication pending

D4 hard-trait upgrade:
  biological expert decision pending

metaTraits production data plane:
  official versioned upstream or approved stable query path absent

exact organism_uid -> traits path:
  unresolved after completed negative initial test

M3-EXT stage 2:
  teacher arrangement pending
```

这些事项均未被主交付误标为完成。

## 7. 锁定边界

```text
[x] no confidence mapping invented
[x] no M4b code
[x] no M4c code
[x] no MicrobeTraitTool implementation
[x] no TraitFilterLayer implementation
[x] no hard thresholds invented
[x] no M3-EXT asset expansion or model run
[x] no new teacher acceptance claimed
```

## 8. 审计结论

本次交付可以作为 07-23/07-24 清单的“已有裁定位置说明 + 当前状态闭合”提交。
它不构成 M4b/M4c 解锁，也不替代明天刘老师对 D4 专家升级和反应预测路线的判断。
