---
type: concept
title: Agent 与 Ontology 五层交互架构
created: 2026-10-11
updated: 2026-10-11
tags: [Palantir, Ontology, Agent, 架构, 语义层]
related: [本体与agent协同, 语义元素与动态元素两分法, 确定性走context探索走query, 防幻觉的架构化机制, action分级与确认机制, 本体作为约束层, 工具调用, 工作流与人工介入]
sources: ["零点未来：AI+企业/第 5 集｜19分钟揭秘Palantir Agent和Ontology如何交互.md"]
evidence_status: unknown
---

# Agent 与 Ontology 五层交互架构

## 定义

Agent 与 Ontology 五层交互架构是视频作者零点未来在「AI+企业」第 5 集中提出的一种分层描述：把 Agent 与 Ontology 之间的交互拆成 Context、Query、Logic、Action、Governance 五层，其中前四层各承担一类交互职责，Governance 层作为权限、审计与安全约束贯穿前四层。作者称这套划分用于回答「本体建好之后 Agent 怎么用」这一问题。

## 来源观点

以下均为视频作者在该段口播中提出的观点，属 `unknown / 待外部核验`。

- **第一层 Context Layer**（官方名 Retrieval Context）：确定性触发，每条消息都执行，不需要 LLM 判断是否需要检索。三种准备方式为 Ontology Context、Document Context、Function-backed Context。
- **第二层 Query Layer**：LLM 自主决定查什么，支持过滤、聚合、检索、沿关系链搜索与逐层追溯；查的是 Ontology 里的对象和关系，而不是写 SQL。
- **第三层 Logic Layer**：调用封装好的业务函数，不让 LLM 自己算；LLM 拿到的是结构化结果而非原始数据，其工作是理解意图、选择函数、用自然语言解释结果。
- **第四层 Action Layer**：执行受控业务变更，高风险操作需用户确认，低风险操作自动执行；辅助工具包括 update application variable、command tool、request clarification。
- **第五层 Governance Layer**：权限、审计、安全约束贯穿前四层。作者称这是「Palantir 与普通 Agent 框架最核心的差异」。

作者用一条端到端链路把五层串起来：Top 10 注入 → 过滤华南仓加延误条件 → 沿 Link 追溯 Order/Customer → 调用函数算风险 → LLM 生成回答 → 用户确认 → 分派承运商、创建异常 case、更新 Ontology、留审计日志。

## 已核验事实

暂无。本页内容全部来自单一视频作者口播，本地 ASR 为 `partial`，无一手文档或官方材料佐证。

## 项目分析

- 本页是 [[concepts/本体与agent协同]] 的机制展开：该上位概念此前缺少「建好之后怎么用」的分层描述，本集填补了这一空白。
- 五层中的 Governance 层与 [[concepts/本体作为约束层]] 的「受治理接口」主张同向，可视为该判断在 Agent 交互侧的具体化。
- Context Layer 的 Ontology Context / Document Context 与 [[concepts/本体给事实-rag给依据]] 同构：本体提供事实、文档提供依据。
- Action Layer 的高/低风险分级与 request clarification 可扩展 [[concepts/工作流与人工介入]]、[[concepts/agent中断条件与检查点]]。
- Logic Layer 的函数化计算与 [[concepts/规则引擎推导]] 相关，但对象不同：前者是业务函数，后者是规则推导。

## 反例或边界

- 作者自述的边界：这套交互只在一个已建好的、受治理的 Ontology 之上才成立。
- 五层划分与官方命名是否为 Palantir 官方口径，作者未给出一手出处，需外部核验。
- 端到端链路中「过滤后 32 个」与「23 个里面有 5 个有风险」前后不一致，演示流程数字不闭合。
- 防幻觉机制列举四项（Context、Object Type、权限、函数）与叙述中「三层叠加」说法不一致。

## 关联页面

- [[concepts/本体与agent协同]]
- [[concepts/语义元素与动态元素两分法]]
- [[concepts/确定性走context探索走query]]
- [[concepts/防幻觉的架构化机制]]
- [[concepts/action分级与确认机制]]
- [[concepts/本体作为约束层]]
- [[concepts/工具调用]]
- [[concepts/工作流与人工介入]]
- [[sources/8-零点未来ai企业--38-第-5-集19分钟揭秘palantir-agent和ontology如何交互--4skb72]]

## 开放问题

- 五层架构是否应作为 [[concepts/本体与agent协同]] 的子页，还是独立成页？
- Context / Query / Logic / Action / Governance 是否为 Palantir 官方命名？
- 五层之间是否存在作者未提及的耦合或顺序依赖？