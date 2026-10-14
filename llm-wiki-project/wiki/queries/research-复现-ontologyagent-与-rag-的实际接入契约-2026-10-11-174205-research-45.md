---
type: query
title: "Research: 复现 Ontology、Agent 与 RAG 的实际接入契约"
created: 2026-10-12
origin: deep-research
tags: [research]
---

# Research: 复现 Ontology、Agent 与 RAG 的实际接入契约

# Ontology、Agent 与 RAG 的实际接入契约复现

**页面类型**：综合（Synthesis）
**主要来源**：[1] Tool Calling with LangChain；[2] LangGraph 客服升级案例；[3] Agent Search with LangGraph；[4][5][6] Agentic RAG 企业实践指南

## 一、问题界定

既有 wiki 页面已从原理层讨论过 [[本体与agent协同]]、[[本体给事实-rag给依据]]、[[agent与ontology五层交互架构]]。但要把三者"复现"成一条可运行链路，还缺一层工程问题：**它们之间实际以什么接口对接**。本页把接入契约拆成四组边界：

| 契约 | 两端 | 核心内容 | 本轮证据 |
|---|---|---|---|
| A 模型—工具 | 模型 ↔ 工具集 | `bind_tools` 的 schema 契约 | [1] |
| B Agent—RAG | Agent ↔ 检索器 | 检索作为动作、决策权归属 | [4][5][6] |
| C 编排—运行时 | 图 ↔ 状态/人工 | 路由、升级、并行、状态管理 | [2][3] |
| D 本体—调用方 | 本体 ↔ Agent/RAG | 事实、约束、动作的导出 | 本轮来源未覆盖，见跨页推论 |

```
用户请求
   │
   ▼
[LangGraph 状态机] ──路由──▶ [升级 / 人工审核]（中断与检查点）
   │
   ▼
[Agent 模型] ──bind_tools──▶ 工具目录
   │                          ├─ 本体结构化查询（确定性）
   │                          ├─ 图遍历 / 子图检索
   │                          ├─ RAG 语义检索（证据）
   │                          └─ Action 调用（分级确认）
   ▼
[观察结果回填] ──▶ 下一轮推理 / 产出回答
```

复现案例可对照 FDE 客服中台课程中的 [[fde-本体应用工作台]] 与 [[订单客服本体]]。

## 二、契约 A：模型—工具（`bind_tools`）

[1] 给出 LangChain 侧的统一入口 `ChatModel.bind_tools(...)`，并列出四种可混用的工具定义形态：

| 形态 | 代码要点 | 语义描述来源 |
|---|---|---|
| Pydantic class | `class multiply(BaseModel)` + `Field(..., description=...)` | 类 docstring 与字段 `description` |
| LangChain tool | `@tool` 装饰普通函数 | 函数 docstring |
| 普通 Python 函数 | 直接传入 `subtract` | 函数 docstring |
| OpenAI-format dict | `{"name", "description", "parameters"}` | `description` 与 JSON schema（可带 `title` 与 `description`） |

示例中 `llm_with_tools = llm.bind_tools([multiply, exponentiate, add, subtract])`，注释说明每次调用时"所有工具定义都会传给模型"[1]。

契约要点归纳：

- **三要素**：名称（name）、语义描述（description）、参数 JSON schema（parameters / required）。
- **description 是路由依据**：模型选择哪个工具主要取决于描述文本，描述质量直接决定动作选择正确率。
- **全量注入**：绑定即随每次调用传入全部工具定义 [1]，工具规模大时必须配合目录治理手段，见 [[tool-search与工具目录治理]]、[[programmatic-tool-calling]]。
- **缺口**：[1] 只展示"绑定"，未展示工具执行、结果回填与多轮循环；示例使用 `langchain_core.pydantic_v1` 与 `claude-3-sonnet-20240229`（[[anthropic]]），存在版本陈旧风险；注释写 "all three" 而实际列出四个工具定义，属文档笔误。

对本体的含义（跨页推论）：把本体中的动作与查询模板按上述三要素导出，即可成为 Agent 可调用的工具；这与 [[action-pipeline-automation-function工具分工]] 的工具分工、[[语义元素与动态元素两分法]] 的分类可直接对齐。此映射待一手文档核验（见第七节）。

## 三、契约 B：Agent—RAG（检索即动作）

三家厂商对 Agentic RAG 的定义高度一致——**把检索嵌入自主推理与决策循环**：

- Moveworks：Agentic RAG 结合 RAG 与 AI Agent，将自主推理与决策能力引入检索 [6]；
- Toloka：Agentic RAG 模拟一套工作流——先决定做什么、再收集上下文、再推理；示例场景为内部金融研究 [5]；
- Cohere：面向企业真实工作流的 Agentic RAG 落地指南，覆盖 RAG Agent 的用途 [4]。

