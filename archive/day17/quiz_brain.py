from question_model import Question


class QuizBrain:
    def __init__(self, _questions: list[Question]):
        self.questions = _questions
        self.question_number = 0
        self.score = 0

    def next_question(self):
        _current_question = self.questions[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {_current_question.text}. (True/False)")
        self.check_answer(answer, _current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def check_answer(self, u_answer, q_answer):
        if u_answer == q_answer:
            print("Correct")
            self.score += 1
        else:
            print("Wrong")
        print(f"The correct answer was: {q_answer}")
        print(f"Score is: {self.show_score()}\n")

    def show_score(self):
        return f"{self.score}/{self.question_number}"
