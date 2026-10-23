import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS設定：別ポート（index.htmlは5500番、このAPIは8000番）から来る
# fetch を許可する。本番で公開するときは allow_origins を絞るべきだが、
# 開発中は "*"（全部許可）で進める。
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
)


@app.get("/regions")
def regions():
    conn = sqlite3.connect("data/paddy.db")
    rows = conn.execute("SELECT DISTINCT local_gove FROM parcels;").fetchall()
    conn.close()
    return rows

@app.get("/parcels")
def parcels(region: int, threshold: float = 0.0):
    conn = sqlite3.connect("data/paddy.db")
    rows = conn.execute(
        "SELECT * FROM parcels WHERE local_gove = ? AND (final_label = '水田' OR stage2_prob >= ?)",
        (region, threshold)
    ).fetchall()
    conn.close()
    return rows
