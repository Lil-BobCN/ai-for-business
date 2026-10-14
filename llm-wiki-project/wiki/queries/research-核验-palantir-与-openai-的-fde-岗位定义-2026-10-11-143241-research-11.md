---
type: query
title: "Research: 核验 Palantir 与 OpenAI 的 FDE 岗位定义"
created: 2026-10-11
origin: deep-research
tags: [research]
---

# Research: 核验 Palantir 与 OpenAI 的 FDE 岗位定义

# Palantir 与 OpenAI 的 FDE 岗位定义核验

本页针对 [[fde岗位定义与palantir-openai实践待核验]] 中悬置的问题，用两家公司的一手招聘页面与外部二手解读做一次交叉核验：哪些定义要素在双方材料中一致出现，哪些只在单方或单一来源出现，哪些仍无法判定。核心结论是：**招聘文本层面双方确有可核验的交集（嵌入客户、写生产代码、范围界定与取舍、直面客户决策层），但"FDE"这个缩写本身并不是两家公司统一的官方岗位名**，且 [[fdeforward-deployed-engineer前线部署工程师]] 页面所用的英文全称与 Palantir 招聘标题存在名称差异。

## 一、证据基础与覆盖度

本次材料共 9 条，可分为两层：

| 层级 | 来源 | 性质 |
| --- | --- | --- |
| 一手 | Palantir 招聘页 [1]、Lever 岗位页 [2]、LinkedIn 岗位页 [3]；OpenAI 招聘页 [4][5][6][8] | 公司官方或官方渠道发布 |
| 二手 | FDE Academy 指南 [7][9] | 第三方培训/社区站点，含组织归属、地点清单、日常流程等归纳 |

必须先说明抓取完整性问题：[1] 是 Palantir 招聘总站的文案，正文在 "Forward Deployed ..." 处截断；[4] 是 OpenAI FDE - SF 岗位，正文未抓到，仅剩合规条款尾部。这两条只能作为存在性证据，不能作为职责文本证据。

## 二、Palantir 侧：岗位名称与职责原文

### 2.1 名称

可核验的一手岗位标题是 **Forward Deployed Software Engineer**（[2][3]，两个渠道一致）。[1] 中出现 "Forward Deployed ..." 但被截断，无法判断其完整名称。这意味着：Palantir 官方招聘语境下更常见的写法是 FDSE 而非 FDE；wiki 中以 "FDE" 作为跨公司泛称仍然可用，但在引用 Palantir 原文时应保留 `Forward Deployed Software Engineer` 这一标识符。

### 2.2 职责条目

[2] 列出的核心职责为三条：

- 与工程师同伴协作进行架构与设计决策（Collaborating with fellow engineers on architecture and design decisions）；
- 开发面向客户需求量身定制的应用（Developing custom applications tailored to customer needs）；
- 参与塑造团队策略、推动项目从想法走到部署，并"提高你的疼痛阈值以交付真实价值"（Shaping team strategy and driving projects from ideation to deployment, increasing your pain threshold to deliver real value）。

[3] 在三者之外补出一条 **"Engaging directly with customer stakeholders, from technical teams to executives"**——即客户接口从技术团队一直延伸到高管层。

### 2.3 读法

三条职责分别对应"工程内功""定制交付""端到端推动"，与 [[fde四项能力框架]]、[[fde完整工作闭环]] 的既有归纳方向一致，可作为该两项概念的招聘文本级锚点。"increasing your pain threshold" 属于强烈的公司文化措辞，目前仅见于单条 posting [2]，不宜推广为 Palantir 所有 FDE 岗位的通用表述。[1] 中 "ship code to production" 出现在招聘总站层级文案，不能直接当成 FDE 岗位职责证据。

## 三、OpenAI 侧：岗位家族、组织归属与职责原文

### 3.1 名称与岗位家族

OpenAI 官方页面同时使用了两种标题：**Forward Deployed Engineer (FDE)**（[4][5]，另有 Gov 版本 [8]）与 **Forward Deployed Software Engineer**（[6]）。也就是说，"FDE / FDSE 是同一岗位的两种叫法还是两条序列"这一问题在 OpenAI 侧同样存在，与 Palantir 侧的名称问题形成同类缺口。

### 3.2 职责原文

FDE - Singapore [5] 给出五条：

