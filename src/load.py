# load.py
import pandas as pd
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from dotenv import load_dotenv

def load_to_db_and_parquet(df: pd.DataFrame, parquet_path: str = "data/processed/processed_data.parquet"):
    """
    Сохраняет данные в .parquet и записывает в PostgreSQL (max 100 строк).
    """
    try:
        os.makedirs(os.path.dirname(parquet_path), exist_ok=True)
        df.to_parquet(parquet_path, index=False)
        print(f"✅ Данные сохранены в {parquet_path}")

        # Загружаем переменные окружения
        load_dotenv("write_to_db.env")

        db_url = os.getenv("DB_URL")
        db_port = os.getenv("DB_PORT")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME", "homeworks")

        # Подключаемся к БД
        engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_name}")
        df = df.head(100)
        df.columns = [col.lower() for col in df.columns]
        
        table_name = "gabdrakhmanova"
        df.to_sql(name=table_name, con=engine, schema="public", if_exists="replace", index=False)
        print(f"✅ Данные записаны в таблицу {table_name}")

        # Проверяем первые 5 строк
        with Session(engine) as session:
            result = session.execute(text(f"SELECT * FROM public.{table_name} LIMIT 5"))
            rows = result.fetchall()
            print("🔍 Проверка данных в таблице:")
            for row in rows:
                print(row)
    except Exception as e:
        raise RuntimeError(f"Ошибка при выгрузке данных: {e}")
