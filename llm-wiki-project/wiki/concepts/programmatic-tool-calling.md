---
type: concept
title: programmatic tool calling（PTC）
tags: [PTC, programmatic tool calling, 工具调用, 成本]
related: [长任务agent五项基础设施, 判断计算执行三分法, tool-search与工具目录治理, 工具调用]
sources: ["零点未来：AI+企业/第 12 集｜9分钟OpenAI这次卖的不只是模型.md"]
evidence_status: unknown
created: 2026-10-11
updated: 2026-10-11
---

# programmatic tool calling（PTC）

## 定义

视频作者在该段口播中提出：programmatic tool calling（PTC）指允许 Agent 用程序并行调用工具、串联工具，以及过滤和组合结果，最后只把真正重要的信息交给模型上下文。

## 来源观点

作者称，过去很多 Agent 的工作方式是「LLM 思考一次、调用 tool，结果回来再拿 LLM 思考一次、再调用 tool」，一个任务下来几十次模型调用，不仅慢而且非常贵；但很多工作其实没有必要让 LLM 每一步都参与。作者举例：拿到 10 万条日志，合理做法不是把 10 万条全部扔给模型，而是先用代码过滤、聚合、统计，最后只剩 20 条异常再交给模型分析。作者提到，之前讲 DeepSeek Harness 时也提到过 PTC 模式。

## 已核验事实

无。「10 万条日志筛成 20 条异常」为作者的说明性举例，非实测数据。

## 项目分析

PTC 与 [[concepts/判断计算执行三分法]] 是同一思路的机制与原则两面：机制上把批量计算移出模型调用，原则上明确每一步该由谁执行。

## 反例或边界

- 作者未说明程序化调用的沙箱边界与权限控制方式。
- 示例为工程排障场景，业务写操作场景未检验。

## 关联页面

- [[concepts/判断计算执行三分法]]
- [[concepts/长任务agent五项基础设施]]
- [[concepts/工具调用]]

## 开放问题

- PTC 与既有 tool calling 在计费与可观测性上的差异是什么？