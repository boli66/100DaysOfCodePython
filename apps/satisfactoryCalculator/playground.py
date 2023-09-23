from tkinter import *
def y():
    print("y")
def d():
    print("d")
def a():
    print(a)

class main(Tk):
    def __init__(self):
        super().__init__()
        self.title("Clicker")
        self.config(padx=20, pady=20, bg="black")

        self.clicks = 0
        self.button = Button(text="Clicks: 0", font=("arial", 18, "bold"), foreground="cyan",background="#1a1a1a",
            command=self.click)
        self.button.pack()
        self.mainloop()

    def click(self):
        self.clicks += 1
        self.button["text"] = f"Clicks: {self.clicks}"


main()