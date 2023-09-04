from turtle import Turtle,Screen
import pyautogui as py

class turtle(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()

class shape:
    def __init__(self, turtle: Turtle):
        self.width = 20* turtle.shapesize()[1]
        self.height = 20*turtle.shapesize()[0]

        self.corners = {}

        self.corners["ul"] = (-(self.width/2)+turtle.xcor(), self.height/2+turtle.ycor())
        self.corners["ur"] = ((self.width/2)+turtle.xcor(), (self.height/2)+turtle.ycor())
        self.corners["dl"] = (-(self.width/2)+turtle.xcor(), -(self.height/2)+turtle.ycor())
        self.corners["dr"] = ((self.width/2)+turtle.xcor(), -(self.height/2)+turtle.ycor())

def collided(turtle1 = turtle(), turtle2 = turtle()):
    t1 = shape(turtle1)
    t2 = shape(turtle2)

    # left side

screen = Screen()
turtle1 = turtle()
turtle2 = turtle()

turtle2.fd(30)


screen.exitonclick()
