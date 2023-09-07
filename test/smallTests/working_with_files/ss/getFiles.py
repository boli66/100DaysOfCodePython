def getFile(path: str):
    with open(path)as f:
        lines = f.read()
        with open(path.split("/")[-1], "w") as f:
            f.write(lines)

getFile("./../lib.py")