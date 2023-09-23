from lib import *
import lib
def lt():
    turn_left()

def rt():
    for i in range(3):
        lt()
def turn_around():
    for i in range(2):
        lt()
def fd(times=1):
    for i in range(times):
         if(front_is_clear()):
             move()

def div(x,y):
    return int(x/y)
x = 0
y = 0
while front_is_clear():
    x+=1
    fd()
lt()
while front_is_clear():
    fd()
    y+=1

lt()
for i in range(div(x,2)):
    fd()
lt()
for i in range(div(y,2)):
    fd()
put()




















