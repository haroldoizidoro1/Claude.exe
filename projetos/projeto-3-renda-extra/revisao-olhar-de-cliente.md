# Revisão com olhar de cliente (26/10/2026)

Lido como se eu fosse a Beatriz (BeOn) recebendo o e-mail, abrindo a vitrine e depois o contrato.

## Prioridade alta (resolver antes de enviar)
1. **A vitrine fala a língua da Amazon, e a BeOn talvez não rode para a Amazon.** O site deles fala em sellers de Mercado Livre, Shopee, Amazon e Magalu (first/last mile, line haul para o vendedor). VRID, Relay e penalidade por VRID são do mundo de quem é transportadora contratada pela Amazon. Para a BeOn, o mais provável é "SLA por cliente (seller), coleta e entrega no prazo, por agregado". Ação: ajustar o texto do e-mail para não afirmar que eles têm o problema do Relay e preparar uma versão "genérica de transportadora" da vitrine (mesma estrutura, outros nomes).
2. **E-mail longo demais.** ~550 palavras. Dono de empresa lê em 30 segundos. Ação: versão curta (~180 palavras) com 1 dor, 1 número, o link e o convite; os detalhes ficam na vitrine e na chamada.
3. **"Há alguns anos".** Pela linha do tempo (Amazon desde nov/2025), é cerca de 1 ano. Se ela olhar o LinkedIn, perde confiança. Ação: tirar o tempo ou dizer a verdade ("trabalho com performance de transportadoras que rodam para Amazon, Shopee e J&T").
4. **O caso da demonstração soa como caso real.** "O que mais me orgulha... a transportadora do exemplo... quando a operação passou a ver" narra um resultado que não aconteceu. E 88% de indevidos pode soar exagerado para quem é do ramo. Ação: falar "a demonstração simula..." e trazer o número como possibilidade, não como resultado.
5. **Regras de faturamento vieram do painel da empresa onde você trabalha** (meta 99%, R$ 100 por VRID, teto 2%, bônus 0,5%/1,5%). Decisão pendente: trocar por valores genéricos ou manter como "exemplo ajustável". Conferir também se citar "BRLog" na vitrine expõe ferramenta interna.

## Prioridade média
6. **9 abas na primeira visita.** Para quem abre pelo e-mail, é muita coisa. Ação: uma aba/faixa "Comece por aqui" com 3 passos ("veja o resultado do mês → veja os atrasos → veja o guia do operador").
7. **Vitrine no celular.** Ela vai abrir o link no telefone. Conferir as abas principais em 400 px e se o link público abre sem login.
8. **E-mail pessoal (gmail).** Funciona, mas um endereço com nome profissional passa mais segurança. Opcional, depois do 1º cliente.
9. **Preço no primeiro e-mail.** Ajuda a filtrar, mas pode encerrar a conversa antes da chamada. Alternativa: deixar só "condição especial para as primeiras parceiras" e abrir os valores na chamada.

## Contrato (o que um cliente questionaria)
10. **Suporte só à noite e aos sábados**, e a operação deles roda 24 h. Ela vai perguntar "e se parar na terça às 10h?". Ação: deixar claro que o painel não para por falta do suporte (planilha/HTML seguem funcionando) e definir um canal de urgência.
11. **12 meses com renovação automática + mínimo de 3 meses + multa.** Para piloto, pode assustar. Ação: piloto de 3 meses sem renovação automática; depois, contrato anual.
12. **Aceite tácito em 5 dias e limitação de responsabilidade** são justos, mas vão ser lidos com lupa. Manter, explicando na conversa.
13. **Uso de IA com dados deles.** Vão perguntar qual ferramenta e onde ficam os dados. Ter a resposta pronta (dados mascarados, sem treino de modelo, conferir os termos da ferramenta usada).
14. **Hospedagem ainda indefinida.** Recomendação: Opção B (conta da própria BeOn na Vercel), com login no servidor para a área de faturamento.

## Para você (não para o cliente)
15. **Emprego atual:** a BeOn é do mesmo setor. Não usar horário, equipamento, dados nem ferramentas internas da empresa; manter tudo fora do expediente.
16. **Ritmo:** hoje passou do horário combinado (20h30 às 23h). O projeto é de meses; vale respeitar o limite.

## Próximos passos sugeridos (amanhã)
1. Decidir o item 5 (regras de faturamento).
2. E-mail curto + texto que não presume Amazon (itens 1 a 4).
3. Faixa "Comece por aqui" na vitrine e teste no celular (itens 6 e 7).
4. Ajustes do contrato para o piloto (itens 10 e 11).
5. Enviar para a BeOn.

## Status (26/10/2026, aplicado)
- 1 · Vitrine ganhou faixa "Comece por aqui" dizendo que é exemplo Amazon e que se adapta a SLA por seller/agregado; e-mail v3 não presume Amazon. **Não feito:** versão completa da vitrine para sellers (fazer depois do diagnóstico).
- 2 · E-mail curto (v3, ~200 palavras) criado; v2 ficou como base.
- 3 · "Há alguns anos" removido das duas versões.
- 4 · Caso agora é "a demonstração simula"; o 88% saiu do e-mail (continua no painel).
- 5 · Regras de faturamento trocadas por valores genéricos (R$ 150 por VRID, teto 3%, bônus 1% + 1%; meta 99% fica, pois é a meta pública da BeOn). "BRLog" removido da vitrine.
- 6 · Faixa "Comece por aqui" com 3 botões.
- 7 · Testado em 400 px: as 8 abas sem rolagem lateral; gota das abas corrigida no celular. **Não verificado:** abrir o link público sem login (só você consegue, depois de compartilhar).
- 8 · v3 cita só "condição especial"; valores na chamada (v2 mantém os valores).
- 10, 11, 14 · Contrato v1: canal de urgência (4 h, a qualquer hora), piloto de 3 meses sem renovação automática, hospedagem B marcada como recomendada.
- 13 · Resposta pronta sobre IA e dados no arquivo do e-mail.
- 15, 16 · Pessoais, sem ação de código.
