# extract.py
import pandas as pd
import os

def extract_data(file_id: str, output_path: str = "data/raw/raw_data.csv") -> pd.DataFrame:
    """
    Загружает данные с Google Drive по ID файла и сохраняет их в data/raw.
    """
    try:
        file_url = f"https://drive.google.com/uc?id={file_id}"
        print(f"Загрузка данных из {file_url}...")
        df = pd.read_csv(file_url)
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"✅ Исходные данные сохранены в {output_path}")
        return df
    except Exception as e:
        raise RuntimeError(f"Ошибка при загрузке данных: {e}")
