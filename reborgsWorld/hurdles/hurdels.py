# Do not include this while running
def move():
    pass
def turn_left():
    pass
def front_is_clear():
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
hurdles = 6
move()
for i in range(0,hurdles-1):
    jump()
    move()
jump()