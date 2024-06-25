import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

car_speed = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    screen.update()

    car_manager.move_cars()

    if car_manager.has_collided(player):
        game_is_on = False

    if player.road_crossed():
        scoreboard.increase_level()
        player.reset_player()
        car_manager.create_car()
        car_speed *= 0.9

scoreboard.game_over()
screen.exitonclick()