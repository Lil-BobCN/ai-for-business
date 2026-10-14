---
type: query
title: Workflow 定义与既有页面口径冲突待核验
created: 2026-10-11
updated: 2026-10-11
tags: [workflow, Agent, 待核验, 定义冲突]
related: [workflow与agent的分界, 工作流与人工介入, 五个工作流设计模式]
sources: ["零点未来：AI+企业/第 8 集｜8分钟7种Agent系统设计模式拆解.md"]
evidence_status: unknown
---

# Workflow 定义与既有页面口径冲突待核验

## 问题本身

「零点未来」第 8 集视频作者把 workflow 定义为「LLM 被编排在预先写死的代码路径里，流程固定，模型只在每一步里面去干活，不能决定下一步」。Wiki 既有 [[concepts/工作流与人工介入]] 可能对 workflow 有不同界定（如含人工节点的编排）。两者是否构成定义冲突？

## 当前已知

- 本集定义：workflow 中 LLM 不能决定下一步，流程写死；agent 中 LLM 动态决定执行过程。
- 本集给出的 workflow 例：RAG（检索→拼提示词→生成，顺序写死）。
- 既有页 [[concepts/工作流与人工介入]] 的具体界定尚未在本页核验。

## 冲突来源

- 本集定义与既有页可能的口径差异：既有页可能把含人工节点的编排也归入 workflow，而本集把 workflow 限定为「LLM 被编排在写死的代码路径里」。

## 缺口

- 既有页 [[concepts/工作流与人工介入]] 对 workflow 的确切界定。
- 两个定义是否可以并存（如按「LLM 是否决定下一步」与「是否含人工节点」两个维度分别划分）。

## 建议搜索式

- LLM workflow vs agent definition who decides next step
- agentic workflow human in the loop definition orchestration
- workflow automation vs AI agent boundary criteria

## 下一步研究动作

1. 核对 [[concepts/工作流与人工介入]] 的现有定义。
2. 若构成冲突，在两个页面中并列描述，保留双方来源与证据状态。
3. 若可并存，明确两个维度的划分边界。