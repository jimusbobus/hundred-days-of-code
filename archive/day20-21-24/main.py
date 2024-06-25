from turtle import *
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=605, height=605)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")

moving = True
while moving:
    screen.update()
    time.sleep(snake.speed)

    snake.move()

    if snake.collision():
        scoreboard.reset()
        snake.reset()

    if snake.head.distance(food.position()) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

screen.exitonclick()
