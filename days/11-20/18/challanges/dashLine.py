import turtle
t = turtle.Turtle()

def dashLine(dashes):
    dashLength = 5
    t.pendown()
    for i in range(0, dashes):
        t.fd(dashLength)
        if(t.isdown()):
            t.penup()
        else:
            t.pendown()
    t.pendown()

def init():
    t.color("green1")
    t.speed(9999)
def main():
    init()
    dashLine(50)


main()
turtle.Screen().exitonclick()