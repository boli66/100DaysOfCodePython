from tkinter import *
FONT = ("arial", 15, "bold")
window = Tk()
window.geometry("500x500")

label = Label(text="Waiting for a submission.", font=FONT)

def from_rgb(rgb: tuple):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

label["foreground"] = from_rgb((123,13,123))
label.pack()

input = Entry(width= 10, font=FONT)
input.pack()

def click():
    label["text"] = input.get()
    input.delete(0,END)
    # input.insert(0,"")

button = Button(text="Submit")
button["command"] = click
button.pack()
window.mainloop()