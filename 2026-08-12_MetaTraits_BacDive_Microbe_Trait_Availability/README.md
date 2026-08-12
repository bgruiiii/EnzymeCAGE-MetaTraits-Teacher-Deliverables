# EnzymeCAGE 微生物侧 MetaTraits + BacDive 性状/可获得性探索交付包

Date: 2026-08-12

## 1. 交付包目的

本交付包整理 EnzymeCAGE 微生物侧 host/source trait 探索结果，重点回答：

1. 由 Rhea/UniProt 得到的微生物来源能否在 MetaTraits 中获得物种级性状；
2. 同一批来源能否在 BacDive 中获得菌株或物种级证据；
3. 如果不强求锁定 UniProt 原始菌株，BacDive 是否能提供该物种下可获得的代表菌株与保藏编号；
4. MetaTraits 与 BacDive 在性状数量、覆盖率和信息类型上如何互补；
5. 后续微生物侧特征构建应采用什么设计。

## 2. 总体结论

建议采用 hybrid schema：

```text
MetaTraits = 主性状矩阵
BacDive = 菌株身份 / 代表菌株可获得性 / 保藏编号 / 培养条件 / 分离来源补充
```

原因：

- MetaTraits 在物种级提供高维、标准化 trait matrix，更适合作为模型主性状来源；
- BacDive 在 exact strain evidence、culture collection number、culture medium、isolation source、country 等方面有独特价值；
- 两者覆盖并不完全重合，存在互补。

## 3. 数据 universe

本次分析使用 EnzymeCAGE final clean microbe source universe：

```text
source_signature 总数: 2,478
enzyme-source rows: 145,607
taxonomy scope: bacteria + archaea + fungi
```

BacDive 主要面向 prokaryotes，因此真菌单独标记为 non-scope，不作为 BacDive 缺失处理。

## 4. 关键结果

### 4.1 MetaTraits 物种级覆盖

MetaTraits 覆盖：

```text
1,638 / 2,478 = 66.1%
row-weighted: 114,325 / 145,607 = 78.5%
```

MetaTraits 性状维度：

```text
923 个 reconstructed trait_name
confirmed covered source 平均约 156.8 个 unique trait_name
```

主要性状类别包括：

- environmental preferences；
- morphology；
- metabolism；
- physiology；
- genome；
- enzymes；
- metabolites；
- safety；
- habitat/generalism。

### 4.2 BacDive 全量 closure 覆盖

BacDive closure 后 validated species-or-better：

```text
1,746 / 2,478 = 70.5%
row-weighted: 121,243 / 145,607 = 83.3%
```

Exact-strain evidence：

```text
exact_strain_main: 597 / 2,478 = 24.1%
exact_strain_conservative: 592 / 2,478 = 23.9%
exact_strain_hard: 555 / 2,478 = 22.4%
```

Culture collection availability among BacDive validated species-or-better：

```text
1,737 / 1,746 = 99.5%
```

### 4.3 MetaTraits 与 BacDive 覆盖互补

Main-policy overlap：

| Category | source_signature count |
|---|---:|
| both covered | 1,508 |
| BacDive only | 238 |
| MetaTraits only | 130 |
| neither | 602 |

这说明两者不是简单替代关系。MetaTraits 更适合提供性状矩阵，BacDive 更适合补充身份、可获得性和来源证据。

### 4.4 BacDive species-level representative strain expansion v2

对 BacDive species-level validated 的 1,149 个 source_signature 展开该 species 下多个 representative strain records。

v2 结果：

```text
species-level source_signatures: 1,149
expanded representative BacDive strain records: 52,956
sources with at least one representative record: 1,149 / 1,149 = 100.0%
sources with at least one culture collection number: 1,149 / 1,149 = 100.0%
```

其他元数据覆盖：

| Metadata type | source count | fraction |
|---|---:|---:|
| type-strain record | 1,099 / 1,149 | 95.6% |
| culture medium | 1,067 / 1,149 | 92.9% |
| isolation source | 1,089 / 1,149 | 94.8% |
| country / geographic source | 1,030 / 1,149 | 89.6% |
| genome accession | 1,086 / 1,149 | 94.5% |

解释边界：

- species-level representative strain 不等于原始 UniProt exact strain；
- 如果只在 species level 命中 BacDive，应标记为 representative strain availability；
- exact strain evidence 仍以 BacDive closure 中的 exact-strain policy 为准。

## 5. 文件夹结构

```text
metatraits_bacdive_microbe_trait_deliverable_2026-08-12/
├── README.md
├── MANIFEST.files
├── MANIFEST.sha256
├── manifest.json
├── 01_metatraits_species_coverage/
├── 02_bacdive_full_closure/
├── 03_bacdive_vs_metatraits_trait_comparison/
└── 04_bacdive_species_representative_strain_expansion/
```

## 6. 子目录说明

### 01_metatraits_species_coverage

MetaTraits 物种级覆盖结果。

| File | Meaning |
|---|---|
| `METATRAITS_SPECIES_LEVEL_COVERAGE_PROBE_2026-08-12.md` | MetaTraits coverage probe 报告 |
| `coverage_summary.json` | MetaTraits 覆盖汇总 |
| `source_signature_metatraits_coverage.csv` | 每个 source_signature 的 MetaTraits 覆盖状态 |

### 02_bacdive_full_closure

BacDive 全量 2,478 source closure 结果。

