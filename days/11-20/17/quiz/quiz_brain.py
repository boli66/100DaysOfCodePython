import os

from question_model import question
from data import question_data
class quiz:
    def newQuestion(self, index):
        q = question(self.questions[index],index)
        s = q.get()
        if(s):
            print("You got it right!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer was: {q.answer}.")
        print(f'Your current score is {self.score}/{index+1}\n')

    def chooseQuestions(self):
        chosenNums = []
        import random as r
        for i in range(0,10):
            on = True
            while on:
                num = r.randint(0,len(question_data)-1)
                if(not num in chosenNums):
                    chosenNums.append(num)
                    on = False
            self.questions.append(question_data[num])

    def __init__(self):
        self.score = 0
        self.questions = []
        self.chooseQuestions()
        for i in range(0,len(question_data)):
            self.newQuestion(i)
        os.system("cls")
        os.system("color a")
        print(f'Your final score is {self.score}/{len(question_data)}!')