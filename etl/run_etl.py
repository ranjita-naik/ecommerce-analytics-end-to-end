from etl.extract import load_raw_datasets
from etl.transform import transform, create_dim_customers, create_dim_products, create_dim_time
from etl.load_sqlite import load_to_sqlite

def main():
    dfs = load_raw_datasets()
    
    # Fact table
    fact_orders = transform(dfs)
    
    # Dimensions
    dim_customers = create_dim_customers(dfs)
    dim_products  = create_dim_products(dfs)
    dim_time      = create_dim_time(fact_orders)

    # Load all tables
    load_to_sqlite(fact_orders, dim_customers, dim_products, dim_time)

if __name__ == "__main__":
    main()

