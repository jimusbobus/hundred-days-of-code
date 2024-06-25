from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.setheading(90)
        self.color("black")
        self.penup()
        self.reset_player()

    def reset_player(self):
        self.goto(0, -280)

    def move(self):
        self.forward(20)

    def road_crossed(self):
        if self.ycor() >= 280:
            return True
        return False
