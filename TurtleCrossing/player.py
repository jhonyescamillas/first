from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    """A class that represents the player (user). It inherits from the Turtle class
    This class controls the movement and position of the player."""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.move_to_start()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_to_start(self):
        self.goto(STARTING_POSITION)
