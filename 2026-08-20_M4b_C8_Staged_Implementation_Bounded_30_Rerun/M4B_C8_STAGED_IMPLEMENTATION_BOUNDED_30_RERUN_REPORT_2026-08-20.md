# M4b C8 Staged Implementation + Bounded 30 Rerun Report

Date: 2026-08-20

Status:

```text
C8_0_TO_C8_4_STAGED_ONLY_EVIDENCE_READY
C8_3_4_BOUNDED_30_RERUN_PASS_AFTER_REPACK_FIX
C8_5_SMALL_REAL_UPSTREAM_CANDIDATE_TABLE_SMOKE_NOT_YET_RUN
NO_PRODUCTION_MUTATION
```

## 1. 本包回答什么问题

本包回答老师 2026-08-19 对陈浩然侧 C8 的要求中，C8 主链路 staged-only
实装证据是否已经跑通：

```text
C8-0 输入冻结
C8-1 只读 lookup index + 137 个外来源 delta review
C8-2A UID-source expansion harness
C8-3/C8-4 固定 30-row bounded rerun + validator
```

本包不回答：

```text
真实污染物/反应上游候选酶列表是否已经产出；
C8-5 小型真实候选表 smoke 是否已经完成；
是否可以全量 rollout；
是否可以接 production；
是否可以把 trait 用作 hard filter / trait_score。
```

## 2. 老师 2026-08-19 的关键边界

本包按老师 2026-08-19 裁定执行：

```text
C8 staged-only implementation is approved.
Main denominator remains original 2,478 source_signature universe.
137 rescued outside-universe source_signatures are delta review only.
Do not merge the 137 delta sources into the 2,478 main universe.
porTraits is not started in C8 v1.
Fungi remain identity-only.
F5 is observed-only and must never be predicted.
F8 is broad degradation context only, not direct target-pollutant degradation.
F15 is background only and must not rank/filter/recommend.
No hard rejection, no trait_score, no uncalibrated confidence.
No production D4 / production pool / formal asset mutation.
C8-5 requires 30-row bounded rerun + small candidate-table smoke before full rollout.
```

## 3. C8-0 输入冻结

路径：

```text
c8_0_input_freeze/C8_INPUT_SOURCE_AUDIT.md
c8_0_input_freeze/C8_INPUT_SOURCE_AUDIT.json
```

作用：

```text
确认 C8 输入来源、老师授权、C7-1/C7-2 契约、MetaTraits/BacDive evidence、
2,478 主 universe、C7-2 bounded 30 reference、以及不得接 production 的边界。
```

C8-0 不生成 trait_annotation，不运行预测，不修改任何生产资产。

## 4. C8-1 lookup index + delta review

最终回包：

```text
hpc_archives/enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820.tar.gz
hpc_identity/enzymecage_m4b_c8_1_lookup_index_delta_review_dependency_payload_rerun2_repack_fix_20260820.tar.gz.identity.txt
```

本地审计：

```text
audits/C8_1_LOOKUP_INDEX_DELTA_REVIEW_DEPENDENCY_PAYLOAD_RERUN2_REPACK_FIX_LOCAL_AUDIT_2026-08-20.md
```

审计结论：

```text
LOCAL_AUDIT_VERDICT = PASS_TEACHER_READY_C8_1_STAGED_ONLY_CANDIDATE
```

关键结果：

```text
C8_METATRAITS_LOOKUP_INDEX.jsonl = 37,170 rows
C8_BACDIVE_AVAILABILITY_LOOKUP.csv = 2,478 data rows
C8_LOOKUP_SOURCE_UNIVERSE.csv = 2,478 data rows
C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW.csv = 137 data rows
F1-F15 each have exactly 2,478 lookup rows
all 428 fungal F5 rows = FUNGI_IDENTITY_ONLY
delta ∩ main = 0
```

137 个 delta 来源保持：

```text
recommended_status = PENDING_TEACHER_DECISION
inside_original_2478_universe = false
```

这一步不生成 final `trait_annotation.jsonl`，不接 production。

## 5. C8-2A UID-source expansion harness

最终回包：

```text
hpc_archives/enzymecage_m4b_c8_2a_bounded_uid_source_expansion_harness_20260820.tar.gz
hpc_identity/enzymecage_m4b_c8_2a_bounded_uid_source_expansion_harness_20260820.tar.gz.identity.txt
```

本地审计：

```text
audits/C8_2A_BOUNDED_UID_SOURCE_EXPANSION_HARNESS_LOCAL_AUDIT_2026-08-20.md
```

