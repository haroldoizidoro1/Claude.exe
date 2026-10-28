# Planos e preços · transportadora de médio porte (faturamento ~R$ 5–6 mi/mês)
Rascunho de 28/10/2026. Valores são PROPOSTA minha para você negociar; as faixas de mercado em R$ não foram confirmadas por fonte brasileira (ver "Base de preço").

## 0. Antes de tudo: o que você pode cobrar (leia primeiro)
Os 3 painéis que você tem (Performance MREBR/Amazon, Painel Shopee, Performance J&T·MRB) foram feitos dentro da empresa, com dados, marca e regras dela. Se você é CLT, software criado durante o contrato costuma ser da empresa (Lei 9.609/98, art. 4º). Cobrar da própria empresa por eles, como se fossem seus, tende a ser contestado e pode virar problema de confiança ou até jurídico. Por isso:
1. **Não venda o que já existe como produto novo.** Venda o que é NOVO: evolução, automação, manutenção, treinamento, novos painéis, consultoria.
2. **Combine por escrito o que é de quem** (propriedade do que já existe x do que for criado daqui pra frente) antes de falar de preço.
3. **Formato do vínculo:** ser CLT e prestar serviço PJ à mesma empresa é zona de risco (vínculo, "pejotização"). Opções: (a) aditivo ao contrato CLT com cargo/salário/bônus por resultado; (b) contrato de serviço separado, só com advogado trabalhista e contador validando. Decisão sua, com profissional; eu não substituo isso.
4. A regra do Projeto 3 continua: para OUTROS clientes, só dados fictícios e nada interno.

## 1. Como um comprador (dono/diretor de transportadora ~R$ 5–6 mi/mês) enxerga seus painéis
Base: li a estrutura dos 3 artefatos (títulos de seções e abas), não testei cada tela nem conferi os números.
**O que vende:**
- Amazon: é um sistema, não um painel: resultado do mês, desconto na fatura, "quanto cada atraso custa", Amazon x BRLog, consulta por VRID, AdHoc, planos de ação, faturamento por operação/rota, mapa. Isso responde a pergunta cara do dono: "onde perco dinheiro e o que contesto".
- Shopee e J&T: cobrem as regras de cada cliente (sem misturar), com ranking de condutores e custo das ausências de marcação (J&T).
- Faturamento fechado por senha/login, planos de ação, upload de planilha.
**O que o comprador vai questionar (resolva antes de precificar alto):**
1. **Dependência da plataforma:** acesso pelo login do claude.ai. Pergunta da TI: "e se a conta cair, quem tem os dados, tem backup, tem SLA?" Resposta: exportação periódica, cópia em conta da empresa (Vercel/Drive), documentado.
2. **Dependência de uma pessoa** (você). Resposta: documentação, manual do operador, cláusula de continuidade.
3. **LGPD:** nome de motorista e placa. Precisa de cláusula e de acesso por perfil.
4. **Atualização manual:** hoje depende de subir planilha. É justamente o degrau que justifica o plano de Automação.
5. **Padrão visual diferente** entre os 3 (claro no J&T, escuro na Amazon). Aceitável (cada cliente com sua cara), mas vale uma navegação única ("Torre").
6. **Prova de valor:** o dono compra se vir R$. Leve um quadro "antes x depois" com o dinheiro contestado/evitado, medido com a base da própria empresa.

## 2. Planos de assinatura (implantação + mensalidade)
Moeda: R$. Mensalidade = atualização, suporte, ajustes de regra e melhorias dentro do limite de horas.
| Plano | Para quem | O que inclui | Implantação | Mensal |
|---|---|---|---|---|
| **Painel** | 1 cliente (Amazon OU Shopee OU J&T) | Painel sob medida com as regras do cliente, atualização semanal por planilha, 1 treinamento, suporte em horário comercial, 4 h/mês de ajustes | R$ 6.000 a 9.000 | R$ 1.500 a 2.500 |
| **Torre** (recomendado) | Os 3 clientes + faturamento + planos de ação | 3 painéis numa navegação única, faturamento com acesso restrito, desconto/contestação, playbook do operador, backup e documentação, 8 h/mês de ajustes | R$ 15.000 a 22.000 | R$ 4.500 a 6.500 |
| **Torre Automática** | Quem quer zero planilha manual | Tudo da Torre + integração com os sistemas da empresa (Relay, BRLog etc.), atualização diária automática, alertas de risco de atraso | + R$ 12.000 a 25.000 | + R$ 2.500 a 4.500 |
| **Parceiro de Performance** (retainer) | Quem quer o analista de IA dentro da operação | Até 40 h/mês: painéis novos, consultoria de performance, IA aplicada à operação, treinamentos, apresentações para diretoria/clientes, prioridade de atendimento | — | R$ 8.000 a 12.000 |
Automação depende de autorização dos sistemas e dos termos de uso de cada um; o orçamento fecha depois do levantamento.

