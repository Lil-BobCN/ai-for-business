---
type: query
title: "Research: 核验 Semantica 的官方项目与当前 API"
created: 2026-10-12
origin: deep-research
tags: [research]
---

# Research: 核验 Semantica 的官方项目与当前 API

# 核验 Semantica 的官方项目与当前 API

## 结论摘要

本页汇总对 “Semantica” 官方项目归属与当前 API 形态的核验结果。基于现有五项来源，可以确认的要点如下：

1. Semantica 以 Python 包形式发布于 PyPI，版本为 0.7.0，基础安装命令为 `pip install semantica` [1][4]。
2. 其自我定位为“面向高风险、受监管领域的图原生基础设施（Graph-Native Infrastructure for Context and Accountable AI Systems）” [1][4]。
3. 已证实的公开 API 面较窄，仅见 `semantica.ontology` 模块（OWL 生成、SHACL 验证、SKOS 词表）[1]。
4. 来源 [3] 中列出的 REST／WebSocket 端点属于 feature request（#376）中的**提案**，不能当作“当前 API”使用。
5. 官方仓库存在两条互相竞争的线索：`semantica-agi/semantica` [1] 与 `Hawksight-AI/semantica` [2]，二者关系待核验。

### 来源证据一览

| 编号 | 来源 | 提供的信息 |
|-|-|-|
| [1] | GitHub 仓库 README（`semantica-agi/semantica`） | 定位、安装命令、`semantica.ontology` 模块、BibTeX 引用条目 |
| [2] | Docling 文档页（docling-project.github.io） | 指向 `Hawksight-AI/semantica` 的链接、联合安装命令 |
| [3] | GitHub feature request #376 | 提案中的 CLI 与全套 REST／WebSocket 端点、前端技术栈 |
| [4] | PyPI `semantica 0.7.0` | 版本号与与 [1] 一致的定位描述 |
| [5] | LinkedIn 帖“Introducing Semantica” | “开源语义层”定位表述 |

## 一、官方仓库的两条线索

| 线索 | 仓库 | 出现来源 | 相关证据 |
|-|-|-|-|
| A | `semantica-agi/semantica` | [1] | README 标题、BibTeX 引用条目、模块表 |
| B | `Hawksight-AI/semantica` | [2] | Docling 文档给出的 GitHub 链接 |

- 线索 A 的 README 与 PyPI 0.7.0 的页面描述完全一致（“Graph-Native Infrastructure for Context and Accountable AI Systems／Built for High-Stakes, Regulated Domains”）[1][4]，据此**推断** PyPI 包最可能对应 `semantica-agi/semantica`；但来源中未直接展示 PyPI 的项目主页链接，该推断待核验。
- 线索 B 仅出现在 Docling 文档页 [2]，无法判断它是旧仓库、镜像、还是另一同名项目。
- 两条线索的关系（改名、迁移、分叉或同名）在现有来源中没有任何说明，这是本次核验最大的未决问题。该问题与既有页面 [[semantica-评价与既有页面可能冲突]] 的口径校准直接相关。

## 二、PyPI 发行与安装方式

- 包名与版本：`semantica` 0.7.0 [4]。
- 基础安装：`pip install semantica` [1][4]。
- 带可选依赖安装：`pip install "semantica[all]" docling` [2]，说明存在 extras 分组机制；[3] 进一步提出 `semantica[explorer]` 这一 extras（仍属提案）。

## 三、当前 API 面的证据分级

### 3.1 已证实：Python 模块层

来源 [1] 的模块表至少列出：

- `semantica.ontology`：OWL 生成、SHACL 验证、SKOS 词表 [1]。

该表在来源摘录中被截断，仅显示这一行，其余模块未知。

### 3.2 已证实：安装层

- 模块化安装与 extras 机制 [2][3]。

### 3.3 提案中：CLI 与 REST API

来源 [3] 是一份 feature request（“Semantica Knowledge Explorer”，编号 #376），其中给出的 CLI 与 REST API 均标注为 “New … Required”，即尚未发布的规划。按类别整理如下：

| 类别 | 端点（提案） |
|-|-|
| 图探索 | `GET /api/graph/nodes`、`GET /api/graph/edges`、`GET /api/graph/node/{id}`、`.../neighbors`、`.../path`、`.../provenance`、`.../history` |
| 搜索与分析 | `POST /api/graph/search`、`GET /api/graph/analytics`、`GET /api/graph/validation` |
| 决策 | `GET /api/decisions`、`GET /api/decisions/{id}`、`.../chain`、`.../precedents`、`.../compliance` |
| 时序 | `GET /api/temporal/snapshot`、`GET /api/temporal/diff`、`GET /api/temporal/patterns` |
| 富化 | `POST /api/enrich/extract`、`POST /api/enrich/links`、`POST /api/enrich/dedup`、`POST /api/reason` |
| 导入／导出 | `POST /api/import`、`POST /api/export` |
| 注解 | `GET/POST /api/annotations`、`DELETE /api/annotations/{id}` |
| WebSocket | `WS /ws/graph-updates`（导入进度、图变更推送） |

配套提案还包括 CLI 命令（`semantica-explorer --graph my_graph.json --port 8000`，后文示例中省略了 `--port`）以及前端技术栈（React 18 + TypeScript）[3]。

