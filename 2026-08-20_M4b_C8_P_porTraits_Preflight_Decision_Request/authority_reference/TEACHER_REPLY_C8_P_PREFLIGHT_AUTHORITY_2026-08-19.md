# 老师侧回复：C8 实装方案审定 + 两项新增口径裁定 + 弓赛 TP 路线评估验收（2026-08-19）

- 日期：2026-08-19
- 收件：陈浩然（主线 + 微生物侧）、弓赛（分支线，抄送）
- 状态：正式生效

对 2026-08-19 回包（陈浩然侧 C8 实装方案 + 两项新增口径问题；弓赛侧 pollutant TP prediction route evaluation）的独立审查与裁定。本文件为 08-19 正式生效文件，与 08-14 / 08-17 / 08-18 裁定合并执行。

---

## 一、整体进度判定（师生对齐，本轮修正）

```text
- 主线训练 / 排序模型（v1 冻结）：95%，已就绪，非瓶颈
- 智能体编排（底物→反应→酶→菌）：90%，10 节点全接线 + 真跑 PASS，非瓶颈
- 评估体系：100%，不再变动
- fallback 引擎（弓赛）：本轮修正 —— 之前「效果约 38% 未达标」的判定口径有误，
  经 08-19 TP route evaluation 澄清为分层路线（见裁定 5），不再按单一数字卡阈值
- 菌层（陈浩然）：C8 方案已批，启动 staged-only 实装
```

---

## 二、陈浩然（主线 + 微生物侧）

### 裁定 1：MetaTraits bulk TSV 落地 + C7-1 mapping rerun2 → 验收通过

```text
同意 MetaTraits 12 bulk TSV + 2 crosswalk 落晨羽结案，作为 C8 前置证据验收通过。

依据：
· 14/14 gzip test PASS + 14/14 SHA256 recorded；
· 官方 index 日期追溯到位（2026-06-10 10:23）；
· rerun2 修复 F3 / F12 false-positive，15/15 行 + 8/8 负断言通过；
· 数据源走本地 TSV，不依赖失效 MetaTraits API（符合 08-18 裁定要求）。

效力：C8 应直接引用 rerun2 映射口径
（C7_1_LONG_FORM_MAPPING_RERUN2_FALSE_POSITIVE_FIX_2026-08-19），
不得回退早期 header-only 映射。
```

### 裁定 2：C8 TraitFilterLayer staged-only 实装方案 → 批准启动

```text
同意 C8 按 C8-0 至 C8-5 六步启动 staged-only 实装。

依据：
· 输入契约完整（酶候选 / 酶资产 / UID→微生物 / Trait 来源，硬规则 fail-closed）；
· 输出契约 8 文件定义清楚，POLICY_MANIFEST 直接挂冻结契约 ID
  （trait_panel_id / feature_encoding_contract / metatraits_mapping_contract /
  teacher_authorization_id 四项引用正确）；
· 处理规则对齐 C7-1 / C7-2（observed-first、真菌 identity-only、F5 禁预测、
  软补齐仅 F1-F4 / F6-F8）；
· validator 四层检查（asset / mapping / trait / boundary）覆盖完整。

效力与边界：
· 产物严格 staged-only，不接 production、不改 production D4 / pool；
· 不 hard reject、不输出 trait_score、不输出未校准 confidence；
· C8-5 必须先 30-row bounded 复跑 + 小型候选表 smoke，老师确认后再全量。

工程推进点答复：
· C8-1 只读 lookup index 作为 staged 派生物生成 → 允许；
· 首轮 denominator → 保持 2,478 主 universe（见裁定 3）；
· 弓赛 fallback 联调 → 先用小型候选表做接口 smoke，再等效果整改后全量；
· C8 输出 → 仅展示 / 解释 / 覆盖统计，继续禁止 hard filtering 与 trait_score。
```

### 裁定 3：问题一（137 个 2,478 外新来源）→ 批准 delta review，不静默扩入

```text
同意学生建议：原 2,478 继续作为 C7 / C8 已审计主 universe，不静默改 denominator。

137 个 2,478 外 rescued-asset-linked source_signature（bacteria 88 /
archaea 6 / fungi 43）单开 C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW：
· 只做清点与标注，不并入生产或主训练资产；
· 字段按学生建议保留（source_signature / taxonomy_group /
  mapped_pass_uid_count / inside_original_2478_universe /
  metatraits_local_snapshot_covered / bacdive_closure_available_if_checked /
  recommended_status = PENDING_TEACHER_DECISION）。

若后续决定扩入，作为 C8 v1.1 staged universe，不改写原 2,478 历史口径。

依据：denominator 口径一旦静默改写，历史覆盖率统计不可比，属科学诚信红线。
```

### 裁定 4：问题二（porTraits）→ 不自动启动，另开受控 preflight

```text
同意学生建议：C8 v1 不自动启动 porTraits。

C8 v1 先按已冻结路线执行：
· observed-first；
· 本地 MetaTraits TSV lookup（rerun2 口径）；
· BacDive 只补身份 / 保藏编号 / 可获得性证据；
· 允许 predicted soft-fill 仅限已授权字段（F1-F4 / F6-F8），显式标注；
· 真菌 identity-only；
· staged-only。

对 MetaTraits 未覆盖的 bacteria（1,897 中 322 未覆盖）/ archaea
（153 中 90 未覆盖），另开受控 C8-P porTraits Genome Prediction Preflight：
· 只做只读环境核查 + genome FASTA 可获得性核查 +
  query_metatraits=none smoke test + 小样本 phenotype prediction；
· 输出 staged-only prediction evidence，
  source_type = porTraits_genome_prediction；
· 不写 production、不替换 observed、不把 predicted 写成实验事实。

真菌 428 株继续 identity-only，不使用 porTraits v1（v1 面向 prokaryotic
genomes），真菌预测走单独支线另行裁定。
```

