from turtle import Turtle
from random import choice, randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """A class that manages the creating of cars as Turtle class instances. It also controls the movement and
    the speed at which the cars move."""
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(280, randrange(-240, 240, 30))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
