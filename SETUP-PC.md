# Setup no PC

Rápido: `./install-pc.sh` instala OmniRoute, Headroom e claude-mem (claude-code-setup e Task Observer vêm pela conta/`/plugin`).
Testado no container: `npm i -g omniroute` sobe na porta 20128; `headroom-ai[mcp,code]` instala em venv.

# Setup no PC (Claude Code)

Este repositório já traz `.claude/settings.json`, que registra o marketplace do
**claude-mem** e o habilita. Ao abrir o Claude Code nesta pasta no PC, ele pede
para confiar na pasta e instalar o plugin.

```bash
git clone https://github.com/haroldoizidoro1/claude.exe && cd claude.exe
claude            # aceite o prompt de confiança / instalação do plugin
```

Pré-requisito do claude-mem: Node.js 20+ (Bun e uv são instalados sozinhos).
Manualmente: `/plugin marketplace add thedotmack/claude-mem` e `/plugin install claude-mem`.

## Plugins do catálogo da conta (claude-code-setup, Task Observer, Headroom)
Habilitados na conta claude.ai (cartão de instalação) — sincronizam com o PC ao
logar com a mesma conta. Alternativa manual: `/plugin` e buscar no
"Anthropic Directory".

## Headroom (compressão de contexto — projeto headroom-ai, opcional)
```bash
pip install "headroom-ai[mcp,code]"
headroom mcp install          # registra as ferramentas no Claude Code
# ou: headroom wrap claude
```

## OmniRoute (gateway, NÃO é plugin)
Projeto: https://github.com/diegosouzapw/OmniRoute — roda localmente como
gateway; o Claude Code aponta para ele via `ANTHROPIC_BASE_URL`. Isso pode
rotear requisições para modelos que não são da Anthropic. Siga o README do
projeto para instalar e depois exporte:
```bash
export ANTHROPIC_BASE_URL="http://localhost:<porta-do-omniroute>"
export ANTHROPIC_AUTH_TOKEN="<chave gerada no dashboard do OmniRoute>"
```

## claude-mem: instalador alternativo e conta
O README oficial (https://github.com/thedotmack/claude-mem) recomenda também
`npx claude-mem install`. Esse instalador pede login no cmem.ai (e-mail, trial
de 30 dias) e pode sincronizar memórias na nuvem. Para ficar 100% local, use
`CLAUDE_MEM_ONLINE_OPTIN=false npx claude-mem install` ou o caminho por
`/plugin` descrito acima. Não use `npm install -g claude-mem` (só instala a SDK).
Configurações ficam em `~/.claude-mem/settings.json`.

## Headroom: detalhes do README oficial
Repositório: https://github.com/headroomlabs-ai/headroom (pacote PyPI `headroom-ai`).
- Instalação completa: `pip install "headroom-ai[all]"` (ou `uv tool install --python 3.13 "headroom-ai[all]"`;
  em macOS use Python 3.13 se o seu `python3` for mais novo que os wheels). O script usa `[mcp,code]`, mais leve.
- `npm install headroom-ai` é só o SDK TypeScript, sem a CLI.
- `headroom mcp install` registra as ferramentas no Claude Code (é o que o script faz; não redireciona tráfego).
- Opcionais que roteiam o tráfego por um proxy local, então use só se quiser: `headroom wrap claude`
  (desfaz com `headroom unwrap claude`) ou `headroom proxy --port 8787`.
- `headroom learn --verbosity` (simula) e `--apply` mineram sessões com falha e gravam correções em `CLAUDE.local.md`.
- Atualizar: `headroom update`.

## claude-code-setup e Task Observer (fontes oficiais)
- claude-code-setup: https://github.com/anthropics/claude-plugins-official (marketplace `claude-plugins-official`).
- Task Observer: https://github.com/rebelytics/one-skill-to-rule-them-all (plugin `task-observer`).
  Alternativa: `npx skills add rebelytics/one-skill-to-rule-them-all --skill task-observer -g`.
  Só instalar não basta: a ativação vem do `CLAUDE.md` deste repo (carregar a skill no início);
  confirme em uma sessão NOVA. Sinal de que funciona: a pasta `skill-observations/observation-log/` aparece depois de algumas sessões.
- Os dois também estão em `.claude/settings.json`, então o PC os oferece ao abrir a pasta.
- Isto substitui os plugins do cartão do catálogo (versões de terceiros); o Task Observer certo é o do rebelytics.

## OmniRoute + Claude Code (guia oficial, opt-in manual)
Fonte: https://github.com/diegosouzapw/OmniRoute (docs/guides/CLAUDE-CODE-CONFIGURATION.md).
Isto redireciona o Claude Code para o gateway e pode usar modelos que não são da Anthropic.
Nada disso é aplicado automaticamente; rode você mesmo quando quiser.

```bash
npm install -g omniroute && omniroute      # dashboard em http://localhost:20128
# no dashboard: Providers -> conectar Kiro AI ou OpenCode Free (sem cadastro)
omniroute launch                           # abre o claude apontado para o OmniRoute local, só nessa execução
omniroute setup-claude                     # cria perfis em ~/.claude/profiles/<nome>/settings.json
omniroute launch --profile <nome>          # usa um perfil/modelo específico
```
- `omniroute launch` define `ANTHROPIC_BASE_URL` (sem `/v1`) e `ANTHROPIC_AUTH_TOKEN` só para aquela execução;
  um `claude` aberto normalmente continua usando a Anthropic.
- Remoto (VPS): `omniroute connect <host>` e depois `omniroute launch`.
- Modelos não-Claude no `/model`: ligue `EXPOSE_CC_DISCOVERY_ALIASES` (Settings -> Feature Flags) e use
  `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1`. Ajuste `CLAUDE_CODE_AUTO_COMPACT_WINDOW` abaixo da janela real do modelo.
- Variáveis de ambiente só são lidas na inicialização: reinicie o Claude Code após mudar.
- MCP do OmniRoute (110 ferramentas): `claude mcp add-server omniroute --type http --url http://localhost:20128/api/mcp/stream`.
