import random as rand
import turtle as tur


class apple:
    def spawn(self):
        x = rand.randint(-11, 11) * 20
        y = rand.randint(-11, 11) * 20
        self.apple.goto(x, y)

    def remove(self):
        self.apple.hideturtle()

    def checkColision(self, snake):
        for i in range(len(snake.segments)):
            sn = snake.segments
            s = self.apple.pos()
            x = round(s[0])
            y = round(s[1])
            s = sn[i].pos()
            xs = round(s[0])
            ys = round(s[1])

            if ((xs, ys) == (x, y)):
                return True
        return False

    def initApple(self):
        t = tur.Turtle("circle")
        # t.shapesize(0.8, 0.8)
        t.color("red")
        t.speed(0)
        t.penup()
        self.apple = t

    def __init__(self):
        self.apple = None
        self.initApple()
        self.spawn()
