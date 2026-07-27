# M3 下一轮微生物侧前置输入：既有裁定回传与状态闭合

日期：2026-07-26  
对应：

- `TEACHER_REPLY_M3_TASKS_1_7_ACCEPTANCE_AND_TASK7_SCOPE_AND_SNAPSHOT_MTTQ02_2026-07-23(1).md`
- `TEACHER_REPLY_M3_NEXT_ROUND_STUDENT_PREREQUISITES_SUPPLEMENT_2026-07-24(1).md`

状态：**逐项状态闭合完成；既有裁定按原字节回传；不主张新增老师验收；
M4b/M4c 仍未启动**

## 一、先说明 07-24 清单与既有裁定的关系

07-24 补充件写明“不改动上一轮任何裁定”。本次重新核查发现：

1. MT-D1–D8 已在
   `TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md`
   逐项裁定；
2. 07-21 的 M4a 裁定又明确写明“不改动 MT-D1–D8 既有裁定”，并进一步闭合
   MT-D3 tie-break、MT-D8 预加载等问题；
3. 因此本次不重新发明 D1–D8 立场，而是把两份裁定原件按字节回传，并报告
   现有实现和仍待裁定部分。

07-18 原件身份：

```text
filename:
  TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md
document internal date:
  2026-07-16
SHA256:
  230d67ff1e18af34d5c4b5d736f27203bf4c060ee4854eb37b192749a7333606
```

文件名日期与文内日期不同，本文如实同时披露，不擅自修改原件。

## 二、07-23 重申三项的当前状态

| 项目 | 当前状态 | 位置 / 提交 |
|---|---|---|
| ① 07-22 RHEA:11880 原件 | 已按目标 SHA256 回传 | 酶侧仓库根目录；commit `cf06bf6e63b19c1d7cb486ba954e9a42d151da27`；SHA256 `80a3be0c8507a6cbf4f318de0c4735aa04d7c5106c2cc759fb5af7ee9ea356c0` |
| ② Task 7 TraitValue 契约 | 已按 (a) 交付契约与示例，无活代码 | 本仓库 `TRAIT_VALUE_NOT_APPLICABLE_SCHEMA_CONTRACT.md`；commit `20f55d0c4769d85b7f90caaeb7e76d1a596b1ff7` |
| ③ M3-EXT 补充材料 | v0 shortlist 已获“符合授权边界”；后续待老师另行安排 | 当前不补资产、不跑模型、不晋级案例 |

## 三、07-24 P0 项

### P0：D5 新合同版

已按新合同重新审计，不因旧文件同名或早期验收而直接判定满足：

```text
path:
  2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/
commit:
  48c6e80be60cca285540c65acc5dd337762ede94
index clarification commit:
  324a19e820a7780bbb929ab025f90eccaac4eb5f
student status:
  COMPLETE_AND_INDEPENDENTLY_REAUDITED
new teacher acceptance:
  NOT CLAIMED
```

报告已覆盖：

- 10 个 P0 frozen-label positive 且 reaction-group `positive_rank=1` 的酶；
- 10 个 reviewed UniProt 宿主映射，5 个成功 metaTraits 样本；
- 5 份原始 metaTraits JSON；
- 接口/下载稳定性；
- 污水相关性状覆盖度；
- `No robust majority` 比例；
- rate-limit 有界探测；
- NCBI tax ID 直查的负结果与 species-name 查询边界。

### P0：07-22 原件

已在酶侧仓库闭合，见第二节。两个 P0 项分别保留在微生物和酶侧仓库，不混放。

## 四、P1 2.1 反应预测器

三路线统一小试、答案钥匙解锁后评分和独立复算已完成；最终路线未选择。

```text
enzyme repository root entry:
  M3_P1_2_1_REACTION_PREDICTOR_ROUTE_ADJUDICATION_REQUEST_2026-07-26.md
package:
  2026-07-26_M3_P1_2_1_Reaction_Predictor_Route_Adjudication/
commit:
  601d0d384825e4e0fca1e2790de37db7a664c96a
```

