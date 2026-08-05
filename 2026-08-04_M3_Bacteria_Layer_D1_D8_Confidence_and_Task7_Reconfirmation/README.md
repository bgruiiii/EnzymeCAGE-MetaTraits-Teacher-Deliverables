# M3 菌层 D1-D8 / confidence / Task7 再确认包

日期：2026-08-04  
状态：已 GitHub 同步的 teacher-deliverables 可审阅包。
目的：回应黄老师 2026-08-03 清单中菌层下半链相关要求，并避免“之前已经做过但老师没看到路径”的问题。

## 1. 本包覆盖什么

本包覆盖：

```text
D1-D8 逐条立场再确认；
2.2 酶→菌 confidence 来源再确认；
⑤ MetaTraits 数据面接入方式；
⑥ organism ID 对齐；
⑦ 污水 Trait hard/soft 策略；
② Task 7 TraitValue schema + not_applicable 示例再确认。
```

## 2. 本包文件

```text
audits/M3_BACTERIA_LAYER_D1_D8_AND_CONFIDENCE_REQUIREMENTS_REAUDIT_2026-08-04.md
audits/M3_TASK7_TRAITVALUE_NOT_APPLICABLE_2026_08_03_RECONFIRMATION_AUDIT_2026-08-04.md
DELIVERABLE_SHA256SUMS.txt
README.md
```

## 3. 关键结论

### 3.1 D1-D8

D1-D8 不是本轮新做决定，而是 2026-07-18 已经由老师正式裁定。本轮动作是重新把裁定和后续 D3 修正指给老师：

```text
D1: UniProt reviewed primary，KEGG supplement，TrEMBL v1 default not included
D2: v1 不输出伪精确 organism_confidence float；透传原始 evidence dimensions
D3: 后续修正为 supporting-enzyme count descending + numeric NCBI taxon ID ascending
D4: v1 trait 全 soft + uncertainty，不自动删除候选菌
D5: D5 probe 已完成，新合同版已在 2026-07-24/07-26 交付
D6: LLM 推荐需可追溯 evidence，不足则 insufficient_evidence/unknown
D7: 独立 MicrobeCrew
D8: M4a 默认 preload，后续 loading strategy 待性能测试
```

### 3.2 Confidence

当前 v1 口径不是“已经实现 0-1 organism_confidence”。准确说法是：

```text
v1 不输出伪精确 organism_confidence float；
透传 reviewed status、annotation score、protein existence、KEGG multiplicity 等证据维度；
如后续 schema 强制 numeric confidence，需要另写 CONFIDENCE_MAPPING_PROPOSAL.md。
```

### 3.3 D5 / 数据面 / ID 对齐

D5 新合同版索引在仓库根目录：

```text
METATRAITS_D5_2026_08_03_TEACHER_LIST_RECONFIRMATION_INDEX_2026-08-04.md
```

关键边界：

```text
official versioned MetaTraits snapshot 尚未取得；
production 主路径仍应等待 official versioned snapshot；
website endpoint 仅作 experimental fallback；
direct TaxID API 初测为负；
exact_strain = 0；
exact_species = 0；
no_exact_match_established = 10。
```

因此不能写成 exact TaxID -> trait production 通路已打通。

### 3.4 污水 Trait 策略

生物学侧已确认继续采用 soft-only：

```text
污水相关性状保留为用户参考、建议、解释和不确定性提示；
不自动删除候选菌；
不执行 hard rejection；
不做 species/strain 相互继承。
```

已有决定记录：

```text
2026-07-27_M3_D4_Wastewater_Trait_Soft_Policy_Decision/
```

### 3.5 Task 7

Task 7 既有 contract：

```text
TRAIT_VALUE_NOT_APPLICABLE_SCHEMA_CONTRACT.md
2026-07-24_Task7_TraitValue_Not_Applicable_Contract/
```

本轮再确认结论：

```text
Task 7 内容已完成；
不需要新用户生物学决策；
不需要新增 Pydantic 代码、测试或 M4b 实现；
最终回复只需指向既有交付和本轮再确认审计。
```

## 4. 当前边界

本包不启动：

```text
M4b；
M4c；
MicrobeTraitTool；
TraitFilterLayer；
hard filtering；
production organism_uid -> traits；
numeric organism_confidence mapping。
```

## 5. SHA256

见：

```text
DELIVERABLE_SHA256SUMS.txt
```
