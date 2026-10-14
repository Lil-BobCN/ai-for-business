---
type: concept
title: harness 与 sandbox 解耦
tags: [harness, sandbox, 架构分层, 数据主权]
related: [agent-api与模型-api的分界, 企业-ai的data-logic-action三层模型, 上下文压缩的合规边界待核验, 托管sandbox合作方名称待核验, 自建agent运行时与平台托管运行时]
sources: ["零点未来：AI+企业/第 12 集｜9分钟OpenAI这次卖的不只是模型.md"]
evidence_status: unknown
created: 2026-10-11
updated: 2026-10-11
---

# harness 与 sandbox 解耦

## 定义

视频作者在该段口播中提出：运行时（harness，ASR 作 `Honest`）与执行环境（sandbox）是解耦的两个部分——harness 负责怎么思考、怎么协调、上下文管理以及什么时候调用工具；sandbox 负责代码在哪里执行、文件在哪里操作、依赖在哪里安装、计算资源从哪里买。

## 来源观点

作者称，OpenAI 没有把运行时跟执行环境绑死：运行时可以由 OpenAI 托管，但 sandbox 有多种选择——OpenAI 托管的 sandbox、企业自有基础设施，或第三方 sandbox 环境。作者认为这种结构非常重要，因为企业可以把敏感数据的执行环境放在自己的基础设施，同时使用托管的运行时。作者还称，OpenAI 这次与 `cloud failed`〔公司名 ASR 未可靠识别，待确认〕等几家公司一起提供托管沙箱服务。

## 作者给出的分层（结构化保留）

| 层 | 职责 |
|---|---|
| model | 推理、判断、生成 |
| harness（ASR 作 `Honest`） | 上下文管理、工具管理、Sub-Agent、Agent 编排、长期运行 |
| sandbox | 代码执行、文件操作、依赖安装、算力来源 |
| 企业应用层 | 业务数据、工具 actions、权限、规则、用户体验 |

## 已核验事实

无。分层与解耦设计均来自作者口播，属 `unknown / 待外部核验`。

## 项目分析

该分层与既有 [[concepts/企业-ai的data-logic-action三层模型]] 属不同分层，勿合并。解耦的实用价值在于把「谁负责思考与协调」和「代码在哪跑、数据在哪落」拆成两个可以独立选择的决定。

## 反例或边界

- 作者只在 sandbox 一侧给出数据主权答案（执行环境可自持），未回答「哪些上下文可以出企业边界」——模型调用与上下文仍会离开企业边界。
- 托管 sandbox 的合作方名称未可靠识别。

## 关联页面

- [[concepts/agent-api与模型-api的分界]]
- [[concepts/企业-ai的data-logic-action三层模型]]
- [[queries/上下文压缩的合规边界待核验]]
- [[queries/托管sandbox合作方名称待核验]]
- [[comparisons/自建agent运行时与平台托管运行时]]

## 开放问题

- 哪些上下文可以出企业边界，哪些绝对不行？
- 托管 sandbox 与自建 sandbox 在合规与成本上的分档标准是什么？