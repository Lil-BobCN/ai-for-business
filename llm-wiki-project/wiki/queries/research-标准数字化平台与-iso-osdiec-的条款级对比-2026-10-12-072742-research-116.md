---
type: query
title: "Research: 标准数字化平台与 ISO OSD、IEC 的条款级对比"
created: 2026-10-12
origin: deep-research
tags: [research]
---

# Research: 标准数字化平台与 ISO OSD、IEC 的条款级对比

# 标准数字化平台与 ISO OSD、IEC 的条款级对比

> **页面性质**：对比类综合页。依据外部来源 [1]–[14] 整理 ISO OSD、IEC 机制及 ISO/IEC 内容模型一侧的公开事实，并与本 wiki 中"标准数字化平台"标准族页面建立对照框架。
>
> **核心提示（证据边界）**：本批来源均为英文公开页面或报告节选，**不包含中国侧标准的条款原文，也不包含 ISO/IEC Directives、OSD 规范或用户指南的条款级文本**。因此本页目前只能给出对比框架、可对比锚点与核验清单，不能给出条款级映射结论；相关主张按 [[标准数字化平台比iso-osd-iec更系统化主张待核验]] 处理，条款级比对本身处于待启动状态（见 [[正式发布版全文未获取与条款级比对待启动]]）。

## 1. 主题范围与证据边界

本页固定三个国际侧对象与一个中国侧对象：

- **国际侧对象一：ISO OSD（Online Standards Development）**。ISO 主导、ISO 与 IEC 共同建设的在线标准制定平台 [1][4]。
- **国际侧对象二：IEC 侧机制**。包括 IEC 对 OSD 的使用、Standard Information Model（SIM）试点、SMART Standards 相关材料 [2][6][7]；治理背景见 [[iec-smb-sg12]]。
- **国际侧对象三：ISO/IEC 内容模型与标签体系**。包括 IEC & ISO Information Model for SMART content、ISO 的 digitally enhanced content、ISOSTS 与 NISO STS [8][9][10][11][12][13][14]。
- **中国侧对象：标准数字化平台标准族**。核心为 [[gb-t-47012-1-2026-系统架构]]（GB/T 47012.1，标准数字化平台 第 1 部分：系统架构），旁及 [[gb-t-48000-4-2026-协同制定要求]]、[[gb-t-48000-2-2026-参考架构模型]]、[[gb-t-46917-1-2026-标准内容语义化表达通用要求]]、[[gb-t-45508-2025-机器可读标准能力等级模型与评估]] 等（均为本 wiki 已有页面）。

证据边界说明：本资料集的总体边界参见 [[5-标准数字化--6-00-先读我--1qttsu9]] 与 [[5-标准数字化--11-01-标准族总览与关系--itsv1r]]；中国侧标准正文获取状态参见 [[标准正文获取三态]]，部分标准无公开草案的获取路径问题参见 [[9项标准中3项无公开草案的条款内容获取路径待核验]]。

## 2. ISO 侧：Online Standards Development（OSD）

### 2.1 定位与目标

- OSD 为技术社区提供"统一且协调的（unique and harmonized）在线平台"，用于协同开展标准制定，覆盖**从预研阶段直至出版**的全过程 [1]。
- ISO 与 IEC 正在共同建设新的 OSD 平台，目标同样是提供统一、协调的平台 [4]；ANSI 面向美国参与者提供 OSD 平台的一般信息与教育资源 [3]。
- 本 wiki 已有对应实体页 [[在线标准制定osd平台]]。

### 2.2 关键功能（据 [1]）

| 角色 / 场景 | 功能 |
|---|---|
| 工作组（WG）成员 | 在线协同创建标准内容 |
| 成员国 / 成员机构 | 在关键制定阶段"在文档上下文中（in the context of the document）"提交评论；收集国家意见、合并后提交 ISO |
| 委员会经理（Committee Manager） | 在文档上下文中预整理、分类并直接解决评论 |
| ISO 中央秘书处（ISOCS）编辑 | 依据 ISO/IEC Directives 审核文档内容 |

### 2.3 采纳范围与成熟度

- 平台适用于 **90% 的 ISO 交付物**，包括 IS、TS、TR、PAS 与 Guides，覆盖新项目与修订项目 [5]（该来源句子未完，后续内容被截断）。

### 2.4 技术实现

- 平台建设由 Fonto（FontoXML）支持 [4]。

