from time import sleep
from pyautogui import click, position
import win32api, win32con
def click(mouseButtonDown):
    # win32api.SetCursorPos((x, y))  # Set the mouse cursor position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # Press the left mouse button
    sleep(mouseButtonDown)  # Pause for a short time (adjust as needed)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

for i in range(4):
    print(-i+3)
    sleep(1)
delay = 0.0001
time = 0
i = 0
print(1.1*delay)
while time < 1.1:
    #click(delay)
    i += 1
    time+=delay
    #print(round(time,1))
print(i)