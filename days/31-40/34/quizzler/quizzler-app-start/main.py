import json
import random
import time

import requests
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
try:
    with open("data.json") as f:
        question_data=json.load(f)
        random.shuffle(question_data)
except FileNotFoundError:
    params = {
        "amount": 10,
        "type": "boolean"
    }

    api = "https://opentdb.com/api.php"
    question_data = requests.get(api,params).json()["results"]

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

ui = QuizInterface()
quiz = QuizBrain(question_bank,ui)
def valid():
    return ui.answer != None
quiz.next_question()
last = False
def main():
    global last
    if(last):
        last=False
        time.sleep(1)
        quiz.next_question()
        ui.reset()

    if valid():
        quiz.check_answer(ui.answer.__str__())
        last = True
    if(quiz.still_has_questions()):
        ui.after(10,main)
    else:
        ui.setQuestion("Done!")
main()
ui.mainloop()
