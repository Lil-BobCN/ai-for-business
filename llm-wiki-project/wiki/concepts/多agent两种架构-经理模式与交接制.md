---
type: concept
title: 多 Agent 两种架构：经理模式与交接制
created: 2026-10-11
updated: 2026-10-11
tags: [Agent, 多Agent, 经理模式, 交接制, 设计模式]
related: [单agent循环与两个敌人, 五个工作流设计模式, workflow与agent的分界, 单agent与多agent选型比较, 工具调用-mcp-sub-agents-skills-任务组织比较]
sources: ["零点未来：AI+企业/第 8 集｜8分钟7种Agent系统设计模式拆解.md"]
evidence_status: unknown
---

# 多 Agent 两种架构：经理模式与交接制

本页记录「零点未来」第 8 集视频作者拆解的两种多 Agent（Multi-Agent）协作架构。作者把它们定位为自主性阶梯的高段。

## 定义（来源观点，`unknown / 待外部核验`）

### 经理模式

有一个中央的 Agent，作者称为经理 Agent 或 CEO Agent，它通过工具的调用协调一群专家来完成任务。CEO Agent 是唯一直接面向用户的 Agent，像老板一样，把活分给各个组，自己对外汇报。

### 交接制

Agent 有可能是同级别的，没有一个中央的分配者，不同 Agent 之间的执行权可以转给另外一个 Agent，连同对话状态都一起交接过去。

## 适用条件

作者说，当领域差异大到单个 Agent 装不下、工具又多到单个 Agent 放不下的时候，适合上多个 Agent 的模式。

## 作者给出的风险与建议

- 建议先考虑能不能在单个 Agent 上最大化它的能力；
- 多个 Agent 的成本还是比较高的，而且比较难调试；
- 如果遇到问题，有可能是协作的问题、编排的问题，也有可能是单个 Agent 的问题；
- 存在「踢皮球式循环」的风险。

## 项目分析

- 作者主张先榨干单个 Agent，理由是成本更高、故障面更大：协作、编排、单个 Agent 三层都可能出错。潜台词是拆得越多，定位问题的成本涨得越快。
- 可延展方向：给多 Agent 系统先配一份出错归因表，写明每类失败该去查协作层、编排层还是单个 Agent。

## 反例或边界

- 若一个团队的领域边界本身还在争论，把它拆成多个 Agent 可能让问题更难查，而非更清楚。
- 作者未给出「领域差异大到装不下」的可操作判据。

## 关联页面

- [[concepts/单agent循环与两个敌人]]
- [[concepts/五个工作流设计模式]]
- [[concepts/workflow与agent的分界]]
- [[comparisons/单agent与多agent选型比较]]
- [[comparisons/工具调用-mcp-sub-agents-skills-任务组织比较]]

## 开放问题

- 多 Agent「成本更高、更难调试」以及「踢皮球式循环」的风险是否有可核验的案例或数据？