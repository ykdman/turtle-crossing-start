import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Call Player
player = Player()

# Call CarManager
car_manager = CarManager()

# call Scoreboard

scoreboard = Scoreboard()

# Key Reaction
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    # Detecting collision car with player
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect Successful Crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()

screen.exitonclick()