当前建议与待裁定问题均在该包中。本文件不重复选择路线，也不授权
`reaction_prediction_node` 活代码。

## 五、P1 2.2 酶→菌 confidence：沿用 MT-D2 C 修订版

07-18 MT-D2 已明确裁定：

```text
v1:
  不输出 organism_confidence float
保留:
  reviewed 状态
  annotation score
  protein existence
  KEGG multiplicity
禁止:
  LLM 创造数值
  未经老师审阅自行建立 confidence 映射
```

因此 07-24 §2.2 的两条路线不能被理解为要求学生现在重新二选一：

- 不需要另上线一个产生 confidence float 的服务；
- 不能从 Swiss-Prot / TrEMBL 身份擅自硬映射 confidence；
- `cumulative_score = sum(enzyme_score × organism_confidence)` 在 v1 不使用。

已授权并交付的 M4a 实现遵循既有裁定：

```text
host evidence:
  reviewed UniProt primary
  KEGG independent supplement
  TrEMBL excluded in v1
aggregator order:
  supporting_enzyme_count descending
  NCBI taxon ID numeric ascending tie-break
organism_confidence float:
  absent
```

M4a teacher-review package：

```text
2026-07-21_MetaTraits_M4a_Teacher_Review_Decision_Request/
commit:
  65bbd2d459591f068340467740e972a4a689a42d
```

请老师确认继续沿用 MT-D2 C 修订版；本次没有创建
`CONFIDENCE_MAPPING_PROPOSAL.md`，因为当前 v1 不需要。

## 六、D1–D8 逐项闭合

| 决策点 | 既有老师裁定 | 当前执行状态 | 是否还需本轮新选择 |
|---|---|---|---|
| D1 宿主定义 | B+：reviewed UniProt 主证据；KEGG 独立补充；TrEMBL v1 排除 | 已在 M4a 实现与测试 | 否 |
| D2 confidence | C 修订版：v1 不输出 float | 已遵循；无 confidence 映射 | 否 |
| D3 聚合排序 | v1 先锁 supporting-enzyme 数量；07-21 再定 NCBI taxon ID 数字升序 tie-break | 已实现 | 否 |
| D4 Trait 硬约束 | v1 最小保守 allowlist；当前所有 trait 均 soft + uncertainty，不做不可逆剔除 | 默认合同已定；专家升级仍待刘老师 | **是，仅专家升级部分** |
| D5 预调研 | 07-16/07-18 已验收；07-24 新合同版又重新审计提交 | 已完成；不主张新合同版已再次验收 | 否 |
| D6 LLM prompt | 禁绕 hard constraints；每个推荐 ≥2 条可追溯证据；不足则 unknown | 合同已定；M4c 未授权所以未实现 | 否 |
| D7 crew 边界 | 独立 `MicrobeCrew` | 架构裁定已定 | 否 |
| D8 预加载 | 07-21 MT-TQ-04 最终继续 A：启动时预加载 | 已裁定；不切 lazy | 否 |

结论：不是 D1–D8 八项全部悬空。当前只剩 D4 的“由生物学专家将哪些 soft
trait 升级成 hard、方向和阈值”需要刘老师给生物学意见。

## 七、P2 ⑤⑥⑦ 的真实状态

### ⑤ metaTraits 数据面

既有裁定：

```text
production primary:
  official versioned snapshot
online endpoint:
  experimental fallback only
```

`SNAPSHOT_CONTRACT_DRAFT.md` 已于 07-23 获草案 PASS，但当前仍缺官方
`upstream_version` 和可验证的正式 snapshot。D5 实测：

```text
documented /api/v1:
  16/16 HTTP 404
website download:
  bounded usable with retry
stable organism_uid -> traits production path:
  unresolved
```

