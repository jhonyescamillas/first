import turtle
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


def main():
    # create the screen (pong table)
    screen = turtle.Screen()
    screen.title("Pong Game")
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.tracer(0)
    # create paddle instances
    left_paddle = Paddle(-350, 0)
    right_paddle = Paddle(350, 0)
    scoreboard = Scoreboard()
    # create ball instance
    ball = Ball()

    screen.listen()
    # bind movement keys
    screen.onkeypress(left_paddle.move_up, "w")
    screen.onkeypress(left_paddle.move_down, "s")
    screen.onkeypress(right_paddle.move_up, "Up")
    screen.onkeypress(right_paddle.move_down, "Down")

    game_on = True
    current_time = time.time()
    # refers to ball.paddle_bounce function which can only be activated
    # once every 3 seconds to avoid multiple bounces off the paddle
    can_activate = True
    while game_on:
        scoreboard.display()
        time.sleep(ball.movespeed)
        screen.update()
        ball.move()
        # make the ball move
        # detect collision with upper wall and bottom wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.wall_bounce()
        # detect collision with paddles
        if (
            (ball.distance(right_paddle) < 50 and 325 < ball.xcor() < 350)
            or (ball.distance(left_paddle) < 50 and -350 < ball.xcor() < -325)
            and can_activate
        ):
            ball.paddle_bounce()
            can_activate = False
            current_time = time.time()
        next_time = time.time()
        # paddle_bounce function can only be called once every 3 seconds ago
        if next_time - current_time > 3:
            can_activate = True
        # detect left_paddle misses
        if ball.xcor() < -350:
            ball.refresh()
            scoreboard.add_rscore()
        # detect right_paddle misses
        if ball.xcor() > 350:
            ball.refresh()
            scoreboard.add_lscore()
    screen.exitonclick()


if __name__ == "__main__":
    main()
