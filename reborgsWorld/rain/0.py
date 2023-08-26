# Do not include this while running
def move():
    pass
def turn_left():
    pass
def front_is_clear():
    pass
def build_wall():
    pass
# end

#Start

def turn_right():
    for i in range(0, 3):
        turn_left()


def m(times):
    for i in range(0, times+1):
        move()
    pass
def turn_around():
    for i in range(0,2):
        turn_left()
    pass

#real start

m(5)
build_wall()
turn_around()
m(4)


