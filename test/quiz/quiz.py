import time as T
import sys
questions = ["What is the capital of sweden: ",
             "What is the character with index 3 in this string \"1234\": "
             "What is the color of the presidents house in USA: "
             ]
answers = [
    "stockholm",
    "4",
    "white"
]
def inc(Int):Int+1
score = 0
def get(i):
    response = input(questions[i])
    if (str.lower(response) == answers[i]):
        inc(score)
        print("Good Job!")
    else:
        print("Try better next time.")
get(0)
get(1)
get(2)
# Main game loop

# End
print(f"You got {score} points!")