import time
import turtle
import os
from libraries.FileIO.hson import hson
path = f"{os.path.dirname(__file__)}/"

data = hson(f"{path}data.json", {}).get()

t = turtle.Turtle("square")
screen = turtle.Screen()
speed = data["speed"]
def up():
    t.setheading(90)
def left():
    t.setheading(180)
def right():
    t.setheading(0)
def down():
    t.setheading(270)

screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=right, key="Right")
screen.listen()

gameLoop = True

while gameLoop:
    t.fd(speed)
    time.sleep(data["frameSpeed"])


screen.onkey(key="")