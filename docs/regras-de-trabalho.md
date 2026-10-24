# Regras de trabalho do Claude (versão completa)
Resumo no `CLAUDE.md`. Aqui fica o detalhe.

## Visão geral
Os usuários mais avançados do Claude Code não escrevem um arquivo gigante de regras. Dividem as regras por QUANDO o Claude precisa delas e passam as críticas para automação:
1. Camadas: cada regra no nível certo, para não gastar contexto à toa.
2. Curto e acionável: só entra o que muda o comportamento do Claude.
3. Regra crítica vira automação: texto é um pedido, hook e permissão são garantia.

## 1. Organização em camadas
| Camada | Onde fica | O que vai nela | Quando carrega |
|---|---|---|---|
| Global | `~/.claude/CLAUDE.md` | Seu jeito de trabalhar em qualquer projeto: idioma, tom, "pergunte antes de X" | Toda sessão |
| Projeto | `CLAUDE.md` na raiz, versionado no git | Contexto, comandos, pegadinhas, "faça isto, não aquilo" | Toda sessão do projeto |
| Regras por caminho | `.claude/rules/*.md` com filtro de arquivos no topo | Regras que só valem para certos arquivos (ex.: painéis HTML) | Só ao mexer nesses arquivos |
| Documentação | `docs/*.md`, apontada por um "mapa de documentos" no CLAUDE.md | Explicações longas | Só quando o CLAUDE.md aponta |
| Skills, agentes e comandos | `.claude/skills`, `.claude/agents`, `.claude/commands` | Rotinas repetidas (cálculo de atraso, relatório, revisão) | Só quando chamados |

Regra prática: assunto com mais de uns 20 linhas sai do CLAUDE.md e vai para documento ou skill.

## 2. Como escrever o CLAUDE.md
- Tamanho: entre 100 e 300 linhas. O arquivo do próprio time do Claude Code tem cerca de 2,5 mil tokens.
- Entra: comandos exatos, caminhos reais, pegadinhas que já fizeram perder uma sessão, regras explícitas de "faça isto, não aquilo".
- Não entra: boas práticas genéricas que o modelo já conhece ("escreva código limpo").
- Escreva como instrução verificável. "Calcule atraso sempre em código" é melhor que "seja cuidadoso".

## 3. As 4 regras de comportamento (inspiradas em Andrej Karpathy)
1. **Pensar antes de agir:** declarar as suposições, perguntar quando houver dúvida e mostrar as interpretações possíveis em vez de escolher em silêncio. Se existir um caminho mais simples, dizer.
2. **Simplicidade primeiro:** o mínimo que resolve. Nada de funcionalidade não pedida, abstração para uso único ou configuração "para o futuro". Se escreveu 200 linhas e dava em 50, reescreva.
3. **Mudanças cirúrgicas:** mexer só no que foi pedido, sem reformatar nem "melhorar" o vizinho, mantendo o estilo existente. Algo estranho fora do escopo: avisar e não corrigir. Limpar só o que a própria mudança deixou órfão. Cada linha alterada deve ter origem no pedido.
4. **Execução guiada por objetivo:** transformar a tarefa em algo verificável (ex.: um teste que reproduz o bug) e repetir até passar. Em trabalho de vários passos, declarar o plano com uma verificação por passo.

Contrapeso: essas regras favorecem cautela sobre velocidade. Em tarefa trivial, usar bom senso e não fazer perguntas desnecessárias.

## 4. Ideias do harness-engineering
- **Divulgação progressiva:** CLAUDE.md sempre carregado, depois regras por caminho, depois documentos, depois planos raramente usados.
- **Ordem de confiança:** verificação automática vale mais que regra em arquivo, que vale mais que texto solto.
- **Hooks:** formatação ao salvar, bloqueio de segredos no código, testes antes de enviar.
- **Permissões:** listas de permitir e negar em `.claude/settings.json` para deixar o padrão seguro.
- **Limites objetivos:** arquivo e função com tamanho máximo, para o código não inchar.
- **Mapa de documentos:** uma tabela no CLAUDE.md que diz onde está cada assunto.

## 5. O ciclo "errou, vira regra"
- CLAUDE.md versionado no git, atualizado várias vezes por semana.
- Sempre que o Claude erra, entra uma linha curta para ele não repetir (aqui: `docs/erros-viram-regra.md`).
- Revisão semanal: cortar o obsoleto e promover ao CLAUDE.md só o que se repetiu.
- Sempre dar ao Claude um jeito de verificar o próprio resultado (teste, conferência, comparação com a fonte).

## 6. Aplicação na minha operação (logística de cargas secas)
- **Global (`~/.claude/CLAUDE.md`):** português do Brasil; as 4 regras da seção 3; confirmar antes de ação irreversível ou que envie algo para fora; nunca gravar senha ou chave em arquivo; propor "errou, vira regra" depois de uma correção.
- **Projeto (`CLAUDE.md`):** contexto de Qualidade e Performance; clientes Amazon, Shopee e J&T, sem misturar regras; dizer cliente e regra antes de calcular atraso/desconto; separar número nosso do número do cliente; mostrar o motivo do atraso (origem, trânsito ou destino); pendências sem inventar; painéis em HTML offline com sincronização semanal.
- **Regras por caminho:** regras dos clientes e dos painéis, carregadas só ao mexer em HTML, planilhas ou scripts. (Ainda não criadas.)
- **Skills:** `contexto-operacao-logistica` e `diretrizes-trabalho-operacao`.
- **Registro:** `docs/erros-viram-regra.md`.

## 7. Checklist para montar o sistema
1. Criar o CLAUDE.md global com as regras de conduta (seção 3). **Falta:** copiar para `~/.claude/CLAUDE.md` no PC.
2. Criar o CLAUDE.md de cada projeto, curto, com mapa de documentos.
3. Mover regras que valem só para certos arquivos para `.claude/rules/`. **Falta.**
4. Transformar rotinas repetidas em skills.
5. Transformar regras críticas em hook ou permissão. **Falta.**
6. Manter o registro "errou, vira regra" e revisar toda semana.

## Fontes
- https://github.com/multica-ai/andrej-karpathy-skills
- https://github.com/jrenaldi79/harness-engineering
- https://github.com/hesreallyhim/awesome-claude-code
- https://www.claude.com/blog/using-claude-md-files
- https://infoq.com/news/2026/01/claude-code-creator-workflow/
