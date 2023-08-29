class question:
    def __init__(self, question,i):
        self.question = question["question"]
        self.answer = question["correct_answer"]
        self.i = i
    def get(self):
        s = input(f'Q.{self.i}: {self.question} (true/false): ').lower()
        return True if s == self.answer.lower() else False