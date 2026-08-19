# 老师侧裁定：C7-2 冻结 + 1,650 Accession 复核验收（2026-08-17）

对陈浩然侧 2026-08-16 回包（C7-2 feature encoding 提案 + M4 E2 1,650
fetch-failed accession 二次复核）的独立审查与裁定。本文件为 08-17 正式
生效文件，与 08-14 两份裁定合并执行。

---

## 一、C7-2 feature encoding 提案：独立核对 8 项全过 → 冻结

审查对象：`M4B_C7_2_FEATURE_ENCODING_PROPOSAL_2026-08-15.md`（529 行）
+ 本地审计。独立核对结果：

```text
1. 权威引用：以 08-14 FULL_4681_ACCEPTANCE 裁定为 primary authority，
   编号说明（蓝图 C7-2/3 拆分为最新裁定覆盖）正确
2. 7.2 loader 契约对齐：TRAIN_SET_MANIFEST 字段 ⊇ 契约（UniprotID/
   sequence_sha256/esm_shape/p2rank_pocket_residue_count/same_pocket/
   loader_validation_status/dataset0/evidence_tier/mutation 三列/
   dedup/split/inclusion/exclusion）；硬性规则与 fail-closed 五校验逐条
   一致；split=UNASSIGNED_C7_2_PROPOSAL_ONLY 正确占位
3. 7.3 接口对齐：trait_annotation.jsonl 含 asset/mapping/traits(F1-F15
   显式 ID)/row_policy 四段；聚合不归并 F ID；observed/predicted 分离
   不丢 evidence_type；真菌不接收软补齐
4. 证据容器（§4.1）：value_status 五态（OBSERVED_USED /
   PREDICTED_SOFT_FILL_USED / NOT_OBSERVED / NOT_APPLICABLE /
   FUNGI_IDENTITY_ONLY）+ provenance 四字段 + missing_reason；解析规则
   observed 优先、predicted 不覆盖 observed
5. 逐 F 编码（§4.2）：F5 禁预测、F8 仅 broad、F15 不参与排序、
   F9-F14 source-labelled；软补齐允许集 F1-F4/F6-F8 与 08-14 裁定一致
6. policy manifest（§7）：授权 ID 引用正确；真菌 identity-only +
   fungi_no_local_trait_source
7. 校验清单（§8）：schema/asset/provenance/boundary 四层完整；
   1,704 与 1,705 有效口径正确区分，P0DXV0 +1 不静默合并
8. 边界：non-claims 十项完整；MANIFEST 4/4 sha256 通过；local audit PASS
```

**裁定 1：C7-2 提案冻结通过**（作为设计契约冻结）。实施授权：
下一步仅限"只读 schema/validator 实装 + bounded staged 子集"（即提案
§9 范围），仍 staged-only，不构成 TraitFilterLayer 实装或生产授权。

---

## 二、1,650 accession 二次复核：独立验收 + 5 candidate 分级裁定

### 2.1 验收项（全过）

```text
· denominator 交叉：4,681 表 fetch-failed 精确 1,650，表内唯一，全复核
· 无漏报：1,645 no-candidate 行 2,155 probes 全部 404（表内 12 随机
  抽样独立探测亦全 404；此前一次抽样误用 PASS 池 UID 出现 200，作废）
· 5 candidate v6 独立探测全 200（含 U3PT72 另见 2.2）
· O64174 交叉：老师侧 08-14 确认 404 → 学生侧 no-candidate，一致
· P0DXV0 交叉：学生独立发现 v6 存在 ↔ 老师侧 08-14 已收口，双向一致
· 红线：replacement/asset_generation/mutation 全 False；未替换未生成
· 完整性：MANIFEST 18/18 sha256 通过；FIXED_VALIDATION overall_pass；
  repackage 修复范围（scripts/run_log.txt 陈旧条目）确认不影响科学结果
· FINAL_STATUS / 禁止用语 / 表述边界全部正确
```

### 2.2 5 个 candidate 分级裁定

```text
[可用] P0DXV0 → P0DXV0    序列全同（540aa，sha 一致）；老师侧 08-14
                          已收口 PASS；本表为独立交叉确认，一致
[可用] P49823 → A0A8I3PZS7 序列全同（388aa，sha 一致）；v6 200
[可用] P54835 → A0A8I3N404 序列全同（450aa，sha 一致）；v6 200
[存疑] P18173 → Q8SXV0     original 625aa ≠ canonical 612aa（sha 不同）；
                           U3PT72 同为 v6 200 未入选，选择规则未写明
[存疑] P80550 → F1RSB4     original 38aa ≠ canonical 704aa（sha 不同），
                           序列严重不一致；v6 结构存在但非同序列
```

**裁定 2：本任务验收通过（table-only 结案）**。1,645 确认真缺失维持
blocker；5 个 candidate 维持 RECORD_ONLY，其中：

```text
· P0DXV0：维持已收口状态（08-14 老师侧 +1 PASS 有效）
· P49823 / P54835：列为可收口候选（序列全同 + v6 可用），收口动作
  需另行授权（复用 4,681 管线：P2Rank + ESM2 3B + GVP + loader）
· P18173 / P80550：暂不启用。需学生补充：① P18173 的 Q8SXV0 vs
  U3PT72 选择规则与序列一致性说明；② P80550 original 38aa 序列来源
  溯源（manifest 序列疑似截断/异常）。未澄清前不进入任何收口路径
```

---

## 三、学生下一步

【陈浩然】
```text
1. C7-2 已冻结 → 启动 §9 只读 schema/validator 实装（POLICY_MANIFEST /
   TRAIN_SET_MANIFEST / trait_annotation.jsonl / 校验报告），bounded
   staged 子集，回包后老师侧 48h 出意见；
2. 澄清 P18173：Q8SXV0 vs U3PT72 选择规则 + 与 original 625aa 序列
   一致性比对报告；P80550：original 38aa 序列来源溯源；
3. 1,650 复核任务关闭（table-only 结案，无需再动作）。
```

【弓赛】
```text
1. R1 收口 4 项维持（晨羽 9240ded 整改验证）；
2. 7.1 fallback 融合：主路线酶层映射（rxn2enzyme）打通 + 批跑，
   验收表回包。
```

---

## 四、红线延续（随本裁定有效）

```text
1. 5 个 candidate 仅为记录，未替换 UID、未生成资产（与回包声明一致）；
2. C7-2 冻结的是编码契约，不是 TraitFilterLayer 实装授权；
3. P49823/P54835 收口未授权前不执行（授权后按 4,681 管线契约 +
   老师侧收口先例执行，产物入 staged）；
4. 禁止用语继续生效（production backfill / UID replacement / 全量补齐）；
5. 全部 mutation 保持 False。
```

---

本裁定为 08-17 正式生效文件；与 08-14 两份裁定合并执行。
