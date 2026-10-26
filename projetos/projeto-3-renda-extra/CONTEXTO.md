# Contexto do Projeto 3 (ponto de partida para uma nova sessão)
Atualizado em 26/10/2026. Leia isto + `PLANO.md` antes de continuar.

## Decisões já tomadas
1. **Objetivo nº 1:** fechar a PRIMEIRA VENDA de um painel de performance para transportadoras.
2. **Meta pessoal ligada:** juntar R$ 4.000 de reserva (vira notebook/PC/Mac depois). Sem empréstimo.
   - Consignado Itaú (R$ 5.543 em 24x de R$ 398,62, custo real ~4,9% a.m., seguro embutido): recusado.
   - Empréstimo de terceiro para o MacBook: adiado; já existe um notebook sendo pago (R$ 250/mês até mai/2027).
3. **Contrato de trabalho sem exclusividade.** Pode vender por conta própria, mas NUNCA usar dados, painéis com números ou regras internas da empresa. Só dados fictícios.
4. **Quem envia e negocia é o Haroldo.** O Claude prepara mensagens, propostas e rascunhos.
5. **Agenda:** seg a sex 20h30–23h; sábado 4 h; domingo família.
6. **Painéis: o Claude monta a 1ª versão, um por vez (para poupar uso), e o Haroldo ajusta.** Componentes do Estúdio Haroldo: Núcleo, Órbita, Vitral, Galeria, Esteira, Lâminas, Roda, Menisco, Rotas, Orbes.

## O que já existe
- `dados-ficticios/`: bases Amazon (1.272), Shopee (1.164), J&T (1.046 viagens), jul–24/out/2026, com coluna Fase:
  - Amazon: atrasos apontados (OTP+OTA) jul 56 · ago 53 · set 45 · out 26 (out: 3 reais, 23 indevidos = 88%). OTP nosso 91,3% → 99,3%; OTA 94,0% → 99,6% (outubro bate a meta de 99%). VRIDs fictícios mascarados (`11XXXX***`).
  - Shopee: origem/destino de ~62%/61% em jul → 88%/86% em out.
  - J&T: uso do app 46% em jul (R$ 15.200 de desconto por app) → 94% em out (R$ 1.350).
  - Gerador: `gerar_bases.py`. Regras conferidas por código (0 erros).
- `dados-ficticios/base_ficticia_mercado_livre.xlsx`: 1.276 rotas last mile + 12 planos de ação (indicadores genéricos, confirmar os oficiais com o cliente). Gerador: `gerar_base_meli.py`.
- `paineis/amazon/`: Torre Amazon de demonstração (template + `montar.py`), publicada em https://claude.ai/artifact/77t8YBveTUdL7Az4VVXuiK. Alvo do pitch: Murici Logística.
- `identidade-visual.md`: paletas de Amazon, Shopee e J&T e regras de uso de marca.
- `PLANO.md`: preços (Essencial R$ 2.500–3.500 + R$ 400–600/mês · Automação R$ 5.000–8.000 + R$ 800–1.500/mês · Piloto R$ 1.500 + R$ 300/mês por 3 meses), canais e clientes-alvo.
- `abordagens/beon-email.md` (e-mail pronto) · `contrato/contrato-painel-v1.md|.docx` (rascunho v1) · Apresentação: "especialista independente em performance logística".
- MEI: TI não pode ser MEI (2026). Primeira venda por RPA (pessoa física) ou abrir ME no Simples; confirmar com contador.

## Finanças (Caixa do Casal, outubro)
- Entra (Haroldo): ~R$ 3.387 (salário + adiantamento + aluguel), mais VR/VA R$ 660.
- Vazamentos: Pix sem descrição R$ 1.306, lanches no débito R$ 416, Uber/99 R$ 246.
- Regras combinadas: todo Pix com descrição; lanche só no VR; Uber só à noite ou com chuva.

## Em aberto
- Revisão de cliente (`revisao-olhar-de-cliente.md`) aplicada em 26/10. Falta: decidir se manda a v3 com ou sem preço, publicar a vitrine com link público e enviar. Versão da vitrine para SLA de sellers: depois do diagnóstico da BeOn.
- Próximos painéis, um por vez: Shopee, J&T, Mercado Livre (o Haroldo ajusta cada um).
- Nome do serviço/marca.
- Subir as bases para o Google Sheets (oferecido, sem resposta).
- Tarefa agendada de e-mail (ler e deixar rascunho): ligar só quando começar a prospecção.
- Prospecção: `prospeccao.csv` pronto (20 contatos); falta a mensagem de abordagem (passo 6).
