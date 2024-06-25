from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")


class QuizUI:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiziness")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white", bd=0, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.question_text = self.canvas.create_text(125, 150,
                                                     width=250,
                                                     text="Question:",
                                                     font=QUESTION_FONT,
                                                     fill="black")

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, bg='green', bd=0, highlightthickness=0, command=self.true)
        self.true_button.grid(column=0, row=2)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, bg='red', bd=0, highlightthickness=0, command=self.false)
        self.false_button.grid(column=1, row=2)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.next_question()
        self.window.mainloop()

    def false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        # self.score_label.config(text=f"Score: {self.quiz.score}")

    def true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        # self.score_label.config(text=f"Score: {self.quiz.score}")

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz complete")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.next_question)
