---
type: query
title: Context Graph 三方定义冲突待核验
created: 2026-10-11
updated: 2026-10-11
tags: [context-graph, 定义冲突, 待核验]
related: [上下文图谱-context-graph, datahub, atlan, context-graph学术论文出处待核验]
sources: ["零点未来：AI+企业/第 9 集｜ontology, knowledge graph, context graph, code graph&graph engineering一次性搞懂.md"]
evidence_status: unknown
---

# Context Graph 三方定义冲突待核验

## 问题本身

"context graph" 一词在数据平台厂商、学术界与视频作者之间是否存在互不兼容的定义？如果同一份方案里三方各用一套定义，"到底上没上 context graph"这个验收问题还能不能回答？

## 当前已知（均来自本来源作者口播，`unknown / 待核验`）

1. **厂商口径**：一些数据平台厂商，如 DataHub 与 `Atlant`（疑为 Atlan，拼写待确认），站在一家公司的角度，更注重决策轨迹和治理。
2. **学术论文口径**：作者称有一篇论文把 context graph 定义为在知识图谱基础上，为反映当前状态与上下文信息，增加时间、地点、出处、置信度等信息。作者未给出论文出处。
3. **作者口径**：企业此刻的业务上下文。

## 冲突来源

- 本来源作者自己承认 context graph 一词在厂商、学术界和他自己的用法之间并不一致，属显性冲突。
- 三方来源均未在本来源中给出可核验的原始出处（无 URL、无论文标题、无版本号）。

## 缺口

- 缺少 DataHub、Atlan 官方文档中对 "context graph" 的定义原文。
- 缺少作者所指学术论文的具体标题、作者与发表信息。
- 缺少"context graph"在行业标准或权威综述中的通行定义。

## 建议搜索式

- DataHub context graph definition metadata governance
- Atlan context graph data catalog decision lineage
- context graph knowledge graph temporal provenance confidence definition

## 下一步研究动作

1. 检索 DataHub 与 Atlan 官方文档，确认是否使用 "context graph" 术语及其定义。
2. 检索作者所指学术论文，确认其定义与出处。
3. 在方案文档层面，建议显式写出"本文中的 context graph 指什么"，而非争论谁的定义更正确。

## 关联页面

- [[上下文图谱-context-graph]]
- [[datahub]]
- [[atlan]]
- [[context-graph学术论文出处待核验]]