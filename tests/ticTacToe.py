def boardDefault():
    return [
        ["_","_","_"],
        ["_","_","_"],
        ["_","_","_"]
    ]
board = boardDefault()
winBoards = []
for i in range(0,3):
    winBoard = boardDefault()
    for c in range(0, 3):
        winBoard[i][c] = "*"
    winBoards.append(winBoard)

for c in range(0,3):
    winBoard = boardDefault()
    for r in range(0,3):
        winBoard[c][r] = "*"
    winBoards.append(winBoard)

c = 0
for i in winBoards:
    print(i)
    if(c == 2):
        print()
        c = 0
    else:c+=1