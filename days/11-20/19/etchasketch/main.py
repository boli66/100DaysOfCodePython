import turtle

t = turtle.Turtle()
screen = turtle.Screen()

turn = 15
move = 15

def fd():
    t.fd(move)
def bk():
    t.bk(move)
def lt():
    t.lt(turn)
def rt():
    t.rt(turn)
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


def init():
    screen.onkey(fd,"w")
    screen.onkey(bk, "s")
    screen.onkey(lt,"a")
    screen.onkey(rt,"d")
    screen.onkey(clear,"c")
init()



screen.listen()

screen.exitonclick()
