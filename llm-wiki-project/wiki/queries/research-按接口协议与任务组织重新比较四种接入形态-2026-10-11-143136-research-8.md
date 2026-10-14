---
type: query
title: "Research: 按接口、协议与任务组织重新比较四种接入形态"
created: 2026-10-11
origin: deep-research
tags: [research]
---

# Research: 按接口、协议与任务组织重新比较四种接入形态

# 按接口、协议与任务组织重新比较四种接入形态

**一句话结论**：这四种接入形态不在同一层竞争——Tool Calling 决定"调用如何被表达"，MCP 决定"能力如何被发现与连接"，Agent Skills 决定"领域知识与流程如何被封装与激活"，Sub-Agent 决定"任务如何被委派与隔离"。按接口边界、协议性质、任务组织三轴切分后，四者呈现为分层组合，而非互相替代。

## 比较对象与轴的定义

本页比较的四种接入形态：

1. **Tool Calling / Function Calling**：模型与应用之间表达"调用某能力"的交互机制 [1][2]。
2. **MCP（Model Context Protocol）**：MCP 客户端与外部能力提供方之间的协议，规范工具、资源、Prompt 的发现与调用，以及连接和传输 [1]。
3. **Agent Skills**：以 `SKILL.md` 文件夹为载体的模块化能力封装，打包指令、元数据和可选资源（脚本、模板）[6][7][8]。
4. **Sub-Agent（子代理）**：主智能体向子智能体委派任务的组织形态，含 Agent as Tool 与 Sub-Agent 两个子形态 [11]。

口径提示：有来源把"四种"并列表述为 Function Calling、MCP、Skill 与 Tool [3]；本页按研究题目把 Tool 归入 Tool Calling 一系、把 Sub-Agent 单列。归类差异本身是一个待核验点（见下文）。

三轴定义：

- **接口**：调用发生在谁与谁之间（边界），以及暴露的最小粒度。
- **协议**：属于正式协议、开放格式实践还是框架内机制；是否覆盖能力发现与传输。
- **任务组织**：单步能力调用、流程/知识封装，还是任务委派与上下文管理。

## 四种形态各自定位

### Tool Calling / Function Calling：模型—应用的调用表达机制

- 它是模型与应用之间表达"调用某能力"的交互机制，而非跨系统协议；调用意图以函数名与参数的形式表达 [1]。
- 完整回路是回环式的：模型输出调用 → 应用执行 → 结果呈报 LLM → 携带完整对话历史再次调用 API [2]。这条"反馈回路"正是 [[agent-反馈闭环与自我进化]] 的微观形态。
- 执行所有权在宿主框架侧而非模型侧：在 Spring AI 中，由 `DefaultChatClient` 自动注册的 `ToolCallingAdvisor` 拥有工具执行生命周期的所有权 [4]。这与 [[判断计算执行三分法]]、[[harness与sandbox解耦]] 的"判断与执行分离"一致。

### MCP：客户端—能力提供方之间的协议

- 它规范的是工具、资源、Prompt 三类能力的发现与调用，以及连接与传输 [1]——即协议覆盖"能力从哪来、如何发现、如何连上"。
- 关键的层级关系：LLM 随后可以"像调用普通 Function Calling 一样"调用通过 MCP 发现的工具 [2]。即 MCP 不替代调用表达机制，而是叠在 Tool Calling 之下/之外的能力供给层。
- 工程收益有单点证言：Lynxe 框架实践称采用 MCP 后，新工具接入平均耗时从 3 人日（来源此处截断，下降后数值未给出）[3]。
- 治理问题随之出现：本地工具与远程 MCP 工具同名时需自行重命名 [4]，这与 [[tool-search与工具目录治理]]、[[programmatic-tool-calling]] 讨论的问题同源。

### Agent Skills：以文件为载体的能力封装

