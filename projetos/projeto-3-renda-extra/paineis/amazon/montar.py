# Monta torre-amazon.html: injeta a base fictícia da Amazon (CSV) no template.
# Uso: python3 montar.py   (roda dentro desta pasta)
import csv, json
CID = {"Duque de Caxias":[-22.79,-43.31],"Nova Iguaçu":[-22.76,-43.45],"São Gonçalo":[-22.83,-43.05],"Campos dos Goytacazes":[-21.75,-41.32],
       "Cajamar":[-23.36,-46.88],"Betim":[-19.97,-44.20],"Serra":[-20.13,-40.31]}
R = list(csv.DictReader(open("../../dados-ficticios/amazon_viagens_ficticio.csv", encoding="utf-8-sig"), delimiter=";"))
lanes, placas, resumos, ops = [], [], [], []
idx = lambda lst, x: lst.index(x) if x in lst else (lst.append(x) or len(lst) - 1)
CAUSA = {"": -1, "Origem": 0, "Trânsito": 1, "Destino": 2}
TIPO = {"": 0, "Real": 1, "Indevido": 2}
V = []
for r in R:
    o, d = [p.strip().split("/")[0] for p in r["Lane"].split("→")]
    li = next((i for i, l in enumerate(lanes) if l["n"] == r["Lane"]), None)
    if li is None: lanes.append({"n": r["Lane"], "o": o, "d": d}); li = len(lanes) - 1
    res = lambda k: idx(resumos, r[k]) if r[k] else -1
    V.append([r["VRID"], int(r["Mês"]), int(r["Data"][:2]), li, idx(placas, r["Placa"]),
              int(r["Atraso chegada origem (min)"]), int(r["Atraso saída (min)"]), int(r["Atraso destino (min)"]),
              TIPO[r["Tipo OTP"]], TIPO[r["Tipo OTA"]], int(r["Min. Amazon OTP"]), int(r["Min. Amazon OTA"]),
              res("Resumo OTP"), res("Resumo OTA"), CAUSA[r["Motivo do atraso"]],
              1 if r["Vínculo"] == "Frota" else 0, {"": 0, "ADHOC": 1, "Retorno": 2}[r["ADHOC/Retorno"]], idx(ops, r["Operador"]),
              {"": 0, "OK": 1, "Pendente": 2}[r["Evidência"]], int(r["Preço BID (R$)"]), 0 if r["Veículo"] == "Carreta" else 1])
D = {"terra": json.load(open("terra_sudeste.json")), "lanes": lanes, "cid": CID, "placas": placas, "resumos": resumos, "ops": ops, "v": V}
html = open("template.html", encoding="utf-8").read().replace("/*DATA*/null", json.dumps(D, ensure_ascii=False, separators=(",", ":")))
open("torre-amazon.html", "w", encoding="utf-8").write(html)
print(len(V), "VRIDs ·", len(lanes), "lanes ·", round(len(html) / 1024), "KB")
