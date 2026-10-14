---
type: concept
title: Agent framework 下沉
tags: [framework, 下沉, 预测, LangGraph, CrewAI]
related: [langgraph, agent-api与模型-api的分界, 本体与agent协同, 工作流与人工介入]
sources: ["零点未来：AI+企业/第 12 集｜9分钟OpenAI这次卖的不只是模型.md"]
evidence_status: unknown
created: 2026-10-11
updated: 2026-10-11
---

# Agent framework 下沉

## 定义

视频作者在该段口播中提出一个判断：Agent 的 framework 不会突然消失，而是大量通用的 Agent 能力会慢慢往下沉，被模型厂商收编进平台层。

## 来源观点

作者称，LangGraph、CrewAI 这些 framework 不会突然消失，但通用能力在持续下沉：tool calling 已经进入模型的 API，web search、file search、computer use 也进入了一些平台；现在连上下文管理、工具搜索、多 Agent 编排、长任务管理，都由模型厂商开始提供。作者由此建议，未来开发者真正应该投入精力的，可能不再是「我用了哪些 Agent framework」，而是：你的业务 context 是什么？Agent 应该理解哪些业务对象、哪些数据是可信的？有哪些 actions 和 function 可以调用？权限怎么控制？什么事情能够自动运行、什么事情必须人工审批？

## 已核验事实

无。该判断属作者预测，非既成事实。

## 项目分析

作者把「用了哪个框架」降级成实现细节，把业务上下文与治理提到台前——这其实是一次资产位置的搬家。可追问：如果框架每两年换一次，团队的沉淀放在哪一层才不会跟着一起被换掉？

## 反例或边界

- 作者未给出「下沉」的时间尺度与可观测指标。
- 该判断来自平台侧发布叙述，缺少独立证据。

## 关联页面

- [[entities/langgraph]]
- [[concepts/agent-api与模型-api的分界]]
- [[concepts/本体与agent协同]]
- [[concepts/工作流与人工介入]]

## 开放问题

- 通用能力下沉后，企业侧可交接的资产清单应包含哪些条目？