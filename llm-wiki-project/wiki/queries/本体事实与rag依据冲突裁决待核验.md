---
type: query
title: 本体事实与 RAG 依据冲突裁决待核验
created: 2026-10-11
updated: 2026-10-11
tags: [Ontology, RAG, 冲突裁决, 待核验]
related: [本体给事实-rag给依据, 来源溯源, 本体作为约束层]
sources: ["3小时零基础入门FDE！Ontology业务本体原理精讲与项目实战教学，理清知识图谱、RAG与Agent协同，从零搭建企业AI客服中台【附全部源码】/文章/第 12 集｜11-RAG知识增强：本体事实与文档证据融合.md"]
evidence_status: unknown
---

# 本体事实与 RAG 依据冲突裁决待核验

## 问题本身

当一条业务规则既有本体里的结构化约束、又有文档里的原文依据，两者版本不一致时，系统应该以哪一边为准？

## 当前已知

- 视频作者木羽Cheney 在第 12 集口播中提出"本体给事实、RAG 给依据"的分工，并称两者都提供"事实依据"。
- 作者在思考题中自己提出了这个追问，但正文未给出裁决规则。
- 演示界面「核对结果明细」中同时出现规范原文与文件页码，说明两类依据在链路中并存。

## 冲突来源

- 本集口播（`unknown / 待外部核验`）：本体与 RAG 都提供事实依据，未区分强度。
- 分析者判断：本体给出的是建模后的确定事实，RAG 给出的是文档片段，两类依据强度不同。

## 缺口

- 无冲突检测机制、无优先级规则、无版本比对口径。
- 未说明冲突时是否应回退到人工审核。

## 建议搜索式

- ontology vs RAG conflicting facts resolution enterprise knowledge
- knowledge graph structured constraint document evidence conflict precedence
- retrieval augmented generation source of truth conflict handling

## 下一步研究动作

- 查找企业知识库中"结构化约束 vs 文档依据"冲突处理的公开实践。
- 与 [[concepts/来源溯源]] 的最小证据包设计结合，确认版本字段是否足以支撑冲突检测。