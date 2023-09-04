from turtle import Screen, Turtle

def run():
    height = Screen().window_height()

    t = Turtle()
    t.penup()
    t.color("white")
    t.hideturtle()
    t.setheading(90)
    t.pensize(2)
    t.goto(y=-(height/2), x=0)

    def dashLine(length):
        dashLength = 10
        dashes = round(length/dashLength)
        t.pendown()
        for i in range(0, dashes):
            t.fd(dashLength)
            if(t.isdown()):
                t.penup()
            else:
                t.pendown()
        t.pendown()

    dashLine(height)