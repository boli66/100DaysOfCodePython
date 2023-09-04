from turtle import Screen  # , Turtle
import os
import hson
import file
import apple

# Gets the current directory
PATH = f"{os.path.dirname(__file__)}/"

# Gets the data from a file
data = hson.hson(f"{PATH}data.json", {}).get()


def changeHighscore(score):
    path = f"{PATH}users/{data['highscoreFile']}"
    f = file.reader(path)
    high = int(f.getLines()[0])
    f.close()
    if (high < score):
        s = file.writer(path)
        s.ln(str(score))
        s.close()


# Makes a screen
screen = Screen()


# Gives the screen some values
def screenInit():
    screen.setup(width=500, height=500)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)


screenInit()

# Makes the snake
import snake

s = snake.snake(length=data["startLength"], speed=data["moveSpeed"])


# Functions for the inputs
def up():
    s.setHeading(90)


def down():
    s.setHeading(270)


def left():
    s.setHeading(180)


def right():
    s.setHeading(0)


# Gets the inputs to move the snake
# Arrow inputs
screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=right, key="Right")

# Key inputs
screen.onkey(fun=up, key="w")
screen.onkey(fun=down, key="s")
screen.onkey(fun=left, key="a")
screen.onkey(fun=right, key="d")

screen.listen()

# A variable to stop the gameLoop
game = True

# Makes an apple for the snake to eat and stores the score
Apple = apple.apple()

# Makes the label to display the score
import labels

score = labels.scoreLabel(0, screen, False)

# Handles highscores
"""handler = highscore.handler(
    f"{PATH}Highscores.txt",
    screen.textinput("username", "What is your username?")
)"""
# The main gameLoop
while game:
    if (not s.fd()):
        game = False
        continue
    if (Apple.checkColision(s)):
        Apple.remove()
        s.addSegment()
        Apple = apple.apple()
        score.changeScore(1)
    screen.update()
    s.pause()

screen.clear()

changeHighscore(score.score)

screenInit()
labels.gameOver(score.score, screen)
# Makes the screen not disappear at the end of the program
screen.exitonclick()
