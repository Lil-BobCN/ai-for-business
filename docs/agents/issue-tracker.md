# 问题跟踪：GitHub

本仓库的问题和规格说明统一记录在 GitHub Issues 中。所有操作都使用 `gh` 命令行工具。

## 常用操作

- **创建问题**：`gh issue create --title "..." --body "..."`。正文有多行时，使用多行输入方式。
- **查看问题**：`gh issue view <编号> --comments`。需要筛选评论时使用 `jq`，同时获取标签。
- **列出问题**：`gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'`。根据任务补充合适的 `--label` 和 `--state` 条件。
- **评论问题**：`gh issue comment <编号> --body "..."`
- **添加或删除标签**：`gh issue edit <编号> --add-label "..."` 或 `gh issue edit <编号> --remove-label "..."`
- **关闭问题**：`gh issue close <编号> --comment "..."`

在仓库目录中运行命令时，`gh` 会根据 `git remote -v` 自动找到对应的 GitHub 仓库。

## 拉取请求是否参与分类

**拉取请求（PR）不作为需求入口。** 如果以后希望外部 PR 也按需求处理，把这里改成“是”；`/triage` 技能会读取这个设置。

设置为“是”后，PR 使用和问题相同的标签与状态，并改用对应的 `gh pr` 命令：

- **查看 PR**：使用 `gh pr view <编号> --comments` 查看内容和评论，使用 `gh pr diff <编号>` 查看改动。
- **列出需要分类的外部 PR**：运行 `gh pr list --state open --json number,title,body,labels,author,authorAssociation,comments`，只保留 `authorAssociation` 为 `CONTRIBUTOR`、`FIRST_TIME_CONTRIBUTOR` 或 `NONE` 的项目，排除 `OWNER`、`MEMBER` 和 `COLLABORATOR`。
- **评论、修改标签或关闭 PR**：分别使用 `gh pr comment`、`gh pr edit --add-label`、`gh pr edit --remove-label` 和 `gh pr close`。

GitHub 的问题和 PR 共用编号，所以 `#42` 可能表示其中任何一种。先运行 `gh pr view 42`，如果查不到，再运行 `gh issue view 42`。

## 技能要求“发布到问题跟踪系统”时

创建一个 GitHub Issue。

## 技能要求“获取相关任务”时

运行 `gh issue view <编号> --comments`。

## 大型任务探索操作

这部分供 `/wayfinder` 技能使用。

整个任务地图使用一个带有 `wayfinder:map` 标签的问题保存，其中包括“笔记”“已经做出的决定”和“仍不清楚的地方”。创建命令如下：

```powershell
gh issue create --label wayfinder:map
```

如果 GitHub 支持子问题，就把地图下面的任务建成子问题。如果不支持，就把子任务加入地图正文的任务清单，并在每个子问题正文开头写上 `Part of #<地图编号>`。

子问题使用 `wayfinder:<类型>` 标签。类型可以是 `research`、`prototype`、`grilling` 或 `task`。有人开始处理后，把这个问题分配给对应的开发者。

如果 GitHub 支持问题依赖，就用原生依赖关系记录阻塞。如果不支持，在子问题正文开头写：

```text
Blocked by: #<编号>, #<编号>
```

所有阻塞问题关闭后，这个问题才算可以开始。按照地图中的顺序，第一个仍然打开、没有阻塞、也没有分配负责人的子问题，就是下一项工作。

领取任务时运行：

```powershell
gh issue edit <编号> --add-assignee @me
```

完成任务后，把答案写进评论并关闭问题，再把相关说明追加到地图中“已经做出的决定”一节。

