import random

def rand():
    return (random.random()*5)

rand_float = rand()

# print(rand_float)

name1 = input("What is your name: ").lower()
name2 =input("What is their name: ").lower()

love_score = random.randint(1,100)
print(f"Your score is {love_score}%")