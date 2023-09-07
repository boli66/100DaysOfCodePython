import os

# A function that makes dirs
import os
def makeDirs(path):
    if not (os.path.exists(path)):
        os.makedirs(path)

def getFile(path: str,destination):
    name = path.split('/')[-1]
    if(name != "__pycache__"):
        with open(path)as f:
            lines = f.read()
            makeDirs(destination)
            with open(destination+"/"+path.split('/')[-1], "w") as f:
                f.write(lines)
def getDir(path: str):
    folderName = path.split("/")[-1]

    makeDirs(f"./lib")
    for i in os.listdir(path):
        getFile(f"{path}/{i}",f"./lib")


# Temp


# Makes the project folder
makeDirs("./project")
os.chdir("./project")
getDir(r"C:\src\python\TutorialPyCharm\libs\fileMaker\files")
#getFile(r"C:\src\python\TutorialPyCharm\libs\fileMaker\files\fileMaker.py", ".\\")
IN = "./in/"
OUT = "./out/send/"

# Makes a file with all the paths for the project
with open("path.py", "w") as f:
    lines = [
        f'IN = "{IN}"',
        f'OUT = "{OUT}"'
    ]
    lines = [f"{line}\n" for line in lines]
    f.writelines(lines)

with open("main.py","w") as f:
    lines = [
        "import path",
        "# Put your code here"
    ]
    lines = [f"{n}\n" for n in lines]
    f.writelines(lines)

makeDirs(IN)
with open("./in/template.txt", "w") as f:
    f.write("Waiting for a template.")

makeDirs(OUT)
