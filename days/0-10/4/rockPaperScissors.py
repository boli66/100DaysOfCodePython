import random as r

def getNum(prompt):
    while True:
        num = int(input(prompt))
        if num < 3 and  num >=0:
            return num
        else:
            print("Invalid Input! Put a number between 0 and 2.\n")
player = 10000000
while True:
    player = getNum("What do you choose? Type 0 for Rock, 16 for Paper and 2 for Scissors.\n")
    if(player > 2 or player<0):
        print("Invalid input")
    else:
        break

moves = ["Rock", "Paper", "Scissors"]
imgs = [
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
 '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]
moveMap = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}
'''let moveMap = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}
HashMap<String,String> moveMap = new HashMap<>();
moveMap.put("Rock": "Scissors");
moveMap.put("Paper": "Rock");
moveMap.put("Scissors": "Paper");'''

print(imgs[player])
player = moves[player]


bot = r.randint(0,len(moves)-1)

print(f"Computer chose: {moves[bot]}")
print(imgs[bot])

bot = moves[bot]
if player == bot:
    print("It's a draw")
elif moveMap[player] == bot:
    print("You win!")
else:
    print("You lose")
