class Quiz:
    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def test(self):
        for question in self.questions:
            print(question.question)
            print("\n".join(question.choices))
            print()
