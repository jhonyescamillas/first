from turtle import Turtle

FONTSTYLE = ("Courier", 16, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    """A class the represents the scoreboard. It inherits from the Turtle class.
    This class shows the current level that the player is at."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-220, 270)
        self.display()

    def display(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONTSTYLE)

    def update(self):
        self.level += 1
        self.clear()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONTSTYLE)
