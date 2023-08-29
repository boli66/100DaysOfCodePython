import turtle as t
import math
p = t.Turtle()
p.speed(1000)
def circle(size):
    for i in range(0,round(360/size)):
        p.fd(5)
        p.right(size)

turn = 45
for i in range(0,math.ceil(360/turn)):
    print(f"{i}/{math.ceil(360/turn)}")
    p.rt(turn)
    circle(15)
v = math.ceil(360/turn)
print(f"{v}/{v}")


input("Press enter to finish...")