import time
from turtle import Screen
from paddle import Paddle
import os
from ball import Ball
from scoreLabel import scoreLabel
from libraries.FileIO import hson

# Gets the current directory
PATH = f"{os.path.dirname(__file__)}/"

# Gets the data from a file
data = hson.hson(f"{PATH}data.json", {}).get()

screen = Screen()
# Gives the screen values
def initScreen():
    screen.title("Pong")
    screen.tracer(0)
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
initScreen()

# A variable to stop the gameLoop
gameOn = True

#Makes a paddle
paddle1 = Paddle(1)
paddle2 = Paddle(2)

# Score labels
player1 = scoreLabel(1)
player2 = scoreLabel(2)

# Ball
ball = Ball()

# Draws the line in the middle
import gui
gui.run()

# Scores
scores = [0, 0]

# The game loop
while gameOn:
    #closes the game when you click e
    if(paddle1.checkKeyPress()["e"]):
        while(paddle1.checkKeyPress()["e"]):
            pass

    paddle1.move()
    paddle2.move()

    if not(ball.move((paddle1,paddle2))):
        if(ball.xcor() < -400):
            scores[1]+=1
            ball.getready()
            paddle1.Reset()
            paddle2.Reset()

        elif(ball.xcor() > 400):
            scores[0]+=1
            ball.getready()
            paddle1.Reset()
            paddle2.Reset()

    player1.update(scores[0])
    player2.update(scores[1])

    screen.update()
    # print(scores)
    time.sleep(data["frameSpeed"])

# Makes the screen go away once we click it instead of going away at the end of the program
screen.exitonclick()