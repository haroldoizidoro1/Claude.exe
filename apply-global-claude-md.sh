#!/usr/bin/env bash
# Instala global/CLAUDE.md em ~/.claude/CLAUDE.md. Faz backup se já existir e for diferente.
set -euo pipefail
src="$(cd "$(dirname "$0")" && pwd)/global/CLAUDE.md"
dst="$HOME/.claude/CLAUDE.md"
mkdir -p "$HOME/.claude"
if [ -f "$dst" ] && ! cmp -s "$src" "$dst"; then
  cp "$dst" "$dst.bak.$(date +%s)"
  echo "Backup do arquivo anterior criado."
fi
cp "$src" "$dst"
echo "Regras globais instaladas em $dst"
