import keyboard

from window import window
from player import Player
from consts import *
from keyboard import is_pressed


r = window()

player = Player()
player.face("up")
def main():
    r.show()
    run = True

    # Start
    if(is_pressed("space")):
        print("jump")
        player.jump(r)
    if(is_pressed("a")):
        print("left")
        player.face("left")
        player.fd(r)
    if(is_pressed("d")):
        print("right")
        player.face("right")
        player.fd(r)

    # End

    if(run):
        r.show()
        r.after(FRAMESPEED, main)

r.show()
r.after(1, main)
r.mainloop()
