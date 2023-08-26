import os

from bj import *

# Player input
player = [takeCard(),takeCard()]

while getScore(player)<21:
    printScore("Your", player)
    move = input('"hit" or "stand": ').lower()
    if(move == "hit"):
        player.append(takeCard())
    else:
        break


printScore("Your", player)

if(getScore(player) > 21):
    print("You went over. You lose")
else:
    print("Checking...")
