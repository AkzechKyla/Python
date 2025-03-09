import os
import json

directory_path = "../SnakeDataCollection/"

for filename in os.listdir(directory_path):
    if filename.endswith(".json"):
        with open(
            os.path.join(directory_path, filename), "r", encoding="utf-8"
        ) as file:
            data = json.load(file)
            print(f"Loaded {len(data)} URLs from {filename}")
