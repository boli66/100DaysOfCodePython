import turtle
from tkinter.font import Font
class scoreLabel:
    def update(self, highscore = False):
        self.writer.clear()
        write = f"Score: {self.score}"
        if(highscore):
            write+=f", Highest score is: {highscore}."
        self.writer.setx(-(18*(len(write)/2)))
        self.writer.write(write, font=self.font)
    def changeScore(self, amount):
        self.score+=amount
        self.update()

    def initWriter(self, s,y):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("white")
        t.hideturtle()
        t.goto(0, y)
        self.writer = t
        self.update()

    def __init__(self, score, screen, end: bool):
        self.score = score
        self.writer = turtle.Turtle()
        self.font = ("arial", 20, "bold")
        y = 250-30 if not end else 30+10
        self.initWriter(screen, y)


class gameOver:
    def write(self, y):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("white")
        t.hideturtle()
        t.goto(0,y)
        t.write(self.text, font=self.font, align="center")

    def __init__(self, score, screen):
        self.text = "Game Over."
        self.font = ("arial", 20, "bold")
        self.write(0)
        scoreLabel(score, screen, True)

