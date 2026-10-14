---
type: source
title: 第 5 集｜19分钟揭秘Palantir Agent和Ontology如何交互
created: 2026-10-11
updated: 2026-10-11
tags: [Palantir, Ontology, Agent, MCP, 语义层, 零点未来]
related: [palantir, palantir-foundry, aip, 本体与agent协同, agent与ontology五层交互架构, 语义元素与动态元素两分法, 确定性走context探索走query, 防幻觉的架构化机制, action分级与确认机制, 角色仿真与推理过程可视化, palantir-mcp, ontology-mcp, 本体作为约束层, 本体给事实-rag给依据, 工具调用, 工作流与人工介入, agent中断条件与检查点, ontology与数据库schema的三点差异, 规则引擎推导]
sources: ["零点未来：AI+企业/第 5 集｜19分钟揭秘Palantir Agent和Ontology如何交互.md"]
evidence_status: partial
---

# 第 5 集｜19分钟揭秘Palantir Agent和Ontology如何交互

## 来源信息

- **标题**：第 5 集｜19分钟揭秘Palantir Agent和Ontology如何交互
- **作者/平台**：零点未来（Bilibili），系列「AI+企业」（合集共 12 集）
- **URL**：https://www.bilibili.com/video/BV1gFMc6rEVh
- **原始文件路径**：`零点未来：AI+企业/第 5 集｜19分钟揭秘Palantir Agent和Ontology如何交互.md`
- **提取方式**：本地 ASR，非官方字幕
- **证据状态**：`partial`（专名、缩写与数字可能有误）；正文主张均为视频作者口播，属 `unknown / 待外部核验`

## 一句话摘要

视频作者认为，本体建好之后，Agent 与 Ontology 的交互可以拆成五层——Context、Query、Logic、Action、Governance：系统确定性地准备背景知识，模型自己决定要查什么，专业计算交给函数，受控变更交给动作，而权限、审计与安全约束贯穿前面四层；Agent 全程不直接访问底层数据库表，只通过受治理的语义接口与业务世界打交道。

## 主要论点

以下均为视频作者在该段口播中提出的观点，未经独立核验，属 `unknown / 待外部核验`。

1. **Agent 不直接碰底层数据**：在 Palantir 体系中，Agent 不直接访问底层数据库表，也不自由扫描完整的 Ontology schema；它只在配置与授权的权限范围内，通过对象、关系、上下文、函数、动作等与业务交互。作者据此把 Ontology 称为「企业业务世界受治理的语义接口」，把 Agent 称为「用自然语言使用这些接口的操作员」，并类比为「Agent OS」。
2. **Ontology 是操作层而非知识图谱**：作者主张 Ontology 是一个 Operational layer，做在数据库、数据表、模型之上，把底层技术资产翻译成业务语言。Palantir 官方把它分为 Semantic elements（描述世界）与 Kinetic elements（改变世界）两类能力。
3. **五层交互架构**：Context Layer（官方名 Retrieval Context，确定性触发，每条消息都执行）、Query Layer（LLM 自主决定查什么）、Logic Layer（调用封装好的业务函数）、Action Layer（受控业务变更）、Governance Layer（权限、审计、安全约束贯穿前四层）。作者称 Governance 是「Palantir 与普通 Agent 框架最核心的差异」。
4. **防幻觉是架构问题而非提示词问题**：缺 Context、缺 Object Type、缺权限、缺函数，几层叠加后 Agent「根本接触不到」，而非「被告知不能说」。
5. **两套 MCP 边界**：Palantir MCP 面向开发者，可修改 Ontology 类型定义但不能直接写数据；Ontology MCP 面向外部业务 Agent，可读数据、执行 action、写数据，但不能改 Object Type 类型定义。
6. **端到端链路**：Top 10 注入 → 过滤华南仓加延误条件 → 沿 Link 追溯 Order/Customer → 调用函数算风险 → LLM 生成回答 → 用户确认 → 分派承运商、创建异常 case、更新 Ontology、留审计日志。

## 五层架构逐层要点

