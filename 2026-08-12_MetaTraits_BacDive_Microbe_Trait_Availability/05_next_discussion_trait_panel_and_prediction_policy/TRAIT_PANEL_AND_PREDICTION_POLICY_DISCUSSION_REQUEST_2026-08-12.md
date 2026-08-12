# 微生物侧性状面板与预测性状使用策略：待讨论问题清单

Date: 2026-08-12

## 1. 背景

当前微生物侧探索已经形成一个初步稳定的 hybrid 设计：

```text
MetaTraits = primary species-level trait matrix
BacDive = exact-strain evidence + species-level representative strain availability + culture collection numbers + culture medium + isolation/source metadata
```

现有结果表明，MetaTraits 更适合作为主性状矩阵来源，BacDive 更适合补充菌株身份、保藏编号、培养基和分离来源。

但进入后续 schema / feature 设计前，还有一个核心问题需要讨论：

```text
当某个物种的部分关键性状没有实验观测值时，是否允许使用 MetaTraits prediction 补齐？
```

这个问题尤其影响：

- 真菌来源；
- 只覆盖部分性状的细菌/古菌来源；
- 污水污染物降解任务中应优先保留哪些性状；
- observed trait 与 predicted trait 在模型中是否等价，或是否需要分层编码。

## 2. 当前结果对这个问题的提示

### 2.1 MetaTraits all vs no_predictions

在当前 2,478 个 source_signature universe 上：

| MetaTraits snapshot | 覆盖 source_signature | unique trait_name | covered source 平均 unique trait_name | 中位数 |
|---|---:|---:|---:|---:|
| `ncbi_species_summary_all.tsv.gz` | 1,638 | 923 | 156.8 | 154 |
| `ncbi_species_summary_no_predictions.tsv.gz` | 1,638 | 850 | 47.7 | 42 |

解释：

- `all` 和 `no_predictions` 在当前 source 层面的覆盖数相同，都是 1,638；
- 但 `all` 的性状密度明显更高；
- 因此 prediction-like 信息目前主要不是增加“能覆盖多少物种”，而是增加“每个已覆盖物种有多少性状维度”。

### 2.2 真菌覆盖问题

当前 universe 中：

| taxonomy group | source_signature count | MetaTraits all covered | MetaTraits no_predictions covered |
|---|---:|---:|---:|
| target_bacteria | 1,897 | 1,575 | 1,575 |
| target_archaea | 153 | 63 | 63 |
| target_fungi | 428 | 0 | 0 |

BacDive 主要面向 prokaryotes，因此真菌在 BacDive 中被标记为 non-scope。当前 MetaTraits 本地 NCBI species summary 对这 428 个真菌 source 也没有覆盖。

因此，真菌需要单独讨论，不应简单算作 BacDive failure。可选方向包括：

1. 暂时不做真菌性状，只保留 taxonomy/source identity；
2. 寻找真菌专用数据库或资源；
3. 对真菌采用预测性状，但需要单独标注 prediction source 和置信度；
4. 在 v1 中排除真菌性状特征，仅在后续版本补充。

## 3. 当前可获得的 MetaTraits 性状类别

### 3.1 `all` snapshot 中覆盖较广的 group_2

| group_1 | group_2 | covered source count |
|---|---|---:|
| Environmental preferences | Temperature | 1,638 |
| Morphology | Cell envelope | 1,637 |
| Environmental preferences | Atmosphere | 1,631 |
| Metabolism | Produces metabolite | 1,629 |
| Metabolism | Hydrolase activity | 1,627 |
| Physiology | Motility | 1,626 |
| Physiology | Sporulation | 1,623 |
| Environmental preferences | Salinity | 1,622 |
| Environmental preferences | pH | 1,621 |
| Metabolism | Fermentation | 1,621 |
| Metabolism | Reduction | 1,621 |
| Genome | Composition | 1,620 |
| Genome | Gene content | 1,620 |
| Genome | Genome size | 1,620 |
| Metabolism | Catabolic process | 1,615 |
| Metabolism | Carbon utilization | 1,614 |
| Morphology | Cell morphology | 1,613 |
| Enzymes | Enzyme activity | 1,611 |
| Metabolism | Respiration | 1,611 |
| Metabolism | Denitrification | 1,608 |
| Metabolism | Electron acceptor | 1,608 |
| Metabolism | Nitrification | 1,608 |
| Metabolites | Metabolite tests | 1,604 |
| Metabolism | Utilizes metabolite | 1,591 |
| Safety | Biosafety level | 1,477 |

### 3.2 `no_predictions` snapshot 中覆盖较广的 group_2

