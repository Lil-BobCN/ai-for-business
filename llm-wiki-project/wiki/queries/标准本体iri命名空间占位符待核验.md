---
type: query
title: 标准本体IRI命名空间占位符待核验
tags: [待核验, 本体建模, IRI, 命名空间, 占位符]
related: [标准本体, 本体扩展原则, gb-t-48000-3-2026-本体建模要求]
sources: ["标准数字化/2 征求意见稿（草案全文）/2 GB-T-48000.3-2026 本体建模要求/标准正文（文本版）.md"]
evidence_status: unknown
created: 2026-10-12
updated: 2026-10-12
---

# 标准本体IRI命名空间占位符待核验

## 问题本身

GB/T 48000.3-2026（征求意见稿）中所有实体类型与属性的 IRI 均使用 `http://example.org/standard-ontology#` 前缀。该前缀是正式命名空间还是仅为示例占位符，需要在正式发布版或编制说明中核验。

## 当前已知

- 本来源表4 至表17 中所有实体类型的标识符均为 `http://example.org/standard-ontology#<ClassName>`。
- 本来源附录 A 中所有数据属性的标识符均为 `http://example.org/standard-ontology#<propertyName>`。
- `example.org` 是 IANA 保留的示例域名，通常用于文档示例而非生产命名空间。

## 冲突来源

- 若为正式命名空间，则 `example.org` 作为保留示例域名不适合作为标准本体的长期标识。
- 若为示例占位符，则正式命名空间未在本来源中给出，无法直接用于实现。

## 缺口

- 本来源未给出正式命名空间。
- 缺少编制说明中关于命名空间选择的说明。

## 建议搜索式

- GB/T 48000.3 标准本体 IRI 命名空间 standard-ontology
- 国家标准 本体 命名空间 注册 IRI 规范
- example.org 保留域名 本体 命名空间 示例

## 下一步研究动作

1. 获取 GB/T 48000.3 正式发布版全文，核对 IRI 前缀。
2. 查阅编制说明中关于命名空间与 IRI 的说明。
3. 若正式版仍为占位符，评估实现时的命名空间选择策略。