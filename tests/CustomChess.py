import glob
board = [
    [1,1,1],
    [0,0,0],
    [1,1,1]
]
globals()["score"] = 0
def render():
    piece = "i"
    empty = "■"
    for i in board:
        line = ""
        for j in i:
            if j == 1:
                line+=piece
            elif j == 0:
                line+=empty
        print(line)
    print(f"Your score is {globals()['score']}")
render()
def move():
    ins = input("Write piece and destination: ")
    ins = ins.split(" ")
    x = int(ins[0][0])
    y = int(ins[0][1])


    board[y][x] = 0
    x = int(ins[1][0])
    y = int(ins[1][1])
    if board[y][x] == 1:
        globals()["score"] += 1
    board[y][x] = 1
while True:
    move()
    render()