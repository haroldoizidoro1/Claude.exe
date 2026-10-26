# PLANO — Projeto 3: Renda extra com painéis e automações
Prioridade: 3 · Passo máximo: 1 h

## Objetivo
Vender painéis de performance e automações (Google Sheets, HTML offline) para transportadoras e pequenas empresas, usando o Claude. Objetivo nº 1: a PRIMEIRA VENDA do painel. Meta pessoal ligada: juntar R$ 4.000 de reserva (vira notebook/PC/Mac quando fizer sentido), sem empréstimo.

## Pronto quando
- 1º cliente pagante fechado.

## Regras
- Sem exclusividade no contrato (confirmado por mim em 25/10/2026). Mesmo assim: nunca usar dados, painéis ou regras internas da empresa. Só dados fictícios.
- Enviar mensagens, propostas e negociar: só eu. O Claude prepara.
- Gasto máximo: R$ 0 até o 1º cliente.

## Agenda
- Seg a sex: 20h30 às 23h (folga de segunda a sexta quando precisar).
- Sábado: um bloco de 4 h. Domingo: livre, para a família.

## Passos (cada um até 1 h)
1. Bases fictícias (feito em 25/10): `dados-ficticios/` com Amazon 1.250, Shopee 1.180 e J&T 1.060 viagens, cada uma com a regra do seu cliente. Gerador: `gerar_bases.py`.
1b. Painel de demonstração: o Haroldo desenha e monta; o Claude ajuda quando pedido.
2. Segunda demonstração: automação de planilha (ex.: relatório semanal automático no Google Sheets).
3. Página de apresentação (HTML simples, Vercel) com as duas demonstrações e um contato.
4. Definir 2 ou 3 pacotes e preços, com pesquisa de mercado.
5. Lista de 20 empresas para prospectar: `prospeccao.csv` (feito em 26/10; prioridade A = transportadoras com agregados).
6. Mensagem curta de abordagem (WhatsApp/LinkedIn) e modelo de proposta.
7. Enviar as primeiras mensagens (eu envio) e registrar respostas.

## Pesquisa (25/10/2026, a validar)
- Preço freelancer BI no Brasil: R$ 45 a 120/h em marketplaces; analista pleno R$ 130 a 220/h. Consultorias: R$ 5 mil a 18 mil por dashboard (fora do nosso alcance no início).
- Proposta inicial: Painel Essencial R$ 1.200 (1 fonte, até 6 indicadores) · Painel + automação R$ 2.000 · Atualização semanal R$ 300/mês. 1º cliente pode ter desconto de "cliente-piloto" em troca de depoimento.
- Demanda real vista: vaga no Workana de transportadora que atende o Mercado Livre pedindo planilha de coleta + dashboard (indicadores DS, CR, PNR).
- Canais: Workana, 99Freelas, LinkedIn, grupos de transportadoras/agregados no WhatsApp e Facebook, contatos da própria operação (sem usar dado interno).
- Clientes-alvo: transportadoras e agregados que rodam para Shopee (SPX), Amazon (DSP), J&T e Mercado Livre; depois, pequenos comércios com planilha bagunçada.
- Regras de SLA/desconto de cada marketplace não são públicas: o painel deve deixar a regra configurável pelo cliente.

## Em aberto
- Nome do serviço/marca.
- Nicho inicial: transportadoras (prioridade) ou também outros negócios.
