---
type: query
title: "Research: 建立企业 Agent 高风险动作的控制证据"
created: 2026-10-11
origin: deep-research
tags: [research]
---

# Research: 建立企业 Agent 高风险动作的控制证据

# 企业 Agent 高风险动作的控制证据

> 合成页（Synthesis），综合 10 条外部来源 [1]–[10]，建议路径：`synthesis/企业-agent-高风险动作控制证据`。

**控制证据（control evidence）**指企业能够证明"某个高风险动作由谁发起、经谁批准、以什么参数执行、结果如何、能否撤销"的完整记录链。多个来源一致主张：人类审批不能停留在 UI 弹窗层面，审批、权限、日志与回滚必须在 Agent 上线前作为架构要素一并设计 [3][4][9]。本文按"风险分级 → 审批实现 → 证据闭环 → 审计日志 → 治理层"的顺序整理这一主题，并与 wiki 既有页面建立关联。

## 一、问题界定：审批弹窗不足以构成证据

[3] 主张审批应成为一等公民的 API（approval as a first-class API）：企业 Agent 的人工审批常被实现为 UI 弹窗，无法支撑无头运行、审计与跨系统追溯。[1] 用一个邮件 Agent 场景展示了完整的策略形态：

- 允许读取与向少量收件人发送普通邮件；
- 向发件人未使用过的邮件列表发送，需要 IT 管理员审批；
- 阻止外发凭证与财务数据；
- 阻止删除邮件，但允许删除草稿。

该策略同时包含"放行 / 审批 / 阻断"三档，说明控制证据的前提是**按动作类型预先定义策略**，而不是执行时即兴询问 [1][4]。这一思路与 [[action分级与确认机制]] 中的动作分级、确认机制直接对应；[[自主权判据]] 则提供"哪些动作可交给 Agent 自主"的前置判断依据。

## 二、风险分级：审批门放在哪里

各来源采用同构的"风险分级 → 匹配控制模式"结构：

- [4] 提出基于风险的审批门（risk-based approval gates），并把可审计性与可回滚执行列为与审批并列的架构要素；
- [7] 在医疗场景给出对照实现：低风险操作（查询患者姓名）免审批，高风险动作（读取生命体征、医疗状况）要求人工授权；敏感工具被调用时触发 hook 的 `interrupt`，暂停 Agent 循环直至人工响应；
- [6] 把风险等级映射到四种设计模式：**interrupt and resume**（中断-恢复，适合高风险、不可逆动作）、**human as a tool**（适合 Agent 自行标记不确定性的模糊决策）、**approval flows**（适合受政策约束的动作）、**fallback escalation**（兜底升级，覆盖前三者之外的边缘情况）；
- [1] 的邮件策略同样是分档的：普通发送放行、新邮件列表审批、凭证与财务数据直接阻断。

## 三、审批的实现粒度与恢复语义

[5] 给出两个实现粒度：

- **Tool-level HITL**：审批挂在工具调用前。多 Agent 团队运行暂停后，遍历 `active_requirements`（可读 `member_agent_name` 与 `tool_execution.tool_name` 以确认是哪个子 Agent 想调哪个工具），逐项 `confirm()` 或 `reject()`，再 `continue_run()` 恢复；
- **Workflow-level HITL**：审批作为工作流步骤间的检查点，`Step(requires_confirmation=True, confirmation_message=...)`；暂停后遍历 `steps_requiring_confirmation` 人工确认，再 `continue_run()`。

[7] 给出 hook 版实现：`ApprovalHook` 在 `BeforeToolCallEvent` 上注册回调，对敏感工具清单内的调用执行 `event.interrupt()`；拒绝时设置 `event.cancel_tool`；用户选择 "trust always" 后写入会话状态，同一工具在本会话内不再询问。

[1] 补充了**审批恢复语义**——这是控制证据最容易被忽略的一环：

```text
当某个调用需要审批：
    保存该调用与审批引用。
    在审批挂起期间等待。

当审批状态变化：
    已批准：凭该审批，以原始意图重试“未修改的调用”。
    拒绝、取消或过期：终止本次尝试。
```

要点：恢复执行时重试的必须是未被修改的调用，并沿用原始意图；拒绝、取消、过期都导致本次尝试终止，而非降级执行 [1]。这与 [[agent中断条件与检查点]] 互补：后者定义"何时停"，前者定义"停下后如何凭证据恢复"。

## 四、控制证据闭环：权限 → 动作 → 日志 → 复核 → 回滚

[9] 提炼出如下闭环，并为每类动作预先定义"权限、日志字段、回滚路径"三元组（run ledger）：

```text
permission -> action -> log -> review -> rollback
```

