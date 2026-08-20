# 2026-08-20 M4b C8 Staged Implementation + Bounded 30 Rerun

本目录是给黄老师审阅的 C8 主链路 staged-only 实装证据包。

## 老师优先阅读

1. 主报告：
   [`M4B_C8_STAGED_IMPLEMENTATION_BOUNDED_30_RERUN_REPORT_2026-08-20.md`](M4B_C8_STAGED_IMPLEMENTATION_BOUNDED_30_RERUN_REPORT_2026-08-20.md)
2. C8-3/C8-4 30-row bounded rerun 最终审计：
   [`audits/C8_3_4_BOUNDED_30_RERUN_REPACK_FIX_RETURN_LOCAL_AUDIT_2026-08-20.md`](audits/C8_3_4_BOUNDED_30_RERUN_REPACK_FIX_RETURN_LOCAL_AUDIT_2026-08-20.md)
3. C8-1 lookup index + delta review 审计：
   [`audits/C8_1_LOOKUP_INDEX_DELTA_REVIEW_DEPENDENCY_PAYLOAD_RERUN2_REPACK_FIX_LOCAL_AUDIT_2026-08-20.md`](audits/C8_1_LOOKUP_INDEX_DELTA_REVIEW_DEPENDENCY_PAYLOAD_RERUN2_REPACK_FIX_LOCAL_AUDIT_2026-08-20.md)
4. C8-2A UID-source expansion harness 审计：
   [`audits/C8_2A_BOUNDED_UID_SOURCE_EXPANSION_HARNESS_LOCAL_AUDIT_2026-08-20.md`](audits/C8_2A_BOUNDED_UID_SOURCE_EXPANSION_HARNESS_LOCAL_AUDIT_2026-08-20.md)

## 一句话结论

按老师 2026-08-19 裁定，C8 主链路已完成 staged-only 的 C8-0 到 C8-4 证据，
并完成 C8 标签下的固定 30-row bounded rerun。当前结果可作为 C8 主链路小样本
schema/validator 证据回包。

本包 **不声明 C8-5 已完成**。C8-5 的“小型真实上游候选表 smoke”仍需等待上游
真实候选表，不能用 4,681/1,704 harness 或 30 行 bounded 子集冒充真实候选酶。

## 当前主结果

```text
C8-0 input freeze: complete
C8-1 lookup index + C8_DELTA review: PASS after rerun2 repack-fix
C8-2A UID-source expansion harness: PASS
C8-3/C8-4 bounded 30 rerun: PASS after repack-fix
Production mutation: none
Hard rejection / trait_score / uncalibrated confidence: none
Fungi: identity-only
F5: not predicted
F8: no direct target-pollutant degradation claim
F15: not used for ranking/filtering/recommendation
```

## 重要边界

```text
staged-only
不接 production
不改 production D4
不改 production pool
不改 formal assets
不 hard reject
不输出 trait_score
不输出未校准 confidence
不把 predicted evidence 写成 observed experimental fact
不把 137 个 2,478 外 rescued source 静默并入主 universe
不把 bounded 30 行当成真实候选酶列表
不把 4,681 / 1,704 harness 当成后续全库候选范围上限
```

## 包内结构

```text
authority_reference/      老师 08-19 裁定与 C8 实装方案
c8_0_input_freeze/        C8-0 输入冻结审计
c8_1_lookup_delta/        C8-1 lookup index、delta review、验证报告关键文件
c8_2a_uid_source_expansion/ C8-2A UID-source expansion 关键文件
c8_3_4_bounded_30_rerun/  C8-3/C8-4 30-row rerun 最终输出
hpc_archives/             三个最终 Chenyu 回包 tar.gz
hpc_identity/             对应 identity.txt
audits/                   本地审计
prompts/                  executor-only prompts
checksums/                本交付包文件清单与 SHA256
```
