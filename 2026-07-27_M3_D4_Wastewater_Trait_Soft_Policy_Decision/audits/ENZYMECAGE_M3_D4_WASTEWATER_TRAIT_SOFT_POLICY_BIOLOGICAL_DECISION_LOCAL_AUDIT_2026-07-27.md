# M3-D4 污水 Trait 全 soft 生物学决定本地审计

审计日期：2026-07-27（Asia/Shanghai）  
审计对象：

`M3_D4_WASTEWATER_TRAIT_SOFT_POLICY_BIOLOGICAL_DECISION_RECORD_2026-07-27.md`

对象 SHA256：

```text
5e779c822b645a6fdabf98b4b60bc70cc0153b96a8c8eb71c4d2822d5302c272
```

结论：**PASS / T1 ACCURATELY RECORDED / NO M4B OR M4C AUTHORIZATION CLAIMED**

## 1. 会议决定映射

用户转述的会议结论是：

```text
保留 soft
给用户参考和建议
不直接删除候选菌
```

对象准确映射为此前选择卡的 T1：

```text
all traits soft:
  yes

reference/advice/explanation:
  yes

automatic deletion:
  forbidden

hard rejection:
  forbidden
```

未把会议结论扩写为 T2/T3，也未发明 hard threshold。

## 2. 与既有权威裁定一致性

对象与 `TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md`
的 MT-D4 一致：

- temperature / pH / salinity / oxygen 均为 soft；
- biofilm 为 unknown / unused；
- safety/pathogenicity 为 soft warning + 人工复核；
- 不执行不可逆剔除；
- uncertainty 必须保留。

结果：`AUTHORITY_ALIGNMENT = PASS`。

## 3. ID 和数据面边界

对象保留：

```text
exact_strain:
  0

exact_species:
  0

no_exact_match_established:
  10

species-name summary:
  contextual only
```

未发生：

- species 向 strain 继承；
- strain 向 species 继承；
- 把 summary 冒充 exact-ID；
- 把未见 429 写成 unlimited；
- 把 soft evidence 写成生物学不存在。

结果：`ID_AND_EVIDENCE_BOUNDARY = PASS`。

## 4. 实现权限边界

对象明确：

```text
Task 7:
  contract-only

M4b:
  not authorized

M4c:
  not authorized

MicrobeTraitTool:
  not started

TraitFilterLayer:
  not started

complete MicrobeSelectionAgent:
  not started
```

结果：`NO_UNAUTHORIZED_IMPLEMENTATION_CLAIM = PASS`。

## 5. 最终判断

该决定记录可提交黄老师确认 D4 的最终生物学立场。它只冻结 all-soft 政策，不解锁
M4b/M4c，不降低 exact-ID 或 production data-plane 门。

