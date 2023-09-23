import html


def display(data) -> int:
    s = input(f'{html.unescape(data["question"])} True or False:\n')
    if(s.title().strip() == data["correct_answer"]):
        print(f"Correct!\n")
        return 1
    print(f"Wrong! The correct answer was {data['correct_answer']}.\n")
    return 0

import json
with open("data.json") as f:
    questions = json.load(f)

score = 0
for i in questions:
    score += display(i)
print("You got: "+str(score)+"/"+str(len(questions)))