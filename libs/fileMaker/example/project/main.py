import path
from fileMaker import *

# Put your code here
import clear
with open(f"{path.IN}template.txt") as f:
    template = f.read()

names = getFileAsList(f"{path.IN}names.txt")

for name in names:
    file = template
    file = keyWord(file, "[name]", name)

    saveFile(f"{path.OUT}send_to_{name}.txt", file)
