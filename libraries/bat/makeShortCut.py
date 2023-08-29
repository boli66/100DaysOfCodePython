# Input
import os
from libraries.FileIO import terminal as t
os.system("cd C:/src/python/TutorialPyCharm/libraries/bat/")
path = f"{os.path.dirname(__file__)}/"
from libraries.FileIO import terminal, file, hson
data = hson.hson(f"{path}/data.json", {}).get()
OUTPATH = data["outPath"]
DAYSPATH = data["daysPath"]
THIS = data["this"]+f"libraries/bat/"
if input("Open OutFolder[Y/n]: ").lower() != "n":
    pass
else:
    fromDays = input("Do you want to get it from days[Y/n]: ").lower()
    if(fromDays != "n"):
        fromDays = True
    else: fromDays = False
    filePath = input("What is the path of the python file: ")
    filename = input("What is the name of the python file: ")
    batFileName = input("What do you want to call the batchFile: ")
    # Make the file
    # file = open(f"{OUTPATH}{batFileName}.bat", "w")
    path = f"{OUTPATH}{batFileName}.bat"

    print(os.path.dirname(__file__))
    lines = [
        "@echo off",
        f'cd {DAYSPATH if fromDays else ""}{filePath}',
        f"python {filename}.py",
        "pause"
    ]
    f = file.writer(path)
    f.lns(lines)
    f.close()



print(os.path.dirname(__file__))
def openExplorer():
    global DAYSPATH
    lines = [
        f"cd {OUTPATH}",
        f"start ."
    ]
    batName = f"{THIS}/openOutPath.bat"
    f = file.writer(batName)
    f.lns(lines)
    f.close()
    t.run(batName)

openExplorer()
