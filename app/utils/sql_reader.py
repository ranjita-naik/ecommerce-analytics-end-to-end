from pathlib import Path
import sqlite3
import pandas as pd

# Resolve project root reliably on Streamlit Cloud and locally
BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "data" / "ecommerce.db"

def run_query(sql: str) -> pd.DataFrame:
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df

