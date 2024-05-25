from turtle import Turtle

FONTSTYLE = ("Courier", 80, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.lscore = 0
        self.rscore = 0

    def display(self):
        self.goto(-100, 190)
        self.write(self.lscore, align=ALIGNMENT, font=FONTSTYLE)
        self.goto(100, 190)
        self.write(self.rscore, align=ALIGNMENT, font=FONTSTYLE)

    def add_lscore(self):
        self.lscore += 1
        self.clear()

    def add_rscore(self):
        self.rscore += 1
        self.clear()