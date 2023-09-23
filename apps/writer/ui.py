from tkinter import *
BG_COLOR = "#104c77"
FONT = ("arial", 15, "bold")

s = len("Signature: ")
codes = {
    "[CHECKBOX]": "▢",
    "[SIGNATURE]": "Signature: "+"".join(["_" for i in range(51-s)]),
}

def fix(lines):
    l = lines
    for code,result in codes.items():
        l = l.replace(code,result)
    return l


class UI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Writer")
        pad = 20
        self.config(padx=pad, pady=pad, bg=BG_COLOR)

        Button(text="Convert", font=FONT, borderwidth=5, command=self.fix).pack()

        self.window = Text(height=35,width=50, font=FONT)
        self.window.config(borderwidth=5)
        self.window.pack()
        self.mainloop()

    def fix(self):
        lines = self.getText()
        self.window.delete("1.0", "end")
        self.window.insert("1.0", fix(lines))

    def getText(self):
         return self.window.get("1.0", "end-1c")

UI()