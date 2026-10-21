import sqlite3
from fastapi import FastAPI

app = FastAPI()


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
