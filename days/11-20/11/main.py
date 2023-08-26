import os
import sys
import assets
from bj import *

s = input("Do you want to play a game of Black Jack [Y/n]: ")



def main():
    if s == "n":
        sys.exit()
    else:
        os.system("cls")
        print(assets.logo)


    player = [takeCard(),takeCard()]
    printScore("Your", player)
    computer = [takeCard(), takeCard()]
    print(f"Computer's first card: {computer[0]}")
    # Player input
    asd = False
    while getScore(player)<21:
        if(asd):
            player = fixAces(player)
            printScore("Your", player)
        asd = True
        move = input('"hit" or "stand": ').lower()
        print("")
        if(move == "hit"):
            player.append(takeCard())
            player = fixAces(player)
        else:
            break

    # Computer input


    while getScore(computer) < 17:
        computer.append(takeCard())
    computer = fixAces(computer)
    def final(name,deck):
        print(f"{name} final deck is: {deck}, score: {getScore(deck)}.")

    computer = fixAces(computer)
    player = fixAces(player)
    final("Your", player)
    final("Computer's", computer)
    print("")
    if(getScore(player) == getScore(computer)):
        print("Draw")
    elif(getScore(player) > 21):
        print("You went over. You lose")
    elif(getScore(computer) > 21):
        print("You win!")
    elif(getScore(player) > getScore(computer)):
        print("You win!")
    else:
        print("You lose")

    if input("Do you want to play a game of Black Jack [Y/n]: ").lower() == "n":
        sys.exit()
    else:main()


main()