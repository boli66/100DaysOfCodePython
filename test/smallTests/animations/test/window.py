from tkinter import *
ON = "◼"
OFF = "◻"
class window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Animations")
        self.buffer = [[OFF for i in range(5)] for s in range(5)]
        self.label = Label(font=("arial", 18, "normal"))
        self.label.pack()

    def show(self):
        text = ""
        for y in self.buffer:
            for x in y:
                text+=x
            text+="\n"

        self.label["text"] = text
    def on(self,x,y):
        self.buffer[y][x] = ON
    def off(self,x,y):
        self.buffer[y][x] = OFF
