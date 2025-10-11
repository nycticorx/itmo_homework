import requests
import pandas as pd

URL = "https://valorant-api.com/v1/agents"

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
