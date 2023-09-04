from turtle import Turtle
class turtle(Turtle):
    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.speed(0)
        self.penup()