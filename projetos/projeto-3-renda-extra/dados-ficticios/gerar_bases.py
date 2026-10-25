# Gera bases FICTÍCIAS de viagens (Amazon, Shopee, J&T) para montar painéis de demonstração.
import random, csv, sys, os
from datetime import datetime, timedelta
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter

random.seed(20261025)
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
INI = datetime(2026, 7, 1)
NOMES = ["Carlos Menezes","Rafael Souza","Anderson Lima","Bruno Teixeira","Diego Carvalho","Eduardo Pires","Fábio Nunes","Gustavo Rocha",
 "Hugo Barbosa","Igor Cardoso","Jorge Almeida","Leandro Gomes","Marcelo Dias","Nilton Faria","Otávio Ramos","Paulo Moreira",
 "Renato Castro","Sérgio Lopes","Thiago Moura","Vinícius Prado","Wagner Freitas","Alex Monteiro","Cláudio Reis","Danilo Vieira"]
MOT = [(n, f"{random.choice(['RJ','KX','LT','QP','SR'])}{random.randint(0,9)}{random.choice('ABCDEFGHJ')}{random.randint(10,99)}"[:7].upper()) for n in NOMES]
VEIC = ["Truck","Carreta","Toco","VUC"]
fmt = lambda d: d.strftime("%d/%m/%Y %H:%M") if d else ""
mins = lambda a, b: int(round((a - b).total_seconds() / 60))

MOTIVOS = {
 "Origem": ["Carregamento demorado no CD","Motorista apresentou atrasado","Documentação/liberação atrasada","Veículo chegou com pendência"],
 "Trânsito": ["Trânsito intenso","Acidente na rodovia","Parada não programada","Obra na pista","Chuva forte"],
 "Destino": ["Fila de descarga","Base sem doca disponível","Redirecionamento de base","Divergência de lacre na chegada"],
}

def viagem(lanes, tt_lane, ruim):
    dia = INI + timedelta(days=random.randint(0, 115))
    lane = random.choice(lanes); tt = tt_lane[lane]
    std = dia.replace(hour=random.choice([0,2,4,5,6,8,10,13,15,18,20,22]), minute=random.choice([0,15,30,45]))
    sta = std + timedelta(minutes=tt)
    apres_prog = std - timedelta(minutes=60)
    r = random.random()
    # chegada do motorista na origem
    apres = apres_prog + timedelta(minutes=random.randint(5, 70) if r < ruim*0.35 else -random.randint(0, 50))
    # saída: carregamento pode atrasar, ou base libera antes
    if r < ruim*0.5: atd = std + timedelta(minutes=random.randint(5, 90))
    elif random.random() < 0.12: atd = std - timedelta(minutes=random.randint(10, 40))
    else: atd = std + timedelta(minutes=random.randint(1, 4) if random.random() < 0.04 else random.randint(-8, 0))
    # trânsito
    extra = random.randint(10, 150) if random.random() < ruim*0.45 else (random.randint(1, 6) if random.random() < 0.05 else random.randint(-int(tt*0.06)-5, 0))
    ata = atd + timedelta(minutes=tt + extra)
    destino_prob = random.random() < ruim*0.15
    if destino_prob: ata += timedelta(minutes=random.randint(15, 60))
    return dict(dia=dia, lane=lane, tt=tt, std=std, sta=sta, apres_prog=apres_prog, apres=apres, atd=atd, ata=ata, extra=extra, destino_prob=destino_prob)

def causa(v, atr_orig_saida):
    if v["destino_prob"]: return "Destino"
    return "Origem" if atr_orig_saida >= max(v["extra"], 0) else "Trânsito"

