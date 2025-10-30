import pandas as pd
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from dotenv import load_dotenv

def main():
    try:
        # 1. Загружаем переменные из .env файла
        env_path = r"C:\Users\malin\my_project\write_to_db.env"
        load_dotenv(env_path)
        
        # 2. Читаем учетные данные из .env
        db_url = os.getenv("DB_URL")
        db_port = os.getenv("DB_PORT")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME", "homeworks")
        
        print("Учетные данные загружены из .env")

        # 3. Подключаемся к PostgreSQL 
        engine = create_engine(
            f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_name}"
        )
        
        # Проверяем подключение
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ Подключение к PostgreSQL установлено")
        
        # 4. Загружаем датасет 
        df = pd.read_parquet(r"C:\Users\malin\my_project\my_project.parquet")
        df = df.head(100)  # максимум 100 строк
        df.columns = [col.lower() for col in df.columns]
        print(f"✅ Датасет загружен: {len(df)} строк, {len(df.columns)} столбцов")
        
        # 5. Записываем данные в таблицу с фамилией 
        my_table_name = "gabdrakhmanova"  
        df.to_sql(
            name=my_table_name,
            con=engine,
            schema="public",
            if_exists="replace",
            index=False
        )
        print(f"✅ Данные записаны в таблицу {my_table_name}")
        
        # 6. Добавляем комментарий на таблицу 
        with engine.begin() as conn:
            conn.execute(
                text(f"COMMENT ON TABLE public.{my_table_name} IS 'Таблица с анкетами и выборкой смартфон-зависимости'")
            )
        print("✅ Комментарий к таблице добавлен")
        
        # 7. Проверяем первые 5 строк таблицы 
        with Session(engine) as session:
            result = session.execute(text(f"SELECT * FROM public.{my_table_name} LIMIT 5"))
            rows = result.fetchall()
            print(f"\nПервые 5 строк таблицы {my_table_name}:")
            for i, row in enumerate(rows, 1):
                print(f"Строка {i}: {row}")
                
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    main()