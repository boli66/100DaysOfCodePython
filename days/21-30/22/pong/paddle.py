import time

import keyboard
from turtle import Screen
from Turtle import turtle

paddleHeight = 20*5
speed = 10

class Paddle(turtle):
    def Reset(self):
        x = self.variables["x"]
        y = 0
        self.goto(x,y)
    def __init__(self, player):
        super().__init__()
        self.shapesize(stretch_len=1, stretch_wid=5)
        if(player == 1):
            self.variables = {
                "x": -350,
                "up": "w",
                "down": "s",
            }
        else:
            self.variables = {
                "x": 350,
                "up": "up",
                "down": "down",
            }
        self.goto(self.variables["x"], 0)

    def collision(self):
        screen = Screen()
        collided = False
        if not(self.ycor()+paddleHeight/2 < screen.window_height()/2 and self.ycor()-paddleHeight/2 > -screen.window_height()/2):
            collided = True
        return collided

    def checkKeyPress(self):
        keys = {
            "e": False,
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "w": False,
            "s": False,
        }
        for i in keys:
            if(keyboard.is_pressed(i)):
                keys[i] = True

        return keys

    def UP(self, distance):
        pos = self.pos()
        pos = [pos[0], pos[1]]
        pos[1] += distance
        self.goto(pos[0], pos[1])
    def DOWN(self, distance):
        pos = self.pos()
        pos = [pos[0], pos[1]]
        pos[1] -= distance
        self.goto(pos[0], pos[1])

    def up(self):

        self.UP(speed)
        if(self.collision()):
            self.DOWN(speed)
    def down(self):
        self.DOWN(speed)
        if(self.collision()):
            self.UP(speed)


    def move(self):
        for i in [self.variables["up"], self.variables["down"]]:
            if (self.checkKeyPress()[i]):
                if(i == self.variables["up"]):
                    self.up()
                else:
                    self.down()

