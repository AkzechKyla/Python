class Quiz:
    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1

        print(f"\n{self.question_number}. {current_question.question}")
        print("\n".join(current_question.choices))
        user_input = input("Your answer: ")

        self.check_answer(current_question, user_input)

    def check_answer(self, current_question, user_input):
        if current_question.answer == user_input.upper():
            self.score += 1

    def show_total_score(self):
        print(f"\nYou got {self.score}/{len(self.questions)} correct answers!")
