import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()

#Move player up and down
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.move()



    screen.update()









