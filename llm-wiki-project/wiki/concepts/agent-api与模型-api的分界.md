---
type: concept
title: Agent API 与模型 API 的分界
tags: [Agent API, 模型 API, 运行时, 数字员工]
related: [openai, codex, 长任务agent五项基础设施, harness与sandbox解耦, openai-agent-api发布事实待核验]
sources: ["零点未来：AI+企业/第 12 集｜9分钟OpenAI这次卖的不只是模型.md"]
evidence_status: unknown
created: 2026-10-11
updated: 2026-10-11
---

# Agent API 与模型 API 的分界

## 定义

视频作者在该段口播中提出：模型 API 更像「给你一个大脑」，只提供推理、判断与生成；Agent API 更像「给你一个可以持续工作的数字员工的运行时软件」，除模型之外还包含 Agent Loop、Context Management、Tool Management 以及 Sub-Agent 协调等能力。

## 来源观点

作者称，过去开发一个 Agent 通常要自己拼装：最下面是大模型，然后接 Tools，再往上还要自己处理 Memory、Context、Workflow、Tools Calling、Multi-agents、Sandbox、Checkpoint 等。这次 OpenAI 做的事情，是把 Codex 已经在使用的那套运行时直接通过 API 开放出来——使用者只需说明「要完成什么任务、用什么模型、使用什么工具、在哪个环境执行」，剩下的 Agent Loop、上下文管理、工具管理与 Sub-Agent 协调由平台处理。

## 已核验事实

无。本页所有内容均来自视频作者口播，属 `unknown / 待外部核验`。产品名称、发布形式与发布时间均未在视频中给出可核对信息。

## 项目分析

这一分界的实用价值在于把「我们的 Agent 还不好用」翻译成一串可检查的工程项，而不是归因于「模型还不够强」。它与 [[concepts/长任务agent五项基础设施]] 互为表里：前者是产品形态的划分，后者是能力清单。

## 反例或边界

- 作者未说明 Agent API 与既有 Agent framework 在能力上的重叠部分如何划分。
- 「数字员工运行时」是比喻性表述，不构成可验收的能力定义。

## 关联页面

- [[concepts/长任务agent五项基础设施]]
- [[concepts/harness与sandbox解耦]]
- [[queries/openai-agent-api发布事实待核验]]
- [[queries/openai-agent-api正式名称与能力边界待核验]]

## 开放问题

- Agent API 的正式产品名与能力边界是什么？
- 平台托管的运行时与自建运行时在哪些任务长度与合规要求下各自更合适？