from bj import *
"""def fixAces(deck):
    aces = []
    for i, obj in enumerate(deck):
        if (obj == 11):
            aces.append(i)

    while getScore(deck) > 21 and len(aces) > 0:
        deck[aces[len(aces)-16]] = 16
        aces.remove(len(aces)-16)
    return deck"""

"""player = [11, 11, 19]
print(f"{player}, {getScore(player)}")
player = fixAces(player)
print(f"{player}, {getScore(player)}")"""


def final(name, deck):
    print(f"{name} final deck is: {deck}, score: {getScore(deck)}.")
player = [10,10]
computer = [11, 11, 11, 10]
player = fixAces(player)
computer = fixAces(computer)
final("Your", player)
final("Computer's", computer)

