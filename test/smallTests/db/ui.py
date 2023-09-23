from tkinter import *
from tkinter import messagebox
import json
def get(path):
    with open(path) as f:
        return json.load(f)

class UI(Tk):
    def createInput(self, labelText, rc, width=20):
        Label(text=labelText, font=("arial", 17, "bold")).grid(row=rc[0], column=rc[1], columnspan=2)
        question = Entry(width=width, font=("arial", 17, "normal"))
        question.grid(row=rc[0], column=rc[1]+2)
        return question
    def __init__(self):
        super().__init__()
        self.title("Add Question")
        self.config(padx=20,pady=20)

        Label(text="Question: ", font=("arial", 17, "bold")).grid(row=0, column=0, columnspan=2)
        self.question = Entry(width=20, font=("arial", 17, "normal"))
        self.question.grid(row=0, column=2)

        self.question = self.createInput(labelText="Question: ", rc=[0,0])

        self.answerBV = BooleanVar()
        self.answerCB = Checkbutton(variable=self.answerBV, text="Answer (True/False)")
        self.answerCB.grid(row=1, column=0)
        def func():
            self.answer = self.answerBV.get()
        self.answerCB["command"] = func

        self.submit = Button(text="Submit", font=("arial", 15, "normal"))
        self.submit.grid(row=2, column=0, columnspan=3, sticky="we")
        self.questionsL = Label(font=("arial", 14, "normal"))
        self.questionsL.grid(row=3,column=0, columnspan=3, sticky="w")
        self.update()

    def update(self):
        self.questionsL.config(text=f"Question: {len(get('db.json'))}")

    def getQuestion(self):
        if self.question.get() == "":
            messagebox.showinfo("Submition", "Fill in the question please.")
            return None
        answer = str(self.answerBV.get())
        question = self.question.get()
        messagebox.showinfo("Submition", "You question was added successfully")
        return{"question":question, "correct_answer":answer}

    def clear(self):
        self.question.delete(0,END)
        self.answerBV.set(False)