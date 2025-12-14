import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("data/ecommerce.db")

def load_to_sqlite(fact_orders, dim_customers, dim_products, dim_time):
    conn = sqlite3.connect(DB_PATH)

    fact_orders.to_sql("fact_orders", conn, if_exists="replace", index=False)
    dim_customers.to_sql("dim_customers", conn, if_exists="replace", index=False)
    dim_products.to_sql("dim_products", conn, if_exists="replace", index=False)
    dim_time.to_sql("dim_time", conn, if_exists="replace", index=False)

    conn.close()
    print("✅ Loaded fact + dimension tables into SQLite")

