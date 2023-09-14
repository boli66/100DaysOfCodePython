import math
from tkinter import *

window = Tk()
window.geometry("150x100")

FONT = ("arial", 13, "normal")
miles = Entry(width=10, font=FONT)
miles.grid(column=0, row=0)

temp = Label(text="Miles", font=FONT)
temp.grid(column=1, row=0)

text = "0 Kilometers"
showKilometers = Label(text=text, font=FONT)
showKilometers.place(x=0,y=23)

def covert():
    kilometers = int(miles.get())*1.609347
    kilometers = round(kilometers,2)
    showKilometers["text"] = text.replace("0",str(kilometers))

convert = Button(text="Convert")
convert["command"] = covert
convert.place(x=0,y=50)

window.mainloop()
