from Turtle import turtle
from turtle import Turtle, Screen
from paddle import Paddle


class Ball(turtle):
    def getready(self):
        self.bounce_x(False)
        self.goto(0, 0)
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.x_move = 4
        self.y_move = 4

    def __check(self, player, width):
        collided = False
        height = Screen().window_height()
        if not (player > -width / 2 and player < width / 2):
            collided = True
        return collided

    def collision_y(self):

        collided = False
        collided = self.__check(self.ycor(), Screen().window_height())

        return collided

    def collision_paddle(self, paddles):

        collided = False
        if (self.distance(paddles[0]) < 50 and self.xcor() < -340):
            collided = True
        if (self.distance(paddles[1]) < 50 and self.xcor() > 340):
            collided = True

        return collided

    def collision_x(self):
        collided = False

        if not (self.xcor() < Screen().window_width() / 2
                and
                self.xcor() > -(Screen().window_width() / 2)):
            collided = True

        return collided

    def move(self, paddles):
        # Move
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

        # bounce roof floor
        if (self.collision_y()):
            self.bounce_y()

        # Bounce on paddles
        if (self.collision_paddle(paddles)):
            self.bounce_x(True)
        # Death
        if (self.collision_x()):
            return False

        return True

    def bounce_x(self, paddle):
        self.y_move = -self.y_move


    def bounce_y(self):
        self.y_move = -self.y_move
