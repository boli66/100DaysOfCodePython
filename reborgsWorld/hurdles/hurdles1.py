# Do not include this while running
def move():
    pass
def turn_left():
    pass
def front_is_clear():
    pass
def at_goal():
    pass
def right_is_clear():
    pass
def build_wall():
    pass
# end

#Start

def turn_right():
    for i in range(0, 3):
        turn_left()


def m(times):
    for i in range(0, times):
        if (front_is_clear()): move()
    pass
def turn_around():
    for i in range(0,2):
        turn_left()
    pass
def left_is_clear():
    turn_around()
    isClear = right_is_clear()
    turn_around()
    return isClear
def goBack(tiles):
    for i in range(tiles+1):
        move()
    turn_around()
    for i in range(tiles):
        move()
        turn_around()
    pass

#real start

def jump():
    turn_left()
    move()

    turn_right()
    move()
    turn_right()
    move()

    turn_left()

while not at_goal():
    move()
    jump()