## 3. IEC 侧：OSD 与 SMART Standards

### 3.1 IEC 的 OSD 使用

- IEC 侧材料强调三点：完整集成进 IEC 生态系统；在**单一在线工具**中承载完整标准制定工作流；更便捷的评论功能 [2]（来源为节选，"Easier commenting and …" 之后被截断）。

### 3.2 Standard Information Model（SIM）

- 据 2024 年 4 月 BIPM CCU 会议的 IEC 报告：SIM 概念"当时正在国家委员会（NC）层面通过试点（Pilots）测试" [6]；该来源同时提及"市场需求（Market needs）"议题，正文被截断。

### 3.3 SMART Standards

- IEC 材料称，SMART Standards 通过提供"描述标准应用的标准化数据词汇与语法（standardized data vocabulary and grammar）"来增强信息共享与协作；片段中出现 "Pilot 5" 字样，细节被截断 [7]。

### 3.4 IEC & ISO Information Model for SMART content

- 该信息模型"定义核心概念、关系与属性"，目标是使标准内容"可发现、可访问、可互操作……"（Findable, Accessible, Interoperable, …；列表在来源中未结束）[8]。

## 4. 内容形态与编码体系：digitally enhanced content、ISOSTS、NISO STS

### 4.1 ISO digitally enhanced content

- 将标准从静态文档转变为可交互的数字体验，支持导航、检索等能力 [9]。

### 4.2 ISO Standards Tag Set（ISOSTS）

- ISOSTS 是 ISO 标准的 XML 标签集；ISO 提供的示例为独立 XML 文件、不引用 DTD [10]。

### 4.3 NISO Standards Tag Suite（NISO STS）

- NISO STS 是面向标准出版的 XML 标签集，定义用于标记标准的 XML 元素与属性 [11]。
- 技术谱系：NISO STS 基于 ISOSTS，ISOSTS 又基于 JATS [12]。
- 实现层面：以 XML schema 定义文档元素，实现内容与样式的分离 [13]。
- 用途：编码标准的全文、元数据与结构元素，并以 ANSI/NISO 标准形式发布 [14]。
- 可作元数据侧对照的 wiki 页面为 [[gb-t-22373-2021-标准文献元数据]]（属不同体系，映射关系待核验）。

### 4.4 层级区分（分析）

OSD、SIM 与 ISOSTS/NISO STS 分属不同层级，与"标准数字化平台"对比时不应混同：

- **平台/过程层**：OSD，承载制定过程的协同 [1][2]；
- **信息模型层**：SIM、IEC & ISO Information Model [6][8]，可与 [[标准信息模型]]、[[标准信息单元]] 对照；
- **内容编码/语义层**：digitally enhanced content、ISOSTS、NISO STS [9][10][11][12][13][14]，可与 [[标准内容语义化表达]]、[[标准内容通用语义化表达单元]]、[[owl-rdf语义建模]] 对照。

上述对应均为**分析性框架**，尚无条款级证据支撑。

## 5. 对比框架与可对比锚点（分析性，待核验）

### 5.1 维度对照表

| 对比维度 | ISO/IEC 侧（来源） | 中国侧（wiki 页面，待对照） | 核验状态 |
|---|---|---|---|
| 平台定位 | 统一在线制定平台，预研至出版 [1][4] | [[标准数字化平台总体原则]]、[[gb-t-47012-1-2026-系统架构]] | 待条款对照 |
| 生命周期覆盖 | 制定阶段与出版 [1]；IEC"单工具全流程" [2] | [[标准生命周期九阶段]]、[[协同制定过程九阶段]] | 阶段模型是否同构待核验（另见 [[标准生命周期九阶段与既有四阶段概念关系待核验]]、[[协同制定过程九阶段与生命周期四阶段关系待核验]]） |
| 评审与评论协同 | 上下文评论、归类、解决；国家意见收集/合并/提交 [1] | [[流程协同要求]]、[[角色权限矩阵]] | 待条款对照 |
| 架构分层 | 本批来源未见与"业务/保障/实施"平行的分层架构叙述 | [[标准数字化平台业务架构三业务关系]]、[[平台保障架构]]、[[平台实施架构与部署方式]]、[[标准数字化平台资源架构]] | 需补 ISO 侧架构材料 |
| 信息模型 | SIM（NC 试点）[6]；IEC & ISO Information Model [8] | [[标准信息模型]]、[[标准信息单元]] | 概念层面对应，条款级待核验 |
| 内容/语义编码 | digitally enhanced content [9]；ISOSTS [10]；NISO STS [11]–[14] | [[标准内容语义化表达]]、[[语义集成技术要求]] | 目标与粒度不同，须谨慎映射 |
| 能力等级/成熟度评估 | ISO/IEC"五阶段"相关模型（内涵对齐另有核验项，见 [[iso-iec五阶段与能力特征五等级内涵一致性待核验]]） | [[能力特征五等级]]、[[gb-t-45508-2025-机器可读标准能力等级模型与评估]]、[[sam模型]] | 另见 [[smart五层次与sam模型关系及既有页面口径一致性待核验]] |

