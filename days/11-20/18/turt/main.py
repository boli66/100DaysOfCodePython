from turtle import Turtle, Screen

p = Turtle()
p.screen.bgcolor("black")
p.color("green1")
def square(sideLength):
    for i in range(0,4):
        p.fd(sideLength)
        p.right(90)
angle = 1

p.speed(99999)
for i in range(0,360//angle):
    p.right(angle)
    square(100)



Screen().exitonclick()