from etl.extract import load_raw_datasets
from etl.transform import transform
from etl.load_sqlite import load_to_sqlite

def main():
    dfs = load_raw_datasets()
    df = transform(dfs)
    load_to_sqlite(df)

if __name__ == "__main__":
    main()