def salva(nome, cab, linhas, regras, descr):
    with open(f"{OUT}/{nome}.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(cab); w.writerows(linhas)
    return (nome, cab, linhas, regras, descr)

# ---------------- AMAZON ----------------
A_LANES = {"Duque de Caxias/RJ → Cajamar/SP":420,"Duque de Caxias/RJ → Betim/MG":390,"Duque de Caxias/RJ → Serra/ES":480,
 "Nova Iguaçu/RJ → São Gonçalo/RJ":75,"Nova Iguaçu/RJ → Campos dos Goytacazes/RJ":240,"Cajamar/SP → Duque de Caxias/RJ":420,"Betim/MG → Duque de Caxias/RJ":390}
cab = ["ID Viagem","Data","Lane","Tipo de rota","Motorista","Placa","Veículo","Apresentação programada","Chegada na origem","CPT (STD)","Saída real (ATD)","STA destino","Chegada real (ATA)",
       "Transit time (min)","Atraso chegada origem (min)","Atraso saída (min)","Atraso destino (min)","Status nosso","Status Amazon","Divergência","Motivo do atraso","Detalhe do motivo","Desconto (R$)"]
L = []
for i in range(1250):
    v = viagem(list(A_LANES), A_LANES, 0.16); m = random.choice(MOT)
    a1 = max(0, mins(v["apres"], v["apres_prog"])); a2 = max(0, mins(v["atd"], v["std"])); a3 = max(0, mins(v["ata"], v["sta"]))
    late = a1 > 0 or a2 > 0 or a3 > 0  # Amazon: tolerância ZERO nos três pontos
    nosso = "Atrasado" if late else "No prazo"
    cli = nosso if random.random() > 0.05 else ("No prazo" if late else "Atrasado")
    c = causa(v, max(a1, a2)) if late else ""
    L.append([f"AMZ-{26000+i}", v["dia"].strftime("%d/%m/%Y"), v["lane"], "Ad hoc" if "MG" in v["lane"] or "ES" in v["lane"] else "Fixa", m[0], m[1], random.choice(VEIC[:2]),
              fmt(v["apres_prog"]), fmt(v["apres"]), fmt(v["std"]), fmt(v["atd"]), fmt(v["sta"]), fmt(v["ata"]), v["tt"], a1, a2, a3, nosso, cli,
              "Sim" if nosso != cli else "Não", c, random.choice(MOTIVOS[c]) if c else "", "PENDENTE (valor por minuto desconhecido)" if late else 0])
L.sort(key=lambda x: (x[1][6:]+x[1][3:5]+x[1][:2], x[9]))
amz = salva("amazon_viagens_ficticio", cab, L,
 ["Tolerância ZERO nos três pontos: chegada na origem, saída (CPT) e chegada no destino.","Valor do desconto por minuto: PENDENTE. A coluna Desconto fica marcada como pendente.","Status Amazon = número do cliente; Status nosso = calculado por nós. Divergência quando diferem."],
 "Viagens Amazon (RJ, SP, MG, ES), jul a out/2026")

# ---------------- SHOPEE ----------------
S_LANES = {"Duque de Caxias/RJ → São Gonçalo/RJ":70,"Duque de Caxias/RJ → Niterói/RJ":55,"São João de Meriti/RJ → Campo Grande/RJ":95,
 "Duque de Caxias/RJ → Petrópolis/RJ":110,"Duque de Caxias/RJ → Volta Redonda/RJ":150,"Duque de Caxias/RJ → Macaé/RJ":230,"São João de Meriti/RJ → Cabo Frio/RJ":190}
def tol_shopee(tt):
    for lim, t in [(60,5),(180,10),(360,15),(720,20),(1440,25)]:
        if tt < lim: return t
    return 30
cab = ["ID Viagem","Data","Lane","Motorista","Placa","Veículo","Pacotes","Chegada origem programada","Chegada na origem","STD (CPT)","Saída real (ATD)","STA destino","Chegada real (ATA)",
       "Transit time (min)","Tolerância destino (min)","Ajuste de saída (min)","STA ajustado","Janela início","Janela fim","Atraso origem (min)","Resultado origem","Resultado destino",
       "Status Shopee","Divergência","OCC","Motivo do atraso","Detalhe do motivo"]
L = []
for i in range(1180):
    v = viagem(list(S_LANES), S_LANES, 0.25); m = random.choice(MOT); tt = v["tt"]; tol = tol_shopee(tt)
    ajuste = mins(v["atd"], v["std"])  # >0 morosidade (STA sobe); <0 liberação antecipada (STA desce)
    sta_aj = v["sta"] + timedelta(minutes=ajuste); ini = sta_aj - timedelta(minutes=tol); fim = sta_aj + timedelta(minutes=tol)
    atr_o = max(0, mins(v["apres"], v["apres_prog"]))
    r_orig = "Delay" if atr_o > 0 else "No prazo"  # origem: sem tolerância; adiantado não pontua
    r_dest = "Early" if v["ata"] < ini else ("Delay" if v["ata"] > fim else "No prazo")
    occ = "Sim" if r_dest != "No prazo" and random.random() < 0.06 else "Não"
    ruim = r_orig == "Delay" or r_dest != "No prazo"
    nosso_dest = r_dest
    cli = nosso_dest if random.random() > 0.07 else random.choice([x for x in ["Early","Delay","No prazo"] if x != nosso_dest])
    if r_dest == "Delay": c = causa(v, atr_o)
    elif r_orig == "Delay": c = "Origem"
    else: c = ""
    det = ("Chegou antes da janela (Early)" if r_dest == "Early" and not c else (random.choice(MOTIVOS[c]) if c else ""))
    L.append([f"SPX-{48000+i}", v["dia"].strftime("%d/%m/%Y"), v["lane"], m[0], m[1], random.choice(VEIC), random.randint(380, 2600),
              fmt(v["apres_prog"]), fmt(v["apres"]), fmt(v["std"]), fmt(v["atd"]), fmt(v["sta"]), fmt(v["ata"]), tt, tol, ajuste, fmt(sta_aj), fmt(ini), fmt(fim),
              atr_o, r_orig, r_dest, cli, "Sim" if cli != r_dest else "Não", occ, c if c else ("Destino" if r_dest == "Early" else ""), det])
L.sort(key=lambda x: (x[1][6:]+x[1][3:5]+x[1][:2], x[9]))
spx = salva("shopee_viagens_ficticio", cab, L,
 ["Origem: SEM tolerância. Chegou atrasado = Delay. Adiantado na origem não pontua.","Destino: janela STA ajustado ± tolerância pelo transit time (até 1h: 5 · 1h–2h59: 10 · 3h–5h59: 15 · 6h–11h59: 20 · 12h–23h59: 25 · 24h+: 30 min).",
  "Ajuste de saída: liberação antecipada (negativo) puxa o STA para antes; morosidade no carregamento (positivo) empurra o STA para depois.","Early e Delay só pontuam no destino. Indicador da Shopee é por pacotes por viagem.",
  "OCC = ocorrência anulada pela Shopee.","Status Shopee = número do cliente (resultado de destino); Divergência quando difere do nosso cálculo.","Contrato/SLA completo da Shopee: PENDENTE."],
 "Viagens Shopee (somente RJ), jul a out/2026")

# ---------------- J&T ----------------
J_LANES = {"Duque de Caxias/RJ → Nova Iguaçu/RJ":50,"Duque de Caxias/RJ → Niterói/RJ":60,"Duque de Caxias/RJ → Itaboraí/RJ":85,"São João de Meriti/RJ → Resende/RJ":170,
 "Duque de Caxias/RJ → Teresópolis/RJ":120,"Duque de Caxias/RJ → Angra dos Reis/RJ":200}
cab = ["ID Viagem","Data","Lane","Motorista","Placa","Veículo","CPT (STD)","Saída real (ATD)","STA destino","Chegada real (ATA)","Transit time (min)","Atraso destino (min)",
       "Usou app na saída","Usou app na chegada","Desconto atraso (R$)","Desconto app (R$)","Desconto total nosso (R$)","Desconto lançado pela J&T (R$)","Divergência","Motivo do atraso","Detalhe do motivo"]
L = []
for i in range(1060):
    v = viagem(list(J_LANES), J_LANES, 0.05); m = random.choice(MOT)
    a = max(0, mins(v["ata"], v["sta"]))  # tolerância ZERO
    s = "Sim" if random.random() > 0.07 else "Não"; c_ = "Sim" if random.random() > 0.09 else "Não"
    d_atr = a * 10; nao = (s == "Não") + (c_ == "Não"); d_app = 0 if nao == 0 else (50 if nao == 1 else 100)
    tot = d_atr + d_app
    jt = tot if random.random() > 0.06 else tot + random.choice([10, 20, 50, -10, 30])
    jt = max(0, jt)
    c = causa(v, max(0, mins(v["atd"], v["std"]))) if a > 0 else ""
    L.append([f"JT-{71000+i}", v["dia"].strftime("%d/%m/%Y"), v["lane"], m[0], m[1], random.choice(VEIC[1:]), fmt(v["std"]), fmt(v["atd"]), fmt(v["sta"]), fmt(v["ata"]),
              v["tt"], a, s, c_, d_atr, d_app, tot, jt, "Sim" if jt != tot else "Não", c, random.choice(MOTIVOS[c]) if c else ""])
L.sort(key=lambda x: (x[1][6:]+x[1][3:5]+x[1][:2], x[6]))
jt = salva("jt_viagens_ficticio", cab, L,
 ["Tolerância ZERO. R$ 10 por minuto de atraso na chegada.","Uso obrigatório do app: R$ 50 se não usar em um dos pontos (saída ou chegada), R$ 100 se não usar em nenhum.","Os descontos se acumulam por viagem.",
  "Desconto lançado pela J&T = número do cliente; Divergência quando difere do nosso cálculo."],
 "Viagens J&T (somente RJ), jul a out/2026")

# ---------------- Excel único ----------------
wb = Workbook(); ws = wb.active; ws.title = "LEIA-ME"
ws.append(["BASE FICTÍCIA PARA DEMONSTRAÇÃO"]); ws["A1"].font = Font(bold=True, size=14)
ws.append(["Todos os dados (motoristas, placas, IDs, horários, descontos) foram gerados por código. Não há dado real de nenhuma empresa."])
ws.append(["Período: 01/07/2026 a 24/10/2026. Lanes com cidades reais apenas como referência geográfica."]); ws.append([])
for nome, cab, linhas, regras, descr in (amz, spx, jt):
    ws.append([f"{nome}: {descr} — {len(linhas)} viagens"]); ws.cell(ws.max_row, 1).font = Font(bold=True)
    for r in regras: ws.append(["  • " + r])
    ws.append([])
ws.column_dimensions["A"].width = 140
head = PatternFill("solid", fgColor="2A322E")
for nome, cab, linhas, _, _ in (amz, spx, jt):
    s = wb.create_sheet(nome.split("_")[0].replace("jt", "J&T").capitalize() if nome[:2] != "jt" else "J&T")
    s.append(cab)
    for c in s[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = head
    for l in linhas: s.append(l)
    s.freeze_panes = "A2"; s.auto_filter.ref = s.dimensions
    for i, h in enumerate(cab, 1): s.column_dimensions[get_column_letter(i)].width = max(12, min(34, len(h) + 4))
wb.save(f"{OUT}/base_ficticia_3_clientes.xlsx")
for nome, _, linhas, _, _ in (amz, spx, jt): print(nome, len(linhas))
