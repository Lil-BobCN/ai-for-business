---
type: query
title: "Research: 发起 Palantir 官方文档外部研究"
created: 2026-10-11
origin: deep-research
tags: [research]
---

# Research: 发起 Palantir 官方文档外部研究

# Palantir 官方文档外部研究

本页汇总对 Palantir 官方文档（palantir.com 文档站）发起外部研究后获得的阶段性材料与发现。研究动因是：该 wiki 中关于 Palantir 与 Ontology 的内容此前主要来自中文视频解读与第三方文章的转述，遗留多项待核验问题（如 [[五层架构官方命名与划分待核验]]、[[两套mcp能力边界待核验]]），需要通过官方一手口径进行交叉核对。本批次共纳入 9 个来源：7 个 Palantir 官方文档页面 [1][2][3][5][6][7][9] 与 2 篇第三方深度解读 [4][8]，服务于 [[本体与agent协同]] 主题线。

## 一、官方文档体系地图

本批次抓取到的官方文档分布在四个板块：

| 板块 | 代表页面 | 本批次抓取情况 |
| --- | --- | --- |
| Ontology 系统 | The Ontology system [1]、Ontology overview [2]、Ontology [3] | 仅 [3] 含正文摘录，[1][2] 仅记录标题 |
| Ontology 架构 | Ontology architecture（object-backend）[9] | 含数字孪生定义与元素划分 |
| AIP | AIP overview [6]、AIP architecture overview [5] | 含治理与性能表述 |
| Architecture Center | Overview [7] | 含 Data / Logic / Workflow Services 服务分层 |

在本批次材料中，与 agent 主题最相关的两条主线是 Ontology 文档与 AIP 文档；Architecture Center 承担跨平台的分层叙述 [7]。这一结构与该 wiki 中 [[palantir-foundry]]、[[aip]] 两个实体页的关注范围基本对应。

## 二、Ontology 的官方定义与架构

### 数字孪生与两类元素

Ontology architecture 页面给出本批次最明确的一手定义：Ontology 是组织的数字孪生（digital twin），同时包含语义元素（semantic elements，即 objects、properties、links）与动力元素（kinetic elements，即 actions、functions、dynamic security），以支撑各类用例 [9]。

这一定义印证了 wiki 中 [[语义元素与动态元素两分法]] 的整理，也与 [[本体三要素对象属性关系]] 的对象—属性—关系三要素一致。一个值得注意的细节是：官方把 dynamic security（动态安全）明确列入动力元素一侧 [9]，而既有页面 [[action-pipeline-automation-function工具分工]] 主要讨论 Action、Pipeline、Automation、Function 的分工，未将安全机制纳入同一分类，可在后续更新中补充。

### Agent 生态中的 Ontology

官方 Ontology 页面强调：Palantir-native agents 适用的机制同样适用于外部 agent（external agents），从而在 agent 生态持续扩张时保证与 Ontology 的可信交互 [3]。该口径为 wiki 中"内部/外部 agent"的划分提供了官方依据（参见 [[本体与agent接入边界待核验]]），但本批次材料未包含官方对两套 MCP 服务器命名与权限边界的直接表述。

### 第三方解读：语义、动力与动态三层

Medium 上的一篇解读 [8] 以 "Semantic, Kinetic, and Dynamic" 为框架拆解 Ontology，其中语义层被描述为 Ontology 的核心，负责定义领域概念模型——存在哪些实体、如何相互关联 [8]。本批次仅抓取到该段开头，三层框架的完整定义及其与官方"语义元素/动力元素"两分法的映射关系，仍需回到原文核实（见第六节）。

## 三、AIP 架构：治理、性能与服务分层

### 安全与治理

AIP architecture 文档对治理的表述最为完整：人类与 agent 的每一项操作都必须遵守基于角色（role）、标记（marking）与目的（purpose）的控制；这些控制由基础设施、平台与企业安全三层组合实现，可细粒度配置、可动态查询，并记录在表达力强的审计日志中；治理能力统一覆盖平台界面中的运营、工程与开发活动，以及通过 API/SDK 进行的编程访问 [5]。

这段口径为 [[防幻觉的架构化机制]] 与 [[action分级与确认机制]] 提供了官方外部佐证：治理是"每一次操作"的前置约束而非事后补救，"可审计"是架构自带能力，与 [[确定性走context探索走query]] 的分工思路也可互相参照。

### 可扩展性与性能

AIP overview 指出平台架构支持分布式计算，可进行高性能处理与实时分析，服务于 mission-critical 应用 [6]。本批次材料未给出具体性能数字或基准测试。

### Data、Logic 与 Workflow Services

Architecture Center 概述将平台服务划分为 Data Services、Logic Services 与 Workflow Services，三者共同支撑 analytics、applications、AI-driven agents and automations 以及自定义产品；这些能力统一遵循平台级变更管理与发布管理，并遵守管理员配置的安全与治理控制 [7]。

