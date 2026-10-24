# Instruções do projeto

Responda em português do Brasil. As regras gerais de conduta estão em `global/CLAUDE.md`
(instale em `~/.claude/CLAUDE.md` com `./apply-global-claude-md.sh`).

## Task Observer
No início de cada sessão, antes da primeira ferramenta, carregue a skill `task-observer`
(ela observa correções e atritos e propõe melhorias de skills, com revisão humana).
Guia de ativação oficial: references/environments.md em
https://github.com/rebelytics/one-skill-to-rule-them-all

## Contexto
Setor de Qualidade e Performance de uma operação de logística de cargas secas.
Clientes: Amazon, Shopee e J&T. Nunca misture as regras de um cliente com as de outro.
As regras detalhadas de cada cliente ficam nas skills `contexto-operacao-logistica`
(O QUE são as regras) e `diretrizes-trabalho-operacao` (COMO trabalhar). Carregue as duas
sempre que o assunto for atraso, OTP/OTA, CPT, desconto de fatura, painéis ou planilha de viagem.

## Regras que valem sempre
- Antes de calcular atraso ou desconto, diga qual cliente e qual regra está aplicando.
- Separe o número calculado por nós do número que o cliente apresenta e aponte a divergência e a causa.
- Mostre o motivo do atraso (origem, trânsito ou destino) para poder justificar ao cliente.
- Pendências conhecidas (não invente): valor por minuto da Amazon, contrato/SLA da Shopee,
  acesso à planilha online da J&T, lane de MG da Shopee.
- Painéis: HTML offline preenchido pela operação, com sincronização manual semanal com o painel online.
  Legível para operação, supervisão e donos, sem enfeite.

## Mapa de documentos
| Assunto | Onde |
|---|---|
| Tolerâncias, descontos e pendências por cliente | `.claude/rules/clientes.md` (carrega ao mexer em painéis e planilhas) |
| Como editar e testar painéis | `.claude/rules/paineis.md` |
| Instalação no PC | `SETUP-PC.md` |
| Registro de erros e regras novas | `docs/erros-viram-regra.md` |

## Errou, vira regra
Quando o Claude errar e eu corrigir, acrescente a lição em `docs/erros-viram-regra.md`
(uma linha: data, erro, regra). Promova para este arquivo só o que se repetir.
