def turn_right():
    for i in range(0, 3):
        turn_left()
while not at_goal():
    if(front_is_clear()):
        move()
    else:
        turn_left()
        while not right_is_clear():
            move()
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()