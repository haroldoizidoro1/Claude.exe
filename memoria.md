# Memória do projeto

Leia este arquivo no início de cada sessão. Ele guarda decisões e preferências que valem para todas as conversas.

## Preferências do usuário

- Idioma: português do Brasil.
- Aplicar as skills **caveman**, **ultracave** e **graphify** em todas as conversas (pedido em 2026-10-22). Regras de uso abaixo.

## Skills instaladas (2026-10-22)

Ficam em `.claude/skills/`, copiadas sem alteração dos repositórios oficiais (licença Apache-2.0, com LICENSE e NOTICE de cada uma):

| Skill | Fonte | Commit |
|---|---|---|
| caveman | https://github.com/JuliusBrussee/caveman (`skills/caveman`) | `bad48a0` |
| ultracave | https://github.com/JuliusBrussee/caveman (`skills/ultracave`) | `bad48a0` |
| graphify | https://github.com/safishamsi/graphify (`graphify/skill.md` + `graphify/skills/claude/references`) | `847a93f` |

"Caverman" é a mesma caveman. A ultracave é o modo máximo da caveman.

### Como aplicar em toda conversa

- **caveman**: ligada desde a primeira resposta, a sessão inteira, em português. Desliga só com "stop caveman" ou "normal mode". Segue as exceções da própria skill: texto plano para avisos de segurança, ações irreversíveis, perguntas ao usuário e tudo o que fica salvo fora do chat (código, commits, documentos, PRs).
- **ultracave**: substitui a caveman quando o usuário pede `/ultracave` ou `/caveman ultra`. As duas são vozes, então só uma vale por vez.
- **graphify**: em perguntas sobre código, arquitetura ou conteúdo de um projeto, consultar `graphify-out/` primeiro quando existir. Se não existir, oferecer `/graphify .` (a extração semântica gasta tokens). Na primeira execução a skill instala o pacote Python `graphifyy` sozinha.

### Onde vale

- **Este repositório** (PC e nuvem): `.claude/skills/` + seção "Skills sempre ativas" do `CLAUDE.md`.
- **Todos os projetos no PC, com ganchos extras**: rodar `./install-skills-global.sh` uma vez. Ele:
  - instala o plugin oficial `caveman@caveman` no escopo de usuário: skills (caveman, ultracave, megacave e outras), comandos `/caveman-*`, agentes cavecrew e ganchos SessionStart, SubagentStart, UserPromptSubmit e SessionEnd (precisam de Node.js);
  - cria `~/.config/caveman/config.json` com `{"defaultMode": "caveman"}` se não existir (troque para `"ultracave"` para o modo máximo sempre);
  - instala a CLI `graphifyy` e roda `graphify install` (skill global);
  - acrescenta a regra de ativação em `~/.claude/CLAUDE.md` como reserva.
  - Ganchos do graphify são por projeto: `graphify claude install` (consulta o grafo antes de ler arquivos) e `graphify hook install` (refaz o grafo a cada commit).
- **Este repositório também habilita o plugin**: `.claude/settings.json` registra o marketplace `JuliusBrussee/caveman` e `caveman@caveman` (aprovado pelo usuário em 2026-10-22). Ao abrir a pasta, o Claude Code oferece instalar o plugin com os ganchos.
- **Fora do Claude Code** (claude.ai e app): enviar as pastas das skills em Configurações > Capacidades > Skills da conta.

## Outros registros

- 2026-10-22: Painel de Rotina publicado (https://claude.ai/artifact/J7hNVFedq1DNpTVX5hoETM). Código em `painel-rotina/index.html`. Dados salvos na conta Claude do usuário, privados.
- 2026-10-23: Painel conectado ao Google Agenda pelo conector "Google Calendar" do claude.ai (ferramentas `list_calendars`, `list_events`, `create_event`). Lê a semana atual e a próxima (e a semana aberta na Agenda), atualiza a cada 5 min, mostra os eventos na Início e na Agenda e cria compromissos no Google pelo formulário. Os eventos do Google não são gravados no banco do painel. Ligar e escolher agendas em Ajustes > Google Agenda.
- A skill `task-observer` pedida no `CLAUDE.md` não estava instalada na sessão de nuvem de 2026-10-22.
