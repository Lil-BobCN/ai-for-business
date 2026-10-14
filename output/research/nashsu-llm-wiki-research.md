# nashsu/llm_wiki 一手资料研究

> 研究对象：<https://github.com/nashsu/llm_wiki>
>
> 固定证据版本：`main` 在 2026-10-11 的浅克隆，提交 `48fd970e206a02a6d2028d1dbfc41b7a0345bf0b`（提交日期 2026-09-28，提交信息 `fix: verify notarized app inside macOS DMG`）。
>
> 证据等级：以下“已验证事实”来自该提交的 README、TypeScript/Rust 源码或 MCP README；“未验证项”是仓库文档的声明但本次没有真实运行或独立测量；“适配风险”是将这些能力用于当前仓库时的工程判断，不是上游承诺。

## 结论先行

- `llm_wiki` 是 Tauri v2 桌面应用（React/TypeScript 前端 + Rust 后端），以文件系统项目为主：`raw/sources/` 保存来源，`wiki/` 保存 LLM 生成的 Markdown 知识页，`schema.md` 和 `purpose.md` 约束生成方向。README 的架构描述为 Raw Sources → Wiki → Schema。
- 当前仓库的 `raw/` 有 34 个文件（33 个 Markdown、1 个 JSON），分布在 3 个中文专题目录；仓库根目录目前没有 `purpose.md`、`schema.md`、`wiki/` 或 `raw/sources/`。因此不能把仓库根目录直接当作 LLM Wiki 项目打开。研究完成时另见准备中的 `llm-wiki-project/`：已有 `purpose.md`、`schema.md` 和 `raw/sources/` 来源副本，但核验时尚无 `wiki/`，仍需补全项目结构。
- 上游的最小可行流程是：安装桌面应用或源码构建 → 新建项目并选择模板 → 在 Settings 配置 Chat/Ingest LLM → Sources 导入文件 → 等待两阶段 ingest → Chat 查询/Graph 查看 → 定期 Lint 和 Review。
- Deep Research 需要一个 LLM 和已配置的 Web Search/AnyTXT 来源。源码当前将合成结果直接写成 `wiki/queries/*.md`，然后在启用 embedding 时直接建立向量索引；源码注释明确避免把结果再送回 source ingest。README 中仍写着“auto-ingest”，该表述与固定提交源码不一致，应以源码为准。
- MCP/Codex 集成是本机 HTTP API + stdio MCP 的桥接：桌面应用必须运行并开启 API/MCP，MCP 不直接扫描文件夹。README 的工具列表漏列源码已实现的 `llm_wiki_embed_page` 和 `llm_wiki_write_page`；后者默认拒绝覆盖，只有显式 `allow_overwrite: true` 才能替换已有页。

## 已验证事实

### 1. 产品边界与数据模型

