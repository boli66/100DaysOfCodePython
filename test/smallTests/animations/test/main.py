from window import *
FRAMESPEED = 100


r = window()

r.show()

class ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = True

    def fixDir(self):
        if (self.x > 3):
            self.dir = False
        elif (self.x < 1):
            self.dir = True
    def off(self):
        r.off(self.x,self.y)

    def on(self):
        r.on(self.x,self.y)

    def move(self):
        self.fixDir()
        self.off()
        if(self.dir):
            self.x+=1
        else:
            self.x-=1
        self.on()

b = ball(0,2)
def main():
    run = True
    # Start
    b.move()




    # End
    r.show()
    if run:
        r.after(FRAMESPEED, main)

r.after(1, main)
r.mainloop()