- 官方口径：扩展 Claude 功能的模块化能力，打包指令、元数据与可选资源，Claude 会在相关时自动使用 [6]。
- 形态口径：包含 `SKILL.md` 元数据文件的文件夹结构，定义技能名称、描述、版本、作者与执行指令 [7]。
- 生态口径：一种开放格式实践，提供轻量、可移植的方式来封装领域知识和工作流程 [8]。
- 质量关键是 description 的精准度：对比"处理数据库查询"与"将中文业务问题转换为 SQL 查询并分析 MySQL employees 示例数据库，适用于员工信息查询、薪资统计……"两类写法，后者明确触发场景 [5]。
- 与 MCP 的关系被表述为"智能体能力扩展的两种范式" [5]：Skills 偏"教怎么做"，MCP 偏"提供能做什么"。

### Sub-Agent：任务组织与上下文形态

- 两个子形态的分野 [11]：
  - **Agent as Tool**：上下文隔离、无状态，运行在自身独立会话中，无法获取调用方对话历史与状态，每次交互靠单次请求传递；
  - **Sub-Agent（委派式）**：共享主智能体上下文、处于同一会话，可访问主智能体的对话历史和状态，适合多步骤推进的有状态流程。
- 控制权与连接机制：Sub-Agent 模式下控制权集中式，"主智能体说了算"；连接机制是 State，即传递给下一个智能体的信息 [11]。这对应 [[多agent两种架构-经理模式与交接制]] 中的经理模式一侧。
- 框架实现侧佐证：DeepAgents/LangGraph 语境下，子代理为不同任务创建隔离的上下文窗口，配套文件系统、状态图编译、检查点与中断控制 [9][10]。相关的上下文预算问题见 [[上下文压缩]]、[[长任务agent五项基础设施]]。

## 三轴对照表

| 形态 | 接口边界（谁 ↔ 谁） | 协议性质 | 任务组织定位 | 来源 |
| --- | --- | --- | --- | --- |
| Tool Calling / Function Calling | 模型 ↔ 应用（宿主/harness） | 非协议；模型侧能力与调用约定 | 单步能力调用，经反馈回路闭环 | [1][2][4] |
| MCP | MCP 客户端 ↔ 外部能力提供方 | 正式协议；覆盖工具/资源/Prompt 的发现、调用、连接与传输 | 能力供给与目录层；调用仍落到 Function Calling | [1][2] |
| Agent Skills | 宿主 ↔ 文件目录（`SKILL.md` + 资源） | 开放格式实践；轻量可移植，非传输协议 | 领域知识与工作流程封装，按相关度自动激活 | [5][6][7][8] |
| Sub-Agent | 主智能体 ↔ 子智能体（委派） | 框架内机制；以 State 传递连接，无跨框架标准 | 任务分解与委派；上下文隔离或共享 | [9][10][11] |

## 逐轴分析

### 轴一：接口——四者暴露的"面"粒度不同

- Tool Calling 暴露的是函数签名（名称 + 参数），粒度最细 [1][2]。
- MCP 暴露的是能力目录（工具、资源、Prompt 三类原语）加连接与传输 [1]。
- Skills 暴露的是文件目录：`SKILL.md` 元数据 + 可选脚本/模板 [6][7]。
- Sub-Agent 暴露的是"可承接任务的对话体"；两种子形态的差别正在于是否共享调用方上下文 [11]。

四者可以同栈叠加：一个 Sub-Agent 内部用 Skills 组织流程，经由 MCP 发现外部工具，最终仍以 Function Calling 表达每一次具体调用。这也解释了为什么 [[agent-framework下沉]] 会把这类编排能力逐步收进平台层。

### 轴二：协议——从"模型能力"到"正式协议"再到"格式实践"

按各来源对"协议"一词的用法，可归纳出一条标准化程度谱系：

