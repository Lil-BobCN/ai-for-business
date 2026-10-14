#!/bin/sh
set -eu

app_state="$HOME/Library/Application Support/com.llmwiki.app/app-state.json"
mcp_entry="/Applications/LLM Wiki.app/Contents/Resources/mcp-server/dist/src/index.js"

token="$(jq -er '.apiConfig.token | select(type == "string" and length > 0)' "$app_state")"
exec env LLM_WIKI_API_TOKEN="$token" /opt/homebrew/bin/node "$mcp_entry"
