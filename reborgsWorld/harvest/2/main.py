from lib import *

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


def row():
    def t():
        while(object_here()):
            take()
        put()
    for i in range(5):
        t()
        fd()
    t()

fd(2)
lt()
fd(2)
rt()
for i in range(div(6,2)):
    row()
    lt()
    fd()
    lt()

    row()
    rt()
    fd()
    rt()





















