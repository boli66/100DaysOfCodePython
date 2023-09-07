import os

def makeDirs(path):
    if not (os.path.exists(path)):
        os.makedirs(path)

def getFile(path: str,destination):
    name = path.split('/')[-1]
    if not(name == "__pycache__"):

        with open(path)as f:
            lines = f.read()
            makeDirs(destination)
            with open(f"{destination}/{name}", "w") as f:
                f.write(lines)
def getDir(path: str):
    folderName = path.split("/")[-1]

    makeDirs(f"./lib")
    for i in os.listdir(path):
        getFile(f"{path}/{i}",f"./lib")


# Temp
getDir(r"C:\src\python\TutorialPyCharm\libs\fileMaker\files")
