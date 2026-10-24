---
paths:
  - "**/*.html"
  - "**/*.xlsx"
  - "**/*.csv"
  - "**/*.py"
---
# Regras por cliente (resumo; fonte completa: skill contexto-operacao-logistica)

## Amazon (RJ, SP, ES, MG e ad hoc)
- Três pontos medidos: chegada na origem, saída da origem (CPT) e chegada no destino.
- Tolerância ATUAL: 0 minuto (antes era 15). 1 minuto de atraso já conta.
- Valor por minuto de desconto: DESCONHECIDO. Não invente.

## Shopee (somente RJ)
- Origem: sem tolerância para atraso. Chegar adiantado na origem não pontua.
- Destino: tolerância pelo transit time programado (STA destino menos STD origem), igual para Early e Delay:
  até 1h: 5 min | 1h a 2h59: 10 | 3h a 5h59: 15 | 6h a 11h59: 20 | 12h a 23h59: 25 | 24h ou mais: 30.
- Early só pontua no destino. Liberação antecipada e morosidade no carregamento deslocam o STA (ver skill).
- Indicador por pacotes por viagem, não por viagens feitas.

## J&T (somente RJ)
- Desconto de R$10 por minuto de atraso, com carência de 5 min SÓ na chegada ao destino (saída e check-in sem carência). A skill ainda diz "tolerância zero": confirmar com o Haroldo antes de mexer na Torre J&T ou no Painel SLA.
- Uso do app: R$50 se faltar em um ponto (saída ou chegada), R$100 se faltar nos dois. Soma com os R$10 por minuto.

## Ao mudar uma regra
Atualize todos os painéis que a usam (Torre Amazon, Torre Shopee, Torre J&T, Painel SLA, Painel de Uso do App,
Reconciliação, Atrasos Amazon etc.) e liste quais foram alterados.
