for y in range(0,5):
    line = " "
    for i in range(y,5-1):
        line+=" "
    for i in range(0,y):
        line+="*"
    for x in range(0,y):
        line+="*"
    print(line)
line = ""
for i in range(0,10):
    line += "*"
print(line)
for y in range(4, 0, -1):
    line = " "
    for i in range(y, 5 - 1):
        line += " "
    for i in range(0, y):
        line += "*"
    for x in range(0, y):
        line += "*"
    print(line)