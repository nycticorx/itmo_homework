import argparse
from extract import extract_data
from transform import transform_data
from load import load_to_db_and_parquet
from validate import validate_dataframe

def main():
    parser = argparse.ArgumentParser(description="ETL pipeline: extract → transform → load")
    parser.add_argument("--file-id", required=True, help="ID файла Google Drive для загрузки")
    args = parser.parse_args()

    print("🚀 Запуск ETL процесса...")
    df_raw = extract_data(args.file_id)
    validate_dataframe(df_raw)
    df_transformed = transform_data(df_raw)
    validate_dataframe(df_transformed)
    load_to_db_and_parquet(df_transformed)
    print("🎉 ETL процесс успешно завершён!")

if __name__ == "__main__":
    main()
