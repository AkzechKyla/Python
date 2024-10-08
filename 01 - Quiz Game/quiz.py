class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def test(self):
        for question in self.questions:
            print(question.question)
            print("\n".join(question.choices))
            print()
