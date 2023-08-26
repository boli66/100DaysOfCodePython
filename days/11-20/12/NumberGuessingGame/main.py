from random import *
import art
# Generate random number and display the start of the program to the user
random_number = randint(1,100)

# Welcoming the user
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 16 and 100.")
print("")

# Gets the difficulty the user wants to play on easy = 10 guesses hard = 5 guesses
guesses = 0
s = input('Choose a difficulty. Type "easy" or "hard": ').lower()
print("")
if(s == "hard"):
    guesses = 5
else:
    guesses = 10

# Main loop. Runs until the user is out of guesses or guesses the right number
while True:
    # Checks if you have enough guesses to guess if not then tell them they lose and the picked number
    if(guesses < 1):
        # Lose
        print(f"You've run out of guesses, you lose. The number was {random_number}.")
        break
    # Guessing the number
    print(f"You have {guesses} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    # Checking if it is less than more than or equal to the given number if it is equal you win
    if(guess == random_number):
        # Win
        print(f"You got it! The answer was {random_number}.")
        break
    elif(guess < random_number):
        # To low guess
        print("Too low.")
    elif(guess > random_number):
        # To high guess
        print("To high.")
    print("Try again.")
    print("")

    # decrements the guess so that you do not have infinite guesses
    guesses-=1