from turtle import Turtle
from random import choice

INITIAL_HEADING = (25, 40, 115, 130, 205, 220, 295, 305)


class Ball(Turtle):
    """A class representing a ball. Inherits from the Turtle class"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.movespeed = 0.05
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setheading(choice(INITIAL_HEADING))

    def move(self):
        """make the ball move by 10 paces each time"""
        self.forward(10)

    def wall_bounce(self):
        """Make the ball bounce when it hits the top/bottom wall.
        360degrees - current heading"""
        new_heading = -self.heading()
        self.setheading(new_heading)

    def paddle_bounce(self):
        """Make the ball bounce when it hits the top/bottom wall.
        180degrees - current heading"""
        self.setheading(180 - self.heading())
        self.movespeed *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.movespeed = 0.05
        self.setheading(180 - self.heading())
