---
type: source
title: 第 4 集｜14分钟揭秘Palantir一堆文件如何变成Ontology
tags: [Palantir, Foundry, Ontology, 数据链路, FDE, ASR]
related: [palantir, aip, 本体与企业语义层, 文件到本体的五阶段链路, 三条清洗路径, 干净表到本体的映射, 增量更新三层与两个坑, 宽表拆分规则, ontology与数据库schema的三点差异, fdeforward-deployed-engineer前线部署工程师, ontoprompt]
sources: ["零点未来：AI+企业/第 4 集｜14分钟揭秘Palantir一堆文件如何变成Ontology.md"]
evidence_status: partial
created: 2026-10-11
updated: 2026-10-11
---

# 第 4 集｜14分钟揭秘Palantir一堆文件如何变成Ontology

## 来源信息

- **标题**：第 4 集｜14分钟揭秘Palantir一堆文件如何变成Ontology
- **作者/平台**：零点未来（Bilibili），合集《AI+企业》第 4 集
- **URL**：https://www.bilibili.com/video/BV1L4Ek68EWc
- **原始文件路径**：`零点未来：AI+企业/第 4 集｜14分钟揭秘Palantir一堆文件如何变成Ontology.md`
- **提取方式**：本地 ASR 转写（非官方字幕），专名、缩写与数字可能有误
- **证据状态**：`partial`（转写不完整/可能有误）；视频作者口播主张属 `unknown / 待外部核验`

## 一句话摘要

视频作者认为，企业 AI 落地里最容易被跳过、也最耗人的一段，是"一堆文件怎么变成 Ontology"这件脏活累活（Dirty Work）；他以 Palantir 官方文档里的航空公司场景为例，把"数据连接 → 存储 → 清洗解析 → 标准表 → 映射成本体"这条五阶段链路逐段拆开，再补上增量更新、宽表拆分与 FDE 成本这几处现实约束。

## 主要论点（均为作者口播观点，`unknown / 待外部核验`）

1. **企业 AI 落地最易被跳过的是"文件变 Ontology"的 Dirty Work**。作者以 Palantir 官方文档航空公司场景逐段拆解。证据强度：中——场景来自官方文档，但拆解为作者解读。
2. **五阶段链路**：数据连接 → 存储 → 清洗解析 → 标准表 → 映射成本体。三类数据（结构化航班 CSV、半结构化预订 JSON、非结构化维修 PDF）走三条完全不同的清洗路径。
3. **"不做预处理"是治理原则而非工程洁癖**。作者称 Foundry 有 200 种连接器；拉取方式分 snapshot（全量替换）与只追加新数据 `upam`〔待确认〕。
4. **存储层两概念**：dataset（通用容器，被称 git for data）与 media set（媒体文件专用），通过 media reference 关联。
5. **非结构化路径五步**：存 MediaSet → OCR+多模态视觉大模型输出 Markdown → 解析业务字段 → 校验复核（含人工抽样）→ 输出 Clean Maintenance 表并保留指向原 PDF 的列。
6. **映射对应关系**：表→Object Type，行→Object Entity，列→Property，表间关系→Link Type，读写操作→Action Type。Action 写入独立 writeback dataset，不污染原始数据。
7. **Logic 与 Action 让本体"活起来"**。Action 四部分：参数、规则、前置条件、副作用。
8. **增量更新需三层配合**（数据同步、Pipeline 处理、Ontology 索引），且有两个坑：状态覆盖需去重、实时改签与批处理存在时间差窗口。
9. **宽表拆分是最贵的一环**。一个 Object Type 只能对应一张表；Pipeline Builder 的 AI 可辅助写拆分代码，但"哪一列属于哪个实体"仍需人为判断，这是 FDE 最贵的时间。
10. **行业模板沉淀不下来是商业模式问题**。作者判断 Palantir 技术上能做但没动力做，因为 FDE 常驻咨询是其商业模式。真正值钱的是"宽表到实体的 Mapping 规则"产品化，垂直行业玩家更有动力。
11. **Ontology 与数据库 Schema 三点差异**：全链路可追溯、可写回、应用层直接消费（无需写 API）。三点合起来使其成为"Agent 的操作层"。

## 场景与三类数据

作者设定场景：假设你是某航空公司数字化负责人，手上有三类数据。

