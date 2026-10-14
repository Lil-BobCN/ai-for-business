---
type: source
title: 第 12 集｜9分钟OpenAI这次卖的不只是模型
tags: [零点未来, OpenAI, Agent API, harness, sandbox, 上下文压缩, tool search, PTC, multi-agent]
related: [openai, codex, langgraph, agent-api与模型-api的分界, 长任务agent五项基础设施, 上下文压缩, tool-search与工具目录治理, programmatic-tool-calling, 判断计算执行三分法, harness与sandbox解耦, agent-framework下沉, honest-hunnies-harness术语身份待核验, openai-agent-api发布事实待核验, 托管sandbox合作方名称待核验, 企业工具数量量级待核验, 上下文压缩的合规边界待核验, 自建agent运行时与平台托管运行时]
sources: ["零点未来：AI+企业/第 12 集｜9分钟OpenAI这次卖的不只是模型.md"]
evidence_status: partial
created: 2026-10-11
updated: 2026-10-11
---

# 第 12 集｜9分钟OpenAI这次卖的不只是模型

## 来源信息

- **标题**：第 12 集｜9分钟OpenAI这次卖的不只是模型
- **作者/平台**：零点未来（Bilibili），「AI+企业」合集第 12 集
- **URL**：https://www.bilibili.com/video/BV1Lpe56WEGz
- **原始文件路径**：`零点未来：AI+企业/第 12 集｜9分钟OpenAI这次卖的不只是模型.md`
- **提取方式**：本地 ASR，非官方字幕，`partial`
- **证据状态**：`partial`（转写不完整、专名与数字可能失真）；正文中的产品主张、数字与判断均为视频作者口播观点，属 `unknown / 待外部核验`

## 一句话摘要

视频作者认为，这次 OpenAI 真正卖的不只是模型，而是把 Codex 背后那套运行时（ASR 转写为 `Honest`／`hunnies`／`harness`，所指待确认）开放成了 Agent API：上下文压缩、工具检索、程序化调用工具与多 Agent 编排被一起收进平台层——模型只是发动机，企业真正该沉淀的是自己的业务上下文、可调用的动作与治理规则。

## 主要论点链（作者主张，未经核验）

1. 做 Agent 的痛点不在模型，而在模型之外的一整套运行时；
2. OpenAI 把 Codex 里已跑过的这套运行时通过 Agent API 开放；
3. 于是上下文压缩、工具检索、程序化调用工具、多 Agent 编排被收进平台层；
4. 平台同时把运行时与 sandbox 解耦，企业可把执行留在自有基础设施；
5. 通用能力标准化后，framework 不消失但下沉，差异化位置从「用了哪个框架」搬到「业务上下文、可调用动作、权限与审批」；
6. 结论：模型只是发动机，harness 决定车能开多远；企业资产是 context、Ontology、Tools、Business Logic、Governance。

## 作者给出的架构分层（结构化保留）

| 层 | 职责 |
|---|---|
| model | 推理、判断、生成 |
| harness（ASR 作 `Honest`） | 上下文管理、工具管理、Sub-Agent、Agent 编排、长期运行 |
| sandbox | 代码执行、文件操作、依赖安装、算力来源 |
| 企业应用层 | 业务数据、工具 actions、权限、规则、用户体验 |

## 作者给出的长任务 Agent 五项基础设施

上下文管理、工具使用、复杂任务拆解、失败恢复、执行环境。

> 注：该清单与既有页面 [[concepts/生产级agent五件事]] 高度重叠，但列举口径是否一致尚未比对，见 [[queries/长任务五项基础设施与生产级五件事口径待核验]]。

## 四项被收进平台的能力（作者陈述）

- **上下文压缩（context compression）**：接近 context limit 时自动压缩前文、尽量保留后续所需信息，任务可跨多个 context window 继续执行。
- **tool search**：不一次性塞入全部 tool definition，按需检索相关工具 schema 入上下文。
- **programmatic tool calling（PTC）**：用程序并行/串联调用工具、过滤组合结果，只把关键信息交给模型。
- **multi-agent 原生编排**：主 Agent 拆任务给 Sub-Agent，各自维护上下文，主 Agent 汇总。