### 5.2 以"三条主线"作为对照坐标（分析）

本 wiki 记录 GB/T 48000.1（[[gb-t-48000-1-2025-通用指南]]）涉及"标准内容数字化、过程数字化、应用数字化"三条主线（正文定义另有待核验项：[[gb-t-48000-1-2025正文三条主线定义待核验]]），可暂作对照坐标：

- [[过程数字化]] ←→ OSD 的制定过程协同 [1][2]；
- [[标准内容数字化]] ←→ SIM、SMART content 信息模型与 digitally enhanced content [6][8][9]；
- [[应用数字化]] ←→ 机器可读标准与语义集成的目标侧，可参照 [[语义集成技术要求]]。

该坐标有助于组织后续条款级对照表，但两套体系的一一对应关系尚无来源支撑。

### 5.3 条款级对比的最小核验清单（建议）

1. **固定国际侧文本**：ISO/IEC Directives Part 1（程序）与 Part 2（标准内容编制规则）现行版本；OSD 用户指南/需求说明的版本号 [1][5]。
2. **固定中国侧文本**：GB/T 47012.1-2026 正式版（版本差异见 [[gb-t-47012-1正式版与2025-04征求意见稿差异待核验]]）；GB/T 48000.4、GB/T 46917 系列相应条款（文本类型区分见 [[标准档案与标准正文的区分]]）。
3. **统一比较维度**：生命周期阶段、角色与权限、意见（评论）处理、内容粒度（文档/条款/单元）、数据模型与接口、发布与版本、平台架构与部署。
4. **输出三态结论**：逐条给出"对应/部分对应/无对应"并引用来源；无来源支撑项保持空白而非推定。
5. **注意文本类型差异**：ISO 侧材料多为流程性文档或平台功能文档，与 GB/T 架构类标准的条款组织方式不同，条款编号无法直接互译。

## 6. "更系统化"主张的核验要点

关联待核验页：[[标准数字化平台比iso-osd-iec更系统化主张待核验]]。

- 本批来源中，OSD 的公开叙述集中于**制定过程协同**（协同编写、上下文评论、意见处理、中央秘书处审查）[1][2][3][4][5]；ISO/IEC 的**内容语义**工作分布在 SIM、SMART 与标签体系等并行轨道上 [6][7][8][9][10]。
- 若"更系统化"指**架构分层的完整性与业务覆盖广度**：中国侧标准族在 wiki 层面呈现业务、保障、实施、资源等多架构划分（[[标准数字化平台业务架构三业务关系]]、[[平台保障架构]]、[[平台实施架构与部署方式]]、[[标准数字化平台资源架构]]），而本批 ISO/IEC 来源未见对应的分层架构公开材料；但这也可能是**来源选择偏差**（本批未纳入 ISO/IEC 架构类文档），不能据此下结论。
- 若"更系统化"指**制定过程功能深度与部署规模**：OSD 已覆盖 90% 的 ISO 交付物 [5]，规模指标明确；中国侧平台标准的部署与采纳情况未见于本批来源，无法对比。
- 结论：核验前必须先固定比较维度与各自证据文本（条款），并补齐 ISO 侧架构与规范材料（见第 8 节）。

## 7. 矛盾、缺口与不一致

