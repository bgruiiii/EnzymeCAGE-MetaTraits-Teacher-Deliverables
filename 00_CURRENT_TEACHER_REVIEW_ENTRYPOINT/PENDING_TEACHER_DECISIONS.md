# 仍需老师后续裁定的问题（MetaTraits / 菌侧）

日期：2026-08-05  
说明：本文件只列“尚未正式裁定或尚未外部闭合”的事项，避免把建议写成已经批准。

## 1. 尚未闭合的问题

| 问题 | 当前状态 | 不能写成 |
|---|---|---|
| official versioned MetaTraits snapshot | 尚未冻结 | 已拿到稳定 snapshot |
| production organism_uid -> traits 通路 | 尚未闭合 | TaxID/UID 可直接生产查询 |
| M4b / M4c 是否启动 | 未授权启动 | 已进入实现 |
| organism_confidence 0-1 数值实现 | 仅保留路线/裁定背景 | 已在生产实现 |
| 污水 trait 使用方式 | soft evidence，仅供参考/解释/不确定性提示 | hard filter 自动删除候选菌 |
| strain/species 性状关系 | 不能互相继承 | 可以按名称模糊继承 |

## 2. 后续汇报建议口径

```text
菌侧已完成 D5、D1-D8、confidence、ID 对齐和 Task 7 的再确认与路径指引。
M4b/M4c、versioned snapshot、production organism_uid -> traits 通路和 organism_confidence 0-1 实现仍需后续正式授权或外部输入，当前不写成已完成。
```
