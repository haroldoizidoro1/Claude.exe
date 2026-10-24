#!/usr/bin/env bash
# Instala no PC (Linux/macOS/WSL): claude-code-setup e, opcional, OmniRoute.
# Memória é só o CLAUDE.md (+ skills): nada de claude-mem, Headroom ou task-observer.
set -euo pipefail
command -v claude >/dev/null || { echo "Instale o Claude Code primeiro"; exit 1; }

echo "==> Plugin claude-code-setup"
claude plugin marketplace add anthropics/claude-plugins-official || true
claude plugin install claude-code-setup@claude-plugins-official || true

if [ "${1:-}" = "--omniroute" ]; then
  command -v node >/dev/null || { echo "Instale Node.js 20+ primeiro"; exit 1; }
  echo "==> OmniRoute (gateway local, opcional)"
  npm install -g omniroute
fi
echo "Pronto."
