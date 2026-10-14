---
type: source
title: 第 9 集｜ontology, knowledge graph, context graph, code graph&graph engineering一次性搞懂
created: 2026-10-11
updated: 2026-10-11
tags: [ontology, knowledge-graph, context-graph, code-graph, graph-engineering, 零点未来, ASR]
related: [上下文图谱-context-graph, 代码图谱-code-graph, 图谱工程-graph-engineering, 五图两类框架, 本体与知识图谱职责边界待核验, palantir, datahub, atlan, fibo, fhir]
sources: ["零点未来：AI+企业/第 9 集｜ontology, knowledge graph, context graph, code graph&graph engineering一次性搞懂.md"]
evidence_status: partial
---

# 第 9 集｜ontology, knowledge graph, context graph, code graph&graph engineering一次性搞懂

## 来源信息

- 系列：AI+企业（Bilibili 合集，共 12 集）
- 作者：零点未来（Bilibili）
- 平台：Bilibili
- URL：https://www.bilibili.com/video/BV1Mx8S6eE2n
- 原始文件路径：`零点未来：AI+企业/第 9 集｜ontology, knowledge graph, context graph, code graph&graph engineering一次性搞懂.md`
- 提取方式：本地 ASR 口播整理稿（非官方字幕）
- 证据状态：`partial`（ASR 转写不完整，专名、缩写与数字可能有误）；作者主张为 `unknown / 待外部核验`

## 一句话摘要

视频作者用一集把五个带 graph 的词拆成两类：本体、知识图谱、上下文图谱、代码图谱回答的是"系统知道什么"——它们分别是规则书、世界网、业务上下文地图和代码的管网图；图谱工程（Graph Engineering）回答的是另一件事，"系统怎么干活"——它是给 Agent 铺好的那条轨道。

## 主要论点（均为作者口播，`unknown / 待核验`）

1. **五词两类框架**：前四图回答"系统知道什么"，图谱工程回答"系统怎么干活"；作者称"知道什么决定答得对不对"。这是作者自创框架，非行业公认划分。
2. **Palantir ontology 六要素**：objects、links、properties、logic、actions、security。属对既有产品的描述性主张。
3. **开源本体示例**：金融 `FIBO`（ASR 作 `fibre`）、医疗 `FHIR`。`FHIR` 通常被描述为医疗数据交换标准，是否属"开源本体"需单独核实。
4. **上下文图谱三层结构**：语义基础 / 元数据（血缘、质量、责任、权限）/ 决策轨迹——属作者或厂商整理，非通行定义。
5. **context graph 定义分歧**：厂商口径（DataHub、`Atlant`）偏决策轨迹与治理；学术论文口径偏"给事实补时间、地点、出处、置信度"；作者口径为"企业此刻的业务上下文"。作者未给论文出处。
6. **代码图谱构成**：源代码 + 抽象语法树 + 依赖关系 + 执行关系；使用时机为"代码量大到人脑记不住时"。
7. **四层全景架构**与**采购寻源 Agent 示例**：参考架构与演示性示例，非客户案例。

## 作者原表：场景对照

| 场景 | 用哪张图 |
|---|---|
| 机器推理、推出新结论、统一语义术语 | ontology |
| 通用常识问答、推荐、多跳问答 | knowledge graph |
| Agent 进公司干活、影响分析、审计追踪 | context graph |
| 代码导航、改代码影响评估 | code graph |
| 有套路的业务流程编排、稳定可控的 Agent 流水线 | graph engineering |

## 作者原述：四层全景架构

| 层 | 内容 |
|---|---|
| 定义层 | ontology，定义概念与语义关系，是基础 |
| 表示层（表征层） | 知识图谱、上下文图谱、代码数据 |
| 工程层 | graph engineering，给 Agent 的工程运作 |
| 应用层 | 给 Agent 提供的运行环境与运行工具 |

## 作者原述：Palantir ontology 六要素

- objects：实体
- links：实体之间的关系
- properties：实体的属性
- logic：逻辑、规则
- actions：动作
- security：权限操作，即 AI Agents 能做什么

## 作者原述：上下文图谱三层结构

- 底层：语义基础（实体是什么意思）
- 中间：元数据（数据血缘、来源、质量分、负责人、可见范围）
- 顶层：决策轨迹（谁在核实、为何批准了什么）

## 作者原述：graph engineering 的 loop 示例

Agent 调用工具 → 另一个 evaluate Agent 进行检查 → 若不够好则回到该 Agent 循环。作者称这是最简单的 graph engineering。

## 待核验项

1. 作者未给出处的"context graph 学术论文"具体是哪一篇。
2. `FHIR` 是否应归入"开源本体"。
3. 四层架构中定义层未覆盖某域时，上层如何表现。
4. 代码图谱与主干代码的同步延迟是否应作为运维指标。
5. ASR 存疑专名：`倾启`、`来战表`、`自然表`、`Atlant`、`拍什么一件`、`cope`、`反正决策`、`fibre`、`瞻山`。

## 关联页面

- [[上下文图谱-context-graph]]
- [[代码图谱-code-graph]]
- [[图谱工程-graph-engineering]]
- [[五图两类框架]]
- [[本体与知识图谱职责边界待核验]]
- [[palantir]]
- [[datahub]]
- [[atlan]]
- [[fibo]]
- [[fhir]]