1. **平台口径**：[1] 称 OSD 已提供"一个统一平台"，[4] 称 ISO 与 IEC"正在建设"新平台，[2] 强调"集成进 IEC 生态"——三者对建设状态的描述不一致（可能由材料时点不同所致），平台实例是一套还是多套、如何互联，来源均未说明。
2. **成熟度口径**：SIM 截至 2024 年 4 月仍处于 NC 层试点 [6]，而 [8] 以现在时描述信息模型；引用时应注明材料日期。
3. **来源截断**：[2][5][7][8] 均为节选，[8] 的能力列表（Findable, Accessible, Interoperable, …）未结束；引用其完整目标集前需回查原文。
4. **条款级证据缺失**：本批来源无 ISO/IEC Directives 条款、无 OSD 规范条款、无中国侧标准条款原文；"条款级对比"目前不可完成，只能给出框架（见 5.3 节）。
5. **术语层级风险**：OSD（平台）≠ SIM（信息模型）≠ ISOSTS/NISO STS（XML 标签）≠ digitally enhanced content（内容形态）；与中文侧"协同制定""标准信息模型""语义化表达"等术语的映射必须建立对照表。相关一致性核验项：[[标准数字化标准族国际标准一致性程度待核验]]、[[iso-iec五阶段与能力特征五等级内涵一致性待核验]]、[[smart五层次与sam模型关系及既有页面口径一致性待核验]]。
6. **接口层缺口**：中国侧有 GB/T 46917.2 数据接口要求及 [[标准语义知识库数据接口总体框架]]、[[基础接口与高级接口]] 等页面；本批 ISO/IEC 来源未涉及 OSD/SIM 的接口公开规范。
7. **对比基准的稳定性**：平台族自身存在系列构成与编号待核验项（[[标准数字化系列构成五部分与六部分矛盾待核验]]、[[标准数字化平台第1部分标准编号与gb-t-47012-1关系待核验]]、[[标准数字化平台前言已发布部分表述待核验]]），会影响"以哪一版本作为对比基准"的选择。

## 8. 建议补充来源

**ISO 侧**

- ISO/IEC Directives Part 1（程序）与 Part 2（标准内容编制规则）现行版本。
- ISO OSD 帮助中心完整文档：用户指南、角色说明、版本说明与采纳统计（补全 [1][5]）。
- ISO "digitally enhanced content"及路线图页面完整版 [9]。
- ISOSTS 官方 schema 与示例包 [10]。

**IEC 侧**

- IEC/SMB/SG12 输出文件与后续治理安排（[[iec-smb-sg12]]）。
- IEC SMART Standards 路线图/白皮书及 "Pilot 5" 等试点报告完整版 [7]。
- SIM 规范文本与 NC 试点总结（补全 [6]）。
- IEC OSD 页面完整版及 IEC Academy 相关培训材料 [2]。

**模型与出版侧**

- smartsdu.org 上 IEC & ISO Information Model for SMART content 完整页面 [8]。
- NISO STS（ANSI/NISO Z39.102）标准文本、NISO STS 项目文档与 JATS 规范 [11][12][14]。
- 标准出版标签体系与元数据体系（如 [[gb-t-22373-2021-标准文献元数据]]）的映射研究。

**中国侧与对照分析**

- GB/T 47012.1-2026、GB/T 48000 系列、GB/T 46917 系列正式版全文与编制说明；平台相关实践材料（如 [[南方电网标准中台]]、[[国家电网公司数字标准馆]]）。
- 组织方（如 [[全国标准数字化标准化技术委员会]]、[[中国标准化研究院]]）发布的国际对标材料，若存在应优先纳入。

**分析产出**

- "OSD 功能点 × GB/T 47012.1 / GB/T 48000.4 条款"双向对照表；
- ISO/IEC 五阶段与 [[能力特征五等级]] 对照表；SMART 五层次与 [[sam模型]] 对照表。

## 9. 关联页面

- **中国侧平台**：[[gb-t-47012-1-2026-系统架构]]、[[标准数字化平台总体原则]]、[[标准数字化平台业务架构三业务关系]]、[[标准数字化平台资源架构]]、[[平台保障架构]]、[[平台实施架构与部署方式]]
- **中国侧协同与信息模型**：[[gb-t-48000-4-2026-协同制定要求]]、[[协同制定过程九阶段]]、[[角色权限矩阵]]、[[流程协同要求]]、[[数据协同要求]]、[[标准信息模型]]、[[标准信息单元]]、[[gb-t-48000-2-2026-参考架构模型]]
- **国际侧**：[[在线标准制定osd平台]]、[[iec-smb-sg12]]、[[sam模型]]、[[rami-4-0]]
- **语义与接口**：[[gb-t-46917-1-2026-标准内容语义化表达通用要求]]、[[标准内容语义化表达]]、[[语义集成技术要求]]、[[标准语义知识库数据接口总体框架]]
- **待核验与证据边界**：[[标准数字化平台比iso-osd-iec更系统化主张待核验]]、[[标准数字化标准族国际标准一致性程度待核验]]、[[iso-iec五阶段与能力特征五等级内涵一致性待核验]]、[[smart五层次与sam模型关系及既有页面口径一致性待核验]]、[[正式发布版全文未获取与条款级比对待启动]]、[[标准正文获取三态]]、[[5-标准数字化--6-00-先读我--1qttsu9]]、[[5-标准数字化--11-01-标准族总览与关系--itsv1r]]

