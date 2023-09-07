import os


def makeDirs(path):
    if not (os.path.exists(path)):
        os.makedirs(path)


def move(filePath, newFilePath):
    fileName = filePath.split("\\")[-1]

    os.rename(filePath, f"{newFilePath}/{fileName}")


makeDirs("./users")

with open("duck.txt", "w") as f:
    f.writelines(["Hello\n", "World"])

move("./duck.txt", "./users")
