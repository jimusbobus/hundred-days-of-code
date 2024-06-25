from turtle import Turtle
import random
from typing import List

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_CARS = 10


class CarManager:
    def __init__(self):
        self.cars: List[Turtle] = []
        for _ in range(START_CARS):
            self.create_car()

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.turtlesize(stretch_wid=1, stretch_len=2)
        new_car.goto(random.randint(-250, 250), random.randint(-250, 250))
        new_car.setheading(180)
        new_car.speed("fastest")
        self.cars.append(new_car)

    def move_cars(self):
        for _car in self.cars:
            _car.forward(MOVE_INCREMENT)
            # if the _car is at the end of the screen reset it to the far right.
            if _car.xcor() <= -280:
                _car.goto(280, random.randint(-280, 280))
                _car.color(random.choice(COLORS))

    def has_collided(self, _turtle: Turtle):
        for _car in self.cars:
            if _turtle.distance(_car) <= 20:
                return True
        return False
