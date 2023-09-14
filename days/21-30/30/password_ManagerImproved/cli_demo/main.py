def append(path:str,lines:list):
    with open(path)as f:
        s = f.readlines()

    s.extend(lines)
    with open(path,"w") as f:
        f.writelines(s)

def lns(list):
    return [f"{i}\n" for i in list]

lines = [
    "Ayo",
    "That guy do be dripin"
]

ln = []

for i in range(10):
    ln.extend(lines)
    ln.append("")

append("data.txt", lns(ln))