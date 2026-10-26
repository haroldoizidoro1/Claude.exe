# Gera a máscara de terra (1 bit por célula) do Sudeste para o globo de rotas, a partir da textura "terra-dia-4k" do Estúdio Haroldo.
# Uso: python3 mascara_terra.py <terra-dia-4k.jpg>   → grava terra_sudeste.json
import sys, json, base64
from PIL import Image
LAT0, LAT1, LON0, LON1, PASSO = -36.0, -4.0, -60.0, -28.0, 0.16
img = Image.open(sys.argv[1]).convert("RGB"); W, H = img.size; px = img.load()
rows = round((LAT1 - LAT0) / PASSO); cols = round((LON1 - LON0) / PASSO); bits = []
for i in range(rows):
    lat = LAT1 - (i + .5) * PASSO
    for j in range(cols):
        lon = LON0 + (j + .5) * PASSO
        x = min(W - 1, int((lon + 180) / 360 * W)); y = min(H - 1, int((90 - lat) / 180 * H))
        r, g, b = px[x, y]; bits.append(1 if r + g > 46 * 1.0 and not (b > r + 25 and b > g) else 0)
by = bytearray((len(bits) + 7) // 8)
for k, v in enumerate(bits):
    if v: by[k >> 3] |= 1 << (k & 7)
json.dump({"lat1": LAT1, "lon0": LON0, "passo": PASSO, "rows": rows, "cols": cols, "b64": base64.b64encode(bytes(by)).decode()}, open("terra_sudeste.json", "w"))
print(rows, "x", cols, "células ·", sum(bits), "de terra ·", len(base64.b64encode(bytes(by))) // 1024, "KB")
