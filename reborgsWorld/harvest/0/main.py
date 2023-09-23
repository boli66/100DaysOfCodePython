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


def row():
    def t():
        if(object_here()):
            take()
    for i in range(9):
        t()
        fd()

for i in range(div(9,2)):
    row()
    lt()
    fd()
    lt()

    row()
    rt()
    fd()
    rt()





















