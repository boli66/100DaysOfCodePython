def main():
    import time
    from turtle import Turtle, Screen
    import random
    screen = Screen()
    screen.setup(height=300,width=600)
    # Picks witch turtles are playing
    colors = ["red", "blue", "orange", "yellow", "green", "purple"]

    # Stores all the turtles
    turtls = []

    # Gets the spawn points for the turtles
    x = -(screen.window_width()/2)+30
    spaceing = 30
    y = -30 #-(screen.window_height()/2)+100
    y = -(spaceing*len(colors)/2)

    s = Turtle()
    s.shape("turtle")
    s.color("aqua")
    s.setheading(180)

    # Creates the turtles
    for i,obj in enumerate(colors):
        screen.colormode(255)

        t = Turtle()
        t.shape("turtle")

        t.penup()

        t.speed(4)
        t.goto(x,y)
        y+=spaceing
        t.pendown()

        t.color(obj)
        t.speed(0)
        turtls.append(t)

    s.hideturtle()
    do = True

    # Makes a finishline
    end = screen.window_width() / 2 - 25
    s.penup()
    s.goto(end,-(spaceing*len(colors)/2))
    s.pendown()
    s.rt(90)
    s.fd(spaceing*len(colors))

    # Ask the user what they are betting on

    bid = screen.textinput("Bid", "What turtle is going to win? pick a color: ")

    while do:
        # Get a turtle to move
        turtl = random.randint(0,len(turtls)-1)
        turtls[turtl].fd(10)

        # Check if any of the turtles have won
        for i in turtls:
            index = turtls.index(i)
            if i.xcor() > end:
                do = False
                # Win check
                index = turtls.index(i)
                if(colors[index] != bid.lower()):
                    add = "You lose."
                else:
                    add = "You Win!"
                print(f"{add} The {colors[index]} turtle is the winner.")

        time.sleep(0.01)
    # screen.exitonclick()
main()