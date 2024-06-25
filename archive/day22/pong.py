from turtle import *
from paddle import Paddle
from score import Score
from ball import Ball

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

score = Score()

ball = Ball()

right_player = Paddle(360)
left_player = Paddle(-360)

screen.onkeypress(fun=right_player.move_up, key="Up")
screen.onkeypress(fun=right_player.move_down, key="Down")
#
screen.onkeypress(fun=left_player.move_up, key="w")
screen.onkeypress(fun=left_player.move_down, key="s")

playing = True
while playing:
    screen.update()
    ball.move()
    if (ball.ycor() >= 290) or (ball.ycor() <= -290):
        ball.bounce_y()

    if ball.xcor() >= 400:
        score.increase_score_left()
        ball.restart()

    if ball.xcor() <= -400:
        score.increase_score_right()
        ball.restart()

    ball.hit_paddle(right_player)
    ball.hit_paddle(left_player)

screen.exitonclick()

# 1. Create a bat which moved up and down (not beyond top and bottom)
# 2. create a table with a centre line
# 3. create a ball that spawns in the center and moves in a random direction
# 4. create score board
# 5. bake ball bounce of wall and bat
# 6. increment score when player misses bat
