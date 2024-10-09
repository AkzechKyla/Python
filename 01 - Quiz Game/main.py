from data import questions_data
from question import Question
from quiz import Quiz

questions = []

for question in questions_data:
    question_text = question["question"]
    question_choices = question["choices"]
    question_answers = question["answer"]

    new_question = Question(question_text, question_choices, question_answers)
    questions.append(new_question)

quiz = Quiz(questions)

while quiz.still_has_questions():
    quiz.next_question()
