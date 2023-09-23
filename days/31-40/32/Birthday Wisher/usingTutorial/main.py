##################### Extra Hard Starting Project ######################
import json
import datetime as dt
import math
import smtplib
from emailMaker import Email
import random

# 1. Update the birthdays.csv
# Done

user = ["pythondev1233@gmail.com", "zvbdbylnspmsnvzt"]

# 2. Check if today matches a birthday in the birthdays.csv
# Gets The Data
with open("data.json") as f:
    people = json.load(f)

# Gets the current time
t = dt.datetime.now()

# checks if any birthdays are today
def isBirthday(date: dict, tm=t):
    date = date["birthday"]
    date = dt.datetime(year=tm.year,month=date["month"], day=date["day"], hour=8)
    return date == tm

def send(reciver, mail):
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user[0],user[1])
    connection.sendmail(user[0],reciver,str(mail))
    connection.close()

def getBody(name):
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as f:
        template = f.read().replace("[NAME]", name)
    return template

def sendEmail(data):
    mail = Email()
    mail.subject = "Happy Birthday!"
    mail.body = getBody(data["name"])
    send(data["email"], mail)


for i in people:
    date = people[-1]["birthday"]
    t = dt.datetime(year=t.year,month=date["month"], day=date["day"], hour=8)
    def per(d:dt.datetime):
        d = dt.datetime(d.year,d.month,d.day,d.hour,d.minute,math.floor(d.second))
        return d

    print(dt.datetime(2020,12,25,8), per(dt.datetime.now()))
    if(isBirthday(i, t)):
        #sendEmail(i)
        print(f"sent To {i['name']}")