### 第一层 Context Layer（官方名 Retrieval Context）

- 确定性触发，每条消息都执行，不需要 LLM 判断「我需不需要检索」。
- 三种准备方式：
  - **Ontology Context**：从对象类型检索，可绑定固定对象（如选中华南仓后自动拿到库存、面积、负责人）；也可用语义搜索（如「华南仓有没有冷链断链的投诉」，返回最相关的五条）。
  - **Document Context**：从文档中捞取。全文模式把整份合同给 LLM；片段模式只返回最相关的几个文档块。作者称其使用 Vector embedding 找最相关向量。
  - **Function-backed Context**：前两种不够用时，写 TypeScript 或 Python 函数做自定义检索，例如「客户 360」视图同时拉取 CRM 记录、活跃订单、投诉工单，拼成综合情报给 LLM。

### 第二层 Query Layer

- LLM 自主决定查什么，支持过滤、聚合、检索、沿关系链搜索与逐层追溯。
- 关键区别：查的是 Ontology 里的对象和关系，而不是写 SQL；Agent 面对的是订单、承运商、仓库，而不是直接的表和字段。
- 三种典型查询模式：
  - **多条件过滤加聚合**：如「今天的华南仓有多少个延误的高优先级订单」，先 Filter 再 Count 返回 7 个；追问「哪些是 VIP 客户的」，沿 Link 从 Shipment 到 Order 再到 Customer，Service Level 等于 VIP，返回 3 个。
  - **Link 遍历与逐层追溯**：如订单 8832 问「延误是在哪一个环节出问题的」，沿 Link 逐层追溯，可设置最深追溯层数的超参数；示例中从 Shipment 追溯到 Carrier，承运商履约率 72%，归因为车辆故障加枢纽拥堵。
  - **聚合出运营概念**：如「各区域仓库绩效的情况」，按区域 group by 聚合，供管理层看红绿灯看板。

### 第三层 Logic Layer

- 不让 LLM 自己算。作者举例：问「这批延误订单的风险等级怎么样」，没有 function 时 LLM 只能说「看起来有风险」，这不是企业用户能接受的答案。
- 有 function 后，Agent 可调用如 calculate delay risk 的函数：查过去 90 天同路线延误数据、读承运商当前履约评分、调天气 API、看目的地未来 24 小时是否有暴雨，甚至跑已训练好的预测模型，最后输出结构化结果（如「高风险，原因是仓库积压加目的地暴雨预警」）。
- LLM 拿到的是结构化结果而非原始数据；其工作是理解意图、选择函数、用自然语言解释结果。业务规则和模型交给 function。
- 除风险评分外，还包括跨对象业务逻辑的推荐、优化类计算（如资源分配方案）。

### 第四层 Action Layer

- Action Tool 让 Agent 能做 Ontology 的变更，Agent 从问答助手变成业务操作员。
- 两种场景：
  - **高风险操作**：LLM 生成 action 后需用户确认。示例提示：「承运商 B 单价比 A 高 12%，预计增加运费 340 元，但时效可提升 10%，需要你点击确认才执行」。
  - **低风险操作**：自动触发。如天气原因延误两小时，系统自动更新 ETA、自动给客户发通知。
- 三个辅助工具：
  - **update application variable**：让 Agent 改应用状态，如「只看华东」触发页面联动刷新。
  - **command tool**：触发其他应用操作，如在地图上标出五个延误订单。
  - **request clarification**：执行前向用户确认模糊指令，如「你指的是哪个订单」。

### 第五层 Governance Layer

