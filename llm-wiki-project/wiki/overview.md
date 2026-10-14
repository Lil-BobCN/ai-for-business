---
type: overview
title: 企业 AI 语义层与 Agent 研究 Wiki
tags: [企业AI, Ontology, Agent, RAG, 语义层, 标准数字化]
related: [index, log]
sources: []
evidence_status: mixed
created: 2026-10-11
updated: 2026-10-12
---

# 企业 AI 语义层与 Agent 研究 Wiki

本 Wiki 由 `llm-wiki-project/raw/sources/` 派生，服务于 `purpose.md` 列出的关键问题：
企业 AI 语义层由哪些部分组成、Ontology / 知识图谱 / RAG / Agent 如何分工、
企业 Agent 落地需要哪些数据与机制、FDE 交付方法能否从资料中提炼、
以及**哪些结论只是一手资料里的作者主张，哪些已有可复核证据**。

本页只描述 Wiki 的**当前覆盖范围与状态**，不给出研究结论。
阶段性判断请见 [[index]]，逐次摄入记录请见 [[log]]。

## 一、当前资料覆盖（4 组来源，共 50 份）

| 来源组 | 文件数 | 资料性质 | 证据状态 |
| --- | --- | --- | --- |
| `标准数字化/` | 24 | 国家/行业标准的官方条目档案、6 份公开征求意见稿全文与编制说明、7 份原始 PDF | `mixed`：元数据 `verified`；征求意见稿为草案，`partial`；正式发布版条款 `unknown` |
| `3小时零基础入门FDE！…` | 13 | B 站课程 ASR 转写文章 | `partial`（本地 ASR，非官方字幕） |
| `零点未来：AI+企业` | 12 | B 站系列视频 ASR 转写文章 | `partial`（本地 ASR，非官方字幕） |
| `Ontology：AI Coding 在本体中的建模和实战` | 1 | 课程/文章整理 | `partial` |

**证据口径不可混用**：ASR 转写与视频作者主张属于 `unknown / 待外部核验`，
不得因为被多次引用就升级为 `verified`。`标准数字化/` 组内的官方元数据字段
可以在 `std.samr.gov.cn` 详情页逐一复核，但其中的草案条款仍不是正式发布版条款。

## 二、Wiki 当前规模

| 页面类型 | 数量 |
| --- | --- |
| source | 50（与 `raw/sources/` 文件数 1:1） |
| concept | 157 |
| entity | 74 |
| query（开放问题 / 待核验） | 175 |
| comparison | 9 |
| synthesis | 0 |
| decision | 0 |
| external-research | 0 |

摄入队列当前为空。审核队列仍有待人工判断项，处理顺序见
`docs/llm-wiki/操作使用手册.md` 第九节。

## 三、尚未做的事

- **没有 synthesis 与 decision 页面**：按 `purpose.md` 的研究规则，
  只有经明确确认的判断才进入这两类页面，目前还没有任何结论走完这道确认。
- **没有 external-research 页面**：外部联网证据包尚未建立。
  现有 175 个 query 页面记录了缺口与建议搜索式，但都还没有对应的外部核验结果。
- **标准正文的条款级引用仍不可用**：`标准数字化/` 组只保存了元数据与征求意见稿，
  正式发布版条款未获取，任何条款级判断都应先回到
  `https://openstd.samr.gov.cn/bzgk/std/` 在线阅读或正式出版物核对。

## 四、边界

- 原始资料真源：工作区 `raw/`（若存在）→ 派生副本 `llm-wiki-project/raw/sources/`。
  本 Wiki 不反向覆盖 `raw/`。
- 本页及全站页面的 `evidence_status` 分级见 `schema.md`；
  `verified` 只用于 URL、文件哈希、抓取时间、页面元数据等工具直接验证过的事实。
- 图中的边表示页面之间的关联，**不等于**事实已被独立证明。
