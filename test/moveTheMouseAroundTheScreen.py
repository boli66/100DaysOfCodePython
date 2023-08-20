import time as T

import pyautogui as py
xt= py.size().width
yt = py.size().height
print(xt)
xt-=3
yt-=3
py.FAILSAFE = False

print(yt)
for Y in range(0,yt,5):
    for X in range(0,xt,5):
        print(X,Y)
        py.moveTo(X,Y)
        # T.sleep(0.0000001)

