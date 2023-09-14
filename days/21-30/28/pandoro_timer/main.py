from tkinter import *
from checkmark import CheckMark
from reset import Reset
from timer import Timer, Next
from lib import *
import time
import datetime


r = Tk()
def main():
    # Funcs
    def bring_window_to_front():
        r.attributes("-topmost", True)  # Set the window to be topmost
        r.attributes("-topmost", False)  # Reset the window stacking order


    # ---------------------------- CONSTANTS ------------------------------- #


    # ---------------------------- TIMER RESET ------------------------------- #
    scheduleIDs = []
    def after(time,func):
        scheduleIDs.append(r.after(time,func))
    def kill():
        for i in scheduleIDs:
            r.after_cancel(i)
        scheduleIDs.clear()
        for widget in r.winfo_children():
            widget.destroy()
        main()

    # ---------------------------- TIMER MECHANISM ------------------------------- #

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

    # ---------------------------- UI SETUP ------------------------------- #
    # Makes the window and gives it some values
    r.geometry("500x500")
    r.title("Work timer")

    # Makes the tomato Picture and displays it onto the screen
    pics = PhotoImage(file="tomato.png")
    pic = Label(image=pics)
    pic.config(width=200, height=223)
    picG = (200, 223)
    picPlace = (500 / 2 - picG[0] / 2, 500 / 2 - picG[1] / 2)
    pic.place(x=picPlace[0], y=picPlace[1] - 60)

    # Label to show current thing to do
    currentL = Label(text="Timer", font=("sans-serif", 30, "bold"), pady=10)
    currentL.pack(side="top", fill="both")


    # Makes the timer thats on top of the picture
    timer = Timer(picPlace)
    """show_timer = Label(text="00:00")
    show_timer.config(foreground="#ffffff", font=FONT, background="#F26849")
    show_timer.place(x=picPlace[0]+70,y=picPlace[1]+60)"""

    # Makes a button to start the timer
    startB = Button(text=f"Start", foreground="#00e600", font=FONT)
    startB.place(y=430, x=40)

    # Makes a button to reset the timer
    resetB = Button(text=f"Reset", foreground="#e62e00", font=FONT)
    resetB.place(y=430, x=340 + 40)
    resetB["command"] = kill

    # Makes a label to display the checkmarks
    checkmark = CheckMark()

    #timer.setSeconds(SHORT_BREAK_MIN * 60)

    def timeFunc(func):
        def wrapper():
            start = time.time_ns()
            func()
            end = time.time_ns()
            print((end-start)/int("10 000 000".replace(" ",""))) #kilo hecto deca base deci centi mili

        return wrapper
    nextB = Next(r)

    def loop():
        print(nextB.isClicked())
        while not (nextB.isClicked()):
            pass
    def state():
        print(nextB.isClicked())
        nextB.hide()
        nextB.unClick()
        timer.setState()

    # @timeFunc
    def mainLoop():

        # Gets what state the timer is in and responds to the state

        if (timer.countDown()):
            pass
        elif timer.getState() == "Long":
            checkmark.clear()
            timer.setState()
            bring_window_to_front()
            currentL["text"] = "Long Break"
            currentL.pack(side="top", fill="both")

        elif timer.getState() == "Short":
            checkmark.addCheckmark()
            timer.setState()
            bring_window_to_front()
            currentL["text"] = "Short Break"
            currentL.pack(side="top", fill="both")
        elif timer.getState() == "Work":
            timer.setState()
            bring_window_to_front()
            currentL["text"] = "Work"
            currentL.pack(side="top", fill="both")
        after(1 * SECOND, mainLoop)

    startB["command"] = mainLoop
    r.mainloop()


main()
