import requests
import pandas as pd

URL = "https://valorant-api.com/v1/agents"

try:
    response = requests.get(URL, headers={"Content-Type": "application/json"}, timeout=10)
    response.raise_for_status()  # проверяем, что статус ответа 200 (OK)
except requests.exceptions.HTTPError as http_err:
    print(f"Ошибка HTTP: {http_err}")
    data = {}
except requests.exceptions.ConnectionError:
    print("Ошибка соединения: не удалось подключиться к API.")
    data = {}
except requests.exceptions.Timeout:
    print("Ошибка: время ожидания запроса истекло.")
    data = {}
except requests.exceptions.RequestException as err:
    print(f"Произошла ошибка: {err}")
    data = {}
else:
    try:
        data = response.json()
    except ValueError:
        print("Ошибка: не удалось декодировать JSON-ответ от API.")
        data = {}
           
response = requests.get(URL, headers={"Content-Type": "application/json"})
data = response.json()

agents = data.get("data", [])

df = pd.DataFrame([
    {
        "name": agent.get("displayName"),
        "role": agent.get("role", {}).get("displayName") if agent.get("role") else None,
        "developerName": agent.get("developerName"),
        "uuid": agent.get("uuid")
    }
    for agent in agents
])

print(df.head(10))