## 待核验主张清单（均属作者陈述）

1. 发布物为「Agent API」，且是 Codex 运行时的 API 化——产品名、形式、时间均待核；视频只说「刚刚发布」，未给时间点；
2. 「模型 API 给大脑 / Agent API 给数字员工运行时」对比，以及过去自建清单（Memory、Context、Workflow、Tools Calling、Multi-agents、Sandbox、Checkpoint）；
3. 上下文压缩已内建，可跨多个 context window 续跑；
4. 企业工具量级：ERP 100 接口、采购 200 action，最终「上千个、三万个」（草稿原文即写作「上千个三万个」）；
5. tool search 机制与「现场事故」示例（只检索日志查询、deployment、metrics）；
6. PTC 并行/串联/过滤组合，「10 万条日志筛成 20 条异常」为说明性举例；
7. multi-agent 原生提供、Sub-Agent 各自维护上下文、主 Agent 汇总；「500 错误」为举例；
8. harness 与 sandbox 解耦，sandbox 可选托管/自建/第三方；
9. OpenAI 与 `cloud failed` 等合作提供托管 sandbox；
10. tool calling、web search、file search、computer use 已进入平台，上下文管理/工具搜索/多 Agent/长任务管理「开始由模型厂商提供」；
11. **`Honest` 的身份**——本系列反复出现却始终未被可靠识别（第 1 集 1 次，本集 13 处，结尾又转写为 `harness`）；
12. 「framework 会下沉、企业资产在业务侧」属判断与预测，非既成事实。

## ASR 存疑专名清单

| ASR 原文 | 出现语境 | 状态 |
|---|---|---|
| `Honest` / `hunnies` / `harness` | 全文核心术语，本集 13 处 | 所指待确认，见 [[queries/honest-hunnies-harness术语身份待核验]] |
| `collects` | 与 Claude Code 并列，作为上下文压缩体验参照 | 无法识别 |
| `out of jam` | 被列为自建编排的替代方案之一 | 无法识别 |
| `cloud failed` | 被指与 OpenAI 一起提供托管 sandbox | 公司名未可靠识别，见 [[queries/托管sandbox合作方名称待核验]] |
| `inflow` | 多处出现（Agent `inflow`、business application） | 所指待确认 |
| `dbc hunnies` | 作为「类似的事」的举例 | 无法识别 |
| `by bwd6` | 结尾未识别字符 | 无法识别 |

## 边界与反例（当前分析）

- 作者示例几乎全是工程排障（日志、部署、500 错误、事故调查），边界比跨部门业务流程清楚得多；「自动压缩 + 自动拆解」在长审批链业务场景是否成立，视频未检验。
- 「企业不必重复造运行时」与「企业要沉淀 context 与治理」之间存在成本转移：省下的工程资源要投到建模、权限与审批，这部分通常更贵且更依赖业务方。
- 数据主权边界：作者只在 sandbox 一侧给出答案（执行环境可自持），未回答「哪些上下文可以出企业边界」。
- 隐含前提：①Codex 运行时能平移到企业长任务；②「哪些信息可丢」可由平台通用策略决定，无需业务规则参与；③工具目录质量已足够好。

## 关联页面

- [[entities/openai]]、[[entities/codex]]、[[entities/langgraph]]：本集为其补充新主张，均标注 `unknown`。
- [[concepts/生产级agent五件事]]、[[concepts/多agent两种架构-经理模式与交接制]]、[[concepts/工作流与人工介入]]、[[concepts/本体与agent协同]]：本集提供新例证与互链。
- [[concepts/企业-ai的data-logic-action三层模型]]：本集提出的是 model/harness/sandbox 三层，属不同分层，勿合并。
- [[queries/openai-agent-api正式名称与能力边界待核验]]：本集是该 query 的直接新证据来源。

## 开放问题

1. `Honest`／`hunnies`／`harness` 是否同指？是否值得跨集追踪？
2. 本集「五项基础设施」与既有 [[concepts/生产级agent五件事]] 是同一清单还是两套口径？
3. 是否允许在 [[entities/openai]] 中记录「Agent API」这一未核验产品名，还是仅保留在 query 页？