---
type: concept
title: Agent OS
created: 2026-10-11
updated: 2026-10-11
tags: [AgentOS, Ontology, FDE, 企业AI]
related: [本体与agent协同, fde交付方法, 土路与柏油高速路, fdeforward-deployed-engineer前线部署工程师, palantir, 个人提效级与业务域级-agent, agent-os工具与开源状态待核验]
sources: ["零点未来：AI+企业/第 6 集｜6分钟聊聊本体Ontology和Agent那些事.md"]
evidence_status: unknown
---

# Agent OS

Agent OS 是视频作者在《第 6 集｜6分钟聊聊本体Ontology和Agent那些事》中提出的一个命名与定位：本体（Ontology）不是图数据库的别名，而是给 Agent 提供业务语义的操作系统，即 Agent OS。本页记录该来源观点、其边界与待核验项。

## 定义（来源观点）

视频作者在该段口播中提出：本体 Ontology 某种意义上确实涵盖知识图谱数据库的功能，但更核心的是"业务的刻画"，展现业务领域的客观事实和关系，存储重要的业务语义信息。Agent 要通过本体理解这一系列业务语义信息，才能实现业务级别的自动化提效与辅助决策；否则结果可能存在幻觉，或非常通用（如 ChatGPT、Claude 直接给出的结果），每次回答也可能不同。

作者由此把本体定位为"Agent 操作系统，Agent OS"，并称这是目前 Palantir 实践探索出来的、Agent 能够做业务级别准确决策的基础。

## 业务语义信息的具体内容（来源举例）

作者举例的业务语义链条：客户会给我下单 → 订单会包含哪些产品 → 产品由哪些零部件构成 → 这些零部件要从哪些供应商采购。

## 与 FDE 的关系（来源观点）

作者在该段口播中提出：Agent OS 这种类型的产品，本质上的用户不是直接客户，而是 FDE（前线部署工程师）。他引述一段播客说法称，Agent OS 本质上是在无法规模化的路径上把某种东西规模化了——FDE 商业模式本身很难规模化，像一条沙石路，而 Agent OS 给 FDE 搭了一条高速公路，使同一个 FDE 可以服务更多客户，并把领域级别的本体支持沉淀在产品里。

## 已核验事实

无。本页所有内容均来自视频作者口播主张，未经独立核验。

## 项目分析

- 该命名与既有 [[concepts/本体与agent协同]]、[[concepts/企业-ai的data-logic-action三层模型]] 部分相关，但"Agent OS"这一命名与"本体即操作系统"的定位是本集新增。
- 作者本人留有余地：日后不排除有人探索出更轻量化、更快速的方法。
- 评估任何号称平台化的 AI 产品时，"它到底在替谁省时间"（终端客户还是 FDE）可作为可迁移的提问框架。

## 反例或边界

- 作者未否认轻量路线的存在，明确说日后不排除更轻量化方法，这与第 1 集"先用少量样本让 LLM 抽一版本体草稿"方向一致。
- "Agent OS"是否为 Palantir 官方术语，还是作者自创命名，尚待核验。

## 关联页面

- [[concepts/本体与agent协同]]
- [[concepts/fde交付方法]]
- [[concepts/土路与柏油高速路]]
- [[entities/fdeforward-deployed-engineer前线部署工程师]]
- [[entities/palantir]]
- [[concepts/个人提效级与业务域级-agent]]

## 开放问题

1. "Agent OS"是否为 Palantir 官方术语？
2. Agent OS 规模化的是 FDE 的"部署工时"还是"建模决策"？
3. 若 Agent OS 沉淀的是领域本体，新客户的差异化判断由谁来补？