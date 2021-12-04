# Create a Crossing Game with the Turtle Module

from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Crossing Game")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, "Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            scoreboard.game_ended()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.new_level()
        scoreboard.next_level()

screen.exitonclick()
