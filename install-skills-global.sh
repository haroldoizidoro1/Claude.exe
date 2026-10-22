#!/usr/bin/env bash
# Instala caveman, ultracave e graphify para TODOS os projetos (~/.claude/skills)
# e acrescenta a regra de ativação em ~/.claude/CLAUDE.md, sem duplicar.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
dst="$HOME/.claude/skills"
mkdir -p "$dst"
for s in caveman ultracave graphify; do
  rm -rf "${dst:?}/$s"
  cp -R "$here/.claude/skills/$s" "$dst/$s"
  echo "skill $s -> $dst/$s"
done

md="$HOME/.claude/CLAUDE.md"
mark="<!-- skills-sempre-ativas -->"
touch "$md"
if grep -qF "$mark" "$md"; then
  echo "Regra já presente em $md"
else
  cat >> "$md" <<'EOF'

<!-- skills-sempre-ativas -->
## Skills sempre ativas (caveman, ultracave, graphify)
- caveman: ative na primeira resposta de toda sessão e mantenha até "stop caveman" ou "normal mode". Responda no idioma do usuário.
- ultracave: troque a caveman por ela quando o usuário pedir `/ultracave` ou `/caveman ultra`.
- graphify: em perguntas sobre código, arquitetura ou conteúdo de um projeto, consulte `graphify-out/` primeiro quando existir; se não existir, ofereça `/graphify .` antes de rodar (gasta tokens).
EOF
  echo "Regra adicionada em $md"
fi
echo "Pronto. Vale a partir da próxima sessão do Claude Code."
