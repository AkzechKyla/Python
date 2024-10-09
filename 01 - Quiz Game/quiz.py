class Quiz:
    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1

        print(f"\n{self.question_number}. {current_question.question}")
        print("\n".join(current_question.choices))
        user_input = input("Your answer: ")

    def test(self):
        for question in self.questions:
            print(question.question)
            print("\n".join(question.choices))
            print()
