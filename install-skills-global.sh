#!/usr/bin/env bash
# Deixa caveman, ultracave e graphify valendo em TODOS os projetos do PC, com os ganchos extras.
# - caveman: plugin oficial (escopo de usuário) = skills caveman/ultracave/megacave e outras,
#   comandos /caveman-*, agentes cavecrew e ganchos SessionStart, SubagentStart, UserPromptSubmit e SessionEnd.
# - graphify: CLI + skill global; o gancho "sempre ativo" é por projeto (graphify claude install).
# - Regra de ativação em ~/.claude/CLAUDE.md como reserva, sem duplicar.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
command -v claude >/dev/null || { echo "Instale o Claude Code primeiro"; exit 1; }
command -v node >/dev/null || echo "Aviso: os ganchos da caveman precisam de Node.js; sem ele, só a regra do CLAUDE.md vale."

echo "==> caveman (plugin com ganchos, todos os projetos)"
claude plugin marketplace add JuliusBrussee/caveman || true
claude plugin install caveman@caveman || true
# Cópias antigas deste script em ~/.claude/skills duplicariam as skills do plugin.
rm -rf "$HOME/.claude/skills/caveman" "$HOME/.claude/skills/ultracave"
cfg="${XDG_CONFIG_HOME:-$HOME/.config}/caveman/config.json"
if [ ! -f "$cfg" ]; then
  mkdir -p "$(dirname "$cfg")"
  echo '{"defaultMode": "caveman"}' > "$cfg"
  echo "Modo inicial: caveman ($cfg). Troque para \"ultracave\" se quiser o modo máximo sempre."
fi

echo "==> graphify (CLI + skill em todos os projetos)"
if ! command -v graphify >/dev/null; then
  if command -v uv >/dev/null; then uv tool install graphifyy
  elif command -v pipx >/dev/null; then pipx install graphifyy
  else
    python3 -m venv "$HOME/.graphify-venv"
    "$HOME/.graphify-venv/bin/pip" install -U graphifyy
    mkdir -p "$HOME/.local/bin" && ln -sf "$HOME/.graphify-venv/bin/graphify" "$HOME/.local/bin/graphify"
  fi
fi
if command -v graphify >/dev/null; then
  graphify install --platform claude
else
  mkdir -p "$HOME/.claude/skills"
  rm -rf "$HOME/.claude/skills/graphify"
  cp -R "$here/.claude/skills/graphify" "$HOME/.claude/skills/graphify"
  echo "CLI do graphify não encontrada no PATH; copiei só a skill. Abra um terminal novo e rode: graphify install"
fi

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

echo
echo "Pronto. Vale a partir da próxima sessão do Claude Code, em qualquer pasta."
echo "Ganchos do graphify por projeto (opcional, rode dentro de cada projeto):"
echo "  graphify claude install   # consulta o grafo antes de ler arquivos e atualiza o CLAUDE.md do projeto"
echo "  graphify hook install     # reconstrói o grafo a cada git commit"