审计结论：

```text
LOCAL_AUDIT_VERDICT = PASS_TEACHER_READY_C8_2A_BOUNDED_HARNESS
```

关键结果：

```text
input candidate rows = 4,681
consumable PASS assets = 1,704
asset not available = 2,977
C8-3 eligible MAIN_2478 rows = 753
delta review rows = 209
PASS but NOT_MAPPED rows = 742
```

重要解释：

```text
4,681 / 1,704 / 753 是当前 M4 E2 fallback-harness 下的工程验证口径。
它不是最终全库候选酶范围，也不是上游真实候选酶列表。
后续真实 C8 输入仍应来自上游 candidate table:
query_id / pollutant / reaction_candidate / enzyme_uid / enzyme_candidate_source / rank
```

## 6. C8-3/C8-4 固定 30-row bounded rerun

最终回包：

```text
hpc_archives/enzymecage_m4b_c8_3_4_bounded_30_rerun_repack_fix_20260820.tar.gz
hpc_identity/enzymecage_m4b_c8_3_4_bounded_30_rerun_repack_fix_20260820.tar.gz.identity.txt
```

本地审计：

```text
audits/C8_3_4_BOUNDED_30_RERUN_REPACK_FIX_RETURN_LOCAL_AUDIT_2026-08-20.md
```

审计结论：

```text
LOCAL_AUDIT_VERDICT = PASS_TEACHER_READY_C8_3_4_BOUNDED_30_RERUN_REPACK_FIX
```

固定子集：

```text
30 rows = the exact same 2026-08-18 C7-2 bounded 30 rows
10 target_bacteria + 10 target_archaea + 10 target_fungi
P0DXV0 absent
same enzyme_uid/source_signature pairs as 2026-08-18 reference = true
```

输出：

```text
POLICY_MANIFEST.json
TRAIN_SET_MANIFEST.csv
trait_annotation.jsonl
C8_BOUNDED_30_INPUT_TABLE.csv
C8_VALIDATION_REPORT.json / .md
C8_BOUNDARY_VALIDATION_REPORT.md
C8_TRAITFILTERLAYER_CONSUMPTION_CONTRACT.md
scripts/run_c8_3_4_bounded_30_rerun.py
```

独立审计结果：

```text
trait_annotation rows = 30
TRAIN_SET_MANIFEST rows = 30
all 30 rows MAIN_2478
all 30 rows READY_FOR_C8_3_TRAIT_ANNOTATION
fungi identity-only violations = 0
F5 prediction_used=true rows = 0
F9-F15 prediction_used=true rows = 0
F8 direct target-pollutant degradation wording = 0
F15 ranking/filtering/recommendation wording = 0
production/formal mutation flags = 0
```

## 7. 当前还不能声明完成的 C8-5

老师 2026-08-19 要求：

```text
C8-5 must first use 30-row bounded rerun + small candidate-table smoke.
Teacher confirmation is required before full rollout.
```

本包已经完成：

```text
30-row bounded rerun
```

本包尚未完成：

```text
small real upstream candidate-table smoke
```

原因：

```text
C8 不应自行创造真实候选酶列表。
真实上游候选表应由上游污染物/反应/酶候选路线提供。
在该小型候选表冻结前，本包不能把 4,681 harness、1,704 staged assets、
753 eligible rows 或 30 bounded rows 写成真实候选酶结果。
```

## 8. 本包请求老师审阅什么

请老师审阅：

```text
1. C8-0 至 C8-4 staged-only evidence 是否通过；
2. C8-1 的 137 delta review 是否继续保持 PENDING_TEACHER_DECISION；
3. C8-2A harness 口径是否可作为工程验证证据，但不作为真实候选酶池；
4. C8-3/C8-4 固定 30-row bounded rerun 是否通过；
5. 是否同意等待上游小型真实 candidate table 后再做 C8-5 smoke；
6. 是否继续保持 no production / no hard filter / no trait_score / fungi identity-only 等红线。
```

## 9. 与 C8-P porTraits 包的关系

本包是 C8 主链路 staged-only 证据。

另一个同批包：

```text
../2026-08-20_M4b_C8_P_porTraits_Preflight_Decision_Request/
```

是 C8-P porTraits 受控 preflight 决策请求。它不属于 C8 主链路已实装结果；
它只请求老师裁定是否允许后续准备 porTraits runtime/assets/tiny FASTA smoke。
