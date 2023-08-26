def takeCard():
    import assets
    import random
    return random.choice(assets.deck)

def getScore(deck):
    score = 0
    for i in deck:
        score+=int(i)
    return score
def printScore(name,deck):
    score = getScore(deck)
    print(f"{name} cards: {deck}, current score: {score}")

def fixAces(deck):
    aces = []
    for i, obj in enumerate(deck):
        if (obj == 11):
            aces.append(i)
    counter = len(aces)-1
    while getScore(deck) > 21 and counter>=0:
        deck[aces[counter]] = 1
        counter-=1
    return deck