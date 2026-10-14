# Wiki Schema

## Page Types

| Type | Directory | Purpose |
|------|-----------|---------|
| source | wiki/sources/ | 一份原始资料、课程、文章或外部研究来源的摘要和证据信息 |
| concept | wiki/concepts/ | Ontology、RAG、Agent、语义层等概念和方法 |
| entity | wiki/entities/ | 工具、项目、组织、人物、产品或框架 |
| comparison | wiki/comparisons/ | 不同技术、方法、产品或观点的并列比较 |
| query | wiki/queries/ | 尚未解决、存在冲突或需要联网核验的问题 |
| synthesis | wiki/synthesis/ | 基于多个来源形成的阶段性分析和结论 |
| decision | wiki/decisions/ | 已由我确认的项目决策、边界和工作规则 |
| external-research | wiki/external-research/ | 联网研究证据包，必须包含 URL、访问日期和来源类型 |

## Naming

- 文件使用小写 `kebab-case.md`；必要时保留稳定的英文产品名。
- 中文内容可以使用中文标题，但文件名尽量使用短而稳定的拼音或英文 slug。
- 一个页面只承担一个主要主题；跨主题内容使用 `[[wikilinks]]` 连接。
- 不要用一个总结页替代多个来源页；来源页应保留原作者、出处和证据状态。

## Required Frontmatter

```yaml
---
type: source | concept | entity | comparison | query | synthesis | decision | external-research
title: Human-readable title
tags: []
related: []
sources: []
evidence_status: verified | partial | unknown | mixed
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

## Evidence Rules

- `verified` 只用于 URL、文件哈希、抓取时间、页面元数据等已经由工具直接验证的事实。
- `partial` 用于本地 ASR、摘要或不完整转写。
- `unknown` 用于作者主张、案例数字、产品能力或尚未独立核验的判断。
- `mixed` 用于一个页面同时包含多种证据状态；正文必须逐段说明归属。
- 引用视频或 ASR 内容时，使用“视频作者在该段口播中提出……”等归属句。
- 外部研究页必须保留 `url`、`accessed`、`source_kind` 和关键摘录；不要只保存模型生成的二手摘要。

## Page Content Rules

### Source pages

记录标题、作者、平台、URL、原始文件路径、提取方式、证据状态、主要论点和待核验项。

### Concept and entity pages

分开写：定义、来源观点、已核验事实、项目分析、反例或边界、关联页面、开放问题。

### Synthesis and decision pages

必须列出 contributing sources，明确哪些内容是当前分析，哪些内容已经由我确认，哪些仍然待确认。

### Query pages

记录问题本身、当前已知、冲突来源、缺口、建议搜索式和下一步研究动作。

## Contradictions

当来源冲突时：

1. 不静默选择其中一个来源；
2. 在相关页面中描述冲突；
3. 创建或更新 `wiki/queries/` 页面；
4. 保留双方来源和证据状态；
5. 只有完成独立核验或人工判断后，才更新综合结论。

## Source-of-Truth Boundary

- 工作区 `/Users/Admin/orca/ai-for-business/raw/` 是原始真源。
- `llm-wiki-project/raw/sources/` 是供 LLM Wiki 读取的派生副本。
- `llm-wiki-project/wiki/` 是 LLM 生成和人工审核的知识层。
- 不要把 `wiki/` 的推断内容反向覆盖 `raw/`。