| group_1 | group_2 | covered source count |
|---|---|---:|
| Morphology | Cell envelope | 1,627 |
| Genome | Composition | 1,620 |
| Genome | Gene content | 1,620 |
| Genome | Genome size | 1,620 |
| Environmental preferences | Temperature | 1,606 |
| Environmental preferences | Atmosphere | 1,528 |
| Morphology | Cell morphology | 1,507 |
| Safety | Biosafety level | 1,477 |
| Physiology | Motility | 1,454 |
| Physiology | Sporulation | 1,262 |
| Enzymes | Enzyme activity | 1,150 |
| Metabolism | Produces metabolite | 1,125 |
| Metabolism | Hydrolase activity | 1,021 |
| Metabolites | Metabolite tests | 934 |
| Environmental preferences | Salinity | 919 |
| Metabolism | Fermentation | 788 |
| Metabolism | Reduction | 695 |
| Metabolism | Carbon utilization | 576 |
| Metabolism | Catabolic process | 505 |
| Environmental preferences | pH | 420 |

解释：

- 观测值本身已经覆盖了大量基础性状，例如 genome、temperature、atmosphere、cell envelope、cell morphology、biosafety、motility；
- 但对污染物降解很重要的部分代谢生态性状，例如 catabolic process、carbon utilization、pH、salinity、electron acceptor / denitrification / nitrification，在 `all` 中明显更完整；
- 因此是否允许 prediction 进入这些性状类别，需要按任务价值和风险分层讨论。

## 4. 当前可获得的 BacDive 补充信息

BacDive 不建议作为主性状矩阵，但它对实验可获得性和来源追溯很关键。

当前 BacDive closure 结果：

```text
validated species-or-better: 1,746 / 2,478 = 70.5%
exact_strain_main: 597 / 2,478 = 24.1%
hard exact strain: 555 / 2,478 = 22.4%
```

BacDive species-level representative strain expansion v2：

```text
species-level BacDive validated source_signatures: 1,149
expanded representative BacDive strain records: 52,956
with at least one representative strain record: 1,149 / 1,149 = 100.0%
with at least one culture collection number: 1,149 / 1,149 = 100.0%
```

可补充字段：

- exact-strain evidence tier；
- representative strain record count；
- culture collection number count；
- type-strain availability；
- culture medium；
- isolation source；
- country / geographic source；
- genome accession availability。

## 5. 建议讨论的核心性状面板

下面不是最终裁定，而是建议交给 domain review 的候选面板。

| 候选性状模块 | 示例 trait / field | 建议优先级 | 原因 |
|---|---|---|---|
| oxygen tolerance / atmosphere | aerotolerant, oxygen preference, obligate aerobic, obligate anaerobic, facultative anaerobe | high | 决定好氧/厌氧污水环境适配性 |
| temperature | temperature growth, min, max, preference | high | 决定处理温度下能否生长 |
| pH | pH growth, min, max, preference, acidophilic | high | 污水 pH 适配性强相关 |
| salinity | salinity growth, min, max, preference | medium-high | 工业/高盐废水重要 |
| pollutant/catabolic process | degradation: aromatic compound, aromatic hydrocarbon, hydrocarbon, lignin, plastic, cellulose, chitin | high | 与污染物降解能力最接近 |
| substrate/carbon utilization | carbon source, utilizes metabolite, metabolite tests | high | 反映底物范围和代谢灵活性 |
| respiration/electron acceptor | respiration, denitrification, nitrification, electron acceptor traits | high | 对厌氧/缺氧/硝化反硝化环境重要 |
| enzyme activity | oxidase, catalase, hydrolases, arylamidases, glycosidases 等 | medium-high | 可作为代谢能力侧证，但不一定直接对应目标污染物 |
| biosafety | biosafety level | high as warning/filter | 后续实际菌株选择必须考虑 |
| motility | presence of motility | medium | 影响迁移、定殖和接触污染物能力 |
| sporulation | sporulation | medium | 反映环境胁迫下存活能力 |
| gram/cell envelope | gram positive / negative | medium | 影响膜通透性和环境耐受 |
| genome basic traits | GC, genome size, gene count, coding density | medium | 间接反映基因组规模和注释能力 |
| habitat/generalism | generalism score, generalist, habitat count | medium | 生态广适性参考，但当前覆盖较低 |
| BacDive availability/provenance | culture collection, type strain, culture medium, isolation source, country | high for practical follow-up | 不作为主 trait vector，但决定可获得性和实验复现路径 |

## 6. observed / predicted 使用策略讨论选项

### 方案 A：只用 observed traits

优点：

- 最保守；
- 可解释性强；
- 不引入预测偏差。

缺点：

- 每个物种性状维度明显减少；
- 对污染物降解相关的部分代谢生态性状覆盖不足；
- 真菌问题仍无法解决。

当前数据提示：

```text
no_predictions mean unique traits per covered source: 47.7
all mean unique traits per covered source: 156.8
```

