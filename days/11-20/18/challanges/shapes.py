import random as r
import turtle

t = turtle.Turtle()
t.screen.colormode(255)
def shape(sideLength, corners):
    turn = 360/corners
    for i in range(0,corners):
        t.rt(turn)
        t.fd(sideLength)

def init():
    t.color("green1")
    t.speed(9999)
def main():
    init()
    def rInt():
        return r.randint(0,255)
    for i in range(3,10+1):
        t.pencolor(rInt(), rInt(), rInt())
        shape(100,i)


main()

turtle.Screen().exitonclick()