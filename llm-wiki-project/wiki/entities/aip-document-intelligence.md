---
type: entity
title: AIP Document Intelligence
tags: [Palantir, AIP, 非结构化数据, OCR, 多模态]
related: [aip, palantir-foundry, 三条清洗路径, 文件到本体的五阶段链路]
sources: ["零点未来：AI+企业/第 4 集｜14分钟揭秘Palantir一堆文件如何变成Ontology.md"]
evidence_status: unknown
created: 2026-10-11
updated: 2026-10-11
---

# AIP Document Intelligence

AIP Document Intelligence 是 Palantir AIP 中专门处理非结构化文档（如 PDF 扫描件）的产品能力，负责把无数字化结构的文档转成可映射成本体的结构化字段。本页内容来自本来源视频作者的口播解读，属 `unknown / 待外部核验`。

## 定义与定位

在本来源中，它被描述为处理"维修报告 PDF 扫描件"这类非结构化数据的专用产品，是 [[三条清洗路径]] 中第三条路径（非结构化）的承载者。

## 来源观点（作者口播，`unknown / 待外部核验`）

作者称该流程分五个步骤：

1. 把 PDF 存进 MediaSet。
2. 用 OCR 加多模态视觉理解大模型直接看页面，输出 Markdown 格式文字。作者提到可用 Microsoft 的 `Mockdown`〔库名待确认〕开源库把任何非 Markdown 格式转成 Markdown。
3. 从 Markdown 中解析业务字段（如飞机尾号、维修日期、更换零件）。
4. 校验与复核：检查格式是否正确、AI 提取置信度是否够，并随机抽样本对照原始 PDF 核查。作者强调这一步最容易被跳过，也最容易出错。
5. 输出干净的 Clean Maintenance 表，每行保留一列指向原始 PDF，便于追溯。

## 已核验事实

本页暂无经工具直接验证的事实。产品名称、五步流程与 `Mockdown` 库名均待外部核验。

## 项目分析

该产品把"让 AI 读文档"与"人工抽样核查"绑定，等于承认准确率不能靠模型自证。这条链条上真正决定能否上线的，是随机抽查环节。可迁移的关联模式是"一行结构化字段加一列指向原件"（media reference）。

## 反例与边界

- 作者未给出抽样核查的样本量与判定标准，直接影响该路径能否规模化。
- "追溯到原始文件的某一行"在扫描件场景实际对应某一页，作者表述与实际情况有偏差。

## 关联页面

- [[aip]]：AIP Document Intelligence 是 AIP 的具体能力。
- [[palantir-foundry]]：上游存储与 Pipeline。
- [[三条清洗路径]]、[[文件到本体的五阶段链路]]。

## 开放问题

- AIP Document Intelligence 的正式名称与流程是否与作者描述一致。
- `Mockdown` 库的准确名称与用途。
- PDF 路径规模化所需的抽样标准。