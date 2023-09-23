class Email:
    def __init__(self):
        self.subject = ""
        self.body = ""

    def __str__(self):
        return f"Subject:{self.subject}\n\n{self.body}"
