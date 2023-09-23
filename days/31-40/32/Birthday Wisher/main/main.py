import random
import smtplib
from emailMaker import Email
from isBirthday import isBirthday, dt
import json
def date(date:dict):
    return dt.datetime(year=date["year"], month=date["month"], day=date["day"])

def getQuot():
    with open("quotes.txt") as f:
        quotes = f.read().split("\n")
    return random.choice(quotes)

def getEmail():
    mail = Email()
    mail.subject("Happy Birthday!")
    mail.body = getQuot()
    return mail

def send(reciver):
    mail = getEmail()
    email = "pythondev1233@gmail.com"
    appPassword = "zvbdbylnspmsnvzt"
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(email, appPassword)
    connection.sendmail(from_addr=email, to_addrs=reciver, msg=str(mail))

def sendEmail(data):
    if(isBirthday(date(data["birthday"]))):
        send(data["email"])

with open("data.json") as f:
    data = json.load(f)

for i in data:
    sendEmail(i)
