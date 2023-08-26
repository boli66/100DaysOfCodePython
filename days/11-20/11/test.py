import os
import sys
import assets
from bj import *

#s = input("Do you want to play a game of Black Jack [Y/n]: ")



def main():
    #if s == "n":
        #sys.exit()
    #else:
        #os.system("cls")
        #print(assets.logo)


    player = [10,10]
    computer = [11,11,11,10]

    # Computer input


    while getScore(computer) < 17:
        computer.append(takeCard())
    def final(name,deck):
        print(f"{name} final deck is: {deck}, score: {getScore(deck)}.")

    computer = [11, 11, 11,8 ]
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