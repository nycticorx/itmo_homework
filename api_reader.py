import requests
import pandas as pd

# URL неофициального Valorant API
URL = "https://valorant-api.com/v1/agents"  # пример эндпоинта для агентов

def get_data(url):
    response = requests.get(url, headers={"Content-Type": "application/json"})
    try:
        return response.json()  # вернёт словарь
    except ValueError:
        print(response.text[:500])
        return None

def main():
    data = get_data(URL)
    if not data:
        return

    # Обычно API Valorant возвращает словарь с ключом 'data', который содержит список агентов
    agents = data.get('data', [])

    # Превратим в DataFrame с нужными колонками
    df = pd.DataFrame([{
        "name": agent.get("displayName"),
        "role": agent.get("role", {}).get("displayName") if agent.get("role") else None,
        "developerName": agent.get("developerName"),
        "uuid": agent.get("uuid")
    } for agent in agents])
    
    print(df.head(10))

if __name__ == "__main__":
    main()
