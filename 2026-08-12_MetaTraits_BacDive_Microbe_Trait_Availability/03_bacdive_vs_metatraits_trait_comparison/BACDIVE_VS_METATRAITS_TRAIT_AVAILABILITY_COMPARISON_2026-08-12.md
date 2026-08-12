# BacDive 与 MetaTraits 性状可获得性对比报告

Date: 2026-08-12

## 1. 对比目的

本报告比较 BacDive 与 MetaTraits 在 EnzymeCAGE 微生物侧 host/source signature 集合上的性状可获得性。当前问题不是评价哪一个数据库“绝对更好”，而是回答：

1. 如果不强求落到菌株、接受物种级别，哪个来源能提供更多性状信息；
2. 两个来源分别覆盖多少 UniProt-derived source signatures；
3. 在可比性状类别上，哪个来源更完整；
4. 哪些性状类别主要由其中一个数据库提供；
5. 后续集成时应如何分工使用。

## 2. 输入与比较口径

本次比较使用同一个 final clean microbe source universe：

```text
source_signature 总数: 2,478
row-weighted enzyme-source rows: 145,607
```

使用的本地结果文件：

```text
BacDive closure results:
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/16_MetaTraits_Integration_Research_2026-07-15/bacdive_metatraits_hybrid_probe_2026-08-12/bacdive_full_closure_2478_2026-08-12/bacdive_full_closure_results.jsonl

MetaTraits coverage table:
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/16_MetaTraits_Integration_Research_2026-07-15/metatraits_species_coverage_probe_2026-08-12/source_signature_metatraits_coverage.csv

MetaTraits local snapshot:
data/metatraits/ncbi_species_summary_all.tsv.gz
```

重要口径说明：

- BacDive 当前结果是从 API 返回中抽取的 12 个指定字段，统计时只计算 `trait_summary` 中真正非空的字段。
- MetaTraits 是本地物种级性状汇总表，包含大量标准化 `trait_name` 行。其 `trait_count` 不是字段数，而是 trait rows / trait entries 的数量。
- 因此，不能直接把 “BacDive 12 个字段” 与 “MetaTraits 923 个 trait_name” 当成同一种单位比较；更合理的比较方式是：
  - 先比 source coverage；
  - 再比每个已覆盖 source 的性状密度；
  - 最后按可比主题比较，例如温度、氧需求、革兰氏染色、运动性、代谢利用等。

## 3. Source coverage 总体对比

| 指标 | BacDive | MetaTraits |
|---|---:|---:|
| source_signature 总数 | 2,478 | 2,478 |
| 可用覆盖数 | 1,746 | 1,638 |
| 覆盖率 | 70.5% | 66.1% |
| row-weighted 覆盖 | 121,243 / 145,607 | 114,325 / 145,607 |
| row-weighted 覆盖率 | 83.3% | 78.5% |

BacDive 的 1,746 是 closure 后的 validated species-or-better 覆盖，包括 exact strain、validated species-level，以及保守规则救回的 validated species records。MetaTraits 的 1,638 来自 `union_in_ncbi_all=True`。

两者覆盖交集如下：

| 覆盖关系 | source_signature 数 |
|---|---:|
| BacDive 与 MetaTraits 都覆盖 | 1,508 |
| 只有 BacDive 覆盖 | 238 |
| 只有 MetaTraits 覆盖 | 130 |
| 两者都未覆盖 | 602 |

这说明两个数据库并非简单替代关系：BacDive 多覆盖了一部分 MetaTraits 没覆盖的 source，MetaTraits 也补到了部分 BacDive 没覆盖的 source。

## 4. 性状数量总体对比

| 指标 | BacDive | MetaTraits |
|---|---:|---:|
| 当前提取的性状字段 / trait name 种类 | 12 个字段 | 923 个 trait_name |
| 已覆盖 source 上的非空 trait cells / trait rows | 8,027 个非空字段值 | 256,668 个 trait rows |
| 每个已覆盖 source 平均性状数量 | 4.60 个非空字段 | 156.76 个 unique trait_name |
| 每个已覆盖 source 中位性状数量 | 未单独统计 | 154 个 unique trait_name |

结论很直接：如果目标是“不一定到菌株，只要在物种级拿到尽可能丰富的性状向量”，MetaTraits 明显更完整。BacDive 当前抽取层更像身份与培养/来源证据表，不是高维性状矩阵。

## 5. 可比性状类别对比

以下表格按 2,478 个 source_signature 为统一分母。BacDive 使用 validated species-or-better closure 结果中的非空字段；MetaTraits 使用 confirmed-covered source 中对应 `group_1/group_2` 类别。

| 性状主题 | BacDive 有值 source | BacDive 覆盖率 | MetaTraits 有值 source | MetaTraits 覆盖率 |
|---|---:|---:|---:|---:|
| 革兰氏染色 | 446 | 18.0% | 1,637 | 66.1% |
| 细胞形态 | 429 | 17.3% | 1,613 | 65.1% |
| 运动性 | 413 | 16.7% | 1,626 | 65.6% |
| 氧需求 / atmosphere | 754 | 30.4% | 1,631 | 65.8% |
| 温度相关 | 1,391 | 56.1% | 1,638 | 66.1% |
| 代谢物利用 / metabolite tests | 743 | 30.0% | 1,628 | 65.7% |
| 酶活性 | 0 | 0.0% | 1,611 | 65.0% |
| Biosafety | 0 | 0.0% | 1,477 | 59.6% |
| pH | 当前未抽取 | - | 1,621 | 65.4% |
| 盐度 | 当前未抽取 | - | 1,622 | 65.5% |
| 基因组大小 / GC / gene count | 当前未抽取 | - | 1,620 | 65.4% |
| 培养基 | 1,159 | 46.8% | 未作为同类 trait 提供 | - |
| 分离来源 / 国家 | 1,346 | 54.3% | Habitat generalism 356 | 14.4% |