- 紧密嵌入客户团队、理解需求并引导客户采纳所构建的成果；
- 界定工作范围、编排交付顺序、尽早清除阻塞；
- 在范围、速度与质量之间做取舍，必要时调整计划以保住交付；
- 当进展或清晰度依赖代码时，直接写代码；
- 靠清晰度与跟进让团队持续前进。

FDSE - SF [6] 给出两条：深度嵌入战略客户以理解其业务挑战与技术需求；与 Product、Research、Applied 团队协作，保证客户体验、项目成功与可执行的产品反馈回流。

FDE Gov [8] 增加了政府语境：直接与国防、情报、联邦相关方合作，担任其"技术思想伙伴"（technical thought partner），推动采纳并最大化任务影响。

FDE - SF [4] 因抓取不全，无法核对职责是否与 [5] 一致。

### 3.3 二手来源补充

[7] 称 OpenAI 的 FDE 岗位隶属于 **"Model Deployment for Business"**，覆盖 New York City、San Francisco、Dublin、London、Seattle、Madrid、Munich、Paris、Seoul、Singapore、Stockholm、Tokyo 等地；并描述其日常为：写 Python / JavaScript 生产代码、把模型集成进客户既有基础设施（而非单独立一个工具）、上线后持续监控与修复、把经验回流给 Research 与 Product 以影响模型路线图。[9] 进一步把 FDE 的平台构建工作拆为四层——data integration、retrieval、orchestration、evaluation，并称这是"一个永远不会真正结束的 discovery-to-production 循环"。这两条与 [[本体与agent协同]]、[[rag三种实现路径]] 讨论的检索与编排层可以互参，但均属第三方归纳，不能算作公司定义。

## 四、横向对照

| 维度 | Palantir | OpenAI |
| --- | --- | --- |
| 官方标题 | Forward Deployed Software Engineer [2][3]（[1] 截断） | Forward Deployed Engineer [4][5][8] 与 Forward Deployed Software Engineer [6] 并存 |
| 组织归属 | 材料未说明 | "Model Deployment for Business" [7]（二手） |
| 客户类型 | [2][3] 未限定；客户方 stakeholder 含高管 [3] | 战略客户 [6]；Gov 版面向国防/情报/联邦 [8] |
| 核心动作 | 架构协作、定制应用、从 ideation 到 deployment、拉高疼痛阈值 [2] | 嵌入、scope 与排序、取舍、直接写代码、清晰度与跟进 [5] |
| 反馈回流 | 招聘文本未提及 | 明确回流 Research / Product [6][7] |
| 上线后责任 | 一手文本未提及 | [7] 称持续监控、修复、回流；[9] 称循环不结束（均为二手） |

## 五、可以确认的共识点

1. **嵌入客户环境**：双方均把"嵌入"写在职责首位（[3][5][6]）。
2. **直接产出生产代码**：Palantir 的定制应用开发 [2] 与 OpenAI 的"进展依赖代码时直接写" [5]、Python/JS 生产代码 [7] 对应。
3. **端到端推动与取舍**：Palantir 的 ideation→deployment [2] 与 OpenAI 的 scope/sequence/trade-off [5] 是同一类工作的不同措辞。
4. **直面客户决策层**：[3] 的 "technical teams to executives" 与 [8] 的 "technical thought partner" 指向同一种角色定位。
5. **交付与工程团队的反馈回路**：OpenAI 侧证据最完整（[6][7]）；Palantir 侧招聘文本沉默。

## 六、矛盾与证据缺口

1. **名称不一致**：Palantir 一手标题为 FDSE，wiki [[fdeforward-deployed-engineer前线部署工程师]] 使用的英文全称是 Forward Deployed Engineer。是否为同一序列的不同称呼，无证据。
2. **OpenAI 双标题关系不明**：FDE [5] 与 FDSE [6] 的职责条目有交集但不重合，二者是职级差异、地域差异还是职能差异，材料无法回答。
3. **[1]、[4] 抓取不完整**，Palantir 招聘总站与 OpenAI FDE-SF 的完整文本缺席，任何基于这两条的推断都应视为暂定。
4. **组织归属与地点清单仅有二手来源 [7]**，"Model Deployment for Business" 这一名称尚未在 OpenAI 官方页面中得到印证。
5. **上线后责任边界**：对 OpenAI 侧，[7][9] 提供了二手支持，可部分收敛 [[fde上线后迭代责任边界待核验]]；对 Palantir 侧，招聘文本沉默不等于无责任，该问题仍开放。
6. **Echo / Delta 组织模型**：本次全部招聘材料中未出现 [[echo与delta双团队模型]] 的任何字样，该模型目前仍只有播客解读来源，缺乏一手支撑。
7. **数量与薪酬数字**：本批材料不含任何岗位数量、薪酬或比例数据，[[fde相关数字原音与统计口径待核验]]、[[fde政策比例目标与共建基地说法待核验]] 不受本次核验影响。
8. **"FDE 定义原文"层**：若 wiki 需要一条可引用的定义句，目前最接近的是 [7] 的 "own the full arc of a deployment"，但它是二手改写，仍需回溯到 [[bob-mcgrew身份与fde定义原文待核验]] 所指向的原始出处。

