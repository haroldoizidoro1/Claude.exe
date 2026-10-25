---
name: comparar-operacao-cliente
description: Compara os atrasos que a operação registrou (planilha, WhatsApp de passagem de turno) com os que o cliente registrou (painel, site, planilha do cliente) e classifica cada divergência. Use quando o Haroldo pedir para comparar, conferir ou reconciliar números da operação com os do cliente (Amazon, Shopee ou J&T), na análise diária ou na segunda-feira.
---

# Comparar operação x cliente

Esta skill só ensina o MÉTODO. As regras de cada cliente (tolerância, pontos medidos, valor por minuto) vêm da skill `contexto-operacao-logistica`. Não copie regra para cá.

## Ideia central
Nenhuma fonte é a verdade sozinha. O cliente pode apontar atraso que não foi atraso. A operação pode ter esquecido de lançar. Nunca trate um lado como certo sem prova.

Fontes internas: planilhas da operação, WhatsApp (passagem de turno).
Fontes externas: painel, site ou planilha do cliente.

## Passos
1. Diga o cliente e a regra aplicada (tolerância, pontos medidos). Um cliente por comparação, nunca misture.
2. Diga o período e as fontes usadas. Fonte que não consegui abrir: avise, não adivinhe.
3. Cruze por ID da viagem. Por código, nunca de cabeça.
4. Classifique cada atraso:
   - **A** cliente e operação registraram: confere.
   - **B** só o cliente registrou, e há prova interna (ex.: WhatsApp diz que atrasou): falha de preenchimento. Indique turno e operador, se a fonte mostrar.
   - **C** só o cliente registrou e não há prova interna nenhuma: possível atraso indevido. Vai para análise. Não conta como certo.
   - **D** só a operação registrou: atraso nosso que o cliente não apontou.
5. Para B e C, aplique a regra do cliente e mostre quanto cada grupo mexe na performance em %. Calcule em código e mostre os dois números lado a lado. Não decida sozinho qual conta.
6. Para cada atraso, o motivo: origem, trânsito ou destino.
7. Termine com o bloco "Conferido" (ver skill `verificacao`).

## Regras do Haroldo
- Formal e direto. Compacto, mas sem perder precisão.
- Valor ou regra que falta (ex.: valor por minuto da Amazon, contrato da Shopee): escreva "PENDENTE". Nunca invente.
- Divergência sem causa conhecida: diga "causa não identificada". Não chute.

## Exemplos (dados fictícios, só para mostrar o formato)
**Bom 1:** "J&T, 20/10 a 26/10, regra: tolerância 0, R$10/min. 1 atraso em A. 1 em B (viagem EXEMPLO-01: WhatsApp do turno B registra 12 min; planilha vazia). Impacto de B: 120 reais calculados por código. 0 em C."
**Bom 2:** "Amazon, C: viagem EXEMPLO-02, cliente aponta 8 min; sem registro interno. Em análise: pedir evidência ao cliente antes de aceitar. Não incluído no cálculo."
**Mau:** "O cliente aponta 5 atrasos que a operação esqueceu de lançar." Por quê: assume que o cliente está certo, junta B e C, não mostra prova, não diz a regra nem o período.
