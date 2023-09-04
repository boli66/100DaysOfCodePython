import file
import paths

names = file.reader("people.txt").getLines()
group = []
groups = ["fire", "mid", "lame"]
for gr in groups:
    for i in range(round(len(names)/3)):
        group.append(gr)



template = file.reader(paths.Template).getLines()

def checkWord(word, replaceWith, line):
    s = word
    if(s in line):
        index = line.index(s)
        start = line[:index]
        end = line[index + len(s):]
        line = f"{start}{replaceWith}{end}"
    return line
def listInList(list1, word):
    contains = False
    for i in list1:
        if(i in word):
            contains = True
            break
    return contains

def getKeys(dic):
    keys = []
    for i in dic:
        keys.append(i)
    return keys

def makeLetter(name, index):
    out = []
    for dex, i in enumerate(template):
        # s = ["[name]", "[group]"]
        line = i
        replaceWith = {"[name]": name, "[group]": group[index]}
        while(listInList(getKeys(replaceWith), line)):
            for i in replaceWith:
                line = checkWord(i, replaceWith[i], line)
                # print(f"Line = {line}")
        out.append(line)
    return out

for i in names:
    file.writer(f"{paths.OUT}letter_to_{i}.txt").lns(makeLetter(i, names.index(i)))