- 不是单独一层，而是贯穿前四层的约束机制。
- 权限分层示例：调度员登录时 Context 只注入三条线路的 Shipment，只能查这三条线路相关内容，不能调利润查询函数，可计算延误风险但不能计算利润，可自动更新 ETA 但不能指派承运商；区域经理登录时 Context 注入整个华南区概览，可查所有线路加承运商绩效、可查利润、可用优化分配函数分配与更换承运商。
- 防幻觉机制（作者列举四项）：缺财务 Context、缺 Financial Report 的 Object Type、缺财务权限、缺财务函数，几层叠加后 Agent 对营收彻底不知情，最终回答「我没有权限访问公司的财务数据」。
- 所有操作进审计日志：谁、什么时候、通过 Agent 干了什么、结果如何，全链路可追溯。作者称这是很大的工程问题。
- 工具暴露给 Agent 的两种模式：**prompt tool calling**（工具说明写进 prompt，所有模型都支持）与 **native tool calling**（用模型原生 tool calling 能力，可并行调用多个工具）。作者提醒：prompt 里不是把 Ontology schema 全量塞进 system prompt，只是当前 chat 被打开、被授权的那一部分。

## 端到端链路示例

问题：「帮我看一下今年华南仓有哪些订单有延误风险？」

1. **Context Layer** 自动触发，做系统级、确定性触发的语义搜索，返回 Top 10 最相关的 Shipment 注入 LLM，LLM 未参与决策。
2. **Query Layer** 过滤华南仓加延误条件，选出 32 个结果；沿 Link 搜索到 Order 和 Customer，读相关优先级与客户等级。
3. **Logic Layer** 调用函数计算延误风险，23 个里面有 5 个有风险；再调用 `document resolution`（函数名 ASR 如此，所指待确认），给出建议方案。
4. LLM 生成回答，询问是否执行。
5. 用户点击确认后，分派给承运商、创建异常 case、执行并更新 Ontology 结果，同时保存审计日志。

## 内部 Agent 与外部 Agent：两套 MCP

- 五层架构主要描述 local Agent 与 Ontology 之间的交互。
- 外部 Agent 接入有两个机制：
  - **Palantir MCP**：面向开发者，能修改 Ontology 的类型定义，但不能直接写数据。
  - **Ontology MCP**：面向外部业务 Agent，能读数据、执行 action、写数据，但不能改 Object Type 的类型定义。
- 核心原则不变：Agent 通过受治理的 Ontology 接口访问一切，绝不绕过 Ontology 直接碰底层数据。
- 作者称提供了「最小可工作版本」设计，包含若干模块、9 个核心主线与最小用例，可据此构建最小版本的 `Ontology Oval Agent`（ASR 原文如此，写法待确认）。

## Demo 演示

- 首页可开启对话、导入 Ontology、做模型配置。最简三部分：导入 Ontology → 选择 LLM → 对话交互。
- 已上传示例 Ontology，如物流 Ontology、采购 Ontology；作者称会尝试把之前创建本体的部分与这部分结合。
- 可做模型配置（自行添加模型）与用户管理（不同角色设置不同权限，作者称这也是 Governance 的某一层）。
- 对话功能：可问角色、做数据查询、业务函数调用、业务操作；可做角色仿真，对比不同方案的 performance 与 metrics。
- 示例：查询所有订单情况，返回 12 个订单总览，标注高风险订单，其中两个已延误、风险评分达到 100%；针对这两个警戒订单询问建议与角色仿真对比，系统建议两个都更换承运商，给出延误时长缩短多少、额外成本增加多少，并给出综合建议与客户主动沟通建议。
- 「推理过程」功能：展示调用了哪些工具与本体交互——上下文创建（加入哪些上下文给 LLM）、调用 Query Tool 查询本体（Customer、Order、Shipment、Carrier，此处 ASR 另有一个词作 `google`，所指待确认）、调用哪些函数、角色仿真模拟。

## 待核验项

以下均为作者口播陈述，未经独立核实：