契约含义：

- **决策权转移**：检索不再是固定前置步骤，由模型在循环中决定"何时检索、检索什么"（[5] 的 decide→gather→reason）。
- **与既有分界对照**：固定前置检索属于 workflow，循环内自主决定检索则跨入 agent 范畴；[5] 用 "workflow" 描述、[6] 强调 "autonomous reasoning"，存在措辞张力，可视为同一光谱上的强度差异，参见 [[workflow与agent的分界]]。
- **与既有页面呼应**：[[rag三种实现路径]] 给出实现路径分层，Agentic RAG 可理解为"检索即工具"路径的延伸；事实与依据的分工仍按 [[本体给事实-rag给依据]]、[[本体作为约束层]] 执行。
- **未决问题**：检索工具返回体需要携带哪些字段（来源、置信度、时间戳）才能支撑本体事实与文档证据的冲突裁决，本轮来源均未给出，见 [[本体事实与rag依据冲突裁决待核验]]、[[本体事实与rag依据冲突裁决待核验]] 相关的 [[图谱检索与向量检索稳定性对比待核验]]。

## 四、契约 C：编排—运行时（LangGraph：路由、升级、并行、状态）

- [2] 指出真实客服系统不能停在 "agent calls a tool"：还需要**路由逻辑、智能升级（smart escalation）与知识库检索**。其中路由对应 [[五个工作流设计模式]] 中的 routing 模式；升级本质是一种交接（handoff），对应 [[多agent两种架构-经理模式与交接制]]。
- [3] 以 "Beyond RAG" 视角给出 LangGraph Agent Search 的工程要点：**并行化（parallelization）、状态管理与企业级扩展性**。并行化同样属于 [[五个工作流设计模式]] 的既定模式。
- **与既有知识对接**：中断与恢复契约见 [[agent中断条件与检查点]]；LangGraph 实现人机协同审核恢复与业务验收的完整案例见 [[68-3小时零基础入门fdeontology业务本体原理精讲与项目实战教学理清知识图谱rag与agent协同从零搭建企业ai客服中台附全部源码--2-文章--33-第-13-集12-人机协同流程langgraph审核恢复与业--uijrl2|第 13 集：人机协同流程 LangGraph 审核恢复]]；动作分级落地于编排中断点的机制见 [[action分级与确认机制]]；长任务的状态持久化约束见 [[长任务agent五项基础设施]]。
- **缺口**：[2][3] 只给出要点级描述，未提供状态机 schema、checkpointer 配置等可复现细节。

## 五、契约 D：本体侧如何映射（跨页综合）

本轮六个来源**均未直接描述 Ontology 与 Agent/RAG 的对接**，因此本节属基于既有 wiki 的映射推论，须以一手文档核验：

1. **查询契约分层**：确定性查询走结构化查询工具，探索走图/语义检索，对应 [[确定性走context探索走query]] 与 [[本体检索策略选型]]；图侧检索单元为 [[拓扑子图作为检索单元]]。
2. **动作契约**：本体动作按契约 A 的三要素导出为工具，分工见 [[action-pipeline-automation-function工具分工]]；写操作需带分级与确认，见 [[action分级与确认机制]]。
3. **事实/约束契约**：本体提供事实与约束，RAG 提供依据（[[本体给事实-rag给依据]]、[[本体作为约束层]]）；schema 与实例的分层见 [[本体schema与实例事实]]。
4. **协议替代路线**：MCP 把工具目录外置为服务，[[ontology-mcp]] 与 [[palantir-mcp]] 是两条现成路线，能力边界待核验（[[两套mcp能力边界待核验]]）。
5. **防幻觉环节**：契约层需保留校验与追溯位，参见 [[防幻觉的架构化机制]]。

另可对照 [[68-3小时零基础入门fdeontology业务本体原理精讲与项目实战教学理清知识图谱rag与agent协同从零搭建企业ai客服中台附全部源码--2-文章--27-第-12-集11-rag知识增强本体事实与文档证据融合--1ogx78z|第 12 集：本体事实与文档证据融合]] 的融合检索设计。

## 六、最小复现清单（可执行契约）

