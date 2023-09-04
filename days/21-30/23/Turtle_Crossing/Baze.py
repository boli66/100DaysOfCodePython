from turtle import Turtle

class turtle(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.color("white")
        self.speed(0)
