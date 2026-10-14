---
type: concept
title: 确定性走 Context、探索走 Query
created: 2026-10-11
updated: 2026-10-11
tags: [检索设计, Context, Query, Agent, 幻觉]
related: [agent与ontology五层交互架构, 本体给事实-rag给依据, 本体检索策略选型, 防幻觉的架构化机制]
sources: ["零点未来：AI+企业/第 5 集｜19分钟揭秘Palantir Agent和Ontology如何交互.md"]
evidence_status: unknown
---

# 确定性走 Context、探索走 Query

## 定义

「确定性走 Context、探索走 Query」是视频作者零点未来在「AI+企业」第 5 集中给出的一条检索设计分界原则：必须让 Agent 知道的信息放进 Retrieval Context，允许 Agent 自己探索、自己判断的信息放进 Query Layer。

## 来源观点

以下均为视频作者在该段口播中提出的观点，属 `unknown / 待外部核验`。

- **放 Context 的内容**：当前仓库信息、今天的 KPI 信息、权限等级等——每一轮对话都需要这些信息输入，所以在 Agent 给出回答之前作为 context 给到 Agent。
- **放 Query 的内容**：如「帮我对比一下两个仓的情况」「这个承运商过去三十年的表现」（从上下文看疑为「三年」，需核对原音）等临时提出、无法完全提前预测的需求。
- **放错的代价**：
  - Context 里塞太多信息 → token 浪费、噪声干扰，需要上下文处理能力非常强的模型支撑，成本上升；
  - Query 配得太窄 → LLM 可能查不到想要的信息，可能开始编。

作者据此总结：确定性的走 Context，允许 Agent 探索的走 Query Layer。

## 已核验事实

暂无。本页内容全部来自单一视频作者口播，本地 ASR 为 `partial`。

## 项目分析

- 这条原则把「分界线画在哪里」与「成本与幻觉率」直接挂钩：Context 侧过宽推高 token 与噪声，Query 侧过窄推高幻觉率。
- 与 [[concepts/本体给事实-rag给依据]] 同构：Context 侧的 Ontology Context / Document Context 分别对应本体事实与文档依据。
- 与 [[concepts/本体检索策略选型]] 相关：本原则可作为检索策略选型的一条判据。

## 反例或边界

- 作者未讨论「同一条信息既每轮都可能需要、又不一定用得上」时该放哪一侧。
- 该原则的量化边界（多少条上下文算「太多」、多窄算「太窄」）未给出。

## 关联页面

- [[concepts/agent与ontology五层交互架构]]
- [[concepts/本体给事实-rag给依据]]
- [[concepts/本体检索策略选型]]
- [[concepts/防幻觉的架构化机制]]
- [[sources/8-零点未来ai企业--38-第-5-集19分钟揭秘palantir-agent和ontology如何交互--4skb72]]

## 开放问题

- 是否应把「每轮必须注入」和「按需检索」做成两张清单，在需求评审阶段就分开维护？