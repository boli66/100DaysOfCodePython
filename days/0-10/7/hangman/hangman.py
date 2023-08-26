import random
import sys
import words
def listify(string):
    list = []
    for i in string:
        list+=string
    return list
import art

wrongCount = 0
strhg = art.words
words = words.word_list# strhg.split(" ")

def getRandomWord():
    return random.choice(words)
word = getRandomWord()
wordl = []
for i in word:
    wordl+="_"

def printHangman():
    print(art.HANGMANPICS[wrongCount])
def printLogo():
    file = open("hangman.txt")
    l = file.readlines()
    nl = ""
    for i in l:
        nl += i
    print(nl)

def printWord():
    print("".join(wordl))
def printStats():
    printWord()
    printHangman()

printLogo()
guessedChars = []
while "".join(wordl) !=word:
    guess = input("Guess a letter: ").lower()
    guess = guess[0]
    wasIn = False
    if guess in guessedChars:
        print(f"You have already guessed {guess}.")
        continue
    else:
        guessedChars+=guess



    for i, obj in enumerate(word):
        obj = str(obj)
        if(guess == obj.lower()):
            wordl[i] = obj
            wasIn = True
    if not wasIn:
        wrongCount += 1
    printStats()
    if wrongCount >= 6:
        print("You lose")
        sys.exit()

print("You Win!")
