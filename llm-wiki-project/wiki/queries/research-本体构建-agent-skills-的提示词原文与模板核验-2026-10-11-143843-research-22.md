---
type: query
title: "Research: 本体构建 Agent Skills 的提示词原文与模板核验"
created: 2026-10-11
origin: deep-research
tags: [research]
---

# Research: 本体构建 Agent Skills 的提示词原文与模板核验

# 本体构建 Agent Skills 的提示词原文与模板核验

本页核验两类对象：（1）**提示词原文**——本体构建/使用类 Agent Skill、以及其他本体抽取流程中实际使用的 prompt 逐字文本能否落实；（2）**模板**——SKILL.md 及其目录结构、frontmatter 字段、附属文件与脚本的规范形态是否有原文依据。核验材料共 7 项 [1]–[7]，涵盖 Neo4j《Going Meta S03E07》的博客页与视频页 [1][3]、一篇 Medium 文章 [2]、[[anthropic]] 官方 Agent Skills 文档 [4]、一篇 SKILL.md 开发者实践长文 [5]、一篇 arXiv 论文 [6]、一篇五种方法对比的 Substack 文章 [7]。

方法说明：部分来源的采集副本明显是片段（如 [1] 仅含一句结论），因此"在素材中未见提示词原文"只能判定为**本次无法核验**，不等于原内容不存在。

## 核验结论摘要

| 核验项 | 结论 | 依据 |
|---|---|---|
| SKILL.md 目录与文件模板 | 可核验（官方文档与第三方实践互证） | [4][5] |
| frontmatter 字段与行为开关 | 部分可核验（字段语义存在实现差异） | [5] |
| 本体抽取类提示词原文 | 仅 1 条可逐字引用（端到端提示） | [7] |
| 本体构建专用 skill 的提示词与文件原文 | 素材缺失，无法核验 | [1][3] |
| 企业本体 pipeline 的 system prompt 原文 | 仅功能描述，无逐字文本 | [6] |

## Agent Skills 模板：可核验的结构

### 目录与文件形态

Skills 被定义为"可复用的、基于文件系统的资源"，用于赋予 Claude 领域专长（工作流、上下文与最佳实践）[4]。每个 skill 是代码执行环境中的一个目录，agent 以 bash 等常规方式访问 [4]。官方架构图展示的示例技能目录呈现同构模式：`skills/bigquery/` 含 `SKILL.md`、`datasources.md`、`rules.md`；`skills/pdf/` 含 `SKILL.md`、`forms.md`、`reference.md`、`extract_fields.py` [4]。即"主文件 + 领域参考文件 + 可执行脚本"的组合。

存放位置方面，[[claude-code]] 的项目级路径为 `.claude/skills/<skill-name>/SKILL.md`，个人级为 `~/.claude/skills/`，插件分发为 `<plugin>/skills/`；面向跨客户端可移植性的开放标准形态则使用 `.agents/skills/` [5]。`SKILL.md` 文件名大小写必须精确，monorepo 中嵌套的 `.claude/skills/` 会被自动发现 [5]。

### 渐进式披露与上下文注入

Skills 的加载机制是渐进式披露：agent 初始只加载 skill 名称与描述等紧凑元数据，任务匹配后才读取完整指令 [5]。Claude Code 会把渲染后的 Skill 作为一条消息注入会话，后续轮次不再重读文件；上下文压缩后仅保留预算内的近期 Skill 内容——因此超大 Skill 在长会话中是"脆弱"的，而非仅仅不美观 [5]。若指令涉及可执行脚本，脚本经 bash 运行，**只有输出进入上下文，脚本源码本身不进入** [4]。

### frontmatter 字段与行为开关

| 字段/机制 | 作用 | 注意事项 |
|---|---|---|
| `name` / `description` | 触发元数据；description 应写明会触发它的具体用户短语 | claude.ai 上传要求目录名与 `name` 一致，description 上限 200 字符 [5] |
| `disable-model-invocation: true` | 仅用户可调用 | 官方建议用于部署、提交、外发消息等有副作用的工作流 [5] |
| `user-invocable: false` | 隐藏于斜杠菜单，仅作背景知识由模型使用 | [5] |
| `context: fork` + `agent: Explore` | Skill 在派生子代理中运行，重输出与主会话隔离 | 用于研究型、探索型任务 [5] |
| `compatibility` | 声明运行时依赖与工具版本 | [5] |
| `allowed-tools` | Skill 激活期间预批准特定工具 | 规范中标注为实验性；**不限制**可调用工具全集；Claude Agent SDK 中该 frontmatter 明确不生效 [5] |

### 体积、引用与脚本规范

