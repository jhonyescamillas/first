from random import randrange
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.respawn()

    def respawn(self):
        random_pos = (randrange(-280, 300, 20), randrange(-280, 300, 20))
        self.goto(random_pos)