此处出现一个术语对照问题：官方使用 "Workflow Services" [7]，而该 wiki 既有页面使用 [[企业-ai的data-logic-action三层模型]] 的 "Action" 表述，另有 [[action-pipeline-automation-function工具分工]] 的四类工具分工。三者是否指同一层级、Action 是否属于 Workflow Services 的下位概念，本批次材料不足以判定，可参照 [[四层架构是分工还是施工顺序待核验]] 中同类层级问题的处理方式继续追踪。

## 四、Agent 与 Ontology 交互的第三方深度解读

Zero Future Tech 的 Substack 长文 [4] 是本批次唯一的系统性交互解读，核心内容如下。

### 五层交互架构

该文将 agent 与 Ontology 的交互拆为五层：Retrieval Context、Object Query、AIP Logic、Action Tools 与 Governance，并以"查询华南仓今日有延误风险的订单并给出处理建议"作为端到端走查场景 [4]。该命名与 wiki 既有页面 [[agent与ontology五层交互架构]] 同源；官方文档在本批次中未直接出现这套分层命名，其是否为官方用语仍待核验（[[五层架构官方命名与划分待核验]]）。

### 两套 MCP 的分工

该文将 MCP 服务器分为两类 [4]：

- **Palantir MCP（面向 Ontology 构建者 / 开发者）**：探索 Foundry 项目结构、浏览代码库与 Palantir 内部库；为 React OSDK、Python transform、TypeScript function 仓库提供上下文；查看与查询数据集（可运行 SQL 查询、创建 notional datasets，但不能覆盖已有数据）；在 Ontology 中搜索 object types、action types、functions；创建修改 Ontology 类型定义的提案；为 Developer Console 应用重新生成 OSDK。
- **Ontology MCP（OMCP，面向外部业务 agent / Ontology 消费者）**：读取 Ontology 对象与属性；调用暴露的 query functions；触发已授权的 action types；在许可范围内执行 Ontology 数据编辑。

该划分与 [[palantir-mcp]]、[[ontology-mcp]] 两个实体页直接对应，并与来源 [3] 关于"外部 agent"的官方表述方向一致。但 OMCP 的正式名称、权限矩阵与发布状态均未在本批次的官方页面中得到确认，继续挂在 [[两套mcp能力边界待核验]] 名下。

## 五、与既有 wiki 内容的对照

| 主题 | 官方文档口径 | 既有 wiki 内容 | 对照结论 |
| --- | --- | --- | --- |
| Ontology 定义 | 组织数字孪生；语义元素 + 动力元素 [9] | [[语义元素与动态元素两分法]]、[[本体三要素对象属性关系]] | 一致，可回填官方措辞 |
| 面向 agent 的定位 | native 与 external agents 通用 [3] | [[本体与agent协同]] | 官方间接支持 |
| 治理控制 | role / marking / purpose + 审计日志 [5] | [[防幻觉的架构化机制]]、[[action分级与确认机制]] | 官方口径更完整 |
| 服务分层 | Data / Logic / Workflow Services [7] | [[企业-ai的data-logic-action三层模型]] | 命名差异，需对照 |
| Agent 工具接入 | 本批次无官方专属页面 | [[palantir-mcp]]、[[ontology-mcp]] | 仅第三方 [4] 支撑 |
| 五层交互 | 官方页面未出现该分层 | [[agent与ontology五层交互架构]] | 仍属第三方构建 |

## 六、矛盾、缺口与方法论提示

1. **官方页面覆盖不完整**：[1][2] 两个 Ontology 页面本批次仅抓到标题，缺少正文，无法用于逐条核对；AIP Logic、AIP Agent Studio、Ontology MCP 等关键组件的官方页面完全缺席。
2. **"两类术语"与"三层框架"的关系不明**：官方表述是语义元素 / 动力元素两类 [9]，而第三方文章 [8] 使用 Semantic / Kinetic / Dynamic 三层标题。dynamic security 在官方口径中属于动力元素 [9]，是否构成独立第三层需要原文核实。
3. **五层架构命名未获官方确认**：目前仅见于第三方解读 [4]，继续维持 [[五层架构官方命名与划分待核验]] 的开放状态。
4. **两套 MCP 仅一方有官方线索**：来源 [3] 支持"外部 agent"的提法，但 Palantir MCP / OMCP 的名称、能力与权限边界均出自 [4]，需官方文档或发布说明确认。
5. **第三方来源疑似同源**：[4] 的 Substack 域名（zerofuturetech.substack.com）与 wiki 中视频来源"零点未来 AI 企业"系列同名，二者疑似出自同一创作者；若属实，五层架构在视频与 Substack 文章之间可能共享同一表述，不能互为独立佐证，这一点在评估 [[agent与ontology五层交互架构]] 的证据强度时需要说明。
6. **服务分层术语差异**：Workflow Services [7] 与既有页面的 Action 分类口径（[[企业-ai的data-logic-action三层模型]]、[[action-pipeline-automation-function工具分工]]）尚未对齐。
7. **与文件到本体链路的衔接缺席**：本批次未抓取 AIP Document Intelligence 相关官方页面，[[文件到本体的五阶段链路]] 与 [[aip-document-intelligence流程与mockdown库待核验]] 仍缺官方佐证；Ontology 与知识图谱、context graph 的关系亦无官方直接表述（相关开放问题见 [[context-graph三方定义冲突待核验]]、[[本体与知识图谱职责边界待核验]]）。
8. **方法论风险**：本批次来源为公开页面摘录，Palantir 文档是否存在分权限或分版本内容、摘录是否代表页面全文，均未验证。

