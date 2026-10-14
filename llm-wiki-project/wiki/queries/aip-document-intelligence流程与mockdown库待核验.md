---
type: query
title: AIP Document Intelligence 流程与 Mockdown 库待核验
tags: [Palantir, AIP, OCR, 多模态, Mockdown]
related: [aip-document-intelligence, 三条清洗路径]
sources: ["零点未来：AI+企业/第 4 集｜14分钟揭秘Palantir一堆文件如何变成Ontology.md"]
evidence_status: unknown
created: 2026-10-11
updated: 2026-10-11
---

# AIP Document Intelligence 流程与 Mockdown 库待核验

## 问题本身

本来源视频作者描述了 AIP Document Intelligence 处理非结构化 PDF 的五步流程，并提到可用 Microsoft 的 `Mockdown`〔库名待确认〕把非 Markdown 格式转成 Markdown。产品名称、流程与库名均待核验。

## 当前已知

- 作者称五步为：存 MediaSet → OCR+多模态视觉大模型输出 Markdown → 解析业务字段 → 校验复核（含人工抽样）→ 输出 Clean Maintenance 表并保留指向原 PDF 的列。
- 作者称 `Mockdown` 是 Microsoft 的开源库，用于把非 Markdown 格式转 Markdown。

## 冲突来源

- 无直接冲突来源，但均为作者口播，无一手文档佐证。

## 缺口

- 缺少 AIP Document Intelligence 官方产品页与流程说明。
- `Mockdown` 的准确名称、归属与用途不明。

## 建议搜索式

- Palantir AIP Document Intelligence OCR multimodal pipeline
- Microsoft Markdown conversion open source library document
- Palantir AIP 非结构化文档 处理流程

## 下一步研究动作

查阅 Palantir AIP 官方文档 Document Intelligence 章节；检索 Microsoft 相关 Markdown 转换开源库。