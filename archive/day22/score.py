from turtle import *


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(75, 250)
        self.write(f"{self.p1_score}", align="left", font=("Arial", 48, "normal"))
        self.goto(-75,250)
        self.write(f"{self.p2_score}", align="right", font=("Arial", 48, "normal"))

    def increase_score_left(self):
        self.p1_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_right(self):
        self.p2_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
