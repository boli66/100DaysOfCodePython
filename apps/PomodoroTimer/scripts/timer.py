from tkinter import Label
from lib import *
from next import Next

class BaseTimer(Label):
    def __init__(self, picPlace: tuple):
        font = [s for s in FONT]
        font[1] = 23
        super().__init__(text="00:00")
        self.config(foreground="#ffffff", font=font, background="#F26849")
        self.place(x=picPlace[0] + 62, y=picPlace[1] + 57)
        self.seconds = 0
        self.checkmarks = 0

    def setSeconds(self, seconds: int):
        self.seconds = int(seconds)
        self.updateScreen()


    def countDown(self):
        if (self.seconds < 1):
            return False
        else:
            self.setSeconds(self.seconds - 1)
            return True

    def updateScreen(self):
        def c(num):
            if (num < 10):
                return f"0{num}"
            return f"{num}"

        mins = 0
        s = self.seconds
        while s >= 60:
            mins += 1
            s -= 60

        self.config(text=f"{c(mins)}:{c(s)}")

class Timer(BaseTimer):
    def __init__(self, picPlace):
        super().__init__(picPlace)
        self.interval = 0
        self.intervals = PANDOROS
        self.Break = False
        #self.next = Next()
    def getState(self):
        if(self.interval > self.intervals):
            #self.interval = 0
            #self.setSeconds(self.m_to_s(LONG_BREAK_MIN))
            return "Long"

        if(self.Break):
            #self.Break = False
            #self.setSeconds(self.m_to_s(SHORT_BREAK_MIN))
            return "Short"

        #self.setSeconds(self.m_to_s(WORK_MIN))
        #self.Break = True
        #self.interval += 1
        return "Work"
    def setState(self):
        state = self.getState()
        def temp(mins):
            self.setSeconds(m_to_s(mins))

        if(state == "Long"):
            temp(LONG_BREAK_MIN)
            self.interval = 0
            self.Break = False

        elif(state == "Short"):
            temp(SHORT_BREAK_MIN)
            self.Break = False
        else:
            temp(WORK_MIN)
            self.Break = True
            self.interval += 1























