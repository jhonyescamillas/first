from turtle import Turtle

ALIGNMENT = "center"
FONTSTYLE = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.ht()
        self.goto(0, 265)
        with open("data.txt") as data:
            self.highscore = int(data.read())

    def display(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONTSTYLE)

    def add_score(self):
        self.score += 1

    def update_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("data.txt", "w") as data:
            data.write(str(self.highscore))
