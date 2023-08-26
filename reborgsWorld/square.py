def turn_right():
    for i in range(0, 3):
        turn_left()


def m(times):
    for i in range(0, times):
        if (front_is_clear()): move()


# Square
def squareR(sideLength):
    for i in range(0, 4):
        for i in range(1, sideLength):
            m(1)
        turn_right()


def squareL(sideLength):
    turn_left()
    squareR(sideLength)
    turn_right()


turn_left()
squareR(2)
m(3)