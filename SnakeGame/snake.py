from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.snake_head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.make_squares(position)

    def make_squares(self, position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def move(self):
        for num in range(len(self.squares) - 1, 0, -1):
            new_position = self.squares[num - 1].pos()
            self.squares[num].goto(new_position)
        self.squares[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def move_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def move_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def extend(self):
        self.make_squares(self.squares[-1].position())
