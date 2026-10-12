#!/usr/bin/env bash
# Instala no PC (Linux/macOS/WSL): OmniRoute, Headroom, claude-mem, claude-code-setup, task-observer.
# Só instala. Não altera ANTHROPIC_BASE_URL nem redireciona o tráfego do Claude Code.
set -euo pipefail
command -v node >/dev/null || { echo "Instale Node.js 20+ primeiro"; exit 1; }
command -v claude >/dev/null || { echo "Instale o Claude Code primeiro"; exit 1; }

echo "==> OmniRoute (gateway local, porta 20128)"
npm install -g omniroute

echo "==> Headroom (compressão de contexto)"
if command -v pipx >/dev/null; then
  pipx install --force "headroom-ai[mcp,code]"
else
  python3 -m venv ~/.headroom-venv
  ~/.headroom-venv/bin/pip install -U "headroom-ai[mcp,code]"
  mkdir -p ~/.local/bin && ln -sf ~/.headroom-venv/bin/headroom ~/.local/bin/headroom
fi
headroom mcp install || echo "(rode 'headroom mcp install' manualmente se falhou)"

echo "==> Plugins do Claude Code"
claude plugin marketplace add thedotmack/claude-mem || true
claude plugin install claude-mem@thedotmack || true
claude plugin marketplace add anthropics/claude-plugins-official || true
claude plugin install claude-code-setup@claude-plugins-official || true
claude plugin marketplace add rebelytics/one-skill-to-rule-them-all || true
claude plugin install task-observer@one-skill-to-rule-them-all || true

echo "Pronto. Inicie o gateway com: omniroute  (dashboard em http://localhost:20128)"
