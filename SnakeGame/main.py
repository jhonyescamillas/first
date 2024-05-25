"""
Play the classic game of Snake. data.txt saves the highscore record that will be displayed
each time the program is run.
"""

import turtle
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

scoreboard = Scoreboard()


def snake_on():
    screen = turtle.Screen()
    screen.clear()
    scoreboard.score = 0
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    snake = Snake()
    food = Food()
    game_on = True
    while game_on:
        # display the scoreboard up top
        scoreboard.display()
        screen.update()
        # add 0.1-second delay in between each screen update
        time.sleep(0.1)
        # initialize snake movement
        snake.move()
        # screen will begin waiting for key press
        screen.listen()
        screen.onkey(snake.move_up, "Up")
        screen.onkey(snake.move_left, "Left")
        screen.onkey(snake.move_right, "Right")
        screen.onkey(snake.move_down, "Down")
        # detect collision with food
        if snake.snake_head.distance(food) < 10:
            # update the scoreboard and display updated score
            scoreboard.add_score()
            # food will go to another random position
            food.respawn()
            # a new square will be added to the body of the snake
            snake.extend()
        # detect collision with wall
        if abs(snake.snake_head.xcor()) > 290 or abs(snake.snake_head.ycor()) > 290:
            scoreboard.update_highscore()
            snake_on()
        # detect collision with tail
        for square in snake.squares[1:]:
            if snake.snake_head.distance(square) < 15:
                scoreboard.update_highscore()
                snake_on()
    screen.exitonclick()


snake_on()
