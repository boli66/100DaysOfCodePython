import sys

import wow
print("Welcome to treasure island.")
print("Your mission is to find the treasure.")

In = input("You're at a cross road. Where do you go? left or right\n").lower()
if(In != "left"):
    print("You fall into a hole and die. Game Over.")
    sys.exit()

In = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
if(In != "wait"):
    print("You get attacked by an angry trout. Game Over.")
    sys.exit()

In = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose?\n").lower()
if(In == "red"):
    print("It's a room full of fire. Game Over.")
    sys.exit()
elif(In == "blue"):
    print("You enter a room full of beasts. Game Over.")
    sys.exit()
elif(In == "red"):
    print("You found the treasure. You Win!")
    sys.exit()