1. 五层架构的划分与官方命名（Context / Query / Logic / Action / Governance），以及「Governance 贯穿前四层、是 Palantir 与普通 Agent 框架最核心差异」这一判断。
2. Ontology 元素两分法（Semantic elements / Kinetic elements）与示例对象 Order、Warehouse、Customer，以及 Shipment 归属于 Order、Order 归属于 Customer 的 Link 关系。
3. 端到端示例筛选链条：Top 10 → 过滤后 32 个 → 「23 个里面有 5 个有风险」。32 与 23 在叙述中并不自洽，需核对原音。
4. 高风险操作示例数字：承运商 B 单价比 A 高 12%、预计增加运费 340 元、时效提升 10%。
5. 逐层追溯示例：订单 8832、承运商履约率 72%、「车辆故障加枢纽拥堵」的归因结论。
6. 风险函数的数据来源：过去 90 天同路线延误数据、承运商履约评分、天气 API、目的地未来 24 小时天气，以及「已经训练好的预测模型」。
7. 防幻觉机制的层数：文中列举 Context、Object Type、权限、函数四项，而叙述中另有「三层叠加」的说法，列举项与层数不一致，需核对原音。
8. Demo 数字：12 个订单、其中 2 个高风险且风险评分达到 100%。
9. 「这个承运商过去三十年的表现」这一表述（从上下文看疑为「三年」，需核对原音）。
10. 两套 MCP 的能力边界：Palantir MCP 面向开发者、可修改 Ontology 类型定义但不能写数据；Ontology MCP 面向外部业务 Agent、可读数据与执行 action、写数据但不能改 Object Type 定义。
11. 「最小可工作版本」设计所包含的模块数量与「9 个核心的主线」这一说法。
12. Function-backed Context 中函数的实现语言（TypeScript / Python），以及「客户 360」视图的数据来源（CRM 记录、活跃订单、投诉工单）。

## 与既有 Wiki 的关系

- 本集**扩展**既有知识：此前 Wiki 多聚焦「本体怎么建」（第 2、4 集），本集首次系统回答「建好之后 Agent 怎么用」，填补 [[concepts/本体与agent协同]] 的机制空白。
- 本集**强化**「本体作为约束层」「本体给事实」等既有判断，见 [[concepts/本体作为约束层]]、[[concepts/本体给事实-rag给依据]]。
- 与 [[concepts/ontology与数据库schema的三点差异]] 存在潜在张力：该页强调 Ontology 与 schema 的差异，本集进一步主张 Ontology 是「操作层」而非知识图谱，需确认两者是否一致，或本集是否收窄了 Ontology 的定义范围。
- 两套 MCP 与 [[concepts/工具调用]]、[[comparisons/工具调用-mcp-sub-agents-skills-任务组织比较]] 直接相关。
- Action Layer 的高/低风险分级与 request clarification 可扩展 [[concepts/工作流与人工介入]]、[[concepts/agent中断条件与检查点]]。
- Logic Layer 的函数化计算与 [[concepts/规则引擎推导]] 相关。

## 边界与反例

- 作者自述的边界：这套交互只在一个已建好的、受治理的 Ontology 之上才成立。
- 防幻觉依赖「配置文件里没有」，失效模式从「模型乱说」变成「权限配错」，后者更不易被用户察觉，作者未讨论此风险。
- 函数可信性假设：作者主张「业务规则和模型交给 function」，但未说明函数写错时如何发现，Agent 会「错得很自信」。
- 审计日志的消费方缺失：作者把「全链路可追溯」列为工程问题，但未说明谁来看这些记录。
- 角色仿真数字来源不明：demo 中「延误缩短多少、成本增加多少」未说明来自历史回归、规则推算还是模型估计。
- 端到端链路数字不闭合（32 与 23），若演示流程数字都对不上，实际系统的可复现性更需验证。

## 可迁移素材

- 把「Context 放确定性信息、Query 放探索性需求」当作可执行的检索设计原则，用两侧放错的代价校准分界线。
- 把「必须有唯一正确答案的计算」从 LLM 手里拿走，交给可测试的函数，模型只负责理解意图与解释结果。
- 把防幻觉从提示词工程升级为架构约束——让 Agent「接触不到」比「被告知不能说」更可靠。
- 用「高风险要确认、低风险可自动执行」把动作分级，并给不可逆操作配 request clarification 式确认环节。
- 把「角色仿真 + 推理过程可视化」当成决策工具，让使用者看到 Agent 调用了哪些工具、查了哪些对象、算了哪些函数。
- 无论内部 Agent 还是外部 Agent，都只经过受治理的接口访问数据，不绕过中间层直接碰底层表。