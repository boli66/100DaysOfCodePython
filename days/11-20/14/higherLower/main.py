# Imports
import os
import random as r
import sys

import art
import data
import loader

score = 0
loop = False
def main():
    # Welcome the user
    print(art.logo)
    global loop
    if(loop):
        global score
        print(f"You're right! Current score {score}")

    # Show the options
    def getIndex():
        return r.randint(0,len(data.data)-1)
    # Make the two things to guess from
    p1 = getIndex()
    p2 = getIndex()

    # Display them
    print(f'Compare A: {loader.getThing(p1)}')
    print(art.vs)
    print(f"Compare B: {loader.getThing(p2)}")
    # Get the input
    # Ask the user for witch one they think is better
    AorB = input("Who has more followers? Type 'A' or 'B': ").lower()
    p1 = loader.getDict(p1)
    p2 = loader.getDict(p2)
    # Check if the user was correct
    win = False
    if(AorB == "a"):
        if(p1["follower_count"] > p2["follower_count"]):
            win = True
    elif AorB == "b":
        if(p1["follower_count"] < p2["follower_count"]):
            win = True
    # Make an end game
    def end():
        global score
        if(win):
            global loop
            loop = True
            score+=1
            os.system("cls")
            main()
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            sys.exit()
    end()


main()