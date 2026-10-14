---
type: concept
title: Action 分级与确认机制
created: 2026-10-11
updated: 2026-10-11
tags: [Action, 人机协同, 确认, Agent, Palantir]
related: [agent与ontology五层交互架构, 工作流与人工介入, agent中断条件与检查点, 语义元素与动态元素两分法]
sources: ["零点未来：AI+企业/第 5 集｜19分钟揭秘Palantir Agent和Ontology如何交互.md"]
evidence_status: unknown
---

# Action 分级与确认机制

## 定义

Action 分级与确认机制是视频作者零点未来在「AI+企业」第 5 集中描述的 Action Layer 核心机制：把 Agent 可执行的业务变更按风险分级，高风险操作需用户确认后才执行，低风险操作自动触发；并配以 update application variable、command tool、request clarification 三个辅助工具。

## 来源观点

以下均为视频作者在该段口播中提出的观点，属 `unknown / 待外部核验`。

- **高风险操作**：LLM 生成 action 后需用户确认。示例提示：「承运商 B 单价比 A 高 12%，预计增加运费 340 元，但时效可提升 10%，需要你点击确认才执行」。作者举例换承运商、涉及合同与成本的动作属高风险。
- **低风险操作**：自动触发。如天气原因延误两小时，系统自动更新 ETA、自动给客户发通知。
- **三个辅助工具**：
  - **update application variable**：让 Agent 改应用状态，如「只看华东」触发页面联动刷新；
  - **command tool**：触发其他应用操作，如在地图上标出五个延误订单；
  - **request clarification**：执行前向用户确认模糊指令，如「你指的是哪个订单」。作者比喻为护士给药前先确认「你是左手还是右手」，宁可多问一句，也不在不可逆操作上犯错。

## 已核验事实

暂无。本页内容全部来自单一视频作者口播，本地 ASR 为 `partial`。

## 项目分析

- 该机制可扩展 [[concepts/工作流与人工介入]]：把「人工介入」细化为按风险分级的确认策略。
- 与 [[concepts/agent中断条件与检查点]] 相关：高风险确认与 request clarification 都是中断条件的具体形态。
- 与 [[concepts/语义元素与动态元素两分法]] 呼应：Action 属于 Kinetic elements，需事先被建模、被授权。

## 反例或边界

- 作者未给出风险分级的判定标准：什么算高风险、什么算低风险，由谁定义。
- 高风险示例中的数字（12%、340 元、10%）未经核验。
- request clarification 的触发条件（什么算「模糊指令」）未说明。

## 关联页面

- [[concepts/agent与ontology五层交互架构]]
- [[concepts/工作流与人工介入]]
- [[concepts/agent中断条件与检查点]]
- [[concepts/语义元素与动态元素两分法]]
- [[sources/8-零点未来ai企业--38-第-5-集19分钟揭秘palantir-agent和ontology如何交互--4skb72]]

## 开放问题

- 风险分级的判定标准应由业务方还是平台方定义？
- 不可逆操作是否应一律强制确认，而不区分风险等级？