Anthropic 建议 `SKILL.md` 控制在 500 行、约 5,000 tokens 以内，细节外移到 `references/` 并写明加载条件；合格示例是"若 API 返回非 200 则读取 `references/api-errors.md`"，模糊的"见 references/"不合格 [5]。面向 agent 的脚本规范包括：避免交互式提示、以 `--help` 说明用法、错误信息可帮助修复、stdout 输出 JSON/CSV 等结构化结果、诊断写 stderr、可安全重试、固定一次性工具版本 [5]。安全脚本样板的三要素为 `set -euo pipefail`（失败即退出）、stdout 输出 JSON、诊断进 stderr（采集段中代码块原文未完整保留）[5]。

## 本体构建提示词原文盘点

### 逐字可核验：端到端提示（来源 [7]，方法 E）

现有素材中唯一可逐字引用的本体抽取提示词，属于 [[llm驱动本体构建五种流派]] 所述五种方法中的"端到端提示（End-to-End Prompting）"：

```
You are a {domain} ontology expert.
Extract ontology classes and their relationships from the following text.
Only extract what is explicitly stated. Do not add inferred content.
Output format: JSON.
{"classes": [{"name": "...", "definition": "..."}],
 "relationships": [{"source": "...", "target": "...", "type": "..."}]}
Rules: 1. Only extract explicit content  2. Use standardized names  3. Output "None" if ambiguous
Text: {input_text}
```

结构要点：角色设定（`{domain} ontology expert`）、只抽显式内容并禁止推断、内联 JSON schema（classes/relationships）、三条规则、歧义时输出 `"None"` [7]。配套工具有 [[ontoprompt]]（github.com/jingw2/nano-ontoprompt），其项目身份另见 [[ontoplome与ontoprompt是否同一项目待核验]]。

**核验提醒**：这是单条提示词，不是 Agent Skill 模板——没有 SKILL.md、没有渐进式披露、没有配套脚本。把它当作"本体构建 skill 的提示词原文"属范畴混淆；其与 [4][5] 描述的 skill 形态之间只存在"内容是提示词"这一点交集。相关方法论出处与案例核实见 [[五种流派论文与案例待核验]]。

### 仅有功能描述：企业知识图谱 pipeline（来源 [6]）

arXiv 论文《LLM-Driven Ontology Construction for Enterprise Knowledge Graphs》称其 pipeline 使用专门的 system prompt 抽取两类核心元素：Classes（如 Employee、Vehicle）与 Properties（如 operates、hasAccessTo），并强调提示词被严格限定为只关注所提供的 schema [6]。但素材未给出逐字措辞、schema 注入格式与示例数量，**无法核验模板**。已知信息仅支持"存在受 schema 约束的 system prompt"这一结论。

### 素材缺失：Neo4j《Going Meta S03E07》（来源 [1][3]）

该期节目主题与本次核验最直接相关，但采集内容极少：[1] 仅含片段"Skills are composable"与"prompt 只活在聊天窗口或配置文件里"；[3] 提供时间轴（4:24 主题概览：Agent Skills for Ontology Building；9:18 What Are Agent Skills?；11:43 Skills Format）并出现 agentskills.io 字样。**采集中没有任何 SKILL.md 文本、目录截图或提示词正文**，因此该期展示的本体构建/使用 skill 提示词原文在本次素材中完全无法核验。[1] 的唯一可引论点是：skill 是可组合单元，与"聊天窗口/配置文件里的 prompt"不在同一层级。

### 第三方定位表述（来源 [2]）

[2] 称 Ontology 与 Anthropic Skill 框架的主要目标是"教 agent 有效生成自己的代码"。这是第三方解读：官方文档 [4] 的措辞是赋予 agent 领域专长（工作流、上下文、最佳实践），未将"生成代码"列为主要目标。两者可兼容（生成代码是手段之一），但引用 [2] 作为"框架目标原文"并不安全。

## 对本体构建任务的初步映射（推断，待核验）

- 按 [4] 中 bigquery 模式（主文件 + 数据源说明 + 规则文件），本体构建 skill 的合理形态可能是：SKILL.md 主流程 + 领域/数据源说明 + 规则文件 + 校验脚本，与 [[三段式本体建模节奏]]、[[本体建模业务定义数据映射与关系校验]] 的流程可衔接。
- 英文来源标题强调 "Creating **and** Using Ontologies" [1]，与 wiki 中文侧的创建/使用对称结构相呼应：[[本体构建-agent-skills]]（创建侧，Codex 建模与 [[owl]] 生成）与 [[本体问答-agent-skills]]（使用侧）。中文侧材料见对应来源页 [[68-3小时零基础入门fdeontology业务本体原理精讲与项目实战教学理清知识图谱rag与agent协同从零搭建企业ai客服中台附全部源码--2-文章--31-第-8-集07-订单本体构建实战codex建模owl生成与--1qlmpsr]]。
- **以上形态是基于通用模板的外推，未被任何来源直接证实**，列入待核验。