## 七、与既有 wiki 知识的衔接

- [[fde完整工作闭环]]、[[fde交付方法]]、[[fde四项能力框架]]：本次招聘文本为这些概念提供了公司侧锚点，但 [[fde适用三条件]] 属于方法论层判断，招聘页面一般不涉及，二者证据层级不同。
- [[从业务员工中培养自己的-fde]] 与 [[abc-legal]]：描述客户侧自建 FDE 的路径，与本文的厂商派驻 FDE（Palantir / OpenAI 模式）构成两条并行路线，可作对照阅读。
- [[场景数量乘单点专家的瓶颈]]：FDE 作为"单点专家"的产能约束，与两家公司同时多地点、多岗位招聘的现象相互映照。
- [[agent验收指标清单]]、[[业务验收指标口径]]：可与 [9] 的 evaluation 层对照，但 [9] 未给出具体指标，此处仅作索引。

## 八、建议补充的来源

1. Palantir 官方 careers 页面完整抓取，列出所有 "Forward Deployed" 岗位标题，确认 FDSE 与 FDE 是否并存。
2. OpenAI 官网 FDE - SF [4] 的完整 JD；以及 NYC、Dublin、London、Tokyo 等地点 JD 的逐条文本比对，验证职责模板是否统一。
3. OpenAI 官方或官方媒体中 "Model Deployment for Business" 组织名称的一次确认。
4. Palantir 官方工程博客、FDE 校友访谈或公开演讲中关于该岗位全生命周期的自述，用于填补"上线后责任"缺口。
5. 招聘数据平台（Lever、Greenhouse、levels.fyi 等）上两家公司 FDE/FDSE 岗位标题与薪酬的分布统计，用于回应数字类待核验项。
6. Bob McGrew 关于 FDE 定义的原始出处原文（见 [[bob-mcgrew身份与fde定义原文待核验]]）。

**总体判定**：本轮核验把"Palantir 与 OpenAI 的 FDE 岗位定义"从播客转述推进到了招聘文本层——共识部分（嵌入、写码、范围管理、客户决策层接口、反馈回流）已有可引用的原文；分歧部分（岗位命名、双标题关系、上线后责任、组织归属）仍需一手材料补齐，暂不宜在 wiki 中写成确定结论。

## References

1. [Careers | Palantir](https://www.palantir.com/careers/open-positions/) — palantir.com
2. [Palantir Technologies - Forward Deployed Software Engineer - Lever](https://jobs.lever.co/palantir/dab396d4-2f14-4796-aac0-0d82883dccf0) — jobs.lever.co
3. [Palantir Technologies hiring Forward Deployed Software Engineer in ...](https://www.linkedin.com/jobs/view/forward-deployed-software-engineer-at-palantir-technologies-3736674638) — linkedin.com
4. [Forward Deployed Engineer (FDE) - SF - OpenAI](https://openai.com/careers/forward-deployed-engineer-(fde)-sf-san-francisco/) — openai.com
5. [Forward Deployed Engineer - Singapore - OpenAI](https://openai.com/careers/forward-deployed-engineer-singapore-singapore/) — openai.com
6. [Forward Deployed Software Engineer - SF - OpenAI](https://openai.com/careers/forward-deployed-software-engineer-sf-san-francisco/) — openai.com
7. [OpenAI Forward Deployed Engineer Guide 2026 | Salary - FDE Academy](https://fde.academy/blog/openai-forward-deployed-engineer) — fde.academy
8. [Forward Deployed Engineer, Gov - OpenAI](https://openai.com/careers/forward-deployed-engineer-gov-washington-dc/) — openai.com
9. [How Forward Deployed Engineers Build AI Platforms - FDE Academy](https://fde.academy/blog/how-forward-deployed-engineers-build-enterprise-ai-platforms) — fde.academy
