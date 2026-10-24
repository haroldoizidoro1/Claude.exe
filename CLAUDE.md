# CLAUDE.md — memória única

> Este é o ÚNICO lugar de memória. Sem claude-mem e sem CLAUDE.local.md.
> Assunto com mais de ~20 linhas vai para `docs/` ou para uma skill; aqui fica só o resumo e o ponteiro.

## Task Observer
No início de cada sessão, antes da primeira ferramenta, carregue a skill `task-observer`.
Ela só OBSERVA correções e atritos e PROPÕE melhorias para eu revisar. Nada é gravado sem meu ok.
Quando eu aprovar uma melhoria, ela vai para ESTE arquivo (fato/regra) ou para uma skill (processo), conforme a Regra de memória abaixo, e não fica duplicada no log.
Guia de ativação oficial: references/environments.md em https://github.com/rebelytics/one-skill-to-rule-them-all

## Regra de memória (automática)
Quando eu pedir para "salvar", "lembrar", "anotar" ou "da próxima vez faça X":
1. Preferência, fato sobre mim, regra de trabalho ou contexto de projeto → edite ESTE arquivo, na seção certa, sem me perguntar.
2. Se já existir algo parecido, ATUALIZE a linha existente. Nunca crie duplicata.
3. Passo a passo repetível → crie/atualize uma skill em `.claude/skills/<nome>/SKILL.md` e deixe aqui só uma linha apontando para ela.
4. Assunto longo → `docs/<assunto>.md` e uma linha no Mapa de documentos.
5. Depois de uma correção minha, proponha uma linha em `docs/erros-viram-regra.md` (data, erro, regra). Só grave com meu ok.
6. Faça commit e push na branch da sessão e me diga em uma linha o que foi salvo e onde.
7. Mantenha este arquivo curto (meta: menos de 150 linhas). Se passar, mova blocos para docs/skills.

## Quem sou eu
- Nome: Haroldo Izidoro Turetta (Haroldin)
- Idioma: português do Brasil
- Trabalho: analista pleno, setor de Qualidade, área de logística (performance dos clientes). Também crio projetos de IA para a empresa.
- Nível técnico: intermediário — explique só o que for novo.

## Como quero as respostas
- Tamanho médio, com o motivo. Tom informal e amigável. Prefiro passo a passo numerado.
- Antes de começar um projeto, tenha certeza de que terminei de explicar tudo. Não refaça o trabalho toda vez que eu acrescentar um texto: incorpore o novo e siga.

## Mapa de documentos
| Assunto | Onde |
|---|---|
| Regras de trabalho completas (camadas, 4 regras de comportamento, ciclo "errou, vira regra") | `docs/regras-de-trabalho.md` |
| Preferências técnicas completas (código, dados, painéis, vídeo, design) | `docs/preferencias-tecnicas.md` |
| Agente finalizador: pronto, PR, acessos, limites, relatório | `docs/agente-finalizador.md` |
| Lições aprendidas (uma linha cada) | `docs/erros-viram-regra.md` |
| Plano do Projeto 1 | `projetos/painel-planos-de-acao/PLANO.md` |
| Plano do Projeto 2 | `projetos/projeto-2-a-nomear/PLANO.md` |

## Regras de trabalho (resumo)
1. Pensar antes de agir: declarar suposições, perguntar na dúvida, mostrar interpretações possíveis em vez de escolher em silêncio.
2. Simplicidade primeiro: o mínimo que resolve, nada não pedido. Dava em 50 linhas e escrevi 200? Reescreva.
3. Mudanças cirúrgicas: mexer só no pedido, manter o estilo existente. Algo estranho fora do escopo: avisar, não corrigir.
4. Execução guiada por objetivo: tarefa vira algo verificável, com uma verificação por passo.
- Em tarefa trivial, use bom senso e não faça perguntas desnecessárias.
- Plano curto e meu ok antes de mudança grande. Commits pequenos.
- Nunca fazer deploy, apagar dados ou enviar algo para fora sem confirmar.
- Nunca gravar senha, token ou chave em arquivo ou repositório.
- Cálculo sempre por código ou fórmula, nunca de cabeça, e conferido contra a fonte.
- Ao terminar: o que foi feito, o que falta, próximo passo, e o que foi (e não foi) conferido.

## Operação (logística de cargas secas)
- Setor Qualidade e Performance. Clientes: Amazon, Shopee, J&T. Nunca misturar regras entre clientes.
- Antes de calcular atraso ou desconto, dizer qual cliente e qual regra está sendo aplicada.
- Separar o número calculado por nós do número do cliente; apontar divergência e causa.
- Mostrar o motivo do atraso (origem, trânsito ou destino) para justificar ao cliente.
- Painéis: HTML offline, sincronização semanal, legíveis para operação, supervisão e donos.
- Pendências (não inventar): valor por minuto da Amazon, contrato da Shopee, planilha online da J&T, lane de MG da Shopee.
- Enviar dados para terceiros: só eu faço. Se não há dado novo para atualizar, não atualize.

## Áreas e projetos ativos
| Projeto | Objetivo | Estado | Próximo passo | Repositório |
|---|---|---|---|---|
| Painel de planos de ação (prazo 01/11, prioridade: Painel Shopee) | Tratar gargalos e criar ações para não se repetirem | Em andamento (aba "Visão operacional") | Concluir a aba "Visão operacional" | [a informar] |
| Projeto 2 (nome a confirmar): Performance MREBR + Torre Amazon | Performance/faturamento MREBR e registro diário de OTP/OTA | Em andamento | Aguardando de mim: valor por minuto de desconto e explicação da divergência Relay x Performance | [a informar] |

## Agente finalizador (resumo; detalhe em `docs/agente-finalizador.md`)
- Trabalha em branch própria, abre um PR por passo do plano (passo máx. 1 h). Eu aprovo só o que for sensível; merge só com verificações verdes e meu ok.
- Faz sozinho: commit, abrir PR, publicar prévia. Pergunta antes: merge, deploy, apagar, enviar mensagem/e-mail, gastar. Nunca: mudar domínio, DNS ou chaves.
- Gasto máximo: R$ 0. Na dúvida: parar, registrar no relatório e esperar.
- Relatório diário em `RELATORIO.md` do projeto. Verificação pela skill `verificacao`.

## Skills (índice — o detalhe fica em cada skill)
- `contexto-operacao-logistica` — regras de Amazon/Shopee/J&T, OTP/OTA, CPT, SLA.
- `diretrizes-trabalho-operacao` — como trabalhar na operação sem errar.
- `verificacao` — checklist por módulo (dados, sites, vídeo, texto) antes de dizer "terminei".

## Preferências técnicas (resumo; detalhe em `docs/preferencias-tecnicas.md`)
- Sites em HTML/CSS/JS simples, sem framework pesado, a menos que o projeto peça. Painéis em HTML offline.
- Cores, fontes e espaços como variáveis CSS. Legível em celular e computador.
- GitHub (um repositório por projeto), Vercel para publicar, Google Sheets para dados. Trabalho em branch própria.
- Ferramenta, framework ou banco novo: explicar motivo e custo e esperar meu ok.
