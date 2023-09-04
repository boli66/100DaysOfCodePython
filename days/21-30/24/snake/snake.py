import time
import turtle


class snake:
    def addSegment(self):
        pos = self.segments[len(self.segments) - 1].pos()
        self.segments.append(self.createSegment(pos[0], pos[1]))

    def getPos(self):
        return self.segments[0].pos()

    def pause(self):
        time.sleep(self.speed)

    def collision(self):
        # If the head has colided with the tail return false else true
        for i in range(len(self.segments) - 1, 0, -1):
            sn = self.segments
            s = sn[0].pos()
            x = round(s[0])
            y = round(s[1])
            s = sn[i].pos()
            xs = round(s[0])
            ys = round(s[1])

            if ((xs, ys) == (x, y)):
                return False

        # Check if colided with wall
        head = self.segments[0].pos()
        if not (head[0] > -250 and head[0] < 250):
            return False
        elif not (head[1] > -250 and head[1] < 250):
            return False
        return True

    def fd(self):
        pos = self.segments[len(self.segments) - 1].pos()
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].setpos(self.segments[i - 1].pos())
        self.segments[0].fd(20)
        """self.fds += 1
        if(self.fds == 5):
            self.segments.append(self.createSegment(pos[0], pos[1]))
            self.fds = 0"""
        return self.collision()

    def rt(self):
        self.segments[0].rt(90)
        # time.sleep(self.speed)

    def lt(self):
        self.segments[0].lt(90)
        # time.sleep(self.speed)

    def setHeading(self, angle: int):
        h = self.segments[0].heading()
        self.segments[0].setheading(angle)
        self.segments[0].fd(20)
        turnBack = self.collision()
        self.segments[0].bk(20)
        if (not turnBack):
            self.segments[0].setheading(h)

    def createSegment(self, x: int, y: int):
        t = turtle.Turtle("square")
        t.color("white")
        t.penup()
        t.speed(0)
        t.setpos(x, y)

        return t

    def createSnake(self):
        for i in range(0, self.length):
            self.segments.append(self.createSegment(-(i * 20), 0))

    def __init__(self, length: int, speed: int):
        self.length = length
        self.segments = []
        self.speed = speed
        self.fds = 0
        self.createSnake()
