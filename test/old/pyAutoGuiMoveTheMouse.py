import Time

import pyautogui as py

# py.click(10,10)
# py.write("Hello",16)
time.sleep(3)
py.keyDown("left",False,True)
py.sleep(10)
py.keyUp("left")