1. **工具导出（本体侧）**：为每个 Action 与查询模板准备 name、description、parameters JSON schema；可采用 [1] 的任一形态，服务化时以 dict/JSON schema 最通用（[[openai]] 格式）。
2. **绑定与调用**：`llm.bind_tools([...])`；注意全量注入特性 [1]，工具多时配合 [[tool-search与工具目录治理]] 或 [[programmatic-tool-calling]]。
3. **检索工具封装**：把 RAG 检索器包成"输入 query、输出带来源片段"的工具；把本体结构化查询、图遍历分别包成工具——落实 [[确定性走context探索走query]] 的分工，参见 [[本体检索策略选型]]。
4. **编排**：LangGraph 图实现"路由 → 工具 → 观察 →（必要时）升级/中断"；升级接 [[多agent两种架构-经理模式与交接制]] 的 handoff 思路；检查点见 [[agent中断条件与检查点]]。
5. **冲突与防幻觉**：为"本体事实 vs RAG 证据"预置裁决槽位（[[本体事实与rag依据冲突裁决待核验]]），并沿用 [[防幻觉的架构化机制]]。
6. **验收与留痕**：按 [[业务验收指标口径]] 记账；留痕要求见 [[人机协同留痕与快照时效待核验]]；工具打包形态可参考 [[本体问答-agent-skills]]。

## 七、矛盾与缺口

1. **来源覆盖偏差（最大缺口）**：主题为 Ontology、Agent、RAG 三者接入，但 [1]–[6] 无一覆盖 Ontology；第五节全部依赖跨页推论。对应 [[本体与agent接入边界待核验]]。
2. **材料质量**：[2]–[6] 均为指南/博客类二手材料，仅有摘要级信息，无代码与基准数据；[1] 为文档片段，缺执行循环与错误处理。
3. **术语张力**：[5] 用 workflow 描述 Agentic RAG，[6] 强调 autonomous decision making，与 [[workflow与agent的分界]] 的既有分界需要对齐。
4. **全量注入 vs 目录治理**：[1] 的"绑定即全量传参"与大规模工具目录存在冲突，见 [[工具数量阈值10的适用条件待核验]]、[[企业工具数量量级待核验]]。
5. **来源内部小矛盾**：[1] 注释称 "all three of these tool definitions"，实际示例列出四个工具定义（含 `subtract`），属文档笔误或版本陈旧。
6. **契约空位**：冲突裁决与融合检索升级判据两处尚无接口级答案，见 [[本体事实与rag依据冲突裁决待核验]]、[[融合检索升级判据待核验]]。

## 八、待核验问题汇总

- [[本体与agent接入边界待核验]]
- [[本体事实与rag依据冲突裁决待核验]]
- [[融合检索升级判据待核验]]
- [[两套mcp能力边界待核验]]
- [[工具数量阈值10的适用条件待核验]]
- [[企业工具数量量级待核验]]
- [[人机协同留痕与快照时效待核验]]
- [[owl表达与跨系统互操作待核验]]

## 九、建议补充来源

1. LangGraph 官方 tutorials（Customer Support、Agentic RAG、human-in-the-loop），用于核对 [2][3] 的引文与实现细节。
2. LangChain `bind_tools` 最新版官方文档（[1] 使用 `pydantic_v1`，存在版本陈旧风险）。
3. Cohere、Toloka、Moveworks 完整原文及其中引用的架构图与代码仓库（本轮仅见摘要级注释）。
4. Palantir Foundry/AIP 官方文档：Ontology 工具与 Action Type 的导出规范，以及 [[ontology-mcp]]、[[palantir-mcp]] 的协议说明。
5. MCP 官方规范（modelcontextprotocol.io），用于界定 MCP 与 `bind_tools` 两种契约的边界。
6. OpenAI 官方 tools/function calling 文档（[[openai-agent-api发布事实待核验]]）与 Anthropic "Building Effective Agents" 原文（[[anthropic三条铁律与团队合作结论原文待核验]]）。
7. 一手复现实验：以 [[订单客服本体]] 为样例导出 8–12 个工具，跑通 `bind_tools` + LangGraph 升级路由的端到端 demo。

## References

1. [Tool Calling with LangChain](https://www.langchain.com/blog/tool-calling-with-langchain) — langchain.com
2. [LangGraph Customer Support Agent with Escalation - machinelearningplus](https://machinelearningplus.com/gen-ai/langgraph-project-customer-support-agent-escalation/) — machinelearningplus.com
3. [Beyond RAG: Implementing Agent Search with LangGraph for Smarter ...](https://www.langchain.com/blog/beyond-rag-implementing-agent-search-with-langgraph-for-smarter-knowledge-retrieval) — langchain.com
4. [Agentic RAG: A Practical Guide for Enterprises - Cohere](https://cohere.com/blog/agentic-rag) — cohere.com
5. [Agentic RAG systems for enterprise-scale information retrieval](https://toloka.ai/blog/agentic-rag-systems-for-enterprise-scale-information-retrieval/) — toloka.ai
6. [Agentic RAG: Bring the Power of Reasoning to RAG - Moveworks](https://www.moveworks.com/us/en/resources/blog/bring-reasoning-to-agentic-rag) — moveworks.com
