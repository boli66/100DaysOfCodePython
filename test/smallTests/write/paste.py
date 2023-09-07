import pyautogui as py
import keyboard as key
from libraries.FileIO import file
# Point(x=2192, y=34)

def paste():
    with open(f"main.py") as f:
        ss = f.read()

    for i in range(len(ss)):
        key.write("\b")

    with open(f"clipboard.txt") as f:
        key.write(f.read())

    # py.click(2192,34)


