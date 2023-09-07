import turtle
import pandas
from ScoreBoard import ScoreBoard
class question:
    def __init__(self,data: pandas.DataFrame):
        self.data = data
        self.statesLeft = data["state"].to_list()

        self.statesLeft = [i.lower() for i in self.statesLeft]
        self.First = True

    def ask(self, scoreBoard: ScoreBoard):
        if(self.First):
            txt = "Whats one state?"
            self.First = False
        else:
            txt = "Whats another state?"
        title = f"{scoreBoard.score}/{len(self.data['state'].to_list())} States Correct"
        guess = turtle.Screen().textinput(title,txt).lower()

        if(guess == "e"):
            return "stop"

        if(guess in self.statesLeft):
            self.statesLeft.remove(guess)
            return guess
        return False
