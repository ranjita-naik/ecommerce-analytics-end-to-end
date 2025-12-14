import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("data/ecommerce.db")

def load_to_sqlite(df: pd.DataFrame):
    conn = sqlite3.connect(DB_PATH)

    df.to_sql(
        "fact_orders",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()
    print("✅ Loaded data into SQLite")

