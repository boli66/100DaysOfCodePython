import random
import turtle

t = turtle.Turtle()

def init():
    t.pensize(1)
    t.speed(0)
    turtle.colormode(255)

init()
def chooseColor():
    def rInt():
        return random.randint(0,255)
    t.color(rInt(), rInt(), rInt())

def main():
    turn = 3
    for i in range(0,360,turn):
        chooseColor()
        t.circle(140)
        t.rt(turn)


main()


turtle.Screen().exitonclick()