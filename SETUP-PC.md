# Setup no PC

```bash
git clone https://github.com/haroldoizidoro1/claude.exe && cd claude.exe
./install-pc.sh                 # só o claude-code-setup
./install-pc.sh --omniroute     # + gateway opcional
./apply-global-permissions.sh   # mescla as regras de permissão em ~/.claude/settings.json
```

## Memória
Existe um único arquivo: `CLAUDE.md` (regras e contexto) + skills em `.claude/skills/` (processos).
Para valer em todos os projetos, copie o `CLAUDE.md` para `~/.claude/CLAUDE.md` (a parte "Quem sou eu", "Como quero as respostas" e "Regra de memória").

## Removidos de propósito
claude-mem, Headroom e task-observer duplicavam o que o CLAUDE.md + skills já fazem.
Se estavam instalados no PC: `claude plugin uninstall claude-mem@thedotmack`,
`claude plugin uninstall task-observer@one-skill-to-rule-them-all` e `headroom unwrap claude` / `pipx uninstall headroom-ai`.
Apague também `~/.claude-mem/` e `CLAUDE.local.md` se existirem.

## OmniRoute (opcional, não é plugin)
Gateway local que pode rotear para modelos que não são da Anthropic. Só roda quando você pede:
`omniroute launch` (só naquela execução). Fonte: https://github.com/diegosouzapw/OmniRoute
