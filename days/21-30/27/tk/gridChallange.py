from tkinter import *

FONT = ("arial", 13, "normal")
window = Tk()
window.config(padx=10,pady=10, bg="#ab321f")

Label(text="label", font=FONT).grid(column=0, row=0)

Button(text="button1", font=FONT).grid(column=1, row=1)
Button(text="button2", font=FONT).grid(column=2, row=0)

Entry(width=10, font=FONT).grid(column=3, row=2)

window.mainloop()