值得注意：`/api/decisions/*`（chain、precedents、compliance）与 `.../provenance`、`.../history` 等端点，与 [1][4] 中 “Accountable AI”“受监管领域”的定位互相呼应，说明可审计性是该项目宣称的核心方向；但由于这些端点均处于提案阶段，目前只能视为路线图信号，而非可用能力。

## 四、引用与作者元数据

来源 [1] 给出的 BibTeX 条目为：作者 Mohammad Kaif，年份 2026，URL 指向 `semantica-agi/semantica`。年份 “2026” 与 PyPI 版本仍处于 0.7.0 早期阶段的判断存在张力，该年份可能是占位符或预填值，待核验 [1][4]。

## 五、与 Docling 生态的关系

Docling 文档站收录了 Semantica 页面 [2]，并给出 `pip install "semantica[all]" docling` 的联合安装命令。可推测二者存在“文档解析—语义化”方向的集成关系（Semantica 借助 Docling 解析文档），但来源未展示集成代码或所在章节性质，具体关系待核验。

## 六、产品定位口径

| 口径 | 出处 | 表述 |
|-|-|-|
| 图原生基础设施 | [1][4] | “Graph-Native Infrastructure for Context and Accountable AI Systems”，面向高风险、受监管领域 |
| 语义层／语义智能平台 | [5] | “Open-Source Semantic Layer for AI”，弥合原始数据与 AI-ready 知识之间的差距 |

[5] 的 LinkedIn 帖未给出仓库或包名，无法确认其所指与 [1][4] 是同一产品；若为另一同名项目，需要在 wiki 中做消歧。此点与 [[semantica-评价与既有页面可能冲突]] 的评价校验直接相关。

## 七、与既有 wiki 页面的关联

- [[semantica-评价与既有页面可能冲突]]：本页的仓库归属与 API 证据分级可用于校准该页对 Semantica 的描述与评价。
- [[ontology-是操作层还是知识图谱]]、[[本体操作层与知识图谱口径一致性待核验]]：Semantica 的 `semantica.ontology` 同时覆盖 OWL 生成（建模产物）与 SHACL 验证（约束校验），为本体“是操作层还是知识图谱”之争提供了一个工具链样本。
- [[owl-rdf语义建模]]：该概念页可与 Semantica 的 OWL／SHACL／SKOS 模块对照。
- [[gb-t-48000-3-2026-本体建模要求]]、[[标准本体]]、[[gb-t-xxxx-标准知识图谱-第1部分]]、[[gb-t-42131-2022-人工智能-知识图谱技术框架]]：国内标准对本体建模与知识图谱实现指南的要求，可作为与 Semantica 工具链的对照系。
- [[palantir-foundry写回与权限审计能力待核验]]：与 Semantica 提案中的决策链、合规、溯源端点同属“可审计／可追责”主题，且同样处于待核验状态。
- 若需把提案端点与国内语义知识库接口分层对照，可参考 [[标准语义知识库数据接口总体框架]] 与 [[基础接口与高级接口]]（对照方向，来源中尚无直接可比数据）。

## 八、矛盾与缺口清单

1. **仓库归属矛盾**：`semantica-agi/semantica` [1] 与 `Hawksight-AI/semantica` [2] 并存，无来源解释二者关系。
2. **API 状态混淆风险**：[3] 的端点清单极易被误读为“当前 API”，实际为开放中的 feature request。
3. **年份异常**：BibTeX 年份为 2026 [1]，与 PyPI 0.7.0 的版本阶段存在张力。
4. **同名歧义**：[5] 的 “Semantica” 是否与 [1][4] 为同一项目无法确认。
5. **信息缺口**：五项来源均未提供许可证、维护者团队、变更日志、官方文档站、依赖清单等基础元数据；[1] 的模块表也被截断，无法确认除 `semantica.ontology` 外的其他模块。

## 九、建议补充的来源

- PyPI 项目页完整元数据：作者、发布历史、依赖、项目主页 URL（用于确认 PyPI 包与哪个 GitHub 仓库绑定）。
- 两个候选仓库的完整 README、LICENSE、release／tag 与提交历史（用于判断迁移方向与官方性）。
- #376 issue 所属仓库及其状态（open／closed、是否已合并、相关 PR）。
- Docling 官方文档中 Semantica 页面所属章节（集成列表、生态页还是示例），以及其中对指向仓库的说明。
- 若 [5] 指向另一项目，收集其官网／仓库链接，用于建立消歧页。

## References

1. [Graph-Native Infrastructure for Context and Accountable AI Systems · GitHub](https://github.com/semantica-agi/semantica) — github.com
2. [Semantica - Docling - GitHub Pages](https://docling-project.github.io/docling/integrations/semantica/) — docling-project.github.io
3. [[Feature] Semantica Knowledge Explorer — Interactive Dashboard ...](https://github.com/Hawksight-AI/semantica/issues/376) — github.com
4. [semantica - PyPI](https://pypi.org/project/semantica/) — pypi.org
5. [Introducing Semantica: Open-Source Semantic Layer for AI - LinkedIn](https://www.linkedin.com/posts/mohd-kaif-2055a61a9_graphanalytics-contextengineering-knowledgegraphs-activity-7412385915882536962-pnbO) — linkedin.com
