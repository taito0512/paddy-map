import pandas as pd
import sqlite3

def import_csv(csv_path,db_path):
    COLUMNS = ["polygon_uu", "point_lat", "point_lng", "final_label", "stage2_prob", "local_gove"]
    df = pd.read_csv(csv_path)
    df=df[COLUMNS]

    conn = sqlite3.connect(db_path)
    conn.executemany(
        "INSERT OR REPLACE INTO parcels (polygon_uu, point_lat, point_lng, final_label, stage2_prob, local_gove) VALUES (?, ?, ?, ?, ?, ?)",df.values.tolist()
    )
    conn.commit()
    conn.close()



if __name__ == "__main__":
    import_csv("data/sample.csv", "data/paddy.db")
