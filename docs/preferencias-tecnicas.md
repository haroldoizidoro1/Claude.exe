# Preferências técnicas (versão completa)
Resumo no `CLAUDE.md`.

## Como os grandes usuários tratam este tópico
Escrevem a stack como decisão fechada, com o motivo e uma exceção explícita ("a menos que o projeto peça"), para o Claude não propor framework, banco ou ferramenta nova sem necessidade.
1. Uma linha por decisão: ferramenta, motivo e quando abrir exceção.
2. O CLAUDE.md diz COMO construir; um DESIGN.md separado diz COMO deve parecer (cores, tipografia, espaçamento, o que a marca NÃO deve parecer).
3. Cores, fontes e espaços ficam como variáveis (tokens), nunca valores soltos.
4. Por área (dados, site, vídeo, design) existe um fluxo padrão, com ferramentas fixas e verificação ao final.

## Código e sites
- HTML, CSS e JS simples, sem framework pesado, a menos que o projeto peça.
- Painéis e ferramentas internas em HTML offline, abrindo direto no navegador, sem servidor e sem instalação.
- Cores, fontes e espaçamentos como variáveis CSS no topo do arquivo.
- Legível em celular e computador.
- Sem biblioteca externa que a operação não consiga abrir sem internet. **(confirmar)**

## Versionamento e publicação
- Código no GitHub, um repositório por projeto.
- Publicação na Vercel, ligada ao repositório; cada envio para a branch principal vira uma publicação.
- Trabalho em branch própria; nada vai direto para a principal sem eu pedir.
- Nunca publicar segredo, token ou chave no repositório.

## Dados e planilhas
- Google Sheets. Uma aba por assunto, cabeçalho na primeira linha, uma linha por registro, sem células mescladas nos dados.
- Cálculos sempre por fórmula ou código, nunca digitados à mão.
- Separar o dado bruto (fonte) do calculado e do informado pelo cliente.

## Painéis de performance
- Mostrar os NOSSOS números, separados dos do cliente, apontando divergência e causa.
- Poucos indicadores, claros para quem não é da área. Sem gráfico que não responda a uma pergunta.
- Fluxo atual: HTML offline preenchido pela operação e sincronizado manualmente com o painel online toda semana.

## Vídeo e audiovisual **(confirmar quais uso)**
- Padrão dos grandes usuários: roteiro e transcrição primeiro; FFmpeg para corte e conversão; Remotion para vídeos feitos por código; IA generativa só para o que não dá para gravar.
- Revisão com feedback curto e específico, com números e nomes ("a legenda entra aos 3s"), nunca "melhore".

## Design
- Visual definido em um DESIGN.md por projeto: paleta, tipografia, espaçamento e o que a marca não deve parecer.
- Componentes usam só as variáveis (tokens).
- Contraste e legibilidade primeiro, enfeite por último.

## Ferramentas
- Claude Code com GitHub, Vercel, Google (Drive, Sheets, Docs, Gmail, Agenda) e Higgsfield (imagem e vídeo).
- Skills próprias: `contexto-operacao-logistica`, `diretrizes-trabalho-operacao`, `verificacao`.
- claude-mem e Headroom foram removidos (duplicavam o CLAUDE.md). OmniRoute é opcional e só roda quando eu peço. **(confirmar)**

## Regra para decisões novas
Antes de adotar framework, banco ou ferramenta nova, o Claude explica o motivo e o custo e espera minha aprovação. Sem aprovação, vale o simples acima.

## Fontes
- https://aifordevelopers.substack.com/p/designmd-for-design-in-claude-code
- https://www.mindstudio.ai/blog/claude-design-token-management-guide
- https://blog.openreplay.com/making-videos-claude-code-remotion/
- https://mcpmarket.com/tools/skills/video-editing-workflow-1783627927386
