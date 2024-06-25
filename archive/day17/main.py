from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []

for question in question_data:
    new_question = Question(question['question'], question['correct_answer'])
    # print(new_question)
    questions.append(new_question)


game = QuizBrain(questions)


while game.still_has_questions():
    game.next_question()

print(f"Quiz complete, your score is {game.show_score()}")