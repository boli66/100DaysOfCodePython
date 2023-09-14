from consts import *
from tkinter import *
import json
from tkinter import messagebox, simpledialog
player = simpledialog.askstring("Username", "What do you want to call yourself: ")
def off():
    pass
# Cards
class Deck:
    def __init__(self):
        with open("data/newData.json") as f:
            self.cards = json.load(f)
        self.index = 0
    def get(self):
        s = self.cards[self.index]
        self.index += 1
        self.index %= len(self.cards)
        return s
    def remove(self, card):
        self.cards.remove(card.origin)

deck = Deck()

with open(f"data/users/{player}.json", "w") as f:
    json.dump(deck.cards, f)

# Main
card = 0
def start():
    yesB["command"] = off
    noB["command"] = off
    global card
    count = CountDown(3)
    card = Card(deck.get())
    count = CountDown(3)
    countDown(count,card)
    yesB["command"] = right
    noB["command"] = start
def countDown(count,card):
    if(count.down()):
        card.flip()
    else:
        r.after(1*second,countDown, count, card)

#DisplayCard
class CountDown:
    def reset(self):
        self.count = self.time
    def __init__(self, time):
        self.count = time
        self.time = time

    def down(self):
        timeL["text"] = self.count
        if(self.count>0):
            self.count-=1
            r.after(1*second)
            return False
        return True


class Card:
    def __init__(self, card):
        self.origin = card
        names = {}
        for i,key in enumerate(card):
            names[i] = key


        cards = [card[i] for i in card]
        self.name = names[1]
        self.newLang = cards[0]
        self.lang = cards[1]
        r.itemconfig(bg, image=bgBack)
        r.itemconfig(languageL, text=names[0])
        r.itemconfig(textL, text=self.newLang)
    def flip(self):
        r.itemconfig(bg, image=bgFront)
        r.itemconfig(languageL, text=self.name)
        r.itemconfig(textL, text=self.lang)

# Make a game loop

# Flip the card

# Cycle Cards

# Remove Cards

# Check if player got yes/no

# Window
window = Tk()
window.config(padx=50, pady=50, width=1000,height=600, bg=BACKGROUND_COLOR)

# Canvas
r = Canvas(height=526, width=800, bg=BACKGROUND_COLOR)
print(527/2,800/2)
bgFront = PhotoImage(file="images/card_front.png")
bgBack = PhotoImage(file="images/card_back.png")

# Card
bg = r.create_image(400, 263.5,image=bgBack)

# Labels
languageL = r.create_text(400,150,text="Hello", font=("Arial", 40, "italic"))
textL = r.create_text(400,250,text="World", font=("Arial", 60, "bold"))

r.grid(row=0,column=0,columnspan=2)

# yes/no
yesI = PhotoImage(file="images/right.png")
noI = PhotoImage(file="images/wrong.png")

yesB = Button(image=yesI, highlightthickness=0)
noB = Button(image=noI, highlightthickness=0)

yesB.grid(row=1,column=1)
noB.grid(row=1,column=0)

# Time
timeL = Label(text="3", font=("Arial", 40, "normal"), background=BACKGROUND_COLOR)
timeL.grid(row=1, column=0, columnspan=2)

def right():
    deck.remove(card)
    with open(f"data/users/{player}.json", "w") as f:
        json.dump(deck.cards, f)
    start()

start()
window.mainloop()