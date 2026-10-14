---
type: concept
title: 图谱工程（Graph Engineering）
created: 2026-10-11
updated: 2026-10-11
tags: [graph-engineering, 图谱工程, multi-agent, Agent编排, 轨道]
related: [五图两类框架, 上下文图谱-context-graph, 代码图谱-code-graph, 多agent两种架构-经理模式与交接制, 单agent循环与两个敌人]
sources: ["零点未来：AI+企业/第 9 集｜ontology, knowledge graph, context graph, code graph&graph engineering一次性搞懂.md"]
evidence_status: unknown
---

# 图谱工程（Graph Engineering）

图谱工程（Graph Engineering）是视频作者在"零点未来：AI+企业"第 9 集中提出的一个概念，指给 Agent 划流程图、把 Agent 的执行路径固定成轨道的工程方法。作者称它回答的是"系统怎么干活"，与前面四张回答"系统知道什么"的图是两种完全不同的东西。

## 定义（作者口径）

作者在该段口播中提出：graph engineering 是**给 Agent 划流程图**。

具体来说，一个节点干一件事情，一条边决定干完去哪；哪些步骤必须要按规矩来走、哪些放手让模型自己去推断——给 Agent 的自主规划划分得一清二楚，而不是让它自由发挥、错了再补救。

作者总结：graph engineering 本质上是**给 LLM 装上了一个轨道**，然后在入口处让 Agent 自己去判断，其余的路段就按既定的轨道去走——既给了自由，又保证了一个 `cope`（ASR 原文如此，所指待确认）。

## 元素与构件（作者口径）

作者说 graph engineering 有很多元素和构件，比如：

- data engineering
- graph modeling
- retrieval
- reasoning 推理
- Agent 的编排

## 使用时机（作者口径）

- 业务流程有一些固定的套路，而且要稳定、可预期的回答。
- 多个 Agent 之间进行协同工作，需要编一张网络，让 Agent 之间能够互相共享上下文、互相影响、协同工作。

## loop 示例（作者原述）

作者称它本质上是一个 multi-agent 的系统，通过一个网络的结构把 Agent 串起来。最简单的 graph engineering 是一个 loop：

Agent 去调用工具 → 调用工具之后有另外一个 evaluate Agent 进行检查 → 如果不够好的话再回去这个 Agent 进行循环的操作。

## 项目分析

- 该 loop 示例与 [[单agent循环与两个敌人]]、[[多agent两种架构-经理模式与交接制]] 呼应，可交叉引用。
- 与 [[agent与ontology五层交互架构]] 可衔接：graph engineering 对应"系统怎么干活"的执行侧。

## 反例与边界

- 作者把自由集中在入口的判断上，其余路段交给既定轨道。这样换来的是可预期，代价是入口一旦判错，后面整条轨道会顺着错误方向一路跑完——稳定性在这里是放大器而不是保险。
- 作者给出的边界：只在"流程有固定套路、要稳定可预期"时才用；探索性、一次性、不需要稳定结果的场景并不需要它。

## 开放问题

- 出现什么信号时，应该让 Agent 跳出轨道、回到人这里？

## 关联页面

- [[五图两类框架]]
- [[上下文图谱-context-graph]]
- [[代码图谱-code-graph]]
- [[多agent两种架构-经理模式与交接制]]
- [[单agent循环与两个敌人]]