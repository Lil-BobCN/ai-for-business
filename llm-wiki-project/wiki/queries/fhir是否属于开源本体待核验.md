---
type: query
title: FHIR 是否属于开源本体待核验
created: 2026-10-11
updated: 2026-10-11
tags: [fhir, 开源本体, 归类待核验]
related: [fhir, fibo, 本体与知识图谱职责边界待核验]
sources: ["零点未来：AI+企业/第 9 集｜ontology, knowledge graph, context graph, code graph&graph engineering一次性搞懂.md"]
evidence_status: unknown
---

# FHIR 是否属于开源本体待核验

## 问题本身

视频作者在"零点未来：AI+企业"第 9 集中把 FHIR 归入"医疗领域的开源本体"。FHIR 是否应归入"开源本体"？

## 当前已知

- 作者口播（`unknown / 待核验`）：像金融领域、医药领域都有一些开源的本体可以使用，比如金融领域的 `FIBO`（ASR 作 `fibre`，拼写待确认），还有医疗的 FHIR。
- 独立可核验背景：FHIR 通常被公开描述为由 HL7 组织制定的医疗数据交换标准（interoperability standard），而非本体（ontology）。

## 冲突来源

- 作者归类与 FHIR 的通行定位存在张力：数据交换标准与本体在目的、形式化程度、推理能力上并不等同。
- 本来源未给出 FHIR 的官方文档或版本信息。

## 缺口

- 缺少 FHIR 官方对自身定位的表述。
- 缺少 FHIR 是否包含形式化本体层（如 OWL/RDF 表达）的证据。
- 缺少"开源本体"这一分类的权威界定。

## 建议搜索式

- FHIR ontology OWL RDF formal semantics
- HL7 FHIR interoperability standard vs ontology difference
- FIBO FHIR open source ontology comparison

## 下一步研究动作

1. 检索 HL7 FHIR 官方文档，确认其是否提供本体层表达。
2. 对比 FIBO 与 FHIR 的形式化程度，判断二者是否可同归"开源本体"。
3. 将结论回填至 [[fhir]] 与 [[fibo]]。

## 关联页面

- [[fhir]]
- [[fibo]]
- [[本体与知识图谱职责边界待核验]]