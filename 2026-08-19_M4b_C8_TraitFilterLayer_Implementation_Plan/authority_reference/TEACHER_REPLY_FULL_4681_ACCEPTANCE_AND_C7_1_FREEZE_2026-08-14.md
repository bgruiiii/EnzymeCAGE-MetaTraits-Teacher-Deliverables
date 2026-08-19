# 老师侧回复：full 4,681 第二里程碑验收 + C7-1 逐项冻结 + BBD83 transport 验收

- 日期：2026-08-14
- 收件：陈浩然（主线+微生物侧）、弓赛（分支线，抄送）
- 状态：正式生效

---

## 一、独立验证结果（老师侧逐项复算，非采信学生审计）

```text
1. MANIFEST 校验：酶侧 22/22、微生物侧 5/5 全部 sha256 一致
2. full 4,681 状态表复算：
   总行 4,681 = unique UID 4,681（无重复、无缺失）
   PASS_AFDB_P2RANK_PREDICTED_POCKET_D4_LOADER  1,704
   BLOCKED_AFDB_P2RANK_NO_POCKET                1,324
   BLOCKED_AFDB_STRUCTURE_FETCH_FAILED          1,650
   BLOCKED_ESM2_3B_EXTRACTION_FAILED                3
   合计 4,681 ✓ 与 identity / README / 学生声称完全一致
3. mutation checks：4,681 行 × 3 列（formal / production pool / production D4）
   全 False，0 例外
4. evidence_tier：全部 4,681 = lower_evidence_predicted_pocket（红线措辞合规）
5. STAGED_ASSET_MANIFEST：10,224 行 = 1,704 UID × 6 资产，exists 全 True、
   sha256 全非空、bytes 全 >0；manifest UID 集与 PASS 集零差集
6. ≥10 UID 抽样复验（seed 20260814 抽取 12 个 PASS + 3 个 ESM2 失败）：
   72 件资产在晨羽 658M 归档内逐文件 sha256 与 manifest 逐字节一致；
   15 份 per_uid/REPORT.json final_status 与状态表一致，mutation 全 False
7. 晨羽归档：689,316,623 字节，sha256 = b01e7171…38bdd4 与 identity/README 一致
8. BBD83 transport 补交：晨羽 tar.gz 96,158 字节 sha256 = 6f8276fe1b…fc95b2
   与 identity 侧车逐字段一致（archive/sha256/bytes/single_root/manifest_sha256）
```

结论：**本轮 3 份交付（第二里程碑回包、C7-1 候选表、BBD83 transport 补交）全部通过老师侧独立验证，无任何不一致。**

## 二、裁定 1：第二里程碑验收通过（staged-only）

```text
同意 full 4,681 staged status table 结案，作为第二里程碑验收通过。

依据：
· 9 状态机全量落表（9 状态中 4 个非零：PASS 1,704 / NO_POCKET 1,324 /
  FETCH_FAILED 1,650 / ESM2_FAILED 3，其余 5 状态 0）；
· loader 仅 PASS 调用（loader_validation_called=True 只在 1,704 行），
  no-pocket/fetch-failed 行 loader 未调用，状态机语义正确；
· retryable 标志与 reason 字段逐行可审计；
· 边界措辞合规：不写成 production merge / 不写 4,681 全部补齐 /
  不写 strict AlphaFill 等价（README Boundaries 逐条对照通过）；
· mutation 全 False + evidence_tier 全 lower_evidence_predicted_pocket。

观察点（按 08-14 裁定预期，不追平）：
· fetch-failed 1,650（35.2%）与 no-pocket 1,324（28.3%）比例与 Phase 1
  （44% 类）偏差属预期，按实际统计；
· accession review 表对 1,650 fetch-failed 的 secondary 字段为空——
  README caveat 已如实声明，本包不声称做过 1,650 的二次审；
  8 个非病毒终查维持"只入表不替换"，accession review 关闭。

效力：1,704 套 staged 资产（6 件/UID：结构+pocket+特征+loader 验证记录）
入 staged 池，可被下游消费；不构成 production D4 merge，不改 production pool。
```

## 三、裁定 2：C7-1 trait panel 逐项冻结

