---
type: entity
title: Palantir
tags: [Palantir, Ontology, logic-function, Agent, FDE, 企业软件, 数据平台]
related: [本体与agent协同, 工具调用, fde交付方法, 工具调用-mcp-sub-agents-skills-任务组织比较, fde岗位定义与palantir-openai实践待核验, fde相关数字原音与统计口径待核验, palantir-foundry, 标准本体建模要求与palantir-ontology比较, ontology-是操作层还是知识图谱]
sources: ["3小时零基础入门FDE！Ontology业务本体原理精讲与项目实战教学，理清知识图谱、RAG与Agent协同，从零搭建企业AI客服中台【附全部源码】/文章/第 11 集｜10-Agent业务集成：工具调用与订单客服问答.md", "3小时零基础入门FDE！Ontology业务本体原理精讲与项目实战教学，理清知识图谱、RAG与Agent协同，从零搭建企业AI客服中台【附全部源码】/文章/第 4 集｜03-FDE交付方法：从业务需求到AI应用落地.md", "palantir研究/央国企一把手听懂Palantir.md"]
evidence_status: unknown
created: 2026-10-11
updated: 2026-10-12
---

# Palantir

Palantir Technologies 是一家提供数据集成、数据分析与运营决策平台的企业软件公司，核心产品线包括 Foundry、Gotham 与 Apollo，并以“本体（ontology）”作为平台的核心抽象层对外宣传。以上公司身份为可独立核验的公开背景信息，不归因于本页所列视频来源。

> [!note] 来源边界
> 本页“来源观点”均为视频作者的主张或转述，未经独立核验，不能据此认定为 Palantir 已确认的产品能力或岗位定义。

## 来源观点

### 本体定位：《央国企一把手听懂 Palantir》

在 B 站视频《央国企一把手听懂 Palantir》的 ASR 转写中，视频作者把 Palantir 定位为“本体（ontology）解法的提出方”：

- 作者称 Palantir 的思路不是推倒既有系统，而是在既有系统之上加一层本体。
- 作者用“动态数字孪生”“活地图”来解释 Palantir 的本体概念。
- 作者把 Palantir Foundry 描述为“经营沙盘”的载体与既有 IT 投资的“力量倍增器”。

以上均为视频作者主张，未经独立核验。

### Logic function（第 11 集）

第 11 集作者称，Palantir 的官方博客或文档中存在 `logic function` 概念，即把领域本体业务模型中的逻辑封装成 Agent 可以调用的 function。

该集作者还在课程介绍中将 Palantir 与 OpenAI 作为 FDE 定义和企业落地实践的参考对象。

### FDE 定位转述（第 4 集）

第 4 集作者转述一位据称在 Palantir 担任 FDE 14 年的从业者观点，并据此将“以结果为目标”、对可量化业务结果负责描述为 FDE 的核心定位。

这仍是视频作者的转述，不等于已核验的 Palantir 官方岗位定义。

## 已核验事实

- 本页暂无经工具直接验证的一手事实。
- Palantir 官方对本体的定义、Foundry 的能力边界、权限与审计机制均待外部核验。
- 来源没有提供 `logic function` 相关原文章标题、URL、发布日期、函数签名或可复核示例；第 4 集相关转述也未提供从业者姓名。现有材料不足以复核这些说法。

## 项目分析

如果业务本体中的规则、查询和更新被封装为可调用函数，交付团队需要同时定义：

- 函数的业务语义和输入输出；
- 权限与副作用；
- 规则版本、责任人和变更记录；
- 失败、冲突和人工介入条件；
- 执行日志和结果溯源。

这些是视频内容引出的设计问题，不是来源对 Palantir 产品的证明。

《央国企一把手听懂 Palantir》为 Wiki 在 Palantir/本体操作层方向提供了视频侧素材，与 [[标准本体建模要求与palantir-ontology比较]] 直接相关。需要注意：视频中的“名词 + 动词”是作者的解释框架，不等于 Palantir 官方定义。

## 待核验项与开放问题

- `logic function` 的正式名称和官方出处；
- 该概念与普通 tool calling、业务规则和事务更新的边界；
- Palantir Ontology 与 Agent 的正式集成方式；
- 视频作者所说的 FDE 定义是否准确反映官方资料；
- 据称任职 14 年的从业者身份、年限和原始发言；
- Palantir 官方对 ontology 的定义与视频作者的“名词 + 动词”框架差异有多大？
- Foundry 的写回、权限模型与审计链在官方文档中如何描述？

## 反例或边界

- 《央国企一把手听懂 Palantir》视频未给出任何量化数据、案例数字或一手文档引用。
- “不推翻既有 IT 投资”“力量倍增器”属于厂商定位式表述与修辞，落地改造量仍需按项目核验。

## 关联页面

- 本体接入：[[本体与 Agent 协同]]
- 工具封装：[[工具调用]]
- FDE 方法：[[FDE 交付方法]]
- 岗位定义核验：[[FDE 岗位定义与 Palantir、OpenAI 实践待核验]]
- [[palantir-foundry]]
- [[标准本体建模要求与palantir-ontology比较]]
- [[ontology-是操作层还是知识图谱]]
- [[名词动词框架]]