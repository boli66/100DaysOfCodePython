class Base:
    def __str__(self):
        return f"x={self.x}, y={self.y}, dir={self.dir}"
    def turn180(self):
        self.rt()
        self.rt()

    def bk(self,r):
        self.turn180()
        self.fd(r)
        self.turn180()

    def rt(self):
        s = ["up", "right", "down", "left"]
        i = s.index(self.dir)
        i+=1
        while i> len(s)-1:
            i-=len(s)
        self.dir = s[i]
    def lt(self):
        s = ["up", "right", "down", "left"]
        i = s.index(self.dir)
        i-=1
        while i < 0:
            i += len(s)
        self.dir = s[i]
    def __init__(self, x=2, y=2):
        self.x = x
        self.y = y
        self.dir = "left"

    def on(self, r):
        r.on(self.x, self.y)

    def off(self, r):
        r.off(self.x, self.y)

    def face(self, dir):
        self.dir = dir

    def fd(self, r):
        self.off(r)
        if (self.dir == "up" and self.y > 0):
            self.y -= 1
        elif (self.dir == "down" and self.y < 4):
            self.y += 1
        elif (self.dir == "left" and self.x > 0):
            self.x -= 1
        elif (self.dir == "right" and self.x < 4):
            self.x += 1
        self.on(r)
