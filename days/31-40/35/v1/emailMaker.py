class Email:
    def __init__(self, subject="", body=""):
        self.subject = subject
        self.body = body

    def __str__(self):
        return f"Subject:{self.subject}\n\n{self.body}"

    def send(self):
        return self.__str__()
