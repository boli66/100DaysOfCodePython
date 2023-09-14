import time
from tkinter import *

second = 1000

def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if (count > 0):
        r.after(1*second, count_down, count-1)
        return True
    return False


r = Tk()
r.after(1*second, count_down, 5)
r.title("Pomodoro")
r.config(padx=100,pady=50, bg="#f7f5dd")



canvas = Canvas(width=203, height=224, bg="#f7f5dd")

tomato = PhotoImage(file="tomato.png")

canvas.create_image(103,112, image=tomato)
timer_text = canvas.create_text(103,130,text="00:00", font=("Courier", 35, "bold"), fill="white")


canvas.pack()

# print()
r.mainloop()