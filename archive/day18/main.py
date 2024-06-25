import colorgram
import random
from turtle import *
import math


def generate_colours():
    global rgb_colors, rgb_tuple_colors
    rgb_colors = []
    rgb_tuple_colors = []
    colors = colorgram.extract('image.jpg', 15)
    for color in colors:
        if (color.rgb.r > 230) and (color.rgb.r > 230) and (color.rgb.r > 230):
            print("Colour probably near white, ignore")
        else:
            rgb_colors.append(color.rgb)
            rgb_tuple_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

    print(rgb_tuple_colors)
    print(rgb_colors)


def draw_line_of_dots(_turtle: Turtle, _length):
    for i in range(_length):
        _turtle.dot(20, random.choice(colours))
        if i != (_length - 1):
            _turtle.forward(50)


def about_turn(_turtle: Turtle):
    is_east = _turtle.heading() == 0
    _turtle.setheading(90)
    _turtle.forward(50)
    if is_east:
        _turtle.setheading(180)
    else:
        _turtle.setheading(0)


def hurst_it(_turtle: Turtle, _size):
    _dot_diameter = 20
    _dot_gap = 50
    _partition = ((_dot_gap - (_dot_diameter / 4)) * _size) / 2
    # print(f"DEBUG: _partition: {_partition}")
    _initial_distance = math.sqrt((_partition ** 2) + (_partition ** 2))
    _initial_direction = 225
    # print(f"DEBUG: _initial_distance: {_initial_distance}")
    _turtle.penup()
    _turtle.setheading(_initial_direction)
    _turtle.forward(_initial_distance)
    _turtle.setheading(0)
    for _ in range(_size):
        draw_line_of_dots(_turtle, _size)
        about_turn(_turtle)


# generate_colours()
colours = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
           (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149)]

# Paint a painting with 10x 10 spots
# dot diameter is 20
# space is 50

tim = Turtle()
tim.speed("fastest")
colormode(255)
screen = Screen()

hurst_it(tim, 25)

# # Closes the window.
screen.exitonclick()