- **结构化航班运营数据**：CSV 或 Database，来自 `欧罗克`〔数据库名待确认〕与 MySQL；字段含出发时间、状态、飞机尾号。
- **半结构化乘客预订数据**：JSON，来自 OTA 订票系统；每份预定单嵌套乘客信息与多段行程。
- **非结构化维修报告**：PDF 扫描件，工程师手写维修记录，无数字化结构。

## 五阶段链路骨架

| 阶段 | 名称 | 关键动作 |
|---|---|---|
| 1 | 数据连接 | 原封不动拉入，不做预处理；连接器对接数据源；snapshot 或只追加新数据 |
| 2 | 存储 | dataset（通用容器，带版本）与 media set（媒体专用），用 media reference 关联 |
| 3 | 清洗解析 | 结构化走自动推断 Schema；半结构化走 Explode 摊平；非结构化走 OCR+多模态 |
| 4 | 标准表 | 输出 Clean Flight、Clean Maintenance 等干净表 |
| 5 | 映射成本体 | 表→Object Type，行→Object Entity，列→Property，关系→Link Type，读写→Action Type |

## 三条清洗路径

- **结构化（CSV/Database）**：Apply Schema 按钮扫描样本自动识别时间/数字/文字类型；再用拖拽式 Pipeline Builder 过滤去重，得到 Clean Flight 表。
- **半结构化（JSON/XML）**：核心操作 Explode，把嵌套结构炸开摊平；一份预订 JSON 变成乘客表与预订表，用订单 ID 关联。
- **非结构化（PDF 扫描件）**：AIP Document Intelligence 五步——存 MediaSet → OCR+多模态视觉大模型输出 Markdown（作者提到可用 Microsoft 的 `Mockdown`〔库名待确认〕把非 Markdown 格式转 Markdown）→ 解析业务字段 → 校验复核（含人工抽样）→ 输出 Clean Maintenance 表并保留指向原 PDF 的列。

## 干净表到本体的映射

- 一张干净表 → 一个 Object Type
- 表里每一行 → 一个 Object Entity（如航班号 CA1234）
- 表里每一列 → 一个 Property（如出发时间、状态）
- 两张表之间的关联 → 一个 Link Type（如 Flight 通过尾号关联 Aircraft）
- 数据读写操作 → 一个 Action Type（如改签、更新状态）

Action 写入独立 writeback dataset，不污染原始数据。

## Logic 与 Action

- **Logic**：逻辑推断与计算，自动推导新信息（如从出发时间与实际起飞时间自动算出延误分钟数；跨航班聚合出公司平均延误）。
- **Action 四部分**：参数（输入）、规则（执行时做什么）、前置条件（何时可执行）、副作用（执行后触发什么）。所有修改写入独立记录，不覆盖原始数据，可追溯谁改、改了什么、何时改。

## 增量更新

作者用图书馆比喻：图书馆已有 2000 万本书（历史航班记录），每周新增 100 万本（新航班）。全量重算需每周整理 2100 万本；增量更新只处理新到的 100 万本。

**三层配合**：数据同步只拉新数据 → Pipeline 只处理新增行 → Ontology 索引只更新有变化的对象。三层缺一不可。

**两个坑**：
1. 状态被修改（准点→延误）时，追加模式同步会出现新旧版本并存，需在 Pipeline 去重只保留最新状态。
2. 用户在 Ontology 界面改签是立刻生效，而 Pipeline 批量更新是定时跑，两个来源有时间差窗口；Ontology 会自动合并数据但合并不了时间。

## 宽表拆分与 FDE 成本

现实中企业数据常是一张几百列的大宽表（订单、客户、商品、物流混在一起）。Palantir 有一条硬性规则：一个 Object Type 只能对应一张表。因此宽表必须先拆成聚焦小表（订单表、商品表、物流表），各自映射到对应 Object Type，再用 link 连接。

Pipeline Builder 内置 AI 可辅助写拆分代码，但"怎么拆、哪一列属于哪个实体"仍需人为判断，这是 FDE 工程师最贵的那部分时间。作者判断 Palantir 技术上能沉淀行业模板但没动力做，因为 FDE 常驻咨询是其商业模式；真正值钱的是"宽表到实体的 Mapping 规则"产品化，垂直行业玩家更有动力。