> 维护提示：一旦获取 ISO/IEC Directives、OSD 规范文本与 GB/T 47012.1 正式版条款文本，应在本页补充条款级对照表，并更新 5.1 节"核验状态"列。

## 参考来源

[1] ISO 帮助中心文档：What is Online Standards Development (OSD)（helpdesk-docs.iso.org）
[2] IEC：Online standards development (OSD)（iec.ch）
[3] ANSI：ISO/IEC Online Standards Development (OSD) Platform（ansi.org）
[4] Fonto：Online standards development at ISO and IEC - Supported by Fonto（fontoxml.com）
[5] ISO 帮助中心文档：OSD adoption by ISO committees and eligible projects（helpdesk-docs.iso.org）
[6] BIPM：April 2024 CCU meeting — Report from IEC（bipm.org）
[7] IEC：Unlocking the potential of Smart Standards（iec.ch）
[8] SMART Standards / SDU：IEC & ISO Information Model for SMART content（smartsdu.org）
[9] ISO：Digitally enhanced content（iso.org）
[10] ISO：ISO Standards Tag Set (ISOSTS) Resources（iso.org）
[11] NISO：STS (Standards Tag Suite)（niso.org）
[12] NCBI：NISO STS Project Overview and Update（ncbi.nlm.nih.gov）
[13] SEMI：A Further Look at NISO and the Standards Tag Suite（semi.org）
[14] Metadata Standards Index：NISO Standards Tag Suite (NISO STS)（msi.dublincore.org）

## References

1. [What is Online Standards Development (OSD)](https://helpdesk-docs.iso.org/article/649-what-is-online-standards-development-osd) — helpdesk-docs.iso.org
2. [Online standards development (OSD) - IEC](https://iec.ch/online-standards-development) — iec.ch
3. [ISO/IEC Online Standards Development (OSD) Platform](https://www.ansi.org/osd/online-standards-development-platform) — ansi.org
4. [Online standards development at ISO and IEC - Supported by Fonto](https://www.fontoxml.com/case-study-online-standards-development/) — fontoxml.com
5. [OSD adoption by ISO committees and eligible projects](https://helpdesk-docs.iso.org/article/784-osd-adoption-by-iso-committes-and-eligible-projects) — helpdesk-docs.iso.org
6. [[PDF] April 2024 CCU meeting Report from IEC - BIPM](https://www.bipm.org/documents/20126/218156972/CCU-24-05_a++IEC+Report+to+the+CCU/5a6b8cfa-f2b7-9326-1a32-d9f6f77c3240) — bipm.org
7. [[PDF] Unlocking the potential of Smart Standards - IEC](https://www.iec.ch/system/files/2024-05/2024_iec_smart_pilots_a4_lr.pdf) — iec.ch
8. [IEC & ISO Information Model for SMART content - smartsdu.org](https://smartsdu.org/informationmodel) — smartsdu.org
9. [Digitally enhanced content - ISO](https://www.iso.org/smart) — iso.org
10. [ISO Standards Tag Set (ISOSTS) Resources](https://www.iso.org/schema/isosts/) — iso.org
11. [STS (Standards Tag Suite) | NISO website](https://www.niso.org/standards-committees/sts) — niso.org
12. [NISO STS Project Overview and Update - NCBI](https://www.ncbi.nlm.nih.gov/books/NBK350146/) — ncbi.nlm.nih.gov
13. [A Further Look at NISO and the Standards Tag Suite - SEMI.org](https://www.semi.org/en/standards-watch-2022-Sept/a-further-look-at-niso-and-the-standards-tag-suite) — semi.org
14. [NISO Standards Tag Suite (NISO STS) - Metadata Standards Index](https://msi.dublincore.org/standards/niso-sts) — msi.dublincore.org