- **MCP**：唯一被称为"协议"的形态，且明确覆盖发现、调用、连接、传输 [1]。
- **Agent Skills**：被称为"开放格式实践"，强调可移植与轻量，但不定义传输 [8]。
- **Sub-Agent**：框架内机制，靠 State 传递连接，无跨框架标准 [11]。
- **Tool Calling**：模型侧交互机制，各家 schema 由模型厂商定义 [1][2]。

注意：这条谱系是本页依据各来源措辞做的综合归纳，原始来源并未做同轴排序，属于待核验判断。另需区分技术口径与宣传口径：MCP 技术上定义为"客户端与外部能力提供方之间的协议" [1]，但被引述为"真正的大模型接口标准" [2]——后者把客户端协议上升为模型标准，属评述性表述而非规范表述。

协议层还留下了两个"责任缺口"：命名治理（本地与远程 MCP 工具同名需重命名 [4]）与执行生命周期所有权（落在 `ToolCallingAdvisor` 一类宿主组件 [4]），二者都不由协议本身承担。

### 轴三：任务组织——单步、流程与委派三种粒度

- **单步**：Tool Calling 的反馈回路，每次执行结果回传后重新调用，上下文随完整对话历史累积 [2]。
- **流程**：Skills 封装领域知识与工作流程，由宿主按相关度自动激活 [5][6][8]；可与 [[五个工作流设计模式]]、[[workflow与agent的分界]] 对照使用。
- **委派**：Sub-Agent 的上下文隔离/共享两分 [11]；与 [[单agent与多agent选型比较]]、[[面向制品与面向角色]] 的拆解讨论直接相关。

此处存在一个口径冲突：DeepAgents 语境强调子代理"创建隔离的上下文窗口" [9][10]，而 OpenHands 语境把"共享上下文"记为 Sub-Agent 的特征、把"隔离"归给 Agent as Tool [11]。两者可能描述的是不同实现（隔离式 subagent 与委派式 sub-agent 同名不同义），需核验。

## 矛盾、口径冲突与缺口

1. **替代论 vs 分层论**：来源引述"Function Calling 已经过时，MCP 才是真正的大模型接口标准"（53AI，2025-04-24；腾讯云开发者，2025-04-10），但同一来源又说明 MCP 发现的工具"像调用普通 Function Calling 一样"被调用 [2]。二者是分层关系；替代论属二手评述。
2. **Sub-Agent 上下文：隔离还是共享**：[9][10] 与 [11] 的口径冲突（见上节），可能是实现差异而非事实矛盾。
3. **Skills 定义三口径**：[6] 强调使用方式（自动激活的模块化能力）、[7] 强调文件形态（`SKILL.md` 文件夹）、[8] 强调生态属性（开放格式实践）。三者相容但侧重不同，尚无统一权威定义。
4. **数字孤证**：[3] 的"新工具接入 3 人日"为 Lynxe 框架自述，且原文截断，无第三方验证。
5. **四种形态的边界归类本身有争议**：[3] 的四项并列（Function Calling、MCP、Skill、Tool）与本页口径（Tool 归入 Tool Calling、Sub-Agent 单列）不同，归类依据未被来源明确论证。
6. **潜在的第五种接入形态**：以本体/知识图谱为能力源的接入（如 [[ontology-mcp]]、[[palantir-mcp]]）目前多借道 MCP 实现，是否构成独立形态存疑，参见 [[两套mcp能力边界待核验]]、[[本体与agent接入边界待核验]]、[[本体作为约束层]]。本页未将其计入"四种"。

## 与既有 wiki 的连接

- 工具目录与治理：[[tool-search与工具目录治理]]、[[programmatic-tool-calling]]
- API 与执行分界：[[agent-api与模型-api的分界]]、[[判断计算执行三分法]]、[[harness与sandbox解耦]]、[[agent-framework下沉]]
- 多 Agent 与任务组织：[[多agent两种架构-经理模式与交接制]]、[[单agent与多agent选型比较]]、[[面向制品与面向角色]]、[[协作协议优先于编程能力]]
- 反馈与长任务：[[agent-反馈闭环与自我进化]]、[[长任务agent五项基础设施]]、[[上下文压缩]]
- 宿主与厂商：[[anthropic]]、[[claude-code]]、[[codex]]、[[opencode]]
- 本体接入（候选第五形态）：[[ontology-mcp]]、[[本体与agent接入边界待核验]]、[[本体与agent协同]]

