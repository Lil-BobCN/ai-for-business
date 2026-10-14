---
type: concept
title: 长任务 Agent 五项基础设施
tags: [长任务, Agent, 基础设施, 验收清单]
related: [生产级agent五件事, agent-api与模型-api的分界, 上下文压缩, tool-search与工具目录治理, programmatic-tool-calling, 多agent两种架构-经理模式与交接制, 长任务五项基础设施与生产级五件事口径待核验]
sources: ["零点未来：AI+企业/第 12 集｜9分钟OpenAI这次卖的不只是模型.md"]
evidence_status: unknown
created: 2026-10-11
updated: 2026-10-11
---

# 长任务 Agent 五项基础设施

## 定义

视频作者在该段口播中提出：一个 Agent 若要在企业生产环境中连续工作几十步、几百步，除模型之外还需要五项基础设施——上下文管理、工具使用、复杂任务拆解、失败恢复、执行环境。作者称这些过去往往需要开发者自己搭建。

## 来源观点

作者用比喻说明：像 GPT 这样的模型是汽车的发动机，而运行时（ASR 作 `Honest`）更像变速箱、方向盘、底盘、导航和控制系统；发动机再强，没有后面这些东西，车也很难稳定跑几百公里。作者的概括是「Demo 很容易，真正做生产系统却非常难」。

## 已核验事实

无。该清单为作者口播归纳，属 `unknown / 待外部核验`。

## 项目分析

该清单可直接当作自研或选型的验收表使用。它与既有页面 [[concepts/生产级agent五件事]] 高度重叠，但列举口径是否一致尚未比对——按 schema 规则，冲突应记入 query 而非静默择一，见 [[queries/长任务五项基础设施与生产级五件事口径待核验]]。

## 反例或边界

- 作者未说明五项之间的优先级，也未给出任何一项的验收标准。
- 清单来自平台侧发布叙述，示例集中在工程排障场景，跨部门业务流程是否同样适用未检验。

## 关联页面

- [[concepts/生产级agent五件事]]
- [[concepts/agent-api与模型-api的分界]]
- [[concepts/上下文压缩]]
- [[concepts/tool-search与工具目录治理]]
- [[concepts/programmatic-tool-calling]]
- [[concepts/多agent两种架构-经理模式与交接制]]

## 开放问题

- 五项中哪一项最容易被自研团队低估工作量？
- 该清单与 [[concepts/生产级agent五件事]] 是同一套口径还是两套？