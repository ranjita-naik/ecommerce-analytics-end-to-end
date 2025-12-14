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


def create_dim_customers(dfs):
    customers = dfs["customers"].copy()
    dim_customers = customers.rename(columns={
        "customer_unique_id": "customer_unique_id",
        "customer_city": "city",
        "customer_state": "state",
    })
    dim_customers = dim_customers[["customer_id", "customer_unique_id", "city", "state"]]
    return dim_customers


def create_dim_products(dfs):
    products = dfs["products"].copy()
    dim_products = products[[
        "product_id",
        "product_category_name"
    ]]
    return dim_products


def create_dim_time(df):
    # Extract DATE only (drop timestamp)
    df["order_date"] = df["order_purchase_timestamp"].dt.date

    min_date = df["order_date"].min()
    max_date = df["order_date"].max()

    # Build proper date range (pure date, no time)
    time_df = pd.DataFrame({
        "date": pd.date_range(min_date, max_date)
    })

    time_df["date_key"] = time_df["date"].dt.strftime("%Y%m%d")
    time_df["year"]     = time_df["date"].dt.year
    time_df["month"]    = time_df["date"].dt.month
    time_df["month_name"] = time_df["date"].dt.strftime("%B")
    time_df["day"]      = time_df["date"].dt.day
    time_df["weekday"]  = time_df["date"].dt.strftime("%A")

    return time_df

