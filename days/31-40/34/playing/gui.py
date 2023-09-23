import html
import time
from tkinter import *
import requests

def question():
    # https://opentdb.com/api.php?amount=30&category=18&type=boolean
    api = "https://opentdb.com/api.php"
    params = {
        "amount": 1,
        "category": 18,
        "type": "boolean"
    }
    data = requests.get(api, params=params).json()["results"][0]
    lbl.setText(html.unescape(data["question"]))


class label(Canvas):
    def __init__(self):
        wh = (800,80)
        super().__init__(width=wh[0],height=wh[1])
        self.lbl = self.create_text(wh[0]/2,wh[1]/2, text="DDDScriptDDD", font=("arial",18,"normal"),
            width=wh[0])
    def setText(self, newText):
        self.itemconfig(self.lbl,text=newText)

window = Tk()
window.config(padx=20,pady=20,height=200, width=800)

lbl = label()
lbl.place(x=0,y=0)
question()
trueB = Button(text="True", font=("arial", 18, "normal"))
trueB.place(x=400,y=85)
falseB = Button(text="False", font=("arial", 18, "normal"))
falseB.place(x=260,y=85)
score=Label(text="Score: 0/0", font="")

window.mainloop()