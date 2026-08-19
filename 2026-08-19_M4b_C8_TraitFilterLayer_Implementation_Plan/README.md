# 2026-08-19 M4b C8 TraitFilterLayer Implementation Plan

本目录对应黄老师 2026-08-18 任务单中陈浩然侧：

```text
08-20 前：提交 C8 实装方案 / 拆解待审
```

## 老师优先阅读

1. C8 实装方案与拆解：
   [`M4B_C8_TRAITFILTERLAYER_IMPLEMENTATION_PLAN_AND_TASK_BREAKDOWN_2026-08-19.md`](M4B_C8_TRAITFILTERLAYER_IMPLEMENTATION_PLAN_AND_TASK_BREAKDOWN_2026-08-19.md)
2. 本地审计：
   [`audits/M4B_C8_TRAITFILTERLAYER_IMPLEMENTATION_PLAN_LOCAL_AUDIT_2026-08-19.md`](audits/M4B_C8_TRAITFILTERLAYER_IMPLEMENTATION_PLAN_LOCAL_AUDIT_2026-08-19.md)
3. 证据索引：
   [`evidence_index/C8_EVIDENCE_INDEX_2026-08-19.md`](evidence_index/C8_EVIDENCE_INDEX_2026-08-19.md)
4. C8 实装前新增口径问题：
   [`pending_teacher_decisions/M4B_C8_PENDING_TEACHER_DECISIONS_RESCUED_SOURCES_AND_PORTRAITS_2026-08-19.md`](pending_teacher_decisions/M4B_C8_PENDING_TEACHER_DECISIONS_RESCUED_SOURCES_AND_PORTRAITS_2026-08-19.md)

## 当前结论

这是 **C8 方案 / 拆解待审**，不是 C8 实装结果。

方案建议 C8 按以下 staged-only 路线推进：

```text
C8-0 输入冻结与路径预检
C8-1 构建只读 trait lookup index
C8-2 候选 UID 到微生物来源展开
C8-3 生成 trait_annotation.jsonl
C8-4 validator 与边界报告
C8-5 bounded-to-full staged rollout
```

## 核心边界

```text
staged-only
不接 production
不改 production D4
不改 production pool
不调用 MetaTraits API
不调用 BacDive API
不运行在线 genome prediction
不生成新酶资产
不 hard reject 微生物
不输出 trait_score
不输出未校准 confidence
真菌本轮 identity-only
F5 availability / culture collection number 禁止预测
F8 broad degradation 不能写成目标污染物直接降解事实
F15 仅低覆盖生态背景，不参与排序/评分/推荐
```

## 已满足的前置条件

```text
1,704 PASS staged enzyme assets 已由老师 2026-08-14 验收；
C7-1 F1-F15 trait panel 已由老师 2026-08-14 冻结；
C7-2 feature encoding proposal 已由老师 2026-08-17 冻结；
C7-2 只读 schema/validator bounded 30 已完成并本地审计 PASS；
MetaTraits bulk TSV 已落 Chenyu；
C7-1 MetaTraits long-form mapping rerun2 已修复 false-positive 并本地审计 PASS。
```

## 待老师审定

主方案中没有擅自新增生物学口径决定。另有两个实装前新增口径问题已单独列入
`pending_teacher_decisions/`，请老师裁定后再进入后续 staged rollout。

仍建议老师审定以下工程推进点：

```text
只读 lookup index 是否可作为 staged 派生物生成；
C8 首轮 full staged rollout 的 denominator；
是否先用小型候选表与弓赛 fallback 输出做接口 smoke；
C8 是否继续限定为展示/解释/覆盖统计，不启用 hard filtering 或 trait_score。
补资产后牵出的 137 个 2,478 外 source_signature 是否扩入 C8 staged universe；
MetaTraits 未覆盖的 bacteria / archaea 是否另行授权 porTraits preflight。
```
