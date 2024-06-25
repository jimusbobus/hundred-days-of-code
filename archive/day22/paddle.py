from turtle import Turtle

MOVE_DISTANCE = 20
PADDLE_LENGTH = 5


class Paddle(Turtle):
    def __init__(self, _xcor):
        super().__init__("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(_xcor, 0)

    def move_up(self):
        # print(f"DEBUG: Paddle Up y_core={self.ycor()}")
        if self.ycor() <= 250:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        # print(f"DEBUG: Paddle Down y_core={self.ycor()}")
        if self.ycor() >= -220:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)