```text
候选表 15 项，全部冻结（每项含允许/禁止引用 + 覆盖率 + 师姐讨论栏，
结构满足 08-14 裁定 §3 要求；覆盖口径 2478 菌株，5 类允许引用
与 08-12 裁定④一致）。

【第一屏冻结 5 项】
F1 oxygen_tolerance      —— observed 优先，predicted 软补齐须标注
F2 temperature           —— 同上
F3 pH                    —— 同上
F4 salinity              —— 同上
F5 bacdive_availability  —— observed 记录只读；禁止预测保藏编号；
                            代表株必须显式标注物种级（species representative），
                            不得写成原始 UniProt 精确株

【追问展开冻结 10 项】
F6 respiration_electron_acceptor —— 允许软补齐（resp 11.5% no-pred 缺口）
F7 carbon_and_substrate_utilization —— 仅广义代谢背景，非污染降解证据
F8 degradation_capacity_broad   —— 仅广义降解背景；禁止"可降解用户输入
    污染物"表述（红线：不得从该 trait 单独断言目标降解事实）
F9 enzyme_activity     —— 上下文标签，prediction-like 记录须标源
F10 motility           —— 生态/定殖背景，prediction-like 须标注
F11 cell_morphology    —— 表型背景
F12 cell_envelope_gram —— 表型背景
F13 sporulation        —— 应激/持久性背景
F14 genome_basic       —— 基因组背景；禁止 trait_score 语义
F15 habitat_generalism —— 有条件冻结：仅"追问展开的生态背景标签"；
    覆盖 14.4% 须在 UI 标注低覆盖；prediction-like/clustering 源须标注；
    不参与任何排序/评分/推荐

【全局约束（随冻结生效）】
· 真菌 428 株：identity-only 展示，不启用任何 predicted 软补齐；
· observed 永远优先，predicted 永不覆盖 observed（表内逐项重申）；
· 全 panel 无 hard rejection、无未校准置信度、无 trait_score；
· policy manifest fail-closed 门禁按 08-13 蓝图执行；
· 冻结后特征编码提案（C7-2）须引用本冻结表条目 ID（F1-F15）。
```

## 四、裁定 3：BBD83 209a4b4 transport 补交验收通过

```text
· 晨羽 tar.gz + identity 侧车已就位，sha256 逐字段匹配；
· 归档与 08-12 return 目录字节一致；
· MANIFEST.sha256 self-hash 约定已知 caveat，沿用 08-12 审计记录；
· 科学闭包 NOT_CLAIMED 认可（本包仅收 transport 缺口，不改科学覆盖结论）；
· v4.2（9240ded）归因验证老师侧已完成：76 无候选 = 63 无兼容位点 +
  9 候选化学无效 + 4 donor case_012 阻塞 + 2 兜底降级；coverage 7/83。
```

## 五、学生下一步

```text
【陈浩然】
1. 启动 C7-2：feature encoding 提案（引用 F1-F15 条目 ID，真菌 identity-only）；
2. 1,650 fetch-failed 二次 accession 复核可择机启动（独立于验收，非前置）；
3. 等待 TraitFilterLayer 实装授权路径（C7-3 起按蓝图顺序执行）。

【弓赛】
1. R1 收口 4 项（p1_preflight.py / authority docs 6 份 / data 装配契约 /
   复现命令合同）——晨羽 9240ded 已同步，全量回归不可复现待整改；
2. BBD83 v4.2 无需重跑（老师侧已完成），确认产物契约一致即可。

【下一步衔接】
· full 4,681 结案 → 完成度按 74% 基线重算（第二里程碑 +11%）；
· 1704 套 staged 资产进入下游（菌层 feature 消费、fallback 融合评估）；
· C7-2 提案回包后老师侧 48h 内出编码冻结意见。
```

## 六、红线延续（随本裁定有效）

```text
1. P2Rank predicted-pocket = lower-evidence tier；
2. 全部产出先 staged，不写 production D4、不改 production pool；
3. FORMAL_ASSET_MUTATION_CHECK 四红线保持 false（本次全量复核 0 例外）；
4. 禁止用语继续生效（见 08-14 裁定 §6 清单）；
5. 本裁定验收 staged 池与冻结 trait panel，不构成 production merge /
   TraitFilterLayer production 接入授权。
```

---

## 七、老师侧后续推进方案（已处理，随本裁定生效）

以下三项基于 08-14 回包信息资产直接产出，供学生侧衔接执行；不改变红线。

### 7.1 fallback 融合提案（策略冻结）