---

## 三、弓赛（分支线）

### 裁定 5：pollutant TP prediction route evaluation → 验收通过 + 修正「38%」口径

```text
弓赛 08-19 提交的 pollutant TP prediction route evaluation 独立核对通过，
验收作为「38% 口径说明 + 根因诊断」的回应（08-18 欠账第一项已清）。

关键修正（老师侧之前「效果约 38% 未达标」判定口径有误，以本包为准）：
· 「38%」对应 ECLIPSE PREDEC OOF 的 Hit@10 = 38/81，是特定保守口径，
  不是整体 fallback 效果；此前未通过 report 完整读出，误判为整体未达标。
· 完整图景是分层路线，不是单一工具：

  ┌ enviPath 本地快照 lookup = 已知路径检索层
  │   Soil/Sludge 1788/1788 parent + 2924/2924 product 完整找回；
  │   这是数据库检索，不是盲预测准确率，不得写成 100% 预测。
  ├ BioTransformer ENVMICRO = 盲预测主基线
  │   BBD83 Hit@10 50/83；Soil/Sludge Hit@10 30.93%；当前最稳。
  └ ECLIPSE PREDEC = 补充候选源
      OOF Hit@10 38/81（保守）；all-fold 66/83（乐观）；
      仍低于 BioTransformer，保留为补充 / 后续优化对象。

裁定：
· 接受分层路线：enviPath lookup first + BioTransformer 主预测 +
  ECLIPSE PREDEC 补充；
· 红线：lookup 结果标注「已知路径检索 / 数据库证据」，不混入
  prediction Hit@K；BioTransformer / ECLIPSE 标注「模型预测候选」；
· 后续：按该分层路线设计系统，酶候选产出后与陈浩然 C8 菌性状层联调；
· 关联：该分层路线即台账 D3「C0 混合路线（检索优先 + 预测 fallback）」的
  技术预研；D2（fallback 选型）/ D3（混合路线）正式裁定仍等效果达标后签发。
```

### 3.1 弓赛剩余欠账（08-18 已列，继续追）

```text
[P0] ① R2 残留：tests/p5/test_p5_invariants.py:67 硬编码
  PROJECT_ROOT = "/Volumes/CC/..." → 改 config 注入，/Volumes/CC 清零
[P0] ② R1 数据面契约：缺 sync_assets.sh、无 .pkl/.csv；README 仍引用
  rxn2enzyme_positives.pkl → 交生成脚本 + 字段 schema + 小样本 + 源数据落晨羽
[P1] ③ 7.1 酶层映射验收表回包：交验收表（覆盖 / 命中 / 漏检口径）

DDL：①② 08-21 前；③ 随批跑一并回包。
```

---

## 四、上下游接口（本轮新增明确）

```text
弓赛分层路线（enviPath lookup → BioTransformer → ECLIPSE 补充）
  ↓ 产出酶候选表（pollutant / reaction / enzyme UID / source）
陈浩然 C8（TraitFilterLayer）
  ↓ 消费酶候选 → 菌性状 F1-F15 注解 → staged 展示 / 覆盖统计

接口约定：
· 弓赛产出的酶候选表字段对齐 C8 输入契约（query_id / pollutant /
  reaction_candidate / enzyme_uid / enzyme_candidate_source / rank）；
· 联调先走小型候选表 smoke，不等 fallback 全量效果整改；
· C8 不替弓赛判断反应预测器是否达标（各自边界独立）。
```

---

## 五、学生下一步

```text
【陈浩然】
1. 启动 C8-0 至 C8-4 staged-only 实装（先 C8-0 输入冻结 → C8-4 validator；
   C8-5 用 30-row bounded 复跑 + 小型候选表 smoke 后回包，待老师确认再全量）；
2. 生成 C8_DELTA_RESCUED_ASSET_SOURCE_SIGNATURE_REVIEW
   （137 个外来源清点表，recommended_status 保持 PENDING_TEACHER_DECISION）；
3. 若需推进 MetaTraits 未覆盖 bacteria / archaea，先交 C8-P preflight 方案，
   老师审定后再启动；
4. P18173 / P80550 澄清维持独立 table-only 任务，不随 C8 主包。

【弓赛】
1. 按分层路线（enviPath lookup first + BioTransformer + ECLIPSE 补充）
   推进系统设计，产出酶候选表供 C8 联调；
2. 清欠账①②（P0）+ 7.1 验收表③（P1）。

【DDL】
· 陈浩然 C8-0 ~ C8-4 实装 + 30-row bounded 复跑：08-22 前回包；
· 陈浩然 C8_DELTA + C8-P 方案：随 C8 主包一并（08-22 前）；
· 弓赛欠账①②：08-21 前；7.1 验收表：随批跑一并回包。
```

---

## 六、红线延续（随本裁定有效）

```text
1. 全部产物 staged-only，不接 production，mutation 三列保持 False；
2. 原 2,478 主 universe 口径不静默改写；137 外来源未裁定扩入前不并入；
3. porTraits 未授权前不启动；真菌不启用 porTraits v1 预测；
4. enviPath lookup 不得写成盲预测准确率；lookup 与 prediction Hit@K 不混；
5. 禁止用语继续生效（production backfill / UID replacement / 全量补齐）；
6. 无 hard rejection、无 trait_score、无未校准 confidence；
7. F5 保藏编号禁止预测；F8 不写成目标污染物直接降解事实；F15 不参与排序。
```

---

本裁定为 08-19 正式生效文件；与 08-14 / 08-17 / 08-18 裁定合并执行。
