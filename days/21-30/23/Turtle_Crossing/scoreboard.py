from Baze import turtle
from turtle import Screen

FONT = ("Courier", 24, "normal")


class scoreLabel(turtle):
    def __init__(self, starterText = "", align = "left", pos = (-300, 300 - 36)):
        super().__init__()
        self.hideturtle()
        self.goto(pos)
        self.align = align
        self.update(starterText)

    def update(self, text):
        self.clear()
        self.write(text, font=FONT, align=self.align)


class Scoreboard:
    def __init__(self):
        self.level = 0
        self.label = scoreLabel()
        self.newLevel()

    def newLevel(self):
        self.level += 1
        self.label.update(f"Level: {self.level}")
    def deathScreen(self, fixScreen):
        Screen().clear()
        fixScreen()
        scoreLabel(f"You got to level {self.level}. Good Job!", "center", (0,0))
        Screen().update()