| 动作 | 权限 | 日志 | 回滚 |
| --- | --- | --- | --- |
| 编辑源文件 | 仓库内允许，仓库外询问 | 文件路径、diff 摘要、前后 sha | `git checkout` 或 revert commit |
| 安装依赖 | 询问 | 包名、版本、registry、lockfile diff、安全公告检查 | 卸载包、恢复 lockfile、重跑测试 |
| 推送分支 | 询问 | 分支名、提交、远端、操作者、会话链接 | 删除分支或 revert 提交 |
| 部署预览 | 询问 | 环境、commit sha、配置 diff、URL、检查项 | 重新部署前一个 sha |

日志要"记录决策，而不仅是输出"：除退出码与耗时外，还应包含 `runId`、`actor`、`requestedBy`、`action`、`permission`（如 allowlisted）等字段。回滚必须**在运行前决定**；若动作触及生产数据，回滚可能退化为补偿性迁移、恢复备份、退款或人工清理 [9]。[4] 的结论与此一致：审批、权限、可审计性与可回滚性必须从架构第一天就内建。对编码类 Agent，这套闭环与 [[harness与sandbox解耦]] 的隔离设计互补——沙箱限制"能做到什么"，run ledger 记录"实际做了什么"。

## 五、Agent 审计日志与普通应用日志的差异

[10] 对比了两类日志：应用日志面向故障排查（level、service、latency、status_code），而 Agent 审计日志要回答"谁授权了什么、Agent 以什么身份做了什么"。其字段结构包括：

- `session_id`、`trace_id`：会话与链路追踪；
- `user`：发起人身份；
- `agent`：Agent 标识与版本（示例：`document-summarizer` v1.2.0）——版本号是复现与追责的关键；
- `authorization`：scopes、`session_type`（如 `human_approved`）、`approved_by`、`approved_at`、`expires_at`——审批本身带有效期；
- `action`：工具名、参数、结果状态、延迟；
- `delegation_chain`：initiator（用户）→ executor（Agent）的委托链。

[8] 从合规侧补充"授权时刻要记录什么"以及**撤销证明**：

- 撤销访问时，`last-action` 时间戳用于证明"离职员工的 Agent 访问在某日截止"，这是离职认证（offboarding certification）与 SOC 2 访问审查的检查点；GDPR 删除请求同样依赖该字段 [8]；
- 结构化审计日志使取证查询可以在分钟内完成（来源示例：查询某时间戳的 `agent.github_issue_create` 事件、确认 `connection_id` 指向自家仓库、确认触发消息来自授权 Slack 用户，共耗时 4 分钟）[8]。

两条来源共同说明：控制证据的最小单元不是"一条日志"，而是**授权上下文 + 动作参数 + 委托链 + 时间边界**的组合 [8][10]。其取向与 [[agent可解释性不可信与可审计三元组]] 一致：不依赖模型自述，而依赖可审计的记录结构。

## 六、身份治理与采购审查

- [2] 把 AI Agent 授权治理归纳为身份控制、最小权限与审批三件事，并将其列为 2026 年企业安全议题；
- [4] 强调审批者本身也需要 RBAC——并非所有角色都有资格批准高风险动作；
- [8] 提到企业安全团队在采购审查中会提出的六类问题，但摘要未逐条展开（见缺口 6）。

治理层的检查项可与 [[生产级agent五件事]]、[[agent验收指标清单]]、[[业务验收指标口径]] 相互对照：它们关注"上线前要具备什么"，控制证据回答"上线后如何证明"。该主题也可视为 [[最小闭环与组织治理基础]] 在单次动作粒度上的落地，并与 [[把-agent-当软件管理]] 的立场一致：Agent 动作需要软件工程意义上的权限与变更管理。

## 七、与既有 wiki 内容的关系

- [[action分级与确认机制]]：Palantir 系列的动作分级与确认，对应本文"风险分级 → 审批门"；
- [[agent中断条件与检查点]]：定义中断与检查点机制，本文补充凭审批证据重试的语义；
- [[agent可解释性不可信与可审计三元组]]：提供"可审计"的理论支点；
- [[本体作为约束层]] 与 [[防幻觉的架构化机制]]：本体约束在事前拦截非法动作，控制证据在事后保证可证明，两者构成事前-事后互补；
- [[人机协同留痕与快照时效待核验]]：已有的留痕与快照时效疑问，与本页第五节的"时间边界"问题直接相关。

## 八、矛盾与缺口（待核验）

