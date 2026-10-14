---
type: source
title: 第 11 集｜10分钟企业上 AI，到底用 Function、Workflow，还是 Agent？
tags: [零点未来, AI+企业, Function, Workflow, Agent, 选型, ASR]
related: [function-workflow-agent三分法与组合, 选型两轴与一条红线, 自主权判据, code-first升级阶梯与l0-l4成熟度模型, 最小闭环与组织治理基础, agent可解释性不可信与可审计三元组, agent验收指标清单, workflow与agent的分界, 业务验收指标口径, action分级与确认机制]
sources: ["零点未来：AI+企业/第 11 集｜10分钟企业上 AI，到底用 Function、Workflow，还是 Agent？.md"]
evidence_status: partial
created: 2026-10-11
updated: 2026-10-11
---

# 第 11 集｜10分钟企业上 AI，到底用 Function、Workflow，还是 Agent？

## 来源信息

- **标题**：第 11 集｜10分钟企业上 AI，到底用 Function、Workflow，还是 Agent？
- **作者/平台**：零点未来（Bilibili），系列「AI+企业」共 12 集
- **URL**：https://www.bilibili.com/video/BV1sVbg6LEbS
- **原始文件路径**：`零点未来：AI+企业/第 11 集｜10分钟企业上 AI，到底用 Function、Workflow，还是 Agent？.md`
- **提取方式**：本地 ASR 转写，非官方字幕
- **证据状态**：`partial`（ASR 转写不完整，专名、缩写与数字可能有误）；正文主张为视频作者口播观点，未经独立核验，属 `unknown / 待外部核验`

## 一句话摘要

视频作者在该段口播中提出，企业上 AI 的真正命题不是「要不要上 Agent」，而是「哪一部分需要用模型判断、哪一部分必须由代码、权限系统还有人来控制」；他用一张报销单把 Function、Workflow、Agent 三条路线拆开，并给出两个轴（语义的不确定性、路径的不确定性）加一条红线（后果是否严重、是否容易发现、是否必须有责任主体）作为选型判据，结论是多数企业把 L2 级的 LLM Workflow 做深就已经够用。

## 主要论点

以下均为视频作者在该段口播中提出的观点，未经独立核验，属 `unknown / 待外部核验`。

1. **问题重构**：企业 AI 的真命题不是「要不要上 Agent」，而是「哪一部分交给模型判断、哪一部分必须由代码/权限系统/人控制」。
2. **大厂共识（概括性主张，未给出处）**：OpenAI、Anthropic、Google、Microsoft「几乎都在讲同一句话」——优先用最简单、最可测量的架构，达不到目标才引入模型判断、动态编排、自主执行。
3. **三分法**：规则清楚 → Function；流程可定 → Workflow；只有能自主决定的才叫 Agent。三者可组合：Function 兜底、Workflow 挂上、Agent 只在需随机应变时接管。
4. **两轴 + 一红线判据**：
   - 轴一：语义不确定性（输入是否含自然语言/图片/例外说明）
   - 轴二：路径不确定性（执行前是否已知下一步）
   - 红线：影响大 + 错了难发现 + 必须有人担责 → 必须交人
   - 口诀：**语义不定但路径定 → 单次 LLM/Workflow；两者都不定 → 才考虑 Agent**
5. **Agent 判据修正**：以「自主权大小」而非「会不会拆任务」判定 Agent；Anthropic orchestrator-workers 会动态拆解但外围被严格约束，故不算自主 Agent。
6. **五步与五级**：Code First → 一次 LLM → Workflow → 受约束 Agent → 自主 Agent；对应 L0–L4。强调非竞赛、可共存，**多数企业把 L2 做深即可**。
7. **国内现实**：最先拦路的是系统各管各的、流程没打通、数据口径对不上；走法是先固化规则（Function）、再用 Workflow 切入、保留人工审批口子。
8. **最小闭环**：挑高频、边界清楚、结果可验证的流程先打通再扩大；动手前理顺组织基础与治理基础。
9. **报销单分层分工**（示例数字，非真实制度）：Function 管金额规则与封顶；Workflow 管串联流程与 PDF/图片/发票文本抽取；Agent 只管规则覆盖不到的例外，且必须人点头、由代码付钱。
10. **治理三件事**：权限最小化 + 高影响动作人工审批；不信 Agent 可解释性（看证据/规则/审批记录）；用考试式 evaluation 验收。
11. **收束**：把控制权交给最不需要的那一层；能规则就不模型、能预编排就不临时决定、能留给人就不交机器。

## 结构化数据

本集无 SQL DDL、schema、API 签名或配置表。唯一结构化内容是五级架构成熟度模型与决策矩阵，按原文保留如下。

| 级别 | 名称 | 说明 |
|---|---|---|
| L0 | 纯计算（Function） | 输入输出恒定 |
| L1 | 单次 LLM | 一次分类/抽取/生成 |
| L2 | LLM Workflow | 多数企业默认选择 |
| L3 | bounded agent | 固定工具范围、预算内动态规划 |
| L4 | autonomous agent | 自主规划 |

| 路线 | 成本 | 稳定性 | 灵活性 | 风险 |
|---|---|---|---|---|
| Function | 最低 | 最高 | 最低 | 最低 |
| Agent | 最高 | 最低 | 最高 | 最高 |

## 报销单示例（教学示例，数字为举例）

- **Function**：金额规则、封顶（封顶 2400，实际 2700，只报 2400，超标 300 再查）、缺发票不付款。
- **Workflow**：串联流程 + PDF/图片/发票文本抽取（材料识别 → 字段抽取 → 规则校验 → 异常路由）。
- **Agent**：规则覆盖不到的例外（如临时改去天津、行程变更只有口头标准），负责查证收集证据，但必须人点头、由代码付钱。

## 待核验项

- 大厂共识（OpenAI/Anthropic/Google/Microsoft「优先用最简单、最可测量的架构」）是否有原文出处。
- Anthropic orchestrator-workers 模式的约束描述原文。
- L0–L4 五级模型是否为作者自创或引用。
- 「有研究点破过：模型解释越漂亮，可能根本没有说实话」的出处。
- 作者提到的「项目评审清单」口播未读出内容，无法核对。
- 报销单数字（2300/2700/2400/300）是举例还是真实制度。
- 「接管率、失败样例」作为升级依据的归因（Agent 能力不足 vs 上游数据口径问题）。
- ASR 存疑专名：口播中「北京 p7 啊三网」「进而全新的状态」「性能度」等片段所指待确认。

## 关联页面

- [[concepts/function-workflow-agent三分法与组合]]
- [[concepts/选型两轴与一条红线]]
- [[concepts/自主权判据]]
- [[concepts/code-first升级阶梯与l0-l4成熟度模型]]
- [[concepts/最小闭环与组织治理基础]]
- [[concepts/agent可解释性不可信与可审计三元组]]
- [[concepts/agent验收指标清单]]
- [[concepts/workflow与agent的分界]]
- [[concepts/业务验收指标口径]]
- [[concepts/action分级与确认机制]]
- [[queries/workflow定义与既有页面口径冲突待核验]]