def getLogo(path):
    lines = open(path).readlines()
    line = ""
    for i in lines:
        line += i

    lines = line.split("\n")
    return lines
def printLogo(path):
    lines = getLogo(path)
    for i in lines:
        print(i)


players = {}
import os
def add(name,amount):
    players[name] = amount

printLogo("art.txt")
print("Welcome to the secret action.")

while True:
    name = input("What is your name: ")
    bid = input("What do you want to bid: ")
    add(name, int(bid))
    again = input("Is there another person [Y/n]: ").lower()

    if again != "y":
        os.system("cls")
        break
    os.system("cls")

highest = 0
player = ""
for i in players:
    if players[i] > highest:
        highest = players[i]
        player = i
print(f"{player} won! She bidded {highest}kr.")