class Quiz:
    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions

        self.current_question = self.questions[self.question_number]
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def next_question(self):
        self.question_number += 1

        if self.still_has_questions():
            self.current_question = self.questions[self.question_number]

    def display_question(self):
        print(f"\n{self.question_number + 1}. {self.current_question.question}")
        print("\n".join(self.current_question.choices))

    def check_answer(self, user_input):
        if self.current_question.answer == user_input.upper():
            self.score += 1

    def show_total_score(self):
        print(f"\nYou got {self.score}/{len(self.questions)} correct answers!")