所以该项不能被写成“bulk/query 已生产接入”。下一步取决于官方版本化下载面、
维护方回复或老师批准的其他映射路径，今天不能靠本地改文档解决。

### ⑥ organism ID 对齐

初测已经完成，结论是负结果：

```text
NCBI tax ID direct query:
  10/10 HTTP 404
species-name summary:
  bounded usable
summary JSON tax_id field:
  absent
explicit exact-ID classes:
  exact_strain = 0
  exact_species = 0
  no_exact_match_established = 10
```

这不是“没测”，也不是工作 ID 对齐链路。后续必须跟随 ⑤ 的正式数据面方案。
五个有数据的对象仍只是 `species-name summary only`，不得归入 exact species 或
exact strain；另外五个没有交付 summary。

显式三分类补充与逐行字段：

```text
2026-07-24_MT_D5_New_Contract_Reaudit_and_Resubmission/
ORGANISM_ID_ALIGNMENT_EXPLICIT_TRISTATE_SUPPLEMENT_2026-07-26.md

P0_TOP_MRR_ENZYME_TO_HOST_METATRAITS_CROSSWALK.csv
column:
  metatraits_exact_id_alignment_class
```

这里的 `no_exact_match_established` 只表示当前证据链没有证明 TaxID 精确相等，
不表示 metaTraits 数据库一定不存在该微生物或性状。

### ⑦ 污水 Trait 硬约束

老师当前 v1 默认：

| Trait | 当前角色 |
|---|---|
| temperature | soft |
| pH | soft |
| salinity | soft |
| oxygen_preference | soft |
| biofilm | 不使用，统一 unknown |
| safety/pathogenicity | soft + 人工复核 |

明天需要刘老师确认的最小问题：

1. 是否同意 v1 暂时全部保留 soft，不做自动不可逆剔除？
2. 若要把某项升级为 hard，请逐项给出 trait、方向、数值/类别阈值、适用污水场景
   和依据；不能只说“按常见范围”。
3. 是否确认 biofilm 在当前 0/5 覆盖证据下继续不参与过滤？
4. 是否确认 safety/pathogenicity 继续只做 soft + 人工复核，不自动剔除？

在专家裁定前不自行填写阈值。

## 八、2.3 与后续代码边界

`MicrobeSelectionAgent` 可以理解为已有后端的半装说明，但完整版依赖 M4b 的
`TraitFilterLayer`。当前保持：

```text
MicrobeTraitTool:
  NOT STARTED
TraitFilterLayer:
  NOT STARTED
MicrobeSelectionAgent full implementation:
  NOT STARTED
M4b:
  NOT AUTHORIZED
M4c:
  NOT AUTHORIZED
```

Task 7 契约、D6 prompt 规则和 D4 默认 allowlist 都不等于 M4b/M4c 活代码授权。

## 九、本轮请老师确认

1. 07-18 与 07-21 原裁定继续有效，D1–D8 不需要重新发明一套学生立场；
2. 2.2 继续执行 MT-D2 C 修订版：v1 不输出 `organism_confidence` float；
3. D5 新合同版、Task 7 和 07-22 原件已在上述路径交付；
4. ⑤ 数据面与 ⑥ ID 对齐按已披露负结果保持 fail-closed；⑥ 的显式分类为
   `exact_strain=0 / exact_species=0 / no_exact_match_established=10`；
5. D4 专家升级等待刘老师意见；意见返回后再形成确定性 allowlist/threshold 合同；
6. M4b/M4c、M3-EXT 二阶段和反应预测活代码在分别授权前均不启动。

## 十、证据包

```text
2026-07-26_M3_P1_Microbe_Prerequisites_Status_Closure/
```

其中含：

- 本 README；
- 07-18、07-21、07-23、07-24 四份老师文档原字节；
- 本地独立审计；
- SHA256 清单。

本文件只主张学生侧已有交付和状态说明，不主张老师已经接受本轮重新提交。
