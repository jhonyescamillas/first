"""
A program that lets users play Turtle Crossing. The goal of the game is to get the
turtle to get across to the top of the screen without getting it by passing cars.
The UP arrow moves the turtle. With each time the turtle crosses to the other side,
it starts over from the bottom, increasing the level which increases the speed of
the passing cars.
"""
import time

from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# represents the top of the screen
FINISH_LINE_Y = 280


def main():
    screen = Screen()
    screen.title("Turtle Crossing")
    screen.setup(width=600, height=600)
    screen.tracer(0)
    player = Player()
    screen.listen()
    screen.onkeypress(player.move_up, "Up")
    car_manager = CarManager()
    scoreboard = Scoreboard()
    loop_counter = 0
    # loop indicator
    game_on = True
    while game_on:
        # put a 0.1-second delay before updating the screen
        time.sleep(0.05)
        screen.update()
        scoreboard.display()
        # generate cars after every 5 loops
        if loop_counter % 5 == 0:
            car_manager.create_cars()
        car_manager.move()
        # indicator of loops
        loop_counter += 1
        # detect collision with cars
        for car in car_manager.cars:
            if car.distance(player) < 20:
                game_on = False
                scoreboard.game_over()
        # detect if finished line has been reached
        if player.ycor() >= FINISH_LINE_Y:
            # moves the player back to the bottom of the screen
            player.move_to_start()
            # makes the cars move faster
            car_manager.increase_speed()
            # update the level that's displayed in the scoreboard
            scoreboard.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