## 3. Serviços avulsos (preço de projeto)
| Serviço | Faixa |
|---|---|
| Diagnóstico de performance com a base do cliente (1 semana de viagens) | R$ 2.500 a 6.000 |
| Painel extra (novo cliente/indicador) | R$ 4.500 a 8.000 |
| Automação de planilha/rotina (Google Sheets, relatório automático) | R$ 1.800 a 6.000 |
| Apresentação executiva (reunião de resultado, board, cliente) | R$ 1.200 a 4.500 (deck sob medida) |
| Site institucional (até 5 páginas) | R$ 3.500 a 9.000; manutenção R$ 300 a 800/mês |
| Treinamento de equipe em IA (meio período, até 15 pessoas) | R$ 3.000 a 6.000 |
| Hora avulsa (fora de plano) | R$ 150 a 250 |

## 4. Âncora de valor (por que o preço se sustenta)
Cálculo por código: faturamento R$ 5,5 mi/mês.
| Ganho (contestado + evitado) | Em R$/mês | Torre (R$ 5.500/mês) custa | Retainer (R$ 10.000) custa |
|---|---|---|---|
| 0,3% do faturamento | 16.500 | 33% do ganho | 61% |
| 0,5% | 27.500 | 20% | 36% |
| 1,0% | 55.000 | 10% | 18% |
Use SÓ com número real da empresa (descontos recebidos, multas e atrasos do último fechamento). Sem esse número, a conta é hipótese, não promessa. Primeiro ano da Torre: R$ 18.000 + 12 × R$ 5.500 = R$ 84.000.

## 5. Negociação
**Estrutura da proposta:** apresente 3 opções (Painel / Torre / Torre Automática), com a Torre no meio e destacada. O dono tende a escolher a do meio.
**Ordem da conversa:** (1) dor e número deles; (2) demonstração; (3) prova de valor com a base deles; (4) preço; (5) forma de pagamento.
**Piloto:** 90 dias, escopo fechado (1 painel ou a Torre), critério de sucesso escrito (ex.: "identificar X em atrasos contestáveis"), com abatimento da implantação se virarem para o plano anual.
**Escada de concessões (do menor ao maior custo para você):**
1. Prazo de pagamento (30/60 dias).
2. Parcelamento da implantação em 3x sem juros.
3. 10% de desconto no anual pago à vista.
4. Mensalidade reduzida por 3 meses em troca de depoimento/case.
5. Horas extras de ajuste no 1º mês.
Nunca: baixar preço sem tirar escopo; escopo aberto ("tudo que precisar"); trabalhar sem aceite escrito; entregar a automação sem a autorização dos sistemas.
**Se disserem "tá caro":** pergunte contra o quê. Compare com um analista de dados CLT (salário + encargos) e com o ganho da seção 4; ofereça subir de plano só se houver mais valor, ou descer de plano (Painel) em vez de desconto.
**Se disserem "faz de graça, você já é da casa":** responda com o formato (seção 0): o que está no seu cargo é uma coisa; projeto novo, com meta e prazo, tem remuneração própria (bônus por resultado, aditivo ou contrato).
**Reajuste:** IPCA a cada 12 meses. **Multa/juros:** 2% + 1% ao mês. **Suporte:** o do contrato v1 (`contrato/contrato-painel-v1.md`) serve de base; adaptar IP e vínculo ao caso da sua empresa.

## 6. Base de preço (e o que falta confirmar)
- Referência EUA 2026 (convertida em lógica, não em R$): consultoria de BI US$ 150–350/h; projeto US$ 15–75 mil; retainer US$ 2–8 mil/mês. Fonte: [Perceptive Analytics](https://www.perceptive-analytics.com/how-much-does-power-bi-consulting-cost-in-2026-in-san-antonio/).
- Retainer de consultoria em IA US$ 2–5 mil/mês para 5–10 h: [Refonte Learning](https://www.refontelearning.com/ai/ai-consulting-pricing/); modelo "taxa de implantação + retainer mensal": [MindStudio](https://mindstudio.ai/blog/pricing-ai-automation-projects).
- Brasil (pesquisa anterior, 25/10): freelancer BI R$ 45–120/h; analista pleno R$ 130–220/h. Não achei tabela brasileira de consultoria em R$; as faixas acima são julgamento meu, ancoradas em valor e no porte da empresa (faixa de ~25–50% abaixo do mercado americano).
- Falta: cotação de 2 ou 3 integradores/consultorias locais de BI em logística para calibrar; salário e encargos de um analista de dados da própria empresa (para a comparação "custo de contratar").
