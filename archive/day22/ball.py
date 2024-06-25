from turtle import *
from paddle import Paddle
import random as r
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.ball_speed = 20

    def restart(self):
        self.goto(0, r.randint(-100, 100))
        self.ball_speed = 50
        self.bounce_x()

    def move(self):
        seconds = self.ball_speed / 1000.0
        time.sleep(seconds)
        _xcor = self.xcor() + self.x_move
        _ycor = self.ycor() + self.y_move
        self.goto(_xcor, _ycor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def hit_paddle(self, _paddle: Paddle):
        # print(f"BALL X = {self.xcor()}")
        # print(f"BALL Y = {self.ycor()}")
        # print(f"PADDLE X = {_paddle.xcor()}")
        # print(f"PADDLE Y = {_paddle.ycor()}")
        # print(f"DISTANCE = {_paddle.distance(self)}")

        if (self.distance(_paddle) < 50) and (abs(self.xcor()) >= 340):
            print("CONTACT")
            self.bounce_x()
            self.ball_speed *= 0.9
