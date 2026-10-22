# Instruções do projeto

## Task Observer
No início de cada sessão, antes da primeira ferramenta, carregue a skill `task-observer`
(ela observa correções e atritos e propõe melhorias de skills, com revisão humana).
Guia de ativação oficial: references/environments.md em
https://github.com/rebelytics/one-skill-to-rule-them-all

## Memória
No início de cada sessão, leia `memoria.md`. Registre lá decisões e preferências novas que devam valer nas próximas conversas.

## Skills sempre ativas (caveman, ultracave, graphify)
As três ficam em `.claude/skills/`. Aplique em toda conversa:
- **caveman**: ative na primeira resposta e mantenha a sessão inteira, em português. Desliga só com "stop caveman" ou "normal mode". Respeite as exceções da skill (segurança, ações irreversíveis, perguntas ao usuário e tudo que fica salvo fora do chat sai em texto normal).
- **ultracave**: substitui a caveman quando o usuário pedir `/ultracave` ou `/caveman ultra`.
- **graphify**: em perguntas sobre código, arquitetura ou conteúdo do projeto, consulte `graphify-out/` primeiro quando existir; se não existir, ofereça `/graphify .` antes de rodar (gasta tokens).
