---
type: concept
title: tool search 与工具目录治理
tags: [tool search, 工具目录, 工具治理, 企业工具规模]
related: [长任务agent五项基础设施, 企业工具数量量级待核验, 工具调用, programmatic-tool-calling]
sources: ["零点未来：AI+企业/第 12 集｜9分钟OpenAI这次卖的不只是模型.md"]
evidence_status: unknown
created: 2026-10-11
updated: 2026-10-11
---

# tool search 与工具目录治理

## 定义

视频作者在该段口播中提出：tool search 指不把全部 tool definition（工具定义）一次性塞给模型，而是由 Agent 在真正需要时检索出相关工具，再把对应的 tool schema 加入上下文。

## 来源观点

作者称，现在很多 Agent 一启动就把所有工具定义一次性塞给模型；企业里可能只有 5 个工具时没问题，但可能是 ERP 100 个接口、采购系统 200 个 action，再加上 CRM、财务知识库、MCP server 等，最后可能有「上千个、三万个」的工具〔数字依 ASR 原文，待确认〕，全部塞进 prompt 不仅浪费 token，还会让模型更难选对工具。作者举例：调查一次现场事故时，可能只搜索日志查询、deployment 和 metrics 这几个相关工具，再把 tool schema 加进上下文。作者由此判断，未来企业 Agent 的问题可能不再是「能不能调用工具」，而是「有这么多工具时怎么找到正确的那一个」。

## 已核验事实

无。工具数量与机制描述均来自作者口播，属 `unknown / 待外部核验`。

## 项目分析

检索要选得准，前提是每个工具的命名、描述与权限标注都写得足够清楚——这份工作不会因为有了 tool search 就消失，只是从「写调用代码」挪到了「维护目录」。把工具当成对外接口来治理（命名规范、schema、权限、废弃流程），检索准确率才有可维护的下限。

## 反例或边界

- 命名混乱、描述缺失、权限不清的工具集会让 tool search 失效。
- 作者未说明工具目录的准入与质量责任归属。

## 关联页面

- [[concepts/长任务agent五项基础设施]]
- [[concepts/工具调用]]
- [[concepts/programmatic-tool-calling]]
- [[queries/企业工具数量量级待核验]]

## 开放问题

- 工具数量过千之后，谁负责目录的质量与准入？
- 检索准确率如何度量与回归？