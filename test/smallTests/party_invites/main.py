import os
import path

# Makes a function to create dirs
def makeDirs(path):
    if not (os.path.exists(path)):
        os.makedirs(path)

# Makes the out directory
makeDirs(path.OUT)

# Gets the names
with open(f"{path.IN}names.txt") as f:
    names = f.read()
    names = names.split("\n")
    names = [n.title() for n in names]
with open(f"{path.IN}template.txt") as f:
    template = f.read()

def createMessage(name):
    with open(f"{path.OUT}send_to_{name}.txt", "w") as f:
        lines = template
        lines = lines.replace("[name]", name)
        f.write(lines)
for name in names:
    createMessage(name)