| File | Meaning |
|---|---|
| `bacdive_full_closure_report.md` | 本地 AI 生成的 BacDive closure 报告 |
| `bacdive_full_closure_audit.md` | 本地 AI 自审计 |
| `CODEX_LOCAL_AUDIT_BACDIVE_FULL_CLOSURE_2478_2026-08-12.md` | Codex 复核审计 |
| `bacdive_full_closure_summary.json` | closure 汇总数字 |
| `bacdive_full_closure_results.jsonl` | 2,478 个 source_signature 的完整 BacDive closure 明细 |
| `bacdive_full_designation_confidence.csv` | exact designation 强/中/弱证据分箱 |
| `bacdive_candidate_rescue_review.csv` | candidate_unvalidated rescue 明细 |
| `bacdive_candidate_rescue_synonym_rules.csv` | rescue 使用的 synonym/taxonomy rules |
| `bacdive_metatraits_overlap_summary.json` | BacDive 与 MetaTraits overlap 汇总 |
| `bacdive_metatraits_overlap_by_source_signature.csv` | 每个 source_signature 的 overlap 状态 |
| `bacdive_metatraits_overlap_by_group.csv` | 按 taxonomy group / resolution 的 overlap |
| `bacdive_metatraits_overlap_examples.csv` | overlap 示例 |

### 03_bacdive_vs_metatraits_trait_comparison

MetaTraits 与 BacDive 性状数量和类别对比。

| File | Meaning |
|---|---|
| `BACDIVE_VS_METATRAITS_TRAIT_AVAILABILITY_COMPARISON_2026-08-12.md` | 正式对比报告 |
| `metatraits_confirmed_trait_summary.json` | MetaTraits confirmed-covered trait 数量汇总 |
| `confirmed_comparable_trait_theme_summary.json` | 可比性状主题统计 |
| `metatraits_confirmed_group1_coverage.csv` | MetaTraits group_1 覆盖 |
| `metatraits_confirmed_group2_coverage.csv` | MetaTraits group_2 覆盖 |
| `metatraits_confirmed_top_trait_name_coverage.csv` | MetaTraits top trait_name 覆盖 |
| `source_level_bacdive_metatraits_trait_counts.csv` | 每个 source_signature 的 BacDive/MetaTraits trait count 对照 |

### 04_bacdive_species_representative_strain_expansion

BacDive species-level representative strain / culture collection expansion v2。

| File | Meaning |
|---|---|
| `CODEX_AUDIT_BACDIVE_SPECIES_REPRESENTATIVE_STRAIN_EXPANSION_V2_2026-08-12.md` | v2 展开结果审计 |
| `bacdive_species_representative_expansion_summary_v2.json` | v2 汇总 |
| `bacdive_species_representative_source_summary_v2.csv` | 每个 species-level source 的 representative strain 可获得性汇总 |
| `bacdive_species_representative_strain_records_v2.csv` | 展开的 52,956 条 BacDive representative strain records |

## 7. 推荐阅读顺序

建议先读：

1. `README.md`
2. `03_bacdive_vs_metatraits_trait_comparison/BACDIVE_VS_METATRAITS_TRAIT_AVAILABILITY_COMPARISON_2026-08-12.md`
3. `02_bacdive_full_closure/CODEX_LOCAL_AUDIT_BACDIVE_FULL_CLOSURE_2478_2026-08-12.md`
4. `04_bacdive_species_representative_strain_expansion/CODEX_AUDIT_BACDIVE_SPECIES_REPRESENTATIVE_STRAIN_EXPANSION_V2_2026-08-12.md`

如果需要查具体 source_signature：

- MetaTraits 覆盖看 `01_metatraits_species_coverage/source_signature_metatraits_coverage.csv`
- BacDive closure 看 `02_bacdive_full_closure/bacdive_full_closure_results.jsonl`
- BacDive representative strain / 保藏编号看 `04_bacdive_species_representative_strain_expansion/bacdive_species_representative_source_summary_v2.csv`
- 展开后的 strain record 明细看 `04_bacdive_species_representative_strain_expansion/bacdive_species_representative_strain_records_v2.csv`

## 8. 当前设计建议

后续微生物侧特征建议拆成两层：

### 8.1 Trait vector layer

主来源：MetaTraits

字段示例：

```text
metatraits_trait_vector_available
metatraits_trait_count
metatraits_group_1 / group_2 / trait_name encoded features
trait_resolution = species
```

### 8.2 Availability / provenance layer

主来源：BacDive

字段示例：

```text
bacdive_exact_strain_policy
bacdive_species_representative_available
bacdive_representative_record_count
bacdive_culture_collection_count
bacdive_has_type_strain_record
bacdive_has_culture_medium
bacdive_has_isolation_source
bacdive_has_country
bacdive_record_inclusion_basis
```

## 9. 解释边界

需要保持以下边界：

1. MetaTraits 是 species-level trait source，不应冒充 strain-level trait。
2. BacDive species representative strain records 不应冒充原始 UniProt exact strain。
3. BacDive exact-strain evidence 需要按 main / conservative / hard policy 分层。
4. 真菌在 BacDive 中属于 non-scope，不应计为 BacDive 查询失败。
5. 大 species 的 representative strain records 很多，建模时应使用 source-level summary 或 top-k/capped 方案，避免 record count 直接放大样本权重。

## 10. 结论

本次结果已经支持一个清晰的微生物侧特征集成方案：

```text
MetaTraits 提供主性状矩阵；
BacDive 提供 exact-strain evidence、species-level representative strain availability、保藏编号、培养基和分离来源。
```

这比单独使用任一数据库更稳健：MetaTraits 负责“性状全不全”，BacDive 负责“菌株/代表菌株是否可获得、来源是否可追溯”。

