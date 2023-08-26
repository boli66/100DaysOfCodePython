# Greets the user
print("Welcome to the love calculator")

# Gets the names of the people that are going to be tested
name1 = input("What is your name: ").lower()
name2 =input("What is their name: ").lower()

name1 += name2
score1 = 0
score2 = 0

def check(str,checkstr):
    chars = checkstr
    Sad = 0
    for i in range(0, len(chars)):
        Sad += str.count(chars[i])
    return Sad

score1 = check(name1,"true")
score2 = check(name1,"love")

Score = f"{score1}{score2}"
score = int(Score)
Score+="%"
if score<10 or score>90:
    Score+=", you go together like coke and mentos."
elif score >=40 and score<=50:
    Score+=", you are alright together."

print(f"Your score is {Score}")