1. **"trust always" 与最小权限的张力**：[7] 允许用户在会话内对某工具选择 "trust always" 跳过后续审批，而 [2] 主张最小权限。会话级信任提升效率，但削弱逐次审批的证据颗粒度，且来源未讨论该信任是否可被审计追溯；
2. **审批粒度的分歧**：[3] 主张审批作为平台层的一等公民 API，[5][7] 在 Agent 框架与 hook 层实现，[1] 在动作网关层实现。三者是替代还是分层关系，来源间无统一口径；
3. **不可逆动作的回滚边界**：[9] 承认回滚可能退化为补偿迁移、退款或人工清理；[1] 对"已发送邮件"类动作只给出阻断策略，没有回滚方案。哪些动作必须"先批后做"、哪些允许"先做后补"，缺乏统一判据；
4. **审批过期后的语义**：[1] 规定过期即终止本次尝试，[10] 的 `expires_at` 字段说明审批有有效期，但均未给出有效期设定标准（与动作风险、金额、时间窗的关系）；
5. **证据留存期、防篡改与跨系统关联**：所有来源均未回答控制证据应保存多久、如何防篡改（签名/不可变存储）、以及跨系统（Agent 平台、业务系统、IAM）如何关联同一动作的证据链；
6. **"六类采购问题"未列全文**：[8] 提到企业安全团队在采购审查中提出六类问题，摘要未逐条展开，需回原文核验；
7. **来源质量提示**：[1][2][8][10] 等为厂商博客（部分涉及审批/审计类产品），存在向自身产品倾斜的倾向；[3] 为个人观点文章，证据权重较低。上述判断需以官方文档或标准文本复核。

## 九、建议补充的检索方向

- NIST AI RMF、ISO/IEC 42001 等治理框架——提供证据与文档化的通用要求；
- SOC 2 与 GDPR 对 Agent 审计日志的具体条款，与 [8] 的结论对照；
- WorkOS Airlock 官方文档——[1] 的审批引用持久化与重试细节；
- Dataiku、Agno、AWS 的原始文档与示例代码——[5][6][7] 的实现原文；
- Palantir AIP 的 Action 审计与本体约束文档——与 [[action分级与确认机制]]、[[本体作为约束层]] 对接；
- 学术方向：agent provenance / audit trail 完整性机制（hash chain、不可变日志、跨系统 trace 关联）。

## 附录：本页引用来源

| 编号 | 来源 |
| --- | --- |
| [1] | WorkOS — AI agent approval workflows: handling edits and retries |
| [2] | Sennovate — AI Agent Authorization Governance for Enterprise Security in 2026 |
| [3] | Medium — Your AI Agent Has a Permission Problem: The Next Security Crisis |
| [4] | DZone — Human-in-the-Loop Approval Gates for Enterprise AI Agents |
| [5] | Agno — How to add human-in-the-loop controls to AI agents that actually work |
| [6] | Dataiku — Human-in-the-loop AI agents: design patterns for governance |
| [7] | AWS — Human-in-the-loop constructs for agentic workflows in healthcare and life sciences |
| [8] | Scalekit — Audit Trails for Agent Auth in B2B SaaS: Compliance Guide |
| [9] | Developers Digest — Permissions, Logs, and Rollback for AI Coding Agents |
| [10] | WorkOS — Why AI agent audit logs are different from application logs |

## References

1. [AI agent approval workflows: handling edits and retries - WorkOS](https://workos.com/blog/ai-agent-approval-policies-airlock) — workos.com
2. [AI Agent Authorization Governance for Enterprise Security in 2026](https://sennovate.com/blog/ai-agent-authorization-governance-enterprise-security-in-2026/) — sennovate.com
3. [Your AI Agent Has a Permission Problem: The Next Security Crisis in ...](https://medium.com/illumination/your-ai-agent-has-a-permission-problem-the-next-security-crisis-in-enterprise-ai-185949cdbed7) — medium.com
4. [Human-in-the-Loop Approval Gates for Enterprise AI Agents - DZone](https://dzone.com/articles/human-in-the-loop-approval-enterprise-ai-agents) — dzone.com
5. [How to add human-in-the-loop controls to AI agents that actually ...](https://www.agno.com/articles/how-to-add-human-in-the-loop-controls-to-ai-agents-that-actually-run-in-production) — agno.com
6. [Human-in-the-loop AI agents: design patterns for governance - Dataiku](https://www.dataiku.com/blog/human-in-the-loop-ai-agents) — dataiku.com
7. [Human-in-the-loop constructs for agentic workflows in healthcare and ...](https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-constructs-for-agentic-workflows-in-healthcare-and-life-sciences/) — aws.amazon.com
8. [Audit Trails for Agent Auth in B2B SaaS – Compliance Guide - Scalekit](https://www.scalekit.com/blog/audit-trail-agent-auth) — scalekit.com
9. [Permissions, Logs, and Rollback for AI Coding Agents - Developers Digest](https://www.developersdigest.tech/blog/permissions-logs-rollback-ai-coding-agents) — developersdigest.tech
10. [Why AI agent audit logs are different from application logs - WorkOS](https://workos.com/blog/agent-audit-logs) — workos.com
