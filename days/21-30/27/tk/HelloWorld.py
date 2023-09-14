import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("500x500")
window.resizable(False, False)
window.title("Hello World!")

# Label
txt = "Dummies punched: 0"
label = tk.Label(text=txt)
label.config(font=("arial", 20, "bold"))
label.pack()

# Button
score = 0


def click():
    global score
    score += 1
    label["text"] = txt.replace("0", str(score))


button = Button(text="PRESS ME!")
button["command"] = click
button.pack()

# Entry

input = Entry()
input.config(width=50)
input.pack()

window.mainloop()
