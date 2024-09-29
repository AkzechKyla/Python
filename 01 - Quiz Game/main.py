from data import questions_data

for question in questions_data:
    print(question["question"])
    print("\n".join(question["choices"]))
    print()
