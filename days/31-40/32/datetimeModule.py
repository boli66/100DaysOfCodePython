import datetime as dt
from tkinter import *

window = Tk()

r = Canvas(width=800, height=526)

timeL = r.create_text(400,263,text="", font=("arial", 40, "bold"))

r.pack()

def main():
    def c(s):
        s = str(s)
        if(len(s)<2):s = f"0{s}"
        return s


    time = dt.datetime.now()
    ms = str(time.microsecond)[:3]
    t = f"{c(time.hour)}:{c(time.minute)}:{c(time.second)}.{ms}"
    r.itemconfig(timeL, text=t)

    r.after(1,main)

r.after(1,main)
window.mainloop()
