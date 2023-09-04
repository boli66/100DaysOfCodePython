import time
import turtle

scoreLabel = turtle.Turtle()
screen = turtle.Screen()

screen.tracer(0)

frameSpeed = 0.1
score = 0
game = True
while game:
    # scoreLabel.write(f"Score: {score}")
    scoreLabel.write(f"Score: {score}", move=False, align="left", font=("Arial", 20, "bold"))
    score+=1
    screen.update()
    scoreLabel.clear()
    time.sleep(frameSpeed)