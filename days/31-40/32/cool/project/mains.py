import random
import smtplib

from emailMaker import Email


def send(reciver):
    def getQuot():
        with open("quotes.txt") as f:
            quotes = f.read().split("\n")
        return random.choice(quotes)

    my_email = "pythondev1233@gmail.com"

    #    reciver = "leo@orr.nu"

    mail = Email()
    mail.subject = "Python!"
    mail.body = getQuot()

    appPassword = "zvbdbylnspmsnvzt"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=appPassword)
        for i in range(1):
            connection.sendmail(from_addr=my_email, to_addrs=reciver, msg=str(mail))
