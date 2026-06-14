#!/usr/bin/env python3
"""
Script para crear desafíos de interpolación para subir a MapRoulette.

Lee dos GeoPackages, uno de segmentos (LineString) y otro de nodos (Point).
Ambos están en `EPSG:4326`.

El atributo `idTarea` relaciona a un segmento y dos nodos.
Genera un FeatureCollection por cada `idTarea`.
Los atributos `fid` se descartan.
El GeoJSON generado incluye separadores newline.
"""

import geopandas as gpd

segmentos = gpd.read_file(
    "segmentosCortadosCentro.gpkg"
)

nodos = gpd.read_file(
    "nodosCentro.gpkg"
)


print(len(segmentos))
print(len(nodos))


from shapely.validation import explain_validity

invalidos = segmentos[~segmentos.geometry.is_valid]

for idx, row in invalidos.iterrows():
    print("idTarea:", row["idTarea"])
    print(explain_validity(row.geometry))

invalidos = nodos[~nodos.geometry.is_valid]

for idx, row in invalidos.iterrows():
    print("idTarea:", row["idTarea"])
    print(explain_validity(row.geometry))


segmentos = segmentos[
    ["idTarea", "addr:interpolation", "source", "geometry"]
].copy()

nodos = nodos[
    ["idTarea", "addr:street", "addr:housenumber", "source", "geometry"]
].copy()


segmentos["idTarea"] = segmentos["idTarea"].astype(str)
nodos["idTarea"] = nodos["idTarea"].astype(str)


import json
from shapely import transform
import numpy as np

def redondear_geom(geom, decimales=7):
    return transform(
        geom,
        lambda coords: np.round(coords, decimales)
    )

features = []

# segmentos
for _, row in segmentos.iterrows():
    geom = redondear_geom(row.geometry)

    features.append({
        "type": "Feature",
        "properties": row.drop("geometry").to_dict(),
        "geometry": geom.__geo_interface__
    })

# nodos
for _, row in nodos.iterrows():
    geom = redondear_geom(row.geometry)

    features.append({
        "type": "Feature",
        "properties": row.drop("geometry").to_dict(),
        "geometry": geom.__geo_interface__
    })

geojson = {
    "type": "FeatureCollection",
    "features": features
}

with open("objetosCentro.geojson", "w", encoding="utf-8") as f:
    json.dump(geojson, f, ensure_ascii=False)
