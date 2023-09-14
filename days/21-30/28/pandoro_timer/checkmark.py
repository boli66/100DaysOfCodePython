from tkinter import Label

CHECKMARK = "✓"
CHECKMARKFONT = ("arial", 20, "bold")


class CheckMark(Label):
    def __init__(self):
        super().__init__()
        self.config(text="", font=CHECKMARKFONT, foreground="#00e600")
        self.place(x=170, y=400)

    def clear(self):
        self.config(text="")

    def checkmarks(self):
        return len(self.cget("text"))

    def addCheckmark(self):
        # Gets how many checkmarks there are and returns True if it is over 5 else it returns False
        # ADDS A CHECKMARK
        self.config(text=self.cget("text") + CHECKMARK)

    def reset(self):
        self.config(text="")
