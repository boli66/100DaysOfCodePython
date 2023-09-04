from Turtle import turtle
from turtle import Screen
font = ("Courier", 30, "bold")

class scoreLabel(turtle):
    def __init__(self,player):
        super().__init__()
        self.hideturtle()
        if(player == 1):
            self.vars = {
                "x": -5,
                "align": "right"
            }
        else:
            self.vars = {
                "x": 5,
                "align": "left"
            }
        self.goto(self.vars["x"], Screen().window_height()/2-40)
        self.update(0)

    def update(self, score):
        self.clear()
        self.write(score, font=font, align=self.vars["align"])
