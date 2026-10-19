import sqlite3
from fastapi import FastAPI

app = FastAPI()


@app.get("/regions")
def regions():
    conn = sqlite3.connect("data/paddy.db")
    rows = conn.execute("SELECT DISTINCT local_gove FROM parcels;").fetchall()
    conn.close()
    return rows
