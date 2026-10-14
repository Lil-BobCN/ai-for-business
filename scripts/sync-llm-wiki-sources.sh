#!/usr/bin/env bash
set -euo pipefail

# Keep the workspace's raw/ directory authoritative. LLM Wiki reads the
# derived copy under llm-wiki-project/raw/sources and writes only its own wiki.
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_root="$repo_root/raw"
project_root="$repo_root/llm-wiki-project"
target_root="$project_root/raw/sources"
mode="${1:---dry-run}"

if [[ "$mode" != "--dry-run" && "$mode" != "--apply" ]]; then
  printf '用法: %s [--dry-run|--apply]\n' "$0" >&2
  exit 2
fi

if [[ ! -d "$source_root" ]]; then
  printf '找不到源目录: %s\n' "$source_root" >&2
  exit 1
fi

mkdir -p "$target_root"

rsync_args=(
  -a
  --checksum
  --human-readable
  --itemize-changes
  --exclude '.DS_Store'
)

if [[ "$mode" == "--dry-run" ]]; then
  rsync_args+=(--dry-run)
else
  # A removed canonical source should also disappear from the derived import
  # tree. The canonical raw/ directory is never the rsync destination.
  rsync_args+=(--delete)
fi

rsync "${rsync_args[@]}" "$source_root/" "$target_root/"

if [[ "$mode" == "--dry-run" ]]; then
  printf '%s\n' '预览完成。确认变更后运行: scripts/sync-llm-wiki-sources.sh --apply'
else
  printf '%s\n' '同步完成。请在 LLM Wiki 的“资料源”中执行重新扫描或重新打开项目。'
fi
