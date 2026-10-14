---
type: entity
title: Palantir MCP
created: 2026-10-11
updated: 2026-10-11
tags: [Palantir, MCP, 接口, 开发者]
related: [ontology-mcp, palantir, palantir-foundry, 工具调用, 工具调用-mcp-sub-agents-skills-任务组织比较, agent与ontology五层交互架构]
sources: ["零点未来：AI+企业/第 5 集｜19分钟揭秘Palantir Agent和Ontology如何交互.md"]
evidence_status: unknown
---

# Palantir MCP

## 定义

Palantir MCP 是视频作者零点未来在「AI+企业」第 5 集中提到的一种面向开发者的接入机制，用于让开发者通过 MCP 与 Palantir Ontology 交互。作者称其能力边界是：可以修改 Ontology 的类型定义，但不能直接写数据。

## 来源观点

以下均为视频作者在该段口播中提出的观点，属 `unknown / 待外部核验`。

- 面向开发者。
- 能够修改 Ontology 的类型定义。
- 不能直接写数据。
- 与 Ontology MCP 共同构成外部 Agent 接入的两个机制；作者称无论走哪条路，核心原则不变：Agent 通过受治理的 Ontology 接口访问一切，绝不绕过 Ontology 直接碰底层数据。

## 已核验事实

暂无。本页内容全部来自单一视频作者口播，本地 ASR 为 `partial`，无一手文档或官方材料佐证。

## 项目分析

- 与 [[entities/ontology-mcp]] 构成对照：一个偏「改定义」，一个偏「读写数据与执行 action」。
- 与 [[concepts/工具调用]]、[[comparisons/工具调用-mcp-sub-agents-skills-任务组织比较]] 直接相关：MCP 是工具暴露给 Agent 的一种组织方式。
- 与 [[concepts/agent与ontology五层交互架构]] 相关：五层架构主要描述 local Agent 与 Ontology 的交互，两套 MCP 描述外部 Agent 的接入。

## 反例或边界

- 能力边界（可改类型定义、不可写数据）为作者口播陈述，未经官方文档核验。
- 作者未说明 Palantir MCP 与 Ontology MCP 是否可同时使用、是否存在权限交叉。

## 关联页面

- [[entities/ontology-mcp]]
- [[entities/palantir]]
- [[entities/palantir-foundry]]
- [[concepts/工具调用]]
- [[comparisons/工具调用-mcp-sub-agents-skills-任务组织比较]]
- [[concepts/agent与ontology五层交互架构]]
- [[sources/8-零点未来ai企业--38-第-5-集19分钟揭秘palantir-agent和ontology如何交互--4skb72]]

## 开放问题

- Palantir MCP 与 Ontology MCP 的读写权限边界是否如作者所述？
- 两套 MCP 是否值得独立实体页，还是并入 [[comparisons/工具调用-mcp-sub-agents-skills-任务组织比较]]？