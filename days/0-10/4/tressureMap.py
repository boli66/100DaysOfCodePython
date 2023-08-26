import os
def main():
    board = [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

    def printB():
        for i in board:
            print(i)

    printB()

    cords = input("Where do you want to put the treasure: ")

    x = int(cords[0])
    y = int(cords[1])

    board[y][x] = "X"

    printB()
main()