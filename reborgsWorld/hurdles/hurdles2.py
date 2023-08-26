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
# end

#Start
def turn_right():
    for i in range(0, 3):
        turn_left()

def jump():
    turn_left()
    move()

    turn_right()
    move()
    turn_right()
    move()

    turn_left()

while not at_goal():
    if(front_is_clear()):
        move()
    else:
        jump()