import json


def main():
    print("1. Add actions\n2. Read actions")
    choice = (int(input("\nEnter choice: ")))

    if (choice == 1):
        add_actions()
    elif (choice == 2):
        user_id = "1085820194334703666"
        read_actions(user_id)


def read_actions(user_id):
    with open("data.json", "r") as file:
        data = json.load(file)

    user_data = data.get(user_id, {})
    total_score = user_data.get("total_score", 0)
    actions = user_data.get("actions", {})

    print(f"User ID: {user_id}")
    print(f"Total Score: {total_score}")
    print("Actions:")
    for action, points in actions.items():
        print(f"{action}    {points}")


def add_actions():
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


if __name__ == "__main__":
    main()
