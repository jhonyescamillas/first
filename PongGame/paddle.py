from turtle import Turtle

class Paddle(Turtle):
    """
    A class representing a paddle. Inherits from Turtle class.
    """
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.x = x
        self.y = y
        self.goto(self.x, self.y)

    def move_up(self):
        self.y += 20
        self.goto(self.x, self.y)

    def move_down(self):
        self.y -= 20
        self.goto(self.x, self.y)
