import pandas as pd
from pathlib import Path

RAW_DATA_DIR = Path("data/raw")

def load_raw_datasets():
    """
    Load raw Olist CSV files from data/raw
    """
    datasets = {
        "orders": "olist_orders_dataset.csv",
        "items": "olist_order_items_dataset.csv",
        "customers": "olist_customers_dataset.csv",
        "payments": "olist_order_payments_dataset.csv",
        "reviews": "olist_order_reviews_dataset.csv",
        "products": "olist_products_dataset.csv",
    }

    dfs = {}
    for name, file in datasets.items():
        path = RAW_DATA_DIR / file
        if not path.exists():
            raise FileNotFoundError(f"Missing file: {path}")
        dfs[name] = pd.read_csv(path)

    return dfs

