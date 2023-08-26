import tkinter as tk

root = tk.Tk()

root.title("Hello World")
lb = tk.Label(root, text="Hello World!")
lb.pack()
lb.config(font=20)
root.geometry("200x200")
root.mainloop()