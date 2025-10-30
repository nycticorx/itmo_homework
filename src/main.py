from extract import extract_data
from transform import transform_data_types, clean_data, validate_data
from load import save_data_to_parquet, write_data_to_database, get_db_connection

def main():
    df = extract_data("input.csv")
    df = transform_data_types(df)
    df = clean_data(df)

    if not validate_data(df):
        raise ValueError("Ошибка валидации данных")

    save_data_to_parquet(df, "data/processed_data.parquet")

    conn = get_db_connection(".env", "gabdrakhmanova")
    write_data_to_database(df.head(100), conn)

if __name__ == "__main__":
    main()
