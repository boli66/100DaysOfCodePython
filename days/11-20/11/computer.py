from bj import *

computer = [takeCard(),takeCard()]
printScore("Computer", computer)


while getScore(computer) < 17:
    computer.append(takeCard())

printScore("Computer's", computer)
if getScore(computer)>21:
    print("Computer lose")
else:
    print("Coputer win!")
