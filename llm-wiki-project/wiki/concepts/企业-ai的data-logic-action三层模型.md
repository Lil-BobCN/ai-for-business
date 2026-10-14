---
type: concept
title: 企业 AI 的 Data、Logic 与 Action 三层模型
created: 2026-10-11
updated: 2026-10-11
tags: [企业AI, Ontology, 语义层, Agent, 工作流]
related: ["本体与agent协同", "工作流与人工介入", "aip", "零点未来ai企业--47-第-1-集10分钟企业agentic-workflow落地palantir-ontology--167275e"]
sources: ["零点未来：AI+企业/第 1 集｜10分钟企业Agentic Workflow落地：Palantir & Ontology.md"]
evidence_status: partial
---
# 企业 AI 的 Data、Logic 与 Action 三层模型

这是视频作者对 Palantir Ontology 的一种分层描述：Data 层连接不同系统的数据源，Logic 层表达 Ontology 的语义模型，Action 层承载执行能力。该描述来自本地 ASR 转写，尚未与官方架构资料核对。

## 定义

在本视频的语境中，这三层分别是：

- `Data`：来自不同系统的数据源。
- `Logic`：以 Ontology 表达的业务语义模型。
- `Action`：执行部分，例如 `Workshop` 或 AI Agent 自动化。

作者用“向下连接数据，向上赋能应用”概括三层的位置关系。

## 来源观点

作者把三层描述与一组数据到业务对象的映射放在一起：

| 原文术语 | 作者所述映射 |
|---|---|
| `DataSet` | `Object Type` |
| `Data Table` 的行 | `Object` |
| `Data Table` 的列 | `Property` |
| 不同 `Object Type` | 通过 `Link` 连接 |

上述内容保留为视频中的概念映射，不代表正式 schema、API 或可直接实施的产品规范。转写中专名可能有误。

## 已核验事实

本次摄入未核验官方架构文档，也没有取得可复现实现或 schema。页面所述分层应视为来源观点，不能直接推广为企业 Ontology 的通用标准。

## 项目分析

这套描述把数据连接、业务语义和业务动作放在同一模型中，能帮助讨论 Agent 从读取上下文到执行操作的边界。实施时仍需明确业务对象由谁定义、逻辑如何验证、动作权限如何配置，以及操作结果如何审计。

## 反例与边界

来源没有证明所有企业系统都应采用相同三层结构，也没有给出层间接口、数据同步、错误处理或权限继承规则。某些业务动作可能需要人工审批，不能仅凭该分层描述推定可以自动执行。

## 关联页面与开放问题

- 
- [[concepts/本体与agent协同]]
- [[concepts/工作流与人工介入]]
- [[entities/aip]]
- [[sources/8-零点未来ai企业--47-第-1-集10分钟企业agentic-workflow落地palantir-ontology--167275e]]

仍需核对：该分层是否对应 Palantir 官方资料中的明确结构；`DataSet`、`Object Type`、`Object`、`Property` 与 `Link` 的准确关系是什么？