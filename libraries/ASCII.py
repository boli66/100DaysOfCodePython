def getLogo(path):
    lines = open(path).readlines()
    line = ""
    for i in lines:
        line += i

    lines = line.split("\n")
    return lines
def printLogo(path):
    lines = getLogo(path)
    for i in lines:
        print(i)