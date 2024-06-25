from turtle import Turtle
from typing import List

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_length = 0
        self.initial_snake_length = 3
        self.speed = 0.15
        self.segments: List[Turtle] = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for i in range(0, self.initial_snake_length):
            _pos = (i * (MOVE_DISTANCE * -1), 0)
            self.add_segment(_pos)
        self.head = self.segments[0]

    def add_segment(self, _pos):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(_pos)
        self.segments.append(turtle)
        self.snake_length += 1

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
            # print(
            #     f"DEBUG: seg_num = {seg_num}, xcor = {self.segments[seg_num].xcor()}, "
            #     f"ycor = {self.segments[seg_num].ycor()}")
        self.head.forward(MOVE_DISTANCE)

    def collision(self):
        if self.collision_wall() or self.collision_self():
            # print(f"DEBUG: hit wall or self, {self.head.pos()}")
            return True
        return False

    def extend(self):
        self.speed -= 0.01
        self.add_segment(self.segments[-1].position())

    def collision_wall(self):
        _hit_right_wall = (self.head.xcor() + MOVE_DISTANCE) > 300
        # print(f"DEBUG: Hit right wall = {_hit_right_wall}")
        _hit_top_wall = (self.head.ycor() + (MOVE_DISTANCE / 2)) > 300
        _hit_left_wall = (self.head.xcor() - MOVE_DISTANCE) < -300
        # print(f"DEBUG: Hit left wall = {_hit_left_wall}")
        _hit_bottom_wall = (self.head.ycor() - (MOVE_DISTANCE / 2)) < -300
        # print(f"DEBUG: Hit bottom wall = {_hit_bottom_wall}")
        return _hit_right_wall or _hit_top_wall or _hit_left_wall or _hit_bottom_wall

    def up(self):
        # print("DEBUG: UP")
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # print("DEBUG: DOWN")
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # print("DEBUG: LEFT")
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # print("DEBUG: RIGHT")
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def collision_self(self):
        for _segment in self.segments[1:]:
            if self.head.distance(_segment) < 10:
                return True
        return False

    def reset(self):
        for _segment in self.segments:
            _segment.goto(1000, 1000)
        self.segments: List[Turtle] = []
        self.speed = 0.15
        self.create()
