import pyautogui as py
import keyboard
lastKey = None
while True:
    event = keyboard.read_event()
    if(event.scan_code != lastKey):
        print(event.scan_code)
        lastKey = event.scan_code

