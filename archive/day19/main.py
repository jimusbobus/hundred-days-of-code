import random
from turtle import *

screen = Screen()

# def move_backward():
#     tim.backward(10)
#
#
# def move_forward():
#     tim.forward(10)
#
#
# def move_left():
#     tim.left(10)
#
#
# def move_right():
#     tim.right(10)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(fun=move_forward, key="w")
# screen.onkey(fun=move_backward, key="s")
# screen.onkey(fun=move_left, key="a")
# screen.onkey(fun=move_right, key="d")
# screen.onkey(fun=clear, key="c")
turtle_racers = []


def random_turtle_move():
    _end_line = 220
    _turtle = random.choice(turtle_racers)
    _distance = random.randrange(0, 10)
    _turtle.forward(_distance)
    # print(f"DEBUG: turtle: {_turtle.color()}, x: {_turtle.xcor()}")
    if _turtle.xcor() >= _end_line:
        return _turtle


screen.setup(width=500, height=400)

colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Brown"]
starting_line = -240
starting_position = -150
for colour in colours:
    turtle = Turtle("turtle")
    turtle.color(colour.lower())
    turtle.penup()
    turtle.goto(x=starting_line, y=starting_position)
    turtle_racers.append(turtle)
    starting_position += 60

user_bet = screen.textinput("Make a bet", "Choose a colour!!")

racing = False

if user_bet:
    racing = True

while racing:
    winning_turtle = random_turtle_move()
    if winning_turtle:
        bet_won = winning_turtle.pencolor().lower() == user_bet.lower()
        print(f"The winner is {winning_turtle.color()}, Bet won: {bet_won}")
        racing = False

screen.exitonclick()
