---
type: query
title: 两套 MCP 能力边界待核验
created: 2026-10-11
updated: 2026-10-11
tags: [Palantir, MCP, 待核验, 权限]
related: [palantir-mcp, ontology-mcp, 工具调用, 工具调用-mcp-sub-agents-skills-任务组织比较]
sources: ["零点未来：AI+企业/第 5 集｜19分钟揭秘Palantir Agent和Ontology如何交互.md"]
evidence_status: unknown
---

# 两套 MCP 能力边界待核验

## 问题本身

视频作者零点未来在「AI+企业」第 5 集中称，Palantir MCP 面向开发者、可修改 Ontology 类型定义但不能写数据；Ontology MCP 面向外部业务 Agent、可读数据与执行 action、写数据但不能改 Object Type 定义。这两套 MCP 的读写权限边界是否如作者所述？

## 当前已知

- Palantir MCP：面向开发者，可改 Ontology 类型定义，不能直接写数据。
- Ontology MCP：面向外部业务 Agent，可读数据、执行 action、写数据，不能改 Object Type 类型定义。
- 作者称核心原则不变：Agent 通过受治理的 Ontology 接口访问一切，绝不绕过 Ontology 直接碰底层数据。
- 以上均为作者口播，本地 ASR 为 `partial`。

## 冲突来源

暂无直接冲突来源，但缺少官方文档对照。

## 缺口

- 两套 MCP 是否为 Palantir 官方产品名。
- 权限边界是否如作者所述。
- 两套 MCP 是否可同时使用、是否存在权限交叉。
- 外部 Agent 通过 Ontology MCP 写数据时是否受与 local Agent 相同的 Governance 约束。

## 建议搜索式

- Palantir MCP Ontology developer documentation
- Palantir Ontology MCP external agent access
- Palantir MCP read write permissions boundary

## 下一步研究动作

检索 Palantir 官方文档与开发者文档，核对两套 MCP 的命名与权限边界；在 [[entities/palantir-mcp]] 与 [[entities/ontology-mcp]] 中更新。