import turtle

from libraries.FileIO import file, hson
import os
from turtle import Screen
from key import keyInput
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Gets data from the data file
PATH = f"{os.path.dirname(__file__)}/"
data = hson.hson(f"{PATH}data.json", {}).get()

# Gets the screen
screen = Screen()

# Gives the screen some startup values
def initScreen():
    screen.setup(600,600)
    screen.tracer(0)
    screen.title("Turtle Crossing")
    screen.bgcolor("black")
    screen.update()

initScreen()

# Creates the player
player = Player()

# Creates and manages cars
carManager = CarManager()

# Creates the scoreBoard
scoreboard = Scoreboard()

frames = 0
# GameLoop
while True:
    carManager.update(scoreboard)

    if(frames<60):
        frames += 1
        carManager.update(scoreboard)
        continue

    if(keyInput("e")):
        break

    player.update()

    if(player.newLevel()):
        carManager.newLevel()
        scoreboard.newLevel()
    if(player.deathCheck(carManager.cars)):
        scoreboard.deathScreen(initScreen)
        break

    screen.update()
    time.sleep(data["frameSpeed"])



# Makes the screen not disapear at the end of the program
print("Done")
screen.exitonclick()