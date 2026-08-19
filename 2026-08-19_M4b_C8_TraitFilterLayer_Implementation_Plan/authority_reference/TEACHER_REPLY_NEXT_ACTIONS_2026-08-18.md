# 老师回复：下一步动作与授权（2026-08-18）

发件人：黄老师
收件人：陈浩然（主线 + 微生物侧）、弓赛（GitHub 账号 Frankgonghahaha，分支线）

本回复整合 08-14 / 08-17 / 08-18 三轮裁定，给出两位同学各自的下一步动作与
红线。两位独立执行、独立交付、独立待办编号，不得混用收件人与整改范围。

**本轮交付时间（DDL，均在 3 天内）**

| 收件人 | 交付项 | DDL |
|---|---|---|
| 陈浩然 | metaTraits TSV 落晨羽（回报路径 + 清单 + SHA256） | 08-19 |
| 陈浩然 | C8 实装方案 / 拆解待审 | 08-20 |
| 弓赛 | 38% 口径说明 + 根因诊断 + 整改计划（第一优先） | 08-20 |
| 弓赛 | R1 数据脚本 + R2 路径清欠（P0） | 08-21 |
| 弓赛 | 7.1 酶层映射验收表回包（P1） | 08-21 |

---

## 一、整体进度判定（师生对齐）

```text
- 主线训练 / 排序模型（v1 冻结）：95%，已就绪，非瓶颈
- 智能体编排（底物→反应→酶→菌，M3 线性 + M5 全量双模式）：90%，
  10 节点全接线 + 真跑 PASS，非瓶颈；仅剩 TraitFilterLayer（菌层）与
  reaction fallback 两处占位待填充
- 评估体系：100%，不再变动
- 唯一硬阻塞：弓赛 fallback 引擎（demov2）效果约 38% 未达标、在整改中
  → 卡 F6 三工具对比（D1）+ fallback 选型 D2 + C0 混合路线 D3
```

---

## 二、陈浩然（主线 + 微生物侧）

### 2.1 C8 实装授权（老师侧签发，菌层推进的解锁点）

```text
- 授权：老师侧签发 C8 TraitFilterLayer 实装授权。
- 边界：产物严格 staged-only，不接 production（与 C7-2 同口径）。
- 实装入口（均已就绪，非从零起）：
  ① C7-2 已验收的只读 schema/validator（staged，五校验 fail-closed 契约）
  ② C7-1 trait panel 草案（F1-F15 已冻结：value_status 五态；软补齐允许集
     F1-F4/F6-F8，禁 F5/F9-F15；真菌 identity-only）
- 落地：以 C7-2 validator 为入口起草 TraitFilterLayer 消费契约，
  并与弓赛 fallback 引擎产出的酶候选做上下游联调。
```

### 2.2 metaTraits bulk TSV 落晨羽（P0，可与 2.1 并行）

```text
- 数据源：https://www.bork.embl.de/~robbani/metatraits/
  （12 个 bulk TSV，约 230MB gzip，NCBI/GTDB 双库，family/genus/species 三级）
- 原因：metaTraits API 自 D5（07-24）持续失效（HTML 404），TSV 为唯一
  可用数据源，按 NCBI taxon_id 精确查询 traits
- 交付：① 全部 TSV 落晨羽，回报路径 + 文件清单
        ② SHA256 校验 + 版本日期追溯（支持 MT-TQ-02 snapshot 冻结）
        ③ 明确 TSV 字段与 C7-1 trait panel 的映射口径
```

### 2.3 accession 状态确认

```text
- P18173 / P80550：维持 RECORD_ONLY blocker，无需动作；1,650 accession
  复核已全部结案。
- P49823 / P54835：序列全同 + v6 结构可用，但「收口」= 复用 4,681 管线
  生成新资产入 staged，需老师另行授权；未授权前不动。
```

### 2.4 下一步顺序与 DDL

```text
1. 08-19 前：metaTraits TSV 落晨羽（P0，回报路径 + 清单 + SHA256）
2. 08-20 前：提交 C8 实装方案 / 拆解待审
3. 老师审定 C8 方案后：实装 TraitFilterLayer（消费契约 + 过滤逻辑）
4. 与弓赛 fallback 引擎联调：酶候选 → 菌性状过滤 → 链路闭合
```

### 2.5 红线

```text
- C8 产物 staged-only，不接 production；
- P49823 / P54835 未授权不执行；P18173 / P80550 维持 RECORD_ONLY；
- metaTraits 数据获取走本地 TSV，不依赖失效 API。
```

---

## 三、弓赛（分支线）

### 3.1 老师侧 repo 核实结论

```text
- 最新 commit：9240ded（feat: v4.2 Round B-2 — P0-6 readiness preflight
  + causal classification，R19 整改），相对 main 领先 16 提交
- 已闭环（予以肯定）：schemas 全面落地、tests 补齐
  （contracts/p1/p3/p4/p5，07-28 时为零测试）、生产代码路径已参数化
  （config 走相对路径 data/、reports/）
- 仍欠账三处（见 3.3），且 08-18 起无新提交
```

### 3.2 效果反馈（38% 未达标 = 当前核心阻塞）

```text
老师侧当前掌握：fallback 引擎（demov2）效果约 38%，未达标，仍在整改。
这正是 D1（F6 三工具横向对比）与 D2（fallback 选型）未启动的真实原因。
补齐三项前置：
1. 「38%」评测指标定义与口径（top-1 / 盲评集 / 样本量与切分方式）
2. 效果未达标的根因诊断（哪类底物 / 反应 / 环节主要掉分）
3. 效果提升整改计划与预期可达阈值
硬性顺序：效果达老师侧可接受阈值前，F6 三工具对比（D1）与 fallback
融合裁定（D2/D3）不签发。
```

### 3.3 三处欠账整改

```text
[P0] ① R2 残留：tests/p5/test_p5_invariants.py:67 硬编码
  PROJECT_ROOT = "/Volumes/CC/Enzyme_Agent/depending/CC/branch/ReactionAgent/demov2"
  → 改 ENZYMECAGE_DATA_ROOT / config 注入，仓库 /Volumes/CC 全部清零。
[P0] ② R1 数据面契约：缺 sync_assets.sh、无 .pkl/.csv；README 仍引用
  rxn2enzyme_positives.pkl（3601 条 Rhea 反应）。
  → 交生成脚本（sync_assets.sh + 依赖）+ 字段 schema + 小样本（脱敏）
    + 源数据落晨羽确认；不交二进制 blob。
[P1] ③ 7.1 酶层映射验收表回包：交验收表（覆盖 / 命中 / 漏检口径）；
  晨羽同步最新 commit + BBD83 v4.2 重跑。
```

### 3.4 下一步顺序与 DDL

```text
1. 08-20 前：交「效果整改计划 + 38% 口径说明」（3.2 三项）→ 老师裁定阈值
2. 08-21 前：清欠账①②（P0）；欠账③（7.1 验收表）随批跑一并回包
3. 效果达标 + 欠账清零后，老师签发 F6 三工具对比（D1）授权
```

### 3.5 红线

```text
- fallback 融合裁定（D2/D3）在效果达标前不签发；
- 不交 .pkl 成品，只交生成脚本 + 源数据落晨羽；
- 生产路径不得残留 /Volumes/CC。
```

---

## 四、共同红线（两位共同遵守）

```text
- 禁止用语（production backfill / UID replacement / 全量补齐）继续生效，
  全部 mutation 保持 False；
- 所有产物入 staged 前须老师授权。
```

---

本回复为 08-18 正式生效文件；与 08-14 / 08-17 / 08-18 裁定合并执行。