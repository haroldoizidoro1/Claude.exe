# CLAUDE.md — memória única (preencha os campos entre [colchetes])

> Este é o ÚNICO lugar de memória. Sem claude-mem e sem CLAUDE.local.md.
> Processos repetíveis viram skills (pasta `.claude/skills/`), nunca texto duplicado aqui.

## Task Observer
No início de cada sessão, antes da primeira ferramenta, carregue a skill `task-observer`.
Ela só OBSERVA correções e atritos e PROPÕE melhorias para eu revisar. Nada é gravado sem meu ok.
Quando eu aprovar uma melhoria, ela vai para ESTE arquivo (fato/regra) ou para uma skill (processo), conforme a Regra de memória abaixo, e não fica duplicada no log.
Guia de ativação oficial: references/environments.md em https://github.com/rebelytics/one-skill-to-rule-them-all

## Regra de memória (automática)
Quando eu pedir para "salvar", "lembrar", "anotar" ou "da próxima vez faça X":
1. Se for preferência, fato sobre mim, regra de trabalho ou contexto de projeto → edite ESTE arquivo, na seção certa, sem me perguntar.
2. Se já existir algo parecido, ATUALIZE a linha existente. Nunca crie duplicata.
3. Se for um passo a passo repetível → crie/atualize uma skill em `.claude/skills/<nome>/SKILL.md` e deixe aqui só uma linha apontando para ela.
4. Faça commit e push na branch da sessão e me diga em uma linha o que foi salvo e onde.
5. Mantenha o arquivo curto (meta: menos de 150 linhas). Se passar disso, proponha mover blocos para skills.

## Quem sou eu
- Nome: [seu nome]
- Idioma: português do Brasil
- Trabalho: [ex.: operação logística de cargas secas — Amazon, Shopee, J&T]
- Nível técnico: [iniciante / intermediário / avançado]

## Como quero as respostas
- Direto ao ponto, sem enrolação; explique termos técnicos na primeira vez.
- [outras preferências: tamanho, formato, tom]

## Áreas e projetos ativos
| Projeto | Objetivo | Estado | Próximo passo | Repositório |
|---|---|---|---|---|
| [nome] | [para que serve] | [não iniciado / em andamento / quase pronto] | [1 ação concreta] | [link] |

## Regras de trabalho
- Antes de mudança grande: plano curto e aguardar meu ok.
- Commits pequenos, mensagens claras.
- Nunca fazer deploy, apagar dados ou enviar mensagens externas sem confirmar.
- Ao terminar uma tarefa: dizer o que foi feito, o que falta e o próximo passo.

## Skills (índice — o detalhe fica em cada skill)
- `contexto-operacao-logistica` — Amazon/Shopee/J&T, OTP/OTA, CPT, SLA.
- `verificacao` — checklist por módulo (dados, sites, vídeo, texto) antes de dizer "terminei".
- [adicione aqui uma linha por skill nova]

## Preferências técnicas
- [ex.: sites em HTML/CSS/JS simples, deploy na Vercel, repositório no GitHub]
