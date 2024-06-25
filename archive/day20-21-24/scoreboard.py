from turtle import *

HIGH_SCORE_FILE = "data.txt"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        with open(HIGH_SCORE_FILE, mode='r') as _file:
            self.high_score = _file.read()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score  = {self.score}, High Score = {self.high_score}", align="center",
                   font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = str(self.score)
            self.persist_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def persist_high_score(self, _score):
        with open(HIGH_SCORE_FILE, mode='w') as _file:
            _file.write(_score)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
