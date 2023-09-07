def keyWord(lines,keyword, string):
    return lines.replace(keyword,string)

def getFileAsList(path):
    with open(path,"r") as f:
        return f.read().split("\n")

def saveFile(path,lines:str):
    with open(path,"w") as f:
        f.write(lines)
