# Importando as bibliotecas necessárias
from pystac.extensions.eo import EOExtension as eo
import pystac_client
import planetary_computer
import rasterio
from rasterio import windows, features, warp
import numpy as np
from PIL import Image

# Conectando ao catálogo do Planetary Computer
catalog = pystac_client.Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1",
    modifier=planetary_computer.sign_inplace,
)

# Definindo a área de interesse para Nova York (exemplo: região aproximada de Manhattan)
# Essas coordenadas delimitam um polígono que cobre parte de Manhattan.
area_of_interest = {
    "type": "Polygon",
    "coordinates": [
        [
            [-74.02, 40.70],
            [-73.93, 40.70],
            [-73.93, 40.88],
            [-74.02, 40.88],
            [-74.02, 40.70],
        ]
    ],
}

# Definindo o intervalo de datas para 24 de julho de 2021, entre 15h e 16h
# Se necessário, ajuste o formato do intervalo temporal para refletir a data/hora desejada.
time_of_interest = "2021-07-24T15:00:00Z/2021-07-24T16:00:00Z"

# Realizando a busca por imagens Sentinel-2 L2A com baixa cobertura de nuvens (menos de 10%)
search = catalog.search(
    collections=["sentinel-2-l2a"],
    intersects=area_of_interest,
    datetime=time_of_interest,
    query={"eo:cloud_cover": {"lt": 10}},
)

# Coletando os itens retornados
items = search.item_collection()
print(f"Retornados {len(items)} itens")

# Selecionando o item com a menor cobertura de nuvens
least_cloudy_item = min(items, key=lambda item: eo.ext(item).cloud_cover)
print(
    f"Escolhendo {least_cloudy_item.id} de {least_cloudy_item.datetime.date()} "
    f"com {eo.ext(least_cloudy_item).cloud_cover}% de cobertura de nuvens"
)

# Obtendo a URL do asset de visualização (Cloud Optimized GeoTIFF)
asset_href = least_cloudy_item.assets["visual"].href

# Utilizando rasterio para renderizar a imagem correspondente à área de interesse
with rasterio.open(asset_href) as ds:
    # Calculando os limites da área de interesse
    aoi_bounds = features.bounds(area_of_interest)
    # Convertendo os limites para o sistema de referência espacial da imagem
    warped_aoi_bounds = warp.transform_bounds("epsg:4326", ds.crs, *aoi_bounds)
    # Definindo a janela de leitura baseada nos limites transformados
    aoi_window = windows.from_bounds(transform=ds.transform, *warped_aoi_bounds)
    # Lendo os dados das bandas da área definida
    band_data = ds.read(window=aoi_window)

# Convertendo os dados de formato "band-interleaved" para "pixel-interleaved"
img = Image.fromarray(np.transpose(band_data, axes=[1, 2, 0]))

# Redimensionando a imagem para visualização (definindo uma largura alvo e mantendo a proporção)
target_w = 800
w, h = img.size
aspect = w / h
target_h = int(target_w / aspect)
img_resized = img.resize((target_w, target_h), Image.Resampling.BILINEAR)

# Exibindo a imagem (em ambientes que suportam visualização)
img_resized.show()
