import pandas as pd

def transform(dfs: dict) -> pd.DataFrame:
    orders = dfs["orders"].copy()
    items = dfs["items"].copy()
    customers = dfs["customers"].copy()
    payments = dfs["payments"].copy()
    reviews = dfs["reviews"].copy()
    products = dfs["products"].copy()

    # ---- Parse dates ----
    date_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]

    for c in date_cols:
        orders[c] = pd.to_datetime(orders[c], errors="coerce")

    # ---- Aggregate payments ----
    payment_agg = (
        payments
        .groupby("order_id")
        .agg(
            revenue=("payment_value", "sum"),
            payment_count=("payment_sequential", "max")
        )
        .reset_index()
    )

    # ---- Merge core tables ----
    df = (
        orders
        .merge(customers, on="customer_id", how="left")
        .merge(items, on="order_id", how="left")
        .merge(products, on="product_id", how="left")
        .merge(reviews[["order_id", "review_score"]], on="order_id", how="left")
        .merge(payment_agg, on="order_id", how="left")
    )

    # ---- Feature engineering ----
    df["delivery_delay_days"] = (
        df["order_delivered_customer_date"]
        - df["order_estimated_delivery_date"]
    ).dt.days

    df["order_to_delivery_days"] = (
        df["order_delivered_customer_date"]
        - df["order_purchase_timestamp"]
    ).dt.days

    df["purchase_month"] = (
        df["order_purchase_timestamp"]
        .dt.to_period("M")
        .astype(str)
    )

    return df

