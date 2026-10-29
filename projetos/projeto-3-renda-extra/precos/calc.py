def brl(x): return "R$ {:,.0f}".format(x).replace(",",".")
painel=dict(E=3500,C=6000,I=9000)
auto=dict(E=1800,C=3500,I=6000)
apres=dict(E=1200,C=2800,I=4500)
site=dict(E=3500,C=6000,I=9000)
def comb(n): return 0.05 if n==2 else 0.10 if n==3 else 0.15 if n>=4 else 0
# exemplo do Haroldo: 2 paineis Completo + 1 aula (turma ate 10) + 1 automacao Completo
itens=[painel['C'],painel['C'],1200,auto['C']]
s=sum(itens); d=comb(len(itens)); t=s*(1-d)
print("combo A",s,d,t, "avista5%",t*.95, "3x",t/3, "50/50",t/2)
# combo B: 1 painel integrado + 1 automacao completa + trilha 4 aulas
trilha=4*1200*(1-0.12)
print("trilha",trilha)
itens=[painel['I'],auto['C'],trilha]
s=sum(itens); d=comb(len(itens)); t=s*(1-d); print("combo B",s,d,t,t*.95,t/3)
# combo C pequeno: painel essencial + automacao essencial
itens=[painel['E'],auto['E']]; s=sum(itens); d=comb(2); t=s*(1-d); print("combo C",s,d,t,t*.95,t/3)
# mensal anual
for n,h,m in [("Start",5,850),("Pro",10,1500),("Business",20,2600)]:
    print(n,m,m/h, "anual avista",m*10,"12x",round(m*12*.9/12))
for n,m in [("Basica",300),("Padrao",560),("Plus",1040)]:
    print(n,m,"anual",m*10)
# parcelamento de combo A em 3x
