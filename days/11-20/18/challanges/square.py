from turtle import Turtle, Screen

t = Turtle()

def square(sideLength):
    for i in range(0, 4):
        t.fd(sideLength)
        t.rt(90)

def init():
    t.color("green1")
    t.speed(9999)
def main():
    init()
    square(100)


main()
Screen().exitonclick()