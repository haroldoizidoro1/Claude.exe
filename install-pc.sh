#!/usr/bin/env bash
# Instala no PC (Linux/macOS/WSL): claude-code-setup, task-observer, harness-engineering e, opcional, OmniRoute.
# Memória é só o CLAUDE.md (+ skills): nada de claude-mem ou Headroom.
set -euo pipefail
command -v claude >/dev/null || { echo "Instale o Claude Code primeiro"; exit 1; }

echo "==> Plugin claude-code-setup"
claude plugin marketplace add anthropics/claude-plugins-official || true
claude plugin install claude-code-setup@claude-plugins-official || true

echo "==> Plugin task-observer"
claude plugin marketplace add rebelytics/one-skill-to-rule-them-all || true
claude plugin install task-observer@one-skill-to-rule-them-all || true

echo "==> Plugin harness-engineering (só as skills; nada é alterado até você rodar /setup)"
claude plugin marketplace add jrenaldi79/harness-engineering || true
claude plugin install harness-engineering@harness-engineering || true

if [ "${1:-}" = "--omniroute" ]; then
  command -v node >/dev/null || { echo "Instale Node.js 20+ primeiro"; exit 1; }
  echo "==> OmniRoute (gateway local, opcional)"
  npm install -g omniroute
fi
echo "Pronto."
