---
type: comparison
title: 单 Agent 与多 Agent 选型比较
created: 2026-10-11
updated: 2026-10-11
tags: [Agent, 多Agent, 选型, 比较]
related: [单agent循环与两个敌人, 多agent两种架构-经理模式与交接制, 五个工作流设计模式, agent选型三原则与anthropic三条铁律, 工具调用-mcp-sub-agents-skills-任务组织比较]
sources: ["零点未来：AI+企业/第 8 集｜8分钟7种Agent系统设计模式拆解.md"]
evidence_status: unknown
---

# 单 Agent 与多 Agent 选型比较

本页并列比较「零点未来」第 8 集视频作者给出的单 Agent 与多 Agent 两种方案。所有内容均为视频作者口播，`unknown / 待外部核验`。

## 并列比较

| 维度 | 单 Agent | 多 Agent |
|---|---|---|
| 本质 | 一个 while loop，把 LLM 输出反馈回去校准 | 多个各有专长的 Agent 分工协作 |
| 主要架构 | 循环 + 三个退出条件 | 经理模式（CEO Agent 唯一面向用户）与交接制（同级转移执行权与对话状态） |
| 主要风险 | 重复无效调用、工具过多导致选错工具 | 协作层/编排层/单 Agent 层三重故障面、踢皮球式循环 |
| 成本与调试 | 相对低 | 作者称成本更高、更难调试 |
| 作者建议 | 先最大化单 Agent 能力 | 仅在领域差异大到单 Agent 装不下、工具多到放不下时才上 |

## 作者给出的适用条件

- 上多 Agent 的条件：领域差异大到单个 Agent 装不下、工具又多到单个 Agent 放不下。
- 前置建议：先考虑能不能在单个 Agent 上最大化它的能力。

## 项目分析

- 作者主张先榨干单个 Agent，理由是拆得越多，定位问题的成本涨得越快。
- 可延展方向：给多 Agent 系统先配一份出错归因表，写明每类失败该去查协作层、编排层还是单个 Agent。
- 本页与 [[comparisons/工具调用-mcp-sub-agents-skills-任务组织比较]] 高度相关，可互链对照。

## 反例或边界

- 若一个团队的领域边界本身还在争论，把它拆成多个 Agent 可能让问题更难查，而非更清楚。
- 作者未给出「装不下」的可操作判据，也未给出多 Agent 成本更高的量化数据。

## 关联页面

- [[concepts/单agent循环与两个敌人]]
- [[concepts/多agent两种架构-经理模式与交接制]]
- [[concepts/五个工作流设计模式]]
- [[concepts/agent选型三原则与anthropic三条铁律]]
- [[comparisons/工具调用-mcp-sub-agents-skills-任务组织比较]]