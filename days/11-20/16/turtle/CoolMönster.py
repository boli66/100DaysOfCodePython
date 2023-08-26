import main

t = turtle.Turtle()
def init():
    t.shape("turtle")
    t.screen.bgcolor("black")
init()

def main():
    t.color("blue")
    t.pensize(10)
    t.fd(1)
    t.right(90)
    t.penup()
    t.fd(t.screen.canvheight)
    t.left(90)
    t.pendown()
    t.pensize(2)
    t.hideturtle()
    t.color("green1")

    for i in range(0,360//10):
        print(i)
        # if(i == (360/10)/2):
        #     t.color("black")
        t.fd(10)
        t.left(10)
        x = t.xcor()
        y = t.ycor()
        rotation = t.heading()
        t.setx(0)
        t.sety(0)
        t.setx(x)
        t.sety(y)
        t.setheading(rotation)

main()

screen = turtle.Screen()
print(screen.canvheight)
screen.exitonclick()