从可比类别看，MetaTraits 在大多数标准性状维度上覆盖更全，尤其是：

- morphology；
- motility；
- oxygen / atmosphere；
- metabolism；
- enzyme activity；
- genome traits；
- pH；
- salinity；
- biosafety。

BacDive 的相对强项是：

- exact strain / culture collection / genome accession 级身份证据；
- culture medium；
- isolation source；
- country / geographic source；
- 对部分 exact strain 的字段密度较高。

## 6. MetaTraits 主要提供但 BacDive 当前抽取没有或很弱的性状

MetaTraits 在本集合中覆盖的 `group_1` 类别如下：

| MetaTraits group_1 | 覆盖 source 数 | 占 2,478 比例 |
|---|---:|---:|
| Environmental preferences | 1,638 | 66.1% |
| Morphology | 1,637 | 66.1% |
| Metabolism | 1,630 | 65.8% |
| Physiology | 1,628 | 65.7% |
| Genome | 1,620 | 65.4% |
| Enzymes | 1,611 | 65.0% |
| Metabolites | 1,604 | 64.7% |
| Safety | 1,477 | 59.6% |
| Habitat | 356 | 14.4% |

其中对 EnzymeCAGE 微生物侧最有价值、且 BacDive 当前抽取没有充分提供的包括：

- genome traits：GC percentage、genome size、gene count、coding density；
- pH traits：pH growth、pH minimum、pH maximum、pH preference；
- salinity traits：salinity growth、minimum、maximum、preference；
- enzyme activity：大量实验/注释来源的 enzyme activity trait；
- catabolic / degradation traits：aromatic compound、hydrocarbon、cellulose、chitin、lignin、plastic 等降解相关性状；
- respiration / electron acceptor / denitrification / nitrification 等代谢生态性状；
- biosafety level。

这些维度更接近“物种级微生物生态/代谢性状向量”，适合做模型特征。

## 7. BacDive 主要提供但 MetaTraits 不直接替代的内容

BacDive 当前结果中更有独特价值的是身份链和培养/来源信息：

| BacDive 字段 | 有值 source 数 | 占 2,478 比例 | 说明 |
|---|---:|---:|---|
| culture_medium | 1,159 | 46.8% | 培养条件信息，MetaTraits 不主要提供同类字段 |
| isolation_source | 1,346 | 54.3% | 分离来源，MetaTraits 只有较粗的 habitat/generalism 类信息 |
| country | 1,346 | 54.3% | 地理来源信息 |
| exact strain identity | 597 | 24.1% | 可由 genome accession、保藏号或 strain designation 锁定 |
| hard exact strain identity | 555 | 22.4% | 仅 genome accession + culture collection exact match |

因此 BacDive 不应该被简单看成“MetaTraits 的弱版”。它在菌株证据、保藏号、培养基、分离来源上有独特价值。

## 8. 判断：如果不强求菌株，是否性状越全越好

如果当前目标是为 EnzymeCAGE 加入微生物侧 host/source traits，并且允许只到 species level，那么总体上“性状越全越好”这个方向是成立的，但需要加两个限定：

1. 性状必须有稳定语义和可解释编码，不能只追求数量。
2. 物种级性状不能冒充菌株级性状；需要在特征表中保留 `trait_resolution=species` 或类似字段。

在这个前提下，MetaTraits 更适合作为主性状矩阵来源，因为它给到的 trait dimensions 更丰富、覆盖更均衡。BacDive 更适合作为补充层，用来增强身份可信度、培养条件、分离来源和 exact-strain evidence。

## 9. 建议的集成策略

建议不要二选一，而是采用分层集成：

1. 主性状矩阵：MetaTraits
   - 作为 species-level host trait vector 主体。
   - 优先纳入 environmental preferences、morphology、physiology、metabolism、genome、enzymes、safety 等标准字段。

2. 身份与来源补充：BacDive
   - 记录 exact strain / hard exact strain 证据；
   - 补充 culture medium、isolation source、country；
   - 对 BacDive-only 的 238 个 source，可以作为 MetaTraits 覆盖缺口的补充。

3. 明确分辨率标签
   - `species_level_metatraits`
   - `bacdive_exact_strain`
   - `bacdive_validated_species`
   - `bacdive_culture_or_isolation_metadata`

4. 不建议做的事情
   - 不应把 BacDive species candidate_unvalidated 直接当成命中；
   - 不应把 MetaTraits species-level trait 说成 strain-level trait；
   - 不应只按 trait row 数量判断数据库质量，还要看 trait 是否可编码、是否与模型任务相关。

## 10. 结论

在当前 2,478 个 source_signature universe 上：

- BacDive closure 后覆盖略高：1,746 / 2,478，约 70.5%；
- MetaTraits 覆盖为 1,638 / 2,478，约 66.1%；
- 但 MetaTraits 的性状维度远多于 BacDive 当前抽取字段：923 个 trait_name，已覆盖 source 平均约 156.8 个 unique trait；
- BacDive 当前抽取只有 12 个字段，validated covered source 平均约 4.6 个非空字段；
- 如果允许物种级特征，MetaTraits 更适合作为主性状来源；
- BacDive 更适合作为 exact-strain 身份证据与 culture/isolation/source metadata 补充。

推荐后续把微生物侧特征设计为“MetaTraits 主体 + BacDive 证据/培养来源补充”的 hybrid schema，而不是把二者强行互斥选择。

