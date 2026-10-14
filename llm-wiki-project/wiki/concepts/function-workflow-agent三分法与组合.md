---
type: concept
title: Function、Workflow 与 Agent 三分法与组合
tags: [Function, Workflow, Agent, 选型, 架构]
related: [选型两轴与一条红线, 自主权判据, code-first升级阶梯与l0-l4成熟度模型, workflow与agent的分界, 工具调用]
sources: ["零点未来：AI+企业/第 11 集｜10分钟企业上 AI，到底用 Function、Workflow，还是 Agent？.md"]
evidence_status: unknown
created: 2026-10-11
updated: 2026-10-11
---

# Function、Workflow 与 Agent 三分法与组合

## 定义

Function、Workflow 与 Agent 三分法，是把企业 AI 落地路线按「谁来决定下一步」划分成三种实现方式的方法论：规则清楚就用 Function（函数），流程能定下来就用 Workflow（工作流），只有真正能让 AI 自己定的才叫 Agent（智能体）。

## 来源观点

视频作者在该段口播中提出（`unknown / 待外部核验`）：

- **Function**：像计算器，输入输出永远一样，算钱、查权限、判超标都行，是系统可靠性的基座。
- **单次 LLM**：只能一次次抽一次信息，比如识别发票、抽出日期金额，常常一次调用就够了，不要为这点小事去搭建整套流程。
- **Workflow**：把流程步骤先定好，AI 只干中间看得懂的部分。
- **Agent**：模型自己决定下一步，自己用工具，自己判断什么时候算完。

作者强调这三样不是三选一，而是能够组合到一起：底层 Function 兜底，上面挂 Workflow，真要随机应变的时候，才让 Agent 接管。他还提出「后果越严重，自主权就越小」——越重要的事情，越不能让 AI 自己做主。

## 已核验事实

无。本页内容全部来自视频作者口播，尚无一手资料或独立核验支持。

## 项目分析

三分法的可迁移价值在于把「要不要上 Agent」这个笼统问题，拆成「每一段由谁负责」的分段问题。它与 [[concepts/workflow与agent的分界]] 讨论的是同一主题，但把分界从「是否拆任务」推进到「自主权大小」（见 [[concepts/自主权判据]]）。三分法中的 Workflow 定义（「把流程步骤先定好，AI 只干中间看得懂的部分」）需纳入 [[queries/workflow定义与既有页面口径冲突待核验]] 的口径比对。

## 反例或边界

- 三分法隐含前提是业务流程里存在足够大、足够稳定、可以被写成规则的部分，否则「先用 Function 固化规则」无从下手。
- 「能用规则就不用模型判断」在规则本身频繁变动的业务里反而更贵——把变化写成代码需要发版，而模型对表述的容忍度更高，这条成本在作者账里未出现。

## 关联页面

- [[concepts/选型两轴与一条红线]]
- [[concepts/自主权判据]]
- [[concepts/code-first升级阶梯与l0-l4成熟度模型]]
- [[concepts/workflow与agent的分界]]
- [[concepts/工具调用]]

## 开放问题

- 三分法与第 8 集（Agent 七模式）、第 1 集（Data/Logic/Action 三层模型）在选型判据上是否需统一口径？