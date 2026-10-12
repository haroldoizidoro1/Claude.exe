#!/usr/bin/env bash
# Mescla global-permissions.json em ~/.claude/settings.json (todas as sessões e projetos).
# Preserva as chaves existentes e não duplica regras. Faz backup antes.
set -euo pipefail
src="$(dirname "$0")/global-permissions.json"
dst="$HOME/.claude/settings.json"
mkdir -p "$HOME/.claude"
[ -f "$dst" ] || echo '{}' > "$dst"
cp "$dst" "$dst.bak.$(date +%s)"
python3 - "$src" "$dst" <<'PY'
import json, sys
src, dst = (json.load(open(p)) for p in sys.argv[1:3])
allow = dst.setdefault("permissions", {}).setdefault("allow", [])
for r in src["permissions"]["allow"]:
    if r not in allow: allow.append(r)
json.dump(dst, open(sys.argv[2], "w"), indent=2, ensure_ascii=False)
PY
echo "Regras aplicadas em $dst"
