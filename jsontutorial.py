import json

try:
    with open("data.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}

user_id = input("User ID: ")

if user_id not in data:
    data[user_id] = {
        "total_score": 100,
        "actions": {}
    }

action = input("Action: ")
points = int(input("Points: "))

data[user_id]["actions"][action] = points

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
