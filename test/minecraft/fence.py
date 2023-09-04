logs = int(input("How many logs: "))
planks = int(input("How many planks: "))
planks+=logs*4
print(planks)
sticks = 0
fences = 0
craftStick = 0

def craftSticks():
    global planks
    if(planks > 2):
        global sticks, craftStick
        planks-=2
        sticks+=4
        craftStick+=1
def craftFence():
    global sticks, planks, fences
    if(sticks >= 2):
        planks-=4
        sticks-=2
        fences+=1
        return True
    else:
        return False

while planks>=4:
    if(not craftFence()):
        craftSticks()
print(f"sticks: {sticks}, craftSticks: {craftStick}, fences: craft: {fences} get: {fences*3}; planks left: {planks}")
