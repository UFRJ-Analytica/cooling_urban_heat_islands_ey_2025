import planetary_computer as pc
from pystac_client import Client

# 1. Conectar ao endpoint STAC do Planetary Computer
catalog = Client.open("https://planetarycomputer.microsoft.com/api/stac/v1")

# 2. Fazer uma busca (Search) por items do Sentinel-2 L2A
#    Exemplo: filtrar por bounding box e datas
search = catalog.search(
    collections=["sentinel-2-l2a"],
    bbox=[-47.94, -15.87, -47.87, -15.80],  # exemplo de área
    datetime="2023-01-01/2023-01-10",
    query={"eo:cloud_cover": {"lt": 20}}
)

items = list(search.get_items())
print(f"Encontrados {len(items)} itens.")

# 3. Selecionar um item (cena) específico
item = items[0]

# 4. "Assinar" o item para ter acesso aos URLs temporários (SAS tokens)
#    Isso é obrigatório no Planetary Computer
signed_item = pc.sign(item)

# 5. Acessar, por exemplo, a banda B04 (vermelho)
b04_asset = signed_item.assets["B04"]

# 6. Agora b04_asset.href é uma URL temporária
print(b04_asset.href)

# 7. Se quiser baixar o arquivo GeoTIFF localmente, use requests ou urllib
import requests

r = requests.get(b04_asset.href, stream=True)
with open("b04.tif", "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)

print("Download concluído: b04.tif")
