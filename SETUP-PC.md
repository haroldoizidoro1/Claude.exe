# Setup no PC

```bash
git clone https://github.com/haroldoizidoro1/claude.exe && cd claude.exe
./install-pc.sh                 # claude-code-setup + task-observer + harness-engineering
./install-pc.sh --omniroute     # + gateway opcional
./apply-global-permissions.sh   # mescla as regras de permissão em ~/.claude/settings.json
```

## Memória
Existe um único arquivo: `CLAUDE.md` (regras e contexto) + skills em `.claude/skills/` (processos).
Para valer em todos os projetos, copie o `CLAUDE.md` para `~/.claude/CLAUDE.md` (a parte "Quem sou eu", "Como quero as respostas" e "Regra de memória").

## Removidos de propósito
claude-mem e Headroom duplicavam o que o CLAUDE.md + skills já fazem.
Se estavam instalados no PC: `claude plugin uninstall claude-mem@thedotmack`,
`headroom unwrap claude` / `pipx uninstall headroom-ai`.
Apague também `~/.claude-mem/` e `CLAUDE.local.md` se existirem.

## Task Observer (reinstalado a pedido)
Fonte: https://github.com/rebelytics/one-skill-to-rule-them-all (plugin `task-observer`).
Alternativa: `npx skills add rebelytics/one-skill-to-rule-them-all --skill task-observer -g`.
A ativação vem do `CLAUDE.md` (carregar a skill no início); confirme em uma sessão NOVA. Sinal de que funciona: a pasta `skill-observations/observation-log/` aparece depois de algumas sessões.

## harness-engineering (instalado só como plugin)
Fonte: https://github.com/jrenaldi79/harness-engineering. Traz `/readiness` (analisa o projeto e gera `readiness-report.md` com nota, sem alterar nada sem seu aceite) e `/setup` (escreve hooks, scripts, `.claude/rules/` e ajusta o CLAUDE.md).
Ordem: rode `/readiness` primeiro. O `/setup` só com o ok do Haroldo, porque pode reescrever o CLAUDE.md.

## OmniRoute (opcional, não é plugin)
Gateway local que pode rotear para modelos que não são da Anthropic. Só roda quando você pede:
`omniroute launch` (só naquela execução). Fonte: https://github.com/diegosouzapw/OmniRoute
