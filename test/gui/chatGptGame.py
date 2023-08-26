

import tkinter as tk

def move_box():
    canvas.move(box, dx, dy)
    root.after(10, move_box)  # Call move_box() again after 50 milliseconds

def move_left(event):
    global dx
    dx = -2
    global dy
    dy = 0

def move_right(event):
    global dx
    dx = 2
    global dy
    dy = 0

def move_up(event):
    global dx
    dx = 0
    global dy
    dy = -2

def move_down(event):
    global dx
    dx = 0
    global dy
    dy = 2

root = tk.Tk()
root.title("Move the Box Smoothly")

canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

box = canvas.create_rectangle(180, 180, 220, 220, fill="lime green")

dx, dy = 0, 0  # Initialize the speed of movement

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

move_box()  # Start the smooth movement

root.mainloop()