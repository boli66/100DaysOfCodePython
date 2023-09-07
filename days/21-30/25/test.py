import keyboard as key

def sss():
    key.press("down")
    key.write("print()")

key.add_hotkey("up", sss)

while not key.is_pressed("F12"):
    pass