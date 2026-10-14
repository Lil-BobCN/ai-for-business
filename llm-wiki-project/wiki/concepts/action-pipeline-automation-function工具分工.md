---
type: concept
title: Action、Pipeline、Automation、Function 工具分工
created: 2026-10-11
updated: 2026-10-11
tags: [Ontology, 工具分工, Action, Pipeline, Automation, Function, Palantir]
related: [工具调用, 结构化查询, 规则引擎推导, 本体设计四类反模式, palantir-foundry]
sources: ["零点未来：AI+企业/第 7 集｜15分钟解读Palantir 本体设计原则和行业实践分享.md"]
evidence_status: unknown
---

# Action、Pipeline、Automation、Function 工具分工

## 定义

Action、Pipeline、Automation、Function 工具分工是视频作者在该段口播中转述的 Palantir 本体设计工具选择对照表，按"是否需要人工判断、是否需要转换聚合、是否事件驱动、是否跨对象实时计算"把需求分配到不同工具。作者称其出自 Palantir 官方方法论，但视频中未给出文档出处，属 `unknown / 待外部核验`。

## 来源观点

以下均为视频作者在该段口播中提出的陈述。作者给出的对照表如下：

| 需求特征 | 对应工具 |
|---|---|
| 需要人工判断或用户输入 | Action |
| 需要数据转换或聚合 | Pipeline |
| 需要持续低延迟 | Streaming Pipeline |
| 批量转换 | Batch Pipeline |
| 事件驱动、监听本体变化 | Automation |
| 跨对象复杂实时计算、输入随 Action 变化 | Function 或派生属性 |
| 简单或输入稳定的预计算 | Pipeline Transform |

作者强调，这套对照表的第一个问题是"需不需要人工判断或用户输入"，即起点不是工具能力，而是人在流程里的位置。

## 已核验事实

无。本页内容全部来自单一视频作者口播，尚未独立核验。

## 项目分析

- 该表比 [[concepts/工具调用]]、[[concepts/结构化查询]] 更具体，给出了 Action / Pipeline / Streaming Pipeline / Batch Pipeline / Automation / Function / Pipeline Transform / 派生属性 的细分分工。
- 与 [[concepts/本体设计四类反模式]] 中的金锤子互补：金锤子是选错工具，本表是选对工具的依据。
- 与 [[concepts/规则引擎推导]] 相关：Function 与派生属性承担跨对象实时计算。

## 反例或边界

- 作者未回答：如果一个流程今天由人审批、明天想改成自动触发，是工具要重写，还是只需改配置。
- 对照表是否出自 Palantir 官方方法论尚未核验。

## 关联页面

- [[concepts/工具调用]]
- [[concepts/结构化查询]]
- [[concepts/规则引擎推导]]
- [[concepts/本体设计四类反模式]]
- [[entities/palantir-foundry]]

## 开放问题

- 该工具分工对照表是否出自 Palantir 官方文档？