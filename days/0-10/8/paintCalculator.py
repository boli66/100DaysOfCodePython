import math


def calcPaintCans(height,width,cover):
    cans = (height*width)/cover
    cans = math.ceil(cans)
    return cans

h = int(input("Height of wall: m"))
w = int(input("Width of wall: m"))
print(f"You need to buy {calcPaintCans(h,w,5)} can of paint.")