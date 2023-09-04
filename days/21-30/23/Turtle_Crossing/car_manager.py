from Baze import turtle
import random
import turtle as t

COLORS = ["red1", "orange1", "yellow1", "green1", "blue1", "purple1"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

halfWindowWidth = t.Screen().window_width()/2
x_start = halfWindowWidth-60
x_end = -halfWindowWidth

class car(turtle):
    def __init__(self, speed):
        super().__init__()
        # Gives some values
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.len = 20*self.shapesize()[1]
        self.speed = speed
        self.color(random.choice(COLORS))
        self.setLocation()
    def move(self):
        self.bk(self.speed)

    def setLocation(self):
        x = x_start
        var = round(t.Screen().window_height()/2-60)
        y = random.randint(-var, var)
        self.goto(x, y)


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def update(self, scoreboard):
        if(random.randint(1,round(4/(scoreboard.level/2))) == 1):
            self.createCar()
        self.moveCars()
        self.delCars()

    def delCars(self):
        for i in self.cars:
            if(i.xcor() < x_end):
                self.cars.remove(i)


    def moveCars(self):
        for i in self.cars:
            i.move()

    def createCar(self):
        c = car(self.speed)

        self.cars.append(c)
    def newLevel(self):
        self.speed += MOVE_INCREMENT
