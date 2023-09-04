from Baze import turtle
from key import keyInput

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.restart()

    def move(self):
        if(keyInput("up")):
            self.fd(MOVE_DISTANCE)

    def update(self):
        self.move()

    def newLevel(self):
        if(self.ycor() > FINISH_LINE_Y):
            self.restart()
            return True
        return False

    def restart(self):
        self.goto(STARTING_POSITION)

    def deathCheck(self, cars):
        for i in cars:
            if i.distance(self) <= 20:
                return True
        return False


