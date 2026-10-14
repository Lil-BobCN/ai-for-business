---
type: entity
title: 本体问答 Agent Skills
created: 2026-10-11
updated: 2026-10-11
tags: [Agent Skills, 本体问答, 检索, Codex, 结构化查询, 图遍历, 语义检索]
related: [本体构建-agent-skills, fde-本体应用工作台, fde-ai-应用开发实战课, codex, owl, 结构化查询, 图遍历与bfs扩展, 向量检索与图扩展]
sources: ["3小时零基础入门FDE！Ontology业务本体原理精讲与项目实战教学，理清知识图谱、RAG与Agent协同，从零搭建企业AI客服中台【附全部源码】/文章/第 9 集｜08-本体检索机制：结构化查询、图遍历与语义检索.md"]
evidence_status: unknown
---

# 本体问答 Agent Skills

本体问答 Agent Skills 是视频作者木羽Cheney 在 [[fde-ai-应用开发实战课]] 第二场直播中提供的三个 Agent Skills，用于让 Agent 基于一份本体文件执行本体问答检索。它们与 [[本体构建-agent-skills]] 同族：后者面向"把业务数据建成本体"，本组面向"把建好的本体用起来"。

## 定义与来源观点

视频作者在该集口播中提出，本节课程配套提供了三个 skills，位于 `01 本体问答` 目录，一对一对应三种检索策略：

1. 结构化检索；
2. 图检索；
3. embedding 加图扩展（ASR 写作 inbinding，待确认）。

作者称使用方式是：把 skills 文件放入 [[codex]] 中让其读取，再把上一集产出的业务本体 `.owl` 文件放进去，即可进行构建与查询。

## 已核验事实

- 三个 skills 的存在、目录名与对应关系均来自视频作者口播，属 `unknown / 待外部核验`。
- 本 Wiki 尚未取得 skills 文件本身，其内容、接口与可运行性未独立核验。

## 项目分析

- 三个 skills 与三种检索策略一一对应，说明作者把"检索策略选型"固化成了可交付的 Agent 能力单元，而不是仅停留在讲解层面。
- 与 [[本体构建-agent-skills]] 形成"建模侧 skills → 调用侧 skills"的配对，可作为本体交付物清单的一部分。
- 作者提到 skills 可放入 codex 或某个 Agent 运行环境（ASR 写作 dipstick harness，待确认）中加载。

## 反例或边界

- 作者未说明三个 skills 之间是否会自动路由，还是需要人工选择。
- 作者未说明 skills 在检索失败时的回退行为。

## 关联页面

- [[本体构建-agent-skills]]
- [[fde-本体应用工作台]]
- [[codex]]、[[owl]]
- [[结构化查询]]、[[图遍历与bfs扩展]]、[[向量检索与图扩展]]

## 开放问题

- 三个 skills 是否已实际领取？其内部是否包含检索策略路由逻辑？
- 是否需要把"建模侧 skills + 调用侧 skills"整理成一份完整的本体交付物清单？