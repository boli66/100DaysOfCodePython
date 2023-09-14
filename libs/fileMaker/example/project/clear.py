import os

path = f"./out/send/"

items = os.listdir(path)

for i in items:
    os.remove(path+i)