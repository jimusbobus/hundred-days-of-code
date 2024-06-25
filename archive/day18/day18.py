import random
import turtle
from turtle import *
import colorgram


def draw_shape(_sides, _turtle: Turtle):
    _angle = 360 / _sides
    for side in range(_sides):
        _turtle.forward(100)
        _turtle.right(_angle)


def draw_some_shapes(_turtle: Turtle, _colours: list[str]):
    _initial_shape_sides = 3
    _total_shapes = 6
    for _sides in range(_initial_shape_sides, _total_shapes + _initial_shape_sides):
        _turtle.color(random.choice(colors))
        draw_shape(_sides, _turtle)


def random_colour():
    return random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)


def random_walk(_turtle: Turtle, _length):
    for _ in range(_length):
        direction = int(random.choice([0, 90, 180, 270]))
        _turtle.pencolor(random_colour())
        _turtle.pensize(15)
        _turtle.setheading(direction)
        _turtle.forward(20)
        _turtle.speed("fastest")


def draw_spirograph(_turtle: Turtle):
    _size_of_gap = 5
    _turtle.speed("fastest")
    for _heading in range(0, 360, _size_of_gap):
        _turtle.pensize(30)
        _turtle.pencolor(random_colour())
        _turtle.setheading(_heading)
        _turtle.circle(100)


def draw_dot():
    print("fred")


tim = Turtle()
colormode(255)
screen = Screen()

draw_spirograph(tim)

# # Closes the window.
screen.exitonclick()
