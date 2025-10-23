# write_to_db.py

import pandas as pd
import sqlite3
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

#  1. Читаем учетные данные из SQLite 
sqlite_path = r"C:\Users\malin\Downloads\creds.db"
conn = sqlite3.connect(sqlite_path)
cursor = conn.cursor()
cursor.execute("SELECT url, port, user, pass FROM access LIMIT 1")
db_url, db_port, db_user, db_password = cursor.fetchone()
conn.close()

# 2. Подключаемся к PostgreSQL 
db_name = "homeworks"
engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_name}"
)

# 3. Загружаем свой датасет 
df = pd.read_parquet(r"C:\Users\malin\my_project\my_project.parquet")
df = df.head(100)  # максимум 100 строк
df.columns = [col.lower() for col in df.columns]

# 4. Записываем данные в таблицу с вашей фамилией 
my_table_name = "gabdrakhmanova"  
df.to_sql(
    name=my_table_name,
    con=engine,
    schema="public",
    if_exists="replace",
    index=False
)

#  5. Добавляем комментарий на таблицу 
with engine.begin() as conn:
    conn.execute(
        text(f"COMMENT ON TABLE public.{my_table_name} IS 'Таблица с анкетами и выборкой смартфон-зависимости")
    )

print(f"Данные успешно загружены в таблицу {my_table_name}")

#  6. Проверяем первые 5 строк таблицы 
with Session(engine) as session:
    result = session.execute(text(f"SELECT * FROM public.{my_table_name} LIMIT 5"))
    rows = result.fetchall()
    print("\nПервые 5 строк таблицы:")
    for row in rows:
        print(row)