## 七、建议补充检索的来源

1. Palantir 官方 Ontology 系统文档的完整正文（补齐 [1][2]），以及 object-backend 下 object types、link types、action types 等定义子页 [9]。
2. 官方关于 Ontology MCP / external agent 接入的页面、发布说明或开发者博客，用于确认 [[ontology-mcp]] 的正式命名与权限边界。
3. AIP Logic、AIP Agent Studio、AIP Automate 的官方文档，用于核对五层架构中 "AIP Logic" 层的官方定位。
4. 官方对 dynamic security 的详细说明（细粒度控制、动态查询机制），用于确定其在两类元素划分中的位置。
5. Palantir 官方博客或 engineering blog 中关于 digital twin、Ontology 版本管理的文章。
6. OSDK（Ontology SDK）官方文档，用于核对 [4] 中"为 Developer Console 应用重新生成 OSDK"等开发者侧能力。
7. AIP Document Intelligence 官方文档，用于核验 [[文件到本体的五阶段链路]] 及 [[aip-document-intelligence流程与mockdown库待核验]]。
8. 对照性来源：[[datahub]]、[[atlan]] 等数据平台的官方文档，用于横向比较 ontology / [[上下文图谱-context-graph]] 口径（参见 [[五图两类框架]]）。
9. 官方术语表（glossary）或 Architecture Center 的完整架构图，用于一次性对齐 Services 分层与产品命名。

## 八、相关页面

- 实体：[[palantir-foundry]]、[[aip]]、[[palantir-mcp]]、[[ontology-mcp]]、[[aip-document-intelligence]]
- 概念：[[agent与ontology五层交互架构]]、[[语义元素与动态元素两分法]]、[[防幻觉的架构化机制]]、[[action分级与确认机制]]、[[企业-ai的data-logic-action三层模型]]、[[action-pipeline-automation-function工具分工]]、[[确定性走context探索走query]]
- 来源：[[8-零点未来ai企业--47-第-1-集10分钟企业agentic-workflow落地palantir-ontology--167275e]]、[[8-零点未来ai企业--33-第-7-集15分钟解读palantir-本体设计原则和行业实践分享--1pxgt8y]]、[[8-零点未来ai企业--35-第-4-集14分钟揭秘palantir一堆文件如何变成ontology--1fvocdi]]、[[8-零点未来ai企业--38-第-5-集19分钟揭秘palantir-agent和ontology如何交互--4skb72]]
- 待核验：[[五层架构官方命名与划分待核验]]、[[两套mcp能力边界待核验]]、[[aip-document-intelligence流程与mockdown库待核验]]、[[ontology-oval-agent与document-resolution名称待核验]]、[[本体与agent接入边界待核验]]

本页为外部研究记录，后续批次可在本页基础上追加官方材料并逐条关闭待核验项。

## References

1. [The Ontology system - Palantir](https://palantir.com/docs/foundry/architecture-center/ontology-system/) — palantir.com
2. [Overview • Ontology - Palantir](https://palantir.com/docs/foundry/ontology/overview/) — palantir.com
3. [Ontology - Palantir](https://www.palantir.com/platforms/ontology/) — palantir.com
4. [Palantir AIP Agent-Ontology Interaction: A Deep Dive into the ...](https://zerofuturetech.substack.com/p/palantir-aip-agent-ontology-interaction) — zerofuturetech.substack.com
5. [AIP architecture overview - Palantir](https://palantir.com/docs/foundry/architecture-center/aip-architecture/) — palantir.com
6. [AIP overview - Palantir](https://palantir.com/docs/foundry/aip/overview/) — palantir.com
7. [Overview • Architecture center - Palantir](https://palantir.com/docs/foundry/architecture-center/overview/) — palantir.com
8. [Understanding Palantir's Ontology: Semantic, Kinetic, and Dynamic ...](https://pythonebasta.medium.com/understanding-palantirs-ontology-semantic-kinetic-and-dynamic-layers-explained-c1c25b39ea3c) — pythonebasta.medium.com
9. [Ontology architecture - Palantir](https://palantir.com/docs/foundry/object-backend/overview/) — palantir.com
