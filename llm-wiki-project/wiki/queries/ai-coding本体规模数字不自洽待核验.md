---
type: query
title: AI Coding 本体规模数字不自洽待核验
tags: [待核验, 数字不自洽, 本体规模]
related: [ai-coding-本体系统, catface996]
sources: ["Ontology：AI Coding 在本体中的建模和实战/文章/Ontology：AI Coding 在本体中的建模和实战.md"]
evidence_status: unknown
created: 2026-10-11
updated: 2026-10-11
---

# AI Coding 本体规模数字不自洽待核验

## 问题本身

视频作者 catface996 在《Ontology：AI Coding 在本体中的建模和实战》口播中给出的本体规模数字，在同一段口播内前后不一致，需要核验真实口径。

## 当前已知（作者口播，`unknown`）

| 指标 | 出现的不同数值 |
|---|---|
| Spec instance | 197 个 / 207 个 |
| 规范 | 154 条 / 151 条 |
| 某 Spec 的 User Story | 4 个 / 5 个 |
| 功能性需求 | 7 个 / 11 个 / 16 个 |
| 非功能性需求 | 4 个 / 6 个 |
| 澄清问题 | 3 条 / 29 个 |

相对稳定的数字：class 约 70 个、拓扑子图 23 个、command 25 个、command 依赖 41 条、AC 16 个、任务拆解 45 个、测试用例 34 个、执行 13 次 / 10 个门禁、OpenRouter 余额 1000 美金。

## 冲突来源

- 同一口播内前后不一致。
- 作者已声明本体在不停迭代、数据"可能已经比较老、可能要过时"。

## 缺口

- 缺少系统快照、导出数据或公开文档来确认任一数值。

## 建议搜索式

- catface996 Ontology AI Coding 本体 规模
- AI Coding 本体 class 数量 拓扑子图 command
- bilibili BV1wVb76bE8e Ontology AI Coding

## 下一步研究动作

- 若作者后续发布录屏或文档，优先核对 Spec instance 与规范条数。
- 在未核验前，所有数字仅作"作者自述、待核验"记录，不作为事实。