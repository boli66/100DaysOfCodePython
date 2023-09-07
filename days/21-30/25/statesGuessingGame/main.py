import os.path

import keyboard
import pandas
import turtle
from writer import WriteState, write
import key
import keyboard as py

path = f"{os.path.dirname(__file__)}/"

data = pandas.read_csv(f"{path}50_states.csv")


screen = turtle.Screen()
def initScreen():
    screen.setup(725,491)
    screen.bgpic(f"{path}blank_states_img.gif")
    screen.tracer(0)
    screen.title("State Guesser")
initScreen()

import question
asker = question.question(data)

scoreBoard = question.ScoreBoard(0)

while True:
    guess = asker.ask(scoreBoard)
    # Checks if the guess was wrong or right
    if(guess):
        # Checks if the player wants to exit
        if(guess!="stop"):
            scoreBoard.scored()
            WriteState(guess,data)
        # If the player wants to exit then it runs this
        else:
            import end
            end.end(asker)
            break
        #

    #Checks if the player has won. if the player has won then it showes the win screen
    end = len(data.state.to_list())
    if(scoreBoard.score == end):
        # Values
        txt = "You Won!"
        align = "center"
        xy = (0,0)
        font = ("arial", 20, "bold")

        # Write You Won!
        write(txt,xy,align,font)

        # Update the screen so the user can see it
        screen.update()
        break


    screen.update()

screen.exitonclick()
