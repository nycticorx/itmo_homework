
import pandas as pd

def validate_dataframe(df: pd.DataFrame):
    """
    Проверка корректности DataFrame.
    """
    if df.empty:
        raise ValueError("DataFrame пуст!")
    if df.isnull().all().any():
        print("⚠️ Внимание: некоторые столбцы содержат только NaN.")
    print("✅ Валидация пройдена успешно.")
