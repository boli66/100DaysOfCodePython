from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface(Tk):
    def reset(self):
        self.answer = None
    def __init__(self):
        super().__init__()
        self.answer = None
        self.config(bg=THEME_COLOR, padx=20, pady=20)
        self.title("Quizzler")

        self.canvas = Canvas(width=300,height=300)
        self.question = self.canvas.create_text(150,150, font=("arial", 18, "normal"),width=300)
        self.canvas.grid(row=1, column=0, pady=(0,40))

        self.imgs = PhotoImage(file="images/true.png")
        self.true = Button(image=self.imgs)
        self.true.grid(row=2,column=0, sticky="w")
        def func():
            self.answer = True
        self.true["command"] = func

        self.img = PhotoImage(file="images/false.png")
        self.false = Button(image=self.img)
        self.false.grid(row=2, column=0, sticky="e")
        def func():
            self.answer = False
        self.false["command"] = func

        self.score = Label(font=("arial", 13, "normal"), bg=THEME_COLOR)
        self.score.grid(row=0,column=0, pady=(0,10), sticky="e")
        self.setScore(0,0)


    def setScore(self,newScore:int,questionNumber):
        self.score["text"] = f"score: {newScore}/{questionNumber}"


    def setQuestion(self, newText):
        self.canvas.itemconfig(self.question, text = newText)
    def changeQuestion(self, Text):
        text = self.canvas.itemcget(self.question, "text")
        self.setQuestion(f"{text}{Text}")