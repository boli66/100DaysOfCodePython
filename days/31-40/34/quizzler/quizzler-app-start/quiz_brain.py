import html
import time

from ui import QuizInterface

class QuizBrain:

    def __init__(self, q_list, ui: QuizInterface):
        self.ui = ui
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.ui.canvas.config(bg="white")
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.ui.setQuestion(html.unescape(f"Q.{self.question_number}: {self.current_question.text}?"))

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.ui.canvas.config(bg="green")
        else:
            self.ui.canvas.config(bg="red")

        self.ui.setScore(self.score, self.question_number)