1. README 将应用定义为跨平台桌面个人知识库：LLM 读取文档、持续生成和维护 interlinked wiki；三层结构是 Raw Sources（不可变来源）→ Wiki（LLM 生成）→ Schema（规则与配置）。核心文件约定包含 `wiki/index.md`、`wiki/log.md`、YAML frontmatter 和 `[[wikilink]]`。来源：[README.md#What-We-Kept-from-the-Original](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/README.md#what-we-kept-from-the-original)，第 69-80 行。
2. 新建项目的 Rust 命令会创建 `raw/sources`、`raw/assets`、`wiki/entities`、`wiki/concepts`、`wiki/sources`、`wiki/queries`、`wiki/comparisons`、`wiki/synthesis`，并写入 `schema.md`、`purpose.md`、`wiki/index.md`、`wiki/log.md`、`wiki/overview.md` 和 `.obsidian/` 配置。来源：[src-tauri/src/commands/project.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/project.rs#L16-L235)，第 16-235 行。
3. `schema.md` 的默认页类型为 entity、concept、source、query、comparison、synthesis；页面要求 YAML frontmatter，source 页面另含 authors/year/url/venue。来源：[src-tauri/src/commands/project.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/project.rs#L41-L117)，第 41-117 行；模板实现也在 [src/lib/templates.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/templates.ts#L11-L67)，第 11-67 行。
4. 桌面创建流程先调用 Rust `create_project`，再写入所选模板的 `schema.md`、`purpose.md` 和额外目录，并持久化项目语言选择。来源：[src/components/project/create-project-dialog.tsx](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/components/project/create-project-dialog.tsx#L99-L134)，第 99-134 行；[src/commands/fs.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/commands/fs.ts#L248-L258)，第 248-258 行。

### 2. 安装、启动与初始化

1. 发布版可从 GitHub Releases 获取：macOS Apple Silicon `.dmg`、Windows `.msi`、Linux `.deb`/`.AppImage`。源码构建要求 Node.js 20+、Rust 1.88+、`protoc`；步骤是 `npm install`、`npm --prefix mcp-server ci && npm run mcp:build`、`npm run tauri dev` 或 `npm run tauri build`。来源：[README.md#Installation](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/README.md#installation)，第 396-418 行。
2. 快速开始顺序是新建项目并选模板 → Settings 配置 LLM provider（API key + model）→ 可选配置 Web Search 和 source folder watch → Sources 导入 PDF/DOCX/MD 等 → Activity Panel 观察构建 → Chat 查询 → Graph 查看 → Review 处理人工判断项 → 定期 Lint。来源：[README.md#Quick-Start](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/README.md#quick-start)，第 428-438 行。
3. 桌面设置通过 Tauri Store 保存到全局 `app-state.json`：LLM 配置键是 `llmConfig`，provider 配置是 `providerConfigs`，Chat/Ingest 路由是 `taskModelRouting`，项目级覆盖是 `projectLlmOverrides`，Web Search 是 `searchApiConfig`，向量配置是 `embeddingConfig`。来源：[src/lib/project-store.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/project-store.ts#L8-L18)，第 8-18 行；[src/lib/project-store.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/project-store.ts#L44-L180)，第 44-180 行。

### 3. 导入与两阶段 Ingest

1. README 声称 ingest 是两次顺序 LLM 调用：第一步分析实体、概念、论点、连接、矛盾和结构建议；第二步生成 source summary、entity/concept 页面、`index.md`、`log.md`、`overview.md`、Review items 和 Deep Research 搜索查询。来源：[README.md#3-two-step-chain-of-thought-ingest](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/README.md#3-two-step-chain-of-thought-ingest)，第 106-123 行。
2. ingest 支持 SHA256 增量缓存（未变化来源自动跳过）、持久化串行队列、失败最多自动重试 3 次、递归文件夹导入、`raw/sources/` 外部变更 watch、生成页的 `sources: []` 追溯字段，以及可选的 ingest 后 embedding。来源：[README.md#3-two-step-chain-of-thought-ingest](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/README.md#3-two-step-chain-of-thought-ingest)，第 125-136 行；缓存/队列文件由源码使用 `.llm-wiki/ingest-cache.json`、`.llm-wiki/ingest-queue.json`，见 [src/lib/ingest-cache.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/ingest-cache.ts#L1-L35) 和 [src/lib/ingest-queue.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/ingest-queue.ts#L90-L110)。
3. 当前导入生命周期先检查规则/格式/大小和敏感配置文件，再逐文件 `copyFile` 到项目 `raw/sources/`；文件夹导入保留相对路径、按自然顺序排队，并禁止选择项目本身或项目内目录作为导入源。因此导入会复制来源，不会回写选中的原始目录。来源：[src/lib/source-lifecycle.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/source-lifecycle.ts#L315-L445)，第 315-445 行。
4. ingest 成功后才写入缓存；如果生成被截断、写文件失败或未完成，任务保持 error/retry 状态，可能保留部分文件但不缓存为完成。来源：[src/lib/ingest.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/ingest.ts#L1481-L1560)，第 1481-1560 行。
5. 当前源码的 source summary 会在图片 caption 后重新写入并可重新 embedding；如果 summary 缺失会写入最小 source stub。来源：[src/lib/ingest.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/ingest.ts#L3400-L3448)，第 3400-3448 行。
6. 删除来源具有级联清理：删除 source summary、清理共享实体的 `sources[]`、从 index 移除、清理指向已删页的 wikilink。来源：[README.md#16-file-deletion-with-cascade-cleanup](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/README.md#16-file-deletion-with-cascade-cleanup)，第 337-345 行。对当前 raw 的含义是：先用副本导入并确认来源身份规则，避免把原始资料和生成页混在一起后再执行删除。

### 4. 查询、检索和向量配置

1. Rust 搜索入口扫描项目 `wiki/` 下 Markdown，默认按 `top_k` 限制（代码将请求值 clamp 到内部 `MAX_RESULTS`），最多扫描 10,000 个 Markdown 文件；结果包括关键词命中、可选向量命中和图邻居命中。来源：[src-tauri/src/commands/search.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/search.rs#L20-L60)，第 20-60 行；[src-tauri/src/commands/search.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/search.rs#L327-L495)，第 327-495 行。
2. 中文查询会做 CJK bigram 和单字 token 化，并去掉中英文停用词；因此当前仓库中文标题/正文具备基本词法支持，但质量仍取决于生成页是否保留中文实体和 wikilink。来源：[src-tauri/src/commands/search.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/search.rs#L995-L1065)，第 995-1065 行。
3. 向量检索是可选的，配置包括 `enabled`、OpenAI-compatible embedding endpoint、API key、model、分块大小/重叠、批量和额外 headers；默认关闭。来源：[src/stores/wiki-store.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/stores/wiki-store.ts#L128-L162)，第 128-162 行；默认值见 [src/stores/wiki-store.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/stores/wiki-store.ts#L594-L599)，第 594-599 行。
4. 有向量配置时，搜索先从 LanceDB 取向量结果，再和关键词结果做 RRF 融合；向量失败会回退到关键词结果；之后把图邻居按 15%-30% 的配额混入最终结果，最多使用 20 个 seed。来源：[src-tauri/src/commands/search.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/search.rs#L434-L494)，第 434-494 行；图配额见 [src-tauri/src/commands/search.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/search.rs#L541-L634)，第 541-634 行。

### 5. Deep Research

1. Web Search 支持 Tavily、SerpApi、SearXNG，以及源码当前额外支持 Brave、Bocha、Ollama、Firecrawl；Tavily/SerpApi/Brave/Bocha/Ollama 需要 API key，SearXNG 需要实例 URL，Firecrawl 被视为免 key 来源。来源：[src/stores/wiki-store.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/stores/wiki-store.ts#L63-L126)，第 63-126 行；配置校验见 [src/lib/web-search.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/web-search.ts#L110-L161)，第 110-161 行。
2. Deep Research 可使用 Web、AnyTXT 或 both。每个非空查询调用 Web Search（每条最多 5 个结果），AnyTXT 一次最多请求 15 个结果；所有调用用 `Promise.allSettled`，按 URL/来源+标题+snippet 去重，候选来源总数上限为 `MAX_RESEARCH_SOURCES = 20`，并通过相关性过滤。来源：[src/lib/deep-research.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/deep-research.ts#L16-L18)，第 16-18 行；收集流程见 [src/lib/deep-research.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/deep-research.ts#L403-L482)，第 403-482 行。
3. 合成阶段把搜索结果编号后传给 LLM，系统提示要求用已有 `wiki/index.md` 的 `[[wikilink]]`、`[N]` 引用、指出矛盾/空白、使用中立百科语气。输出先验证，随后写入 `wiki/queries/<date/topic>-<task>.md`，只保存合成中实际引用的来源。来源：[src/lib/deep-research.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/deep-research.ts#L569-L675)，第 569-675 行。
4. 研究页保存后会刷新文件树；若 embedding 开启且有 model，则直接对该 query page 建索引。源码明确说明研究结果已经是生成的 wiki page，避免再走 source ingest，否则会产生第二份 summary 和递归 Review 噪声。来源：[src/lib/deep-research.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/deep-research.ts#L677-L711)，第 677-711 行。

### 6. 模型、MCP、Codex 与本地 API

1. LLM 配置 provider 类型包含 OpenAI、Anthropic、Google、Azure、Ollama、Custom、MiniMax、Claude Code、Codex CLI；配置包含 API key、model、Ollama URL、Custom endpoint、最大上下文字符数、reasoning、ingest reasoning、请求超时、streaming 和自定义 headers。Chat 与 Ingest 可以按 task 路由到不同 preset，项目可有覆盖。来源：[src/stores/wiki-store.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/stores/wiki-store.ts#L27-L61)，第 27-61 行；[src/lib/llm-task-routing.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/llm-task-routing.ts#L40-L70)，第 40-70 行。
2. README 声称本地 API 在 `http://127.0.0.1:19828`，默认 token 保护且仅监听本机；端点包括 health、projects、files/content、reviews、hybrid search、chat、graph、source rescan 和 page embed。来源：[README.md#Local-HTTP-API--MCP-Server--AI-Agent-Skill](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/README.md#local-http-api--mcp-server--ai-agent-skill)，第 440-458 行。
3. MCP server 不直接扫描项目目录，也不复制搜索/图谱逻辑；每个工具调用 `127.0.0.1:19828/api/v1`，继承桌面应用的 project registry、文件权限、search/graph backend 和 Source Watch 规则。要求 Node.js 20+、桌面应用运行、Settings 开启 local HTTP API 与 MCP access，并允许无 token 或设置 `LLM_WIKI_API_TOKEN`。来源：[mcp-server/README.md](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/mcp-server/README.md#requirements)，第 1-20 行。
4. MCP 构建/运行是 `cd mcp-server && npm install && npm run build`，再以 `LLM_WIKI_API_TOKEN=... node dist/src/index.js` 启动；客户端配置把 command 指向绝对路径的 `mcp-server/dist/src/index.js`。来源：[mcp-server/README.md](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/mcp-server/README.md#build)，第 21-49 行。
5. MCP 源码工具包含 status、projects、set_project、files、read_file、reviews、search、chat、graph、rescan、embed_page 和 write_page；`read_file` 通过 API 只允许公开项目路径，例如 `wiki/` 和 `raw/sources/`；write page 必须在 `wiki/` 下，默认不允许覆盖，成功还会进行字节级持久化验证。来源：[mcp-server/src/index.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/mcp-server/src/index.ts#L35-L204)，第 35-204 行。
6. README 提供现成 skill：`npx skills add https://github.com/nashsu/llm_wiki_skill.git --skill llm-wiki`，说明其面向 Claude Code/Codex/兼容 skills runtime，默认只读并返回 wiki page 路径供核验。来源：[README.md#Plug-your-AI-agent-in-with-one-command](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/README.md#plug-your-ai-agent-in-with-one-command)，第 460-472 行。skill 仓库本身本次未固定提交、未独立核查，见“未验证项”。
7. Codex CLI provider 不是远程 API：Rust 后端探测本机 `codex` 命令，并以固定的 `codex exec --json` 子进程运行，把重建后的 prompt 经 stdin 发送、解析 JSONL `item.completed`/`agent_message` 事件并流回 UI；默认超时 10 分钟，可配置范围 1-240 分钟。来源：[src-tauri/src/commands/codex_cli.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/codex_cli.rs#L1-L43)，第 1-43 行；[src-tauri/src/commands/codex_cli.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/codex_cli.rs#L136-L215)，第 136-215 行；解析与前端传输见 [src/lib/codex-cli-transport.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/codex-cli-transport.ts#L1-L33)，第 1-33 行。

### 7. 备份、迁移和限制

1. ZIP 导出会递归打包项目目录（跳过根目录和符号链接），目标必须是项目目录之外的绝对路径。来源：[src-tauri/src/commands/project_maintenance.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/project_maintenance.rs#L134-L190)，第 134-190 行。
2. ZIP 导入要求绝对路径、归档最多 100,000 条目、展开后最多 4 GiB、禁止符号链接和非普通相对路径、必须含 `wiki/index.md`，目标目录必须为空。来源：[src-tauri/src/commands/project_maintenance.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/project_maintenance.rs#L7-L17)，第 7-17 行；[src-tauri/src/commands/project_maintenance.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/project_maintenance.rs#L204-L266)，第 204-266 行。
3. “Rebuild Wiki index”从页面 frontmatter 的 type/title 重建 `wiki/index.md`，按类型分组和标题排序；因此外部手工修改 wiki 页后可重建索引，但这不是对原始来源的恢复。来源：[src-tauri/src/commands/project_maintenance.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/project_maintenance.rs#L269-L355)，第 269-355 行。
4. 迁移 ZIP 会包含隐藏项目状态；源码测试确认 `.llm-wiki/ingest-cache.json` 可随归档 round-trip。来源：[src-tauri/src/commands/project_maintenance.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/project_maintenance.rs#L52-L78)，第 52-78 行。
5. README 列出数据目录：`purpose.md`、`schema.md`、`raw/sources`、`raw/assets`、`wiki`（含 entities/concepts/sources/queries/synthesis/comparisons）、`.obsidian` 和 `.llm-wiki`。来源：[README.md#Project-Structure](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/README.md#project-structure)，第 475-493 行。
6. 项目向量库在 `<project>/.llm-wiki/lancedb`；聊天列表在 `.llm-wiki/conversations.json`、每个对话在 `.llm-wiki/chats/<id>.json`，聊天保存每次只保留最近 100 条并剥离图片 payload。全局设置则在 Tauri app-data 目录的 `app-state.json`，应用 identifier 为 `com.llmwiki.app`，不在项目目录内，因此“项目 ZIP”与“全局模型/API 凭据设置”需要分别处理。来源：[src-tauri/src/commands/vectorstore.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/vectorstore.rs#L48-L50)，第 48-50 行；[src/lib/persist.ts](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/persist.ts#L79-L111)，第 79-111 行；[src-tauri/src/api_server.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/api_server.rs#L734-L737)，第 734-737 行；[src-tauri/tauri.conf.json](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/tauri.conf.json#L3-L5)，第 3-5 行。

## 当前仓库 raw 的适配评估

### 已确认的当前仓库状态

- 当前仓库根目录没有 `purpose.md`、`schema.md`、`wiki/`、`raw/sources/`；只有 `raw/`、`output/`、`tools/`、`docs/` 等目录。
- 研究完成时只读核验了 `llm-wiki-project/` 容器：已有 `purpose.md`、`schema.md`、`raw/sources/` 及来源副本，但尚无 `wiki/` 和 `wiki/index.md`。这说明项目准备已开始；本报告没有创建或修改该容器，容器状态可能被并行主任务继续更新。
- `raw/` 共 34 个文件：33 个 `.md` 和 1 个 `.json`。内容集中于三个中文专题目录：FDE/Ontology 课程逐集稿、Ontology AI Coding 参考资料、`零点未来：AI+企业` 系列稿。
- 文件名含中文、全角标点、空格和较长标题；源码宣称已处理 Unicode-safe string handling 和路径规范化，但本次没有对这些具体文件进行真实导入运行测试。

### 推荐适配路径（最小风险）

1. 使用独立项目容器（当前已有准备中的 `llm-wiki-project/`），补全 `wiki/` 与 `wiki/index.md` 后再用 LLM Wiki 打开；或在应用中新建项目并选择 `Research`/`Business` 模板。不要直接把当前仓库根目录当作项目打开，因为 open-project 校验要求存在 `schema.md` 和 `wiki/`。来源：[src-tauri/src/commands/project.rs](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src-tauri/src/commands/project.rs#L342-L363)，第 342-363 行。
2. 将 `raw/` 下三组资料复制或通过 Sources 的文件夹导入放入新项目的 `raw/sources/`，保留子目录以利用 folder context。不要移动/改写原始仓库的 `raw/`，因为上游把来源当作不可变层，且删除来源会触发级联清理。
3. 先配置中文输出语言、Chat 模型和 Ingest 模型，再小批量导入（例如先导入索引和 1-2 集）验证 source summary、来源路径、中文输出和 wikilink；确认后再批量导入全部 34 个文件。
4. 初始阶段可关闭 embedding，以降低 endpoint 配置和成本风险；关键词 + CJK token + 图扩展已可工作。需要语义检索时再配置 OpenAI-compatible embedding endpoint/model，并在生成页稳定后建立向量索引。
5. Deep Research 只在已有一个可用 LLM 且配置 Web Search（或本地 AnyTXT）后启用。把上游抓取结果视作新的 `wiki/queries` 生成页，并人工检查 `[N]` 引用与 `[[wikilink]]`，不能把它当作原始资料的替代品。

### 对本仓库的主要风险

- **目录边界风险（高）**：当前 raw 不是 LLM Wiki 项目结构；若直接打开会被 `schema.md`/`wiki/` 校验拒绝。必须创建独立项目或先补齐结构；补齐根目录会改变仓库语义，不建议未经单独决策直接做。
- **生成污染风险（中高）**：上游会在导入后写入 wiki 页面、index/log/overview、cache/queue 等状态；应把生成物放在新项目或明确的 `llm-wiki-project/`，不要写回现有 `raw/`。
- **中文长文件与上下文成本（中）**：课程稿和参考资料较长，单次两阶段 ingest 可能触发上下文、超时或输出截断；应分批导入并观察 Activity Panel 的 error/retry。源码虽有 checkpoint，但不能替代分批策略。
- **同质内容与重复实体（中）**：多个系列重复解释 Ontology、RAG、Agent、Knowledge Graph，LLM 可能生成大量重复页或 Review items；需要先定义 schema/purpose 的实体粒度，并定期 Lint/Review。
- **证据边界风险（中高）**：Deep Research 会把搜索摘要交给 LLM 合成；即使保存 `[N]`，也需要人工核对外部 URL、矛盾和引用范围。当前仓库的 raw 是课程讲稿/整理资料，不能自动升级为一手事实。
- **权限与写入风险（中）**：MCP/API 是本机服务但可读写 wiki 页；启用 `llm_wiki_write_page` 或 Codex skill 时，应默认只读，写入仅限新项目且显式允许覆盖。
- **备份误解风险（中）**：ZIP 迁移保存项目目录和 `.llm-wiki` 状态，但不会替代 Git/外部备份，也不应把生成 wiki 当作原始 raw 的唯一副本；当前 raw 仍应由仓库版本控制保护。

## 未验证项与验证方式

- **未运行桌面应用/CLI**：当前环境没有针对 macOS Tauri GUI 的真实启动、创建项目、导入、查询、Deep Research 或 MCP 端到端测试。本报告只验证了源码路径。验证方式：安装发布版或满足 Node/Rust/protoc 后执行 README 的 build/run，并在隔离临时项目中导入 1 个中文 Markdown。
- **未独立验证模型供应商兼容性**：代码声明支持 OpenAI、Anthropic、Google、Azure、Ollama、Custom、MiniMax、Claude Code、Codex CLI，但没有对每个 provider 的真实 API、reasoning、streaming 或中文质量测量。验证方式：为目标 provider 配置最小凭据，运行 connection test 和单文件 ingest。
- **未验证 Deep Research provider 的实时返回质量、抓取完整性和收费**：源码验证了配置校验、并发收集、去重、过滤与写入；网络搜索的实际结果、限流和费用取决于供应商。验证方式：在小项目运行一个明确主题，记录请求、来源数、失败和生成页引用。
- **未验证 `llm_wiki_skill` 外部仓库**：README 给出了安装命令和触发纪律，但 skill 仓库未固定提交、未查看其实现。验证方式：锁定 skill commit，审查其只读/写入工具映射后再在 Codex 隔离环境安装。
- **未验证大规模性能上限**：搜索源码最多扫描 10,000 个 Markdown 文件，导入/图/向量实际容量没有本次基准；当前 raw 仅 34 个文件，不能外推到更大规模。
- **未验证中文文件名跨平台完整链路**：源码测试和注释显示有 Unicode/path normalization 处理，但没有在本机对本仓库全部长中文路径做真实 import/export round-trip。

## README 与源码差异记录

- README 第 46 行写 Deep Research 会“auto-ingest results into wiki”；固定提交的 [src/lib/deep-research.ts#L689-L711](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/src/lib/deep-research.ts#L689-L711) 明确研究页直接写到 `wiki/queries` 并直接 embedding，避免重新走 source ingest。本文按源码记录为当前行为。
- README 第 53、444-458 行概述了 API/MCP 端点，但未完整列出源码的 `llm_wiki_embed_page` 和 `llm_wiki_write_page`；工具定义见 [mcp-server/src/index.ts#L165-L204](https://github.com/nashsu/llm_wiki/blob/48fd970e206a02a6d2028d1dbfc41b7a0345bf0b/mcp-server/src/index.ts#L165-L204)。本文把源码工具作为已验证事实，并把写入风险纳入适配评估。

## 研究边界

本次只做了上游 GitHub 仓库的浅克隆、文件读取、静态检索和当前工作区 `raw/` 只读盘点；没有修改 `raw/`，没有启动上游应用，没有写入上游项目目录，也没有执行删除、覆盖或迁移命令。
