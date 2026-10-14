---
type: query
title: Agent OS 工具与开源状态待核验
created: 2026-10-11
updated: 2026-10-11
tags: [待核验, 开源工具, 领域本体, AgentOS]
related: [agent-os, fibo, bian, ontoprompt, ontoplome与ontoprompt是否同一项目待核验]
sources: ["零点未来：AI+企业/第 6 集｜6分钟聊聊本体Ontology和Agent那些事.md"]
evidence_status: unknown
---

# Agent OS 工具与开源状态待核验

## 问题本身

视频作者在《第 6 集｜6分钟聊聊本体Ontology和Agent那些事》中列举了一批"可快速构建本体"的开源工具与金融领域开源本体，并称国内已有多家公司开发出自己的 Agent OS 产品。这些名称的存在、归属与开源状态均未核验，且 ASR 拼写可能失真。

## 当前已知（来源口播，`unknown`）

- `Onto Flow`〔开源工具名待确认〕——被描述为帮助快速构建 Ontology 本体。
- `Onto EKG`〔拼写待确认〕——被列为类似工具。
- `Onto Plumpt`〔作者自建 demo，拼写待确认〕——作者称在之前视频中出现过，现已做扩展，并植入 Palantir 的知识与方法论。
- `FIBO`〔ASR 作 `Fibro`，拼写待确认〕——金融领域可直接使用的开源本体。
- `BIAN`（Banking Industry Architecture Network）——银行领域的业务语义网络结构。
- 作者称国内已有多家公司开发出自己的 Agent OS 产品，整体方法都是在 Palantir 基础上改良演化，但"现在很难说哪个产品一定就好用或者权威"。

## 冲突来源

- `Onto Plumpt` 与既有 [[entities/ontoprompt]]、[[queries/ontoplome与ontoprompt是否同一项目待核验]] 可能指向同一项目，ASR 拼写不一致，存在命名冲突风险。
- 本集未给出任何工具的产品页、仓库地址或版本信息。

## 缺口

- 上述工具与领域本体的官方名称、维护方、开源许可与可用状态。
- "国内已有多家公司开发出自己的 Agent OS 产品"这一说法的具体公司与产品清单。
- "Agent OS"是否为 Palantir 官方术语。

## 建议搜索式

- FIBO financial industry business ontology open source license
- BIAN Banking Industry Architecture Network semantic standard
- ontology building open source tool Onto Flow Onto EKG

## 下一步研究动作

1. 回到原视频复核上述名称的原始拼写。
2. 分别核验 FIBO 与 BIAN 的官方定位与许可状态。
3. 比对 `Onto Plumpt` 与 `OntoPrompt` 是否为同一项目。