## 待核验清单

- Lynxe"3 人日"的原始出处、下降后数值与统计口径 [3]。
- "Function Calling 已过时，MCP 才是接口标准"原文全文与作者（53AI 2025-04-24；腾讯云开发者 2025-04-10）[2]。
- Sub-Agent 的"隔离/共享上下文"分别对应哪套框架实现，是否存在同名不同义 [9][10][11]。
- MCP 原语集合（工具/资源/Prompt）与传输层定义的完整官方表述 [1]。
- Agent Skills 作为"开放格式"在非 Claude 宿主的采纳范围与规范归属 [6][8]。
- Spring AI `ToolCallingAdvisor` 的注册机制与远程 MCP 工具命名冲突的处理细节 [4]。
- 四种形态的归类边界是否需要一份权威对照（本页口径 vs [3] 口径）。

## 建议补充来源

- MCP 官方规范与架构文档（modelcontextprotocol.io）。
- Anthropic 关于 Agent Skills 的官方公告与工程博客。
- OpenAI Function Calling / Tools 官方文档及与 MCP 的适配说明。
- OpenHands Microagents 官方文档（用于裁决 Sub-Agent 上下文口径）。
- DeepAgents 与 LangGraph 官方文档（子代理与上下文窗口设计）。
- Spring AI Tool Calling 英文官方参考（对应 [4] 的权威版本）。
- 关于"工具接入成本"的第三方实测或基准，以替代 Lynxe 单点证言 [3]。

## References

1. [03-tool-calling.md - vixues/LeAgent - GitHub](https://github.com/vixues/LeAgent/blob/main/docs/interview/03-tool-calling.md) — github.com
2. [LLM中工具调用的完整指南：释放大模型潜能的关键 - 知乎专栏](https://zhuanlan.zhihu.com/p/1909186977066128479) — zhuanlan.zhihu.com
3. [AI工具调用技术解析：Function Calling、MCP、Skill与Tool的关系与选型](https://bbs.csdn.net/weixin_32678995/article/details/100255100) — bbs.csdn.net
4. [工具调用:: Spring AI 参考](https://docs.springframework.org.cn/spring-ai/reference/api/tools.html) — docs.springframework.org.cn
5. [Agent Skills 与MCP：智能体能力扩展的两种范式 - GitHub](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra05-AgentSkills%E8%A7%A3%E8%AF%BB.md) — github.com
6. [Agent Skills - Claude Platform Docs](https://platform.claude.com/docs/zh-CN/agents-and-tools/agent-skills/overview) — platform.claude.com
7. [AI Agent Skills 系统性技术指南：从入门到生产落地](https://zhuanlan.zhihu.com/p/2012180283743568745) — zhuanlan.zhihu.com
8. [4.4 智能体技能：能力扩展规范](https://yeasy.gitbook.io/agentic_ai_guide/di-yi-bu-fen-dan-ti-zhi-neng-jia-gou/04_tools/4.4_skills) — yeasy.gitbook.io
9. [AI Agent架构入门到精通：LangChain重磅DeepAgents深度拆解](https://gitcode.csdn.net/69d113220a2f6a37c59cffee.html) — gitcode.csdn.net
10. [创建能自主研究、管理TODO 列表的AI 智能体 - 知乎专栏](https://zhuanlan.zhihu.com/p/1979154360584922700) — zhuanlan.zhihu.com
11. [AI Agent 框架探秘：拆解OpenHands（14）--- Microagents - 罗西的思考](https://www.cnblogs.com/rossiXYZ/p/19694116) — cnblogs.com
