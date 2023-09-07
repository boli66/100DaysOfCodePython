import keyboard
alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
specialChars = ["ctrl", "shift", "alt", "space"]
arrows = ["up", "down", "left", "right"]

chars = []

for i in alphabet:
    chars.append(i)
chars.extend(specialChars)
chars.extend(arrows)
def keyInputs():
    keys = {}
    for i in chars:
        keys[i] = keyboard.is_pressed(i)
    return keys
def keyInput(x):
    return keyboard.is_pressed(x)