## 矛盾与口径差异

1. **跨客户端范围**：官方文档 [4] 只在 Claude 产品面（API、Claude Code、claude.ai）描述 Skills；[5] 称 Agent Skills 是开放标准，并称同一 skill 可用于 VS Code + GitHub Copilot、Claude Code 与 [[codex]]，还引述 Codex 官方文档称 Skills 支持 CLI、IDE 扩展与 app。该说法需以官方 quickstart 与 Codex 文档一手核实。
2. **`allowed-tools` 三重语义**：规范中实验性、Claude Code 中预批准但不限制工具全集、SDK 中不生效 [5]。
3. **分发与治理**：Claude API 的自定义 Skill 为工作区级共享；claude.ai 的自定义 Skill 为个人所有，不能组织级共享与集中管理 [4]。企业分发本体 skill 时两条路径能力不同。
4. **网络与环境**：Claude API 沙箱无网络访问、不允许运行时装包；Claude Code 有完整网络但建议仅本地装包 [4]。若本体构建 skill 需要连接图数据库或外部本体服务，在 API 环境不可行，需经 MCP 等外挂方式解决——素材未给出该组合的实例，属空白。
5. **自动/手动触发**：官方建议副作用工作流设为仅用户可调用 [5]，与 [2] 的"生成代码"自动化叙事存在张力；本体写入类 skill 归入哪一侧，素材未定论。

## 待核验清单

- Neo4j 节目内本体构建 skill 的目录、SKILL.md 与提示词原文（需完整录像/字幕）[1][3]
- agentskills.io 规范的 frontmatter 完整字段表与 `allowed-tools` 稳定性 [3][5]
- [6] 论文的系统提示词全文与 schema 注入方式
- Codex / GitHub Copilot 原生支持 Agent Skills 的官方证据 [5]
- 本体构建 skill 面对沙箱网络限制的解决方案（MCP 或本地运行）
- 中文侧 [[本体构建-agent-skills]] 与英文侧模板是否同构（命名、目录、frontmatter）
- 关联既有查询：[[本体建模两条路径的验收标准待核验]]；若 skill 内置校验脚本，则 [[本体验证规则来源与自证风险待核验]] 与 [[本体质量度量口径待核验]] 的旧问题会重现

## 建议补充来源

- Neo4j《Going Meta S03E07》完整录像/字幕与配套幻灯片（获取本体构建 skill 提示词原文的直接证据）
- Anthropic 官方《Skill authoring best practices》与《Using Agent Skills with the API》全文（补齐 frontmatter 与脚本规范）
- agentskills.io 规范文本（跨客户端一致性的一手依据）
- OpenAI Codex Skills 官方文档（核实跨客户端说法）
- nano-ontoprompt 仓库 README 与代码（确认端到端提示是否已被打包为 skill 或脚本）
- [6] 论文全文与附录（若含提示词模板）
- 中文侧 FDE 课程第 8 集来源页及 skill 文件原文（与英文模板做同构核验）

**总体判断**：模板层（SKILL.md 目录、frontmatter、渐进式披露、脚本规范）已有可靠原文依据 [4][5]；提示词原文层只落实了一条通用本体抽取提示词 [7]，且其不属于 skill 形态。"本体构建 Agent Skills 的提示词原文"——尤其是 [1][3] 中与本体场景直接对应的 SKILL.md 内容——仍是本次核验的最大空白。

## References

1. [Going Meta S03E07 – Agent Skills For Creating and Using Ontologies](https://neo4j.com/videos/going-meta-s03e07-a-series-on-semantics-knowledge-graphs-and-all-things-ai/) — neo4j.com
2. [Enrich agents with domain-specific knowledge to make AI smarter ...](https://mychen76.medium.com/enrich-agents-with-domain-specific-knowledge-to-make-ai-smarter-ontology-skills-rag-tool-3fa5ee20e52c) — mychen76.medium.com
3. [Going Meta S03E07 – Agent Skills For Creating and Using Ontologies](https://www.youtube.com/watch?v=6bIUwMrKDlk) — youtube.com
4. [Agent Skills - Claude Platform Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — platform.claude.com
5. [Claude Skills and SKILL.md for Developers: VS Code, JetBrains ...](https://www.glukhov.org/ai-devtools/claude-code/claude-skills-for-developers/) — glukhov.org
6. [LLM-Driven Ontology Construction for Enterprise Knowledge Graphs - arXiv](https://arxiv.org/html/2602.01276v1) — arxiv.org
7. [Building Ontology with LLMs: Five Methods Compared](https://zerofuturetech.substack.com/p/building-ontology-with-llms-five) — zerofuturetech.substack.com
