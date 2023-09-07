import pandas
import question
from writer import write
from os.path import dirname

path = f"{dirname(__file__)}/"

class end:
    def __init__(self, question: question.question):
        # prints that the user gave up
        txt = "You gave up"
        align = "center"
        xy = (0, 0)
        font = ("arial", 20, "bold")
        write(txt, xy, align, font)

        # Gets what states the user missed and gets the score the user got
        left = question.statesLeft
        states = len(question.data["state"].to_list())
        score = states-len(question.statesLeft)

        # Turns the data to a csv file and saves it
        data = {"States Missed": left, f"You got {score}/{states}":""}
        pandas.DataFrame(data).to_csv(f"{path}scores/statesMissed.csv")
