from tkinter import Button
from lib import *

class Next(Button):
    def __init__(self, root):
        super().__init__(root, text="Next", font=FONT)
        self.pos = (215, 320)
        self.clicked = False
        self.config(command=self.click)

    def show(self):
        self.place(x=self.pos[0], y=self.pos[1])

    def hide(self):
        self.place_forget()

    def unClick(self):
        self.clicked = False

    def click(self):
        self.clicked = True
    def isClicked(self):
        return self.clicked