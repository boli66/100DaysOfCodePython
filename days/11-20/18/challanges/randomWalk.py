import random
import turtle
import random as r


t = turtle.Turtle()

def chooseSide():
    side = r.randint(1,4)
    t.setheading(side*90)
def chooseColor():
    def rInt():
        return random.randint(0,255)
    t.color(rInt(), rInt(), rInt())

def init():
    t.color("green1")
    turtle.colormode(255)
    t.speed(0)
    t.pensize(15)

def main():
    init()

    while True:
        chooseSide()
        chooseColor()
        t.fd(30)
main()
turtle.Screen().exitonclick()