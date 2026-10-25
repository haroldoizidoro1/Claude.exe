---
name: pdf-semanal-supervisao
description: Monta o conteúdo do PDF executivo semanal que o Haroldo envia à supervisão toda sexta, com os dados da semana anterior (S-1) e o impacto, na performance em %, de operadores que não lançam evidência ou não preenchem a planilha. Use quando ele pedir o relatório semanal, o PDF de sexta ou o envio para a supervisão. A geração do arquivo PDF usa a skill `pdf`.
---

# PDF semanal para a supervisão

Objetivo do documento: mostrar à supervisão que evidência não lançada e planilha não preenchida derrubam a performance (%) por cliente. O Haroldo só encaminha o PDF, sem apresentar. Ele precisa se explicar sozinho.

## Passos
1. Defina o período e escreva no topo. Suposição até ele confirmar: os 7 dias fechados até a quinta anterior à sexta de envio. Se ele disser outro período, use o dele.
2. Rode `comparar-operacao-cliente` para cada cliente, separado (Amazon, Shopee, J&T). Cliente sem dado novo: escreva "sem dado novo no período", não atualize nem invente.
3. Monte o PDF, nesta ordem:
   - Título, período, data de emissão.
   - **Conclusão em 3 linhas no máximo**: performance por cliente e o quanto a falta de lançamento custou.
   - Uma tabela por cliente: atrasos A, B, C, D e impacto em % de B e C.
   - Casos de B por turno/operador, só se a fonte mostrar. Sem tom de acusação: fatos e números.
   - Casos de C como "em análise com o cliente".
   - Pendências e dados faltando.
   - Bloco "Conferido" curto.
4. Corte tudo que não muda a decisão. Quantidade só onde importa. Compactar sem perder precisão: cada número precisa ter fonte e período.
5. Gere o arquivo com a skill `pdf`. Abra o PDF e confira de verdade antes de entregar.
6. Entregue o arquivo pronto. Quem envia é o Haroldo. Nunca envie.

## Regras do Haroldo
- Tom formal e direto, sempre. Sem sujeito de opinião, sem gíria, sem enfeite.
- Máximo de 2 páginas, salvo pedido dele.
- Cada cliente com a própria regra, nunca misturada.

## Exemplos (dados fictícios)
**Bom 1:** primeira página com "J&T: 1 atraso na semana. 1 sem registro da operação (turno B). Impacto estimado: -X,X p.p. na performance" (X calculado por código).
**Bom 2:** "Shopee: sem dado novo no período."
**Mau:** 8 páginas com todas as viagens, gráficos sem pergunta e frase "alguns operadores estão relaxando". Por quê: longo, sem conclusão, acusa sem número e obriga o leitor a procurar a conclusão.