### 方案 B：核心性状 observed 优先，缺失时允许 predicted 补齐

优点：

- 能保留高价值核心性状；
- 避免因为部分 observed 缺失导致整个 source 无法使用；
- 可通过 provenance 字段区分 observed / predicted。

缺点：

- 需要 domain review 先定义核心性状面板；
- 需要明确哪些 trait category 可以预测补齐，哪些不能；
- 模型中需要保留 prediction flag / confidence flag。

建议如果采用该方案，字段至少包含：

```text
trait_value
trait_source = MetaTraits
trait_evidence_type = observed | predicted | missing
trait_resolution = species
trait_category
trait_name
```

### 方案 C：observed 和 predicted 分开编码

优点：

- 不把实验观测和预测结果混为一类；
- 模型可以学习 observed 与 predicted 的可信度差异；
- 审计最清楚。

缺点：

- 特征维度增加；
- 需要更细的 schema 和缺失值策略。

可选编码：

```text
trait_value_observed
trait_value_predicted
trait_observed_available
trait_predicted_available
```

## 7. 需要与 domain reviewer 讨论的问题清单

建议今晚重点讨论以下问题：

1. 是否同意采用 hybrid schema：

   ```text
   MetaTraits 主性状矩阵 + BacDive 可获得性/保藏编号/来源补充
   ```

2. 对真菌 source 如何处理？

   - 暂不加入真菌性状；
   - 寻找真菌专用 trait 数据库；
   - 使用预测性状；
   - 只保留 taxonomy/source identity，不作为 trait-rich source。

3. 对污染物降解任务，哪些性状必须进入核心面板？

   候选高优先级：

   - oxygen tolerance / atmosphere；
   - temperature；
   - pH；
   - salinity；
   - catabolic process / degradation traits；
   - substrate/carbon utilization；
   - respiration/electron acceptor；
   - enzyme activity；
   - biosafety；
   - BacDive culture collection / availability。

4. 对核心面板中 observed 缺失的 trait，是否允许用 predicted 补齐？

5. 哪些性状类别可以使用 predicted？

   可能较适合 prediction 补齐：

   - pH / salinity / temperature preference；
   - aerobic/anaerobic preference；
   - broad catabolic process；
   - broad substrate utilization；
   - respiration/electron acceptor。

   可能需要更谨慎：

   - biosafety；
   - exact pollutant degradation capability；
   - strain-specific traits；
   - culture availability。

6. observed 与 predicted 在模型里是否等价？

   建议不等价，应保留：

   ```text
   evidence_type = observed | predicted
   ```

7. 如果一个物种某个核心性状 observed 缺失，但 predicted 存在，是否：

   - 直接填 predicted；
   - 只作为 soft feature；
   - 同时保留 missing flag；
   - 或者只在解释/排序层使用，不进入训练主特征。

8. BacDive 的 representative strain 是否只作为可获得性证据？

   建议：

   ```text
   species representative strain availability yes/no
   culture collection count
   representative record count
   type strain available yes/no
   ```

   不建议把 species representative strain traits 写成原始 UniProt exact strain traits。

9. 是否需要为每个 source 输出一个最终 trait provenance table？

   建议需要。每个 trait value 都应可追踪：

   ```text
   source_signature
   species_name
   trait_name
   trait_value
   evidence_type
   database
   resolution
   missing_reason
   ```

10. 是否授权进入下一步 production schema / feature encoding？

    当前结果支持 schema 设计，但 implementation 仍需单独授权。

## 8. 推荐的当前立场

建议采用中间路线：

```text
MetaTraits observed traits 优先；
对 domain-defined core traits，如果 observed 缺失且 MetaTraits predicted 存在，可作为 predicted soft feature 补齐；
observed 与 predicted 必须分开标注，不混成同一证据等级；
BacDive 只承担 exact-strain / representative strain availability / culture collection / provenance layer。
```

这能避免两个极端：

- 只用 observed 导致核心性状缺失太多；
- 无条件使用 predicted 导致证据等级混淆。

## 9. 配套文件

本目录提供三个辅助表：

| File | Meaning |
|---|---|
| `prediction_policy_discussion_summary.json` | observed vs all/prediction-like 总体统计 |
| `metatraits_observed_vs_all_group2_summary.csv` | MetaTraits group_2 在 all 与 no_predictions 中的覆盖对比 |
| `metatraits_observed_vs_all_trait_catalog.csv` | 每个 MetaTraits trait_name 的 all/no_predictions 覆盖对比 |
| `metatraits_coverage_by_taxonomy_group.csv` | bacteria/archaea/fungi 覆盖对比 |
| `proposed_pollutant_degradation_trait_panel_for_domain_review.csv` | 建议交给 domain review 的污染物降解微生物性状面板 |

