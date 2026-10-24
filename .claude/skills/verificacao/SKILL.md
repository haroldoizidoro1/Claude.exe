---
name: verificacao
description: Checklist de verificação por módulo (Performance/Dados, Design/Sites, Vídeo/Audiovisual, Texto/Documentos). Use antes de dizer que um passo ou projeto está pronto, ao abrir um PR, ou quando o usuário pedir para conferir/validar um resultado.
---

# Verificação antes de dizer "terminei"

## Como usar
1. Identifique o(s) módulo(s) do que foi entregue (um trabalho pode ter mais de um).
2. Rode cada item de verdade (abrir, medir, comparar). Não marque de memória.
3. No relatório/PR, liste por item: passou, falhou ou não deu para verificar (e por quê).
4. Se algo falhou, corrija e rode de novo. Só então diga que terminou.
5. O critério de "pronto" do projeto (tabela do CLAUDE.md) vale junto com este checklist.

## MÓDULO PERFORMANCE / DADOS
- Totais do painel batem com a planilha de origem, no mesmo período.
- Número calculado por mim separado do número do cliente, com a divergência e a causa.
- Regra de cada cliente aplicada, nunca misturada.

## MÓDULO DESIGN / SITES
- Contraste de texto legível (mínimo 4,5:1) e fontes carregando.
- Responsivo no celular, sem rolagem horizontal.
- Botões, links e formulários funcionam; sem erros no console.
- Conferido contra o guia de estilo (cores, tipografia, espaçamento) do projeto.

## MÓDULO VÍDEO / AUDIOVISUAL
- Resolução, fps e duração conferidos (ffprobe ou equivalente).
- Áudio sem corte nem estouro; legendas sincronizadas.
- Prancha de quadros revisada antes de entregar.

## MÓDULO TEXTO / DOCUMENTOS
- Fatos, nomes e números conferidos na fonte.
- Tom e público-alvo respeitados; sem informação inventada.
