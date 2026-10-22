# sample.csv の polygon_uu に対応する「本物の筆ポリゴン」を抜き出し、
# final_label / stage2_prob を properties に付けて GeoJSON を作る
# これはテストデータ生成なので Claude が書く（CLAUDE.md の例外）
import json
import pandas as pd

SOURCE = "/Users/nagatomotaito/Desktop/筆ポリゴン/2023_tukubamirai.geojson"

sample = pd.read_csv("data/sample.csv").set_index("polygon_uu")

with open(SOURCE, encoding="utf-8") as f:
    all_polygons = json.load(f)

features = []
for feat in all_polygons["features"]:
    uuid = feat["properties"]["polygon_uuid"]
    if uuid not in sample.index:
        continue
    row = sample.loc[uuid]
    features.append({
        "type": "Feature",
        "geometry": feat["geometry"],  # 本物の筆の形をそのまま使う
        "properties": {
            "final_label": row["final_label"],
            "stage2_prob": None if pd.isna(row["stage2_prob"]) else row["stage2_prob"],
        },
    })

geojson = {"type": "FeatureCollection", "features": features}

with open("data/sample_polygons.geojson", "w", encoding="utf-8") as f:
    json.dump(geojson, f, ensure_ascii=False)

print(f"{len(features)} 件を data/sample_polygons.geojson に書き出した")
