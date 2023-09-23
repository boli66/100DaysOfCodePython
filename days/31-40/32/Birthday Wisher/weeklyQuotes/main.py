import random
from emailMaker import *
import datetime as dt
import smtplib

def weekDay(day:int):
    days = "monday tuesday wednesday thursday friday saturday sunday".title().split(" ")
    return days[day]
def getQuot():
    with open("quotes.txt") as f:
        quotes = f.read().split("\n")
    return random.choice(quotes)

def send(reciever, mail):
    appPassword = "zvbdbylnspmsnvzt"
    #appPassword = "pythondev"
    email = "pythondev1233@gmail.com"
    
    t = dt.datetime.now()
        
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(email,appPassword)
    connection.sendmail(from_addr=email,to_addrs=reciever,msg=str(mail))
    connection.close()

t = dt.datetime.now()
if(weekDay(t.weekday()) == "Friday"):
    mail = Email()
    mail.subject = f"Happy {weekDay(t.weekday())}!"
    mail.body = getQuot()
    send(reciever="leo@orr.nu", mail=mail)