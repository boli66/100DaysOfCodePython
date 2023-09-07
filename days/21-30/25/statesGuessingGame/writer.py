import turtle
import pandas
FONT = ("arial", 8, "normal")

class write(turtle.Turtle):
    def __init__(self,txt,xy, align, font):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(xy)
        self.write(txt,align=align,font=font)


class WriteState(turtle.Turtle):
    def Write(self, text, x, y):
        self.goto(x, y)
        self.write(text, align="left", font=FONT)

    def __init__(self, state, data: pandas.DataFrame):
        super().__init__()
        state = state.title()
        self.penup()
        self.hideturtle()
        row = data[data.state == state]
        self.Write(state, row.x.to_list()[0], row.y.to_list()[0])