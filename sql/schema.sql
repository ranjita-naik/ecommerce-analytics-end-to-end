-- Fact table for order-level analytics
CREATE TABLE fact_orders (
    order_id TEXT,
    customer_id TEXT,
    order_status TEXT,

    order_purchase_timestamp TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP,

    revenue REAL,
    payment_count INTEGER,

    delivery_delay_days INTEGER,
    order_to_delivery_days INTEGER,

    review_score INTEGER,

    customer_city TEXT,
    customer_state TEXT,

    product_id TEXT,
    product_category_name TEXT,

    purchase_month TEXT
);

-- Dim Customers
CREATE TABLE dim_customers (
    customer_id TEXT,
    customer_unique_id TEXT,
    city TEXT,
    state TEXT
);

-- Dim Products
CREATE TABLE dim_products (
    product_id TEXT,
    product_category_name TEXT
);

-- Dim Time
CREATE TABLE dim_time (
    date DATE,
    date_key TEXT,
    year INTEGER,
    month INTEGER,
    month_name TEXT,
    day INTEGER,
    weekday TEXT
);
