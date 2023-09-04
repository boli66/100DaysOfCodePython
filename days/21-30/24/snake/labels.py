import turtle
from tkinter.font import Font
class scoreLabel:
    def update(self, highscore = False):
        self.writer.clear()
        write = f"Score: {self.score}"
        if(type(highscore) == type(1)):
            write+=f", Highscore: {highscore}."
        self.writer.setx(0)
        self.writer.write(write, font=self.font, align="center")
    def changeScore(self, amount):
        self.score+=amount
        self.update(self.highscore)

    def initWriter(self, s,y):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("white")
        t.hideturtle()
        t.goto(0, y)
        self.writer = t
        self.update(self.highscore)

    def __init__(self, score, screen,highscore,  end: bool):
        self.score = score
        self.highscore = highscore
        self.writer = turtle.Turtle()
        self.font = ("Courier", 20, "normal")
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

    def __init__(self, score,highscore, screen):
        self.text = "Game Over."
        self.font = ("Courier", 20, "normal")
        self.write(0)
        scoreLabel(score, screen,highscore, True)

