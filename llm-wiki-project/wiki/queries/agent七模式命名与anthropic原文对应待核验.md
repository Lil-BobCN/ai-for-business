---
type: query
title: Agent 七模式命名与 Anthropic 原文对应待核验
created: 2026-10-11
updated: 2026-10-11
tags: [Agent, 设计模式, 待核验, Anthropic, ASR]
related: [五个工作流设计模式, 单agent循环与两个敌人, 多agent两种架构-经理模式与交接制, anthropic, agent选型三原则与anthropic三条铁律]
sources: ["零点未来：AI+企业/第 8 集｜8分钟7种Agent系统设计模式拆解.md"]
evidence_status: unknown
---

# Agent 七模式命名与 Anthropic 原文对应待核验

## 问题本身

「零点未来」第 8 集视频作者拆解的七个 Agent 系统设计模式，其英文命名与归类是否与 Anthropic 公开的 Agent 设计模式体系一一对应？ASR 转写存在误差，需交叉核对。

## 当前已知

- 能按上下文唯一还原的模式名：Prompt Chaining、Routing、Parallelization、Evaluator-Optimizer、while loop。
- 第一个模式的英文名 ASR 前后出现三种形态：`plombed training`、`PoM Training`、`Prompt Training`，本文按上下文还原为 Prompt Chaining。
- 第五个模式「编排」的英文模式名 ASR 未捕获，作者描述为「编排者按输入现场动态拆解任务并派给功能，再合成结果」。
- 并行化两种形态：切分、投票。
- 作者称已在自己的 GitHub 上放出这 7 个模式的示例代码，但视频未给出 URL 或仓库名。

## 冲突来源

- ASR 三种转写形态互相冲突，无法唯一确定第一个模式的英文名。
- 作者描述与 Anthropic 公开体系（如 Sectioning / Voting、Orchestrator-Workers）的对应关系未经核验。

## 缺口

- 作者 GitHub 仓库 URL 与示例代码。
- Anthropic 官方 Agent 设计模式文档的原文命名与分类。

## 建议搜索式

- Anthropic building effective agents workflow patterns prompt chaining routing parallelization
- Anthropic agent design patterns orchestrator workers sectioning voting evaluator optimizer
- 零点未来 Agent 系统设计模式 示例代码 GitHub

## 下一步研究动作

1. 定位作者 GitHub 仓库，核对七个模式的英文命名与示例代码。
2. 对照 Anthropic 官方工程文档，确认模式命名与归类的一一对应关系。
3. 若无法定位作者仓库，则保留 ASR 原文并标注为待确认。