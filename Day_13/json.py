import json

data = {
    "name": "Rashidul",
    "age": 23 }

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)