## Ontology 与数据库 Schema 的三点差异

1. **全链路可追溯**：Ontology 里任意字段值可追溯到原始文件（作者表述为"某一行"，扫描件场景实际对应某一页）。
2. **可写回**：Action 修改写入 writeback dataset，不污染原始数据。
3. **应用层直接消费**：无需再写 API，AI 与应用直接操作 Ontology 对象，可做业务决策与仿真。

三点合起来，使其成为"Agent 的操作层"，而非数据结构目录。

## 作者自述项目进展（`Ontoplome`〔项目名待确认〕）

作者称本集内容将更新到其 GitHub 项目 `Ontoplome`〔ASR 另有 `Ontoplamt`、`Onto Plompt` 等写法〕。演示内容包括：新增数据管道类型，可新建 Pipeline 并选择业务语义（如供应链）；画布中拖出连接器、存储器、转换器、输出；连接器可选文件上传或 MySQL；存储器自动检测或区分 DataSet 与 MediaSet；转换器分析结构化/半结构化/非结构化及宽表，或自动检测；创建本体时支持简易 LLM Prompt 提取方式与 Pipeline Mapping 方式。

## 待核验主张清单（作者陈述，未经独立核实）

- Foundry 有 200 种连接器
- snapshot 与 `upam`〔待确认〕两类拉取方式
- dataset 版本记录与 git for data 说法
- media set / media reference 机制
- AIP Document Intelligence 五步流程与 Microsoft `Mockdown`〔待确认〕库
- "一个 Object Type 只能对应一张表"硬性规则
- Pipeline Builder 内置 AI 拆分能力
- FDE 商业模式动机判断
- 航班 CSV 200 万行、图书馆 2000 万本/每周 100 万本数量级
- 增量更新三层配合与两处时间差
- Ontology 与 Schema 三点差异
- `Ontoplome` 项目功能清单与进度（作者自述）

## 边界与反例

- 这套做法服务于合规严格、体量大、且有专职 FDE 参与的场景。
- 行业模板短期不会因技术原因普及，卡点在厂商商业模式。
- 增量更新在"状态被覆盖"与"用户即时改签"两种情形下会暴露不一致。
- 官方文档的航空公司场景是理想化的三类数据样本；真实企业还有大量数据停留在人手上或纸质流程里。
- PDF 路径准确性交给人工抽样，但样本量与判定标准作者未给出，直接影响能否规模化。
- "追溯到原始文件的某一行"在扫描件场景实际对应某一页，两者不是同一件事。

## 可迁移素材

1. 把"连接 → 存储 → 清洗 → 标准表 → 映射"当作任何本体项目的检查清单。
2. 把"不预处理、保留原件"当成可追溯性的前置条件，而非可选工程偏好。
3. 按结构化、半结构化、非结构化分三条清洗路径，各配固定动作。
4. 沿用 media reference 那种"一行结构化字段加一列指向原件"的关联模式。
5. 建模时坚持一个实体一张表、宽表先拆再映射。
6. 增量更新按"同步、处理、索引"三层分别做增量，并把状态覆盖与写入时效两个坑提前写进设计。

## 关联页面

- [[palantir]]：本集是 Palantir 平台工程细节最密集的来源，应补充 Foundry 数据链路。
- [[aip]]：AIP Document Intelligence 是 AIP 的具体能力。
- [[本体与企业语义层]]、[[本体schema与实例事实]]、[[本体建模业务定义数据映射与关系校验]]：本集把"语义层"落到工程细节。
- [[fdeforward-deployed-engineer前线部署工程师]]、[[fde交付方法]]：本集给出 FDE 成本的具体来源（宽表拆分）。
- [[ontoprompt]]：需核验 `Ontoplome` 是否即此项目。
- [[本体作为约束层]]、[[工具调用]]：Action Type 与 writeback 机制可延伸这些页面。
- [[sources/8-零点未来ai企业--47-第-1-集10分钟企业agentic-workflow落地palantir-ontology--167275e]]：第 1 集讲"语义层"是什么，本集讲"怎么来"，形成上下游关系。

## 开放问题

- `Ontoplome` 与 `OntoPrompt` 是否同一项目。
- "不做预处理"在上游数据不出域时是否成立。
- PDF 路径规模化所需的抽样标准。
- 双写时间差的业务裁决规则。