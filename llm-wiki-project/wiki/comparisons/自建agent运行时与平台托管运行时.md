---
type: comparison
title: 自建 Agent 运行时与平台托管运行时
tags: [buy-or-build, 运行时, 选型, 合规]
related: [agent-api与模型-api的分界, harness与sandbox解耦, 长任务agent五项基础设施, agent-framework下沉]
sources: ["零点未来：AI+企业/第 12 集｜9分钟OpenAI这次卖的不只是模型.md"]
evidence_status: unknown
created: 2026-10-11
updated: 2026-10-11
---

# 自建 Agent 运行时与平台托管运行时

## 比较背景

视频作者在该段口播中提出：底层通用能力越来越可以标准化，企业没有必要把大量工程资源花在重复造 Agent 运行时上面；真正产生差异化的，越来越集中在企业自己的 business context。本页把该主张整理成 buy-or-build 的比较框架。

## 对比维度（当前分析）

| 维度 | 自建运行时 | 平台托管运行时 |
|---|---|---|
| 上下文管理 | 自行实现 summary memory / checkpoint | 平台内建上下文压缩 |
| 工具管理 | 自行维护工具定义与调用代码 | 平台提供 tool search 与 PTC |
| 多 Agent 编排 | 自行用 LangGraph、`out of jam`〔ASR 原文，所指待确认〕或自写 workflow | 平台原生提供 |
| 执行环境 | 完全自持 | 可选托管、自建或第三方 sandbox |
| 差异化位置 | 工程实现细节 | 业务上下文、可调用动作、权限与审批 |

## 来源观点

作者称，企业可以把敏感数据的执行环境放在自己的基础设施，同时使用托管的运行时；并建议开发者往运行时之上的产品迭代，或结合自己的业务上下文打造 business application。

## 已核验事实

无。表中内容为作者主张的整理，属 `unknown / 待外部核验`。

## 边界与张力

- 作者未给出按任务长度与合规要求分档的具体标准。
- 「企业不必重复造运行时」与「企业要沉淀 context 与治理」之间存在成本转移：省下的工程资源要投到建模、权限与审批，这部分通常更贵且更依赖业务方。
- 数据主权只在 sandbox 一侧有答案，上下文一侧的边界规则缺失。

## 关联页面

- [[concepts/agent-api与模型-api的分界]]
- [[concepts/harness与sandbox解耦]]
- [[concepts/长任务agent五项基础设施]]
- [[concepts/agent-framework下沉]]

## 开放问题

- 按任务长度与合规要求，自建与托管的分档线在哪里？