```text
依据：BBD83 83 底物中 76 无候选归因（63 科学无位点 + 9 化学无效 +
4 donor 阻塞）＋ ENVMICRO 对照 62/63（98.4%）生成候选反应，仅 OP=O 无规则。

融合架构（反应层 → 酶层两级）：
· 反应层：主路线 BioTransformer ENVMICRO 为兜底生成器；BBD83 donor
  规则引擎命中时优先，未命中走主路线；产物统一标注来源
  （donor_rule / envmicro_fallback）。
· 酶层：候选反应 → rxn2enzyme 正向映射表（契约：mapping_table +
  matched_reactants + evidence）；酶层映射未打通前只出反应候选，
  不声明酶候选。

合并去重规则：
· 同 UID 同反应：去重保留高证据源（observed > donor_rule > envmicro）；
· ALL_CANDIDATES_CHEMICALLY_INVALID 维持原判定（化学无效为硬事实，
  不因融合翻转）；
· NO_COMPATIBLE_SITE → 主路线候选（标注 fallback，soft）；
· 禁止：hard rejection、未标注预测、"可降解目标污染物"断言。

验收口径：
· 反应层覆盖：7/83 → 预期 ≥ 62/83（OP=O 1 个预期维持无规则）；
· 酶层覆盖：rxn2enzyme 打通后实测；
· 证据标注完整率 100%（无未标注来源产物）。

待学生执行：主路线酶层映射打通 + 融合批跑 + 验收表回包。
```

### 7.2 训练 data loader 契约（v1 冻结）

```text
输入：staged_assets/{UID}/ 六件套（pocket PDB / pocket_info.csv /
seq2feature.pkl / esm_node_feature.torch.pt / gvp_protein_feature_flat.pt /
validation_input.csv）。

硬性校验（fail-closed，任一不过即排除该 UID 并记录）：
· esm_node_feature_shape[0] == p2rank_pocket_residue_count（精确相等）；
· same_pocket_for_esm_node_and_gvp == True；
· loader_validation_status == PASS 且 dataset0_constructed == True；
· formal_assets_mutated / production_pool_mutated / production_d4_mutated
  三列均 False；
· sequence_sha256 与 manifest 一致；evidence_tier=
  lower_evidence_predicted_pocket。

去重：按 sequence_sha256 全局去重（当前 1,704 资产 → 1,597 唯一序列）；
训练集形态由此确定，不引入额外序列。

输出契约：TRAIN_SET_MANIFEST.csv（UniprotID / sequence_sha256 /
esm_shape / gvp_available / same_pocket / loader_status / split 占位）；
下游训练脚本只允许消费该清单内资产。

待学生执行：C7-2 提案按本契约设计 feature encoding，回包后 48h 冻结。
```

### 7.3 菌层特征消费接口草案（v0.1，供 C7-2 引用）

```text
定位：1,597 唯一酶序列资产 → 酶-菌株映射 → TraitFilterLayer 输入。

输入契约（每酶候选一条）：
· asset 侧：uid、sequence_sha256、esm_shape、pocket_score；
· 映射侧：uid → 菌株列表（映射表来源、映射方法、覆盖率）；
· panel 侧：F1-F15 每项注解——observed 字段（来源 DB + 证据强度）/
predicted 软补齐字段（模型 + 标注 fallback）/ 真菌条目 identity-only
  标志；无信息项显式标注 NOT_OBSERVED。

输出契约：trait_annotation.jsonl（每条：uid、菌株、F1-F15 注解、
evidence 标签、覆盖状态）；聚合口径按条目 ID（F1-F15）统计覆盖率
与缺失率，不允许聚合归并丢失条目 ID。

边界：本接口只做特征消费（标注与覆盖统计），不做过滤决策；
过滤决策属 TraitFilterLayer 蓝图范围（C7-3 起）。

待学生执行：C7-2 提案须引用本接口条目 ID，逐项对接。
```

### 7.4 学生衔接清单（随本方案生效）

```text
陈浩然：
· C7-2 提案按 7.2 loader 契约设计 feature encoding，并引用 7.3 接口 ID；
· 1,650 fetch-failed 二次 accession 复核可择机（非前置）。

弓赛：
· 按 7.1 打通主路线酶层映射（rxn2enzyme）并批跑融合，回包验收表；
· R1 收口 4 项维持（晨羽 9240ded 整改）。

验收承诺：学生按上表回包后，老师侧 48h 内出冻结/裁定意见。
```

---

本裁定为 08-14 第二份正式生效文件；与
TEACHER_REPLY_M4_E2_SECOND_MILESTONE_AND_M4B_C7_AUTHORIZATION_2026-08-14.md
合并执行。

（§七 追加于 08-14 收口完成后：P0DXV0 +1 PASS，1,704 → 1,705 有效口径，
见 TEACHER_REVIEW_FINDINGS_3LINE_2026-08-14.md 收口记录）
