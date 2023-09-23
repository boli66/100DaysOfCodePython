import sys
class Email:
    def __init__(self, subject="", body=""):
        self.subject = subject
        self.body = body

    def __str__(self):
        return f"Subject:{self.subject}\n\n{self.body}"

    def send(self):
        return self.__str__()
import requests
from datetime import datetime


users = [
    "leo@orr.nu",
    "lisaorr@live.se",
    "roger.orr@live.se"
]

# stockholm longitude/latitude
#"lon": 18.068581,
#"lat": 59.329323,

# Parameters for the api call
params = {
    "appid": "0c2f4c869a8ac08544b22b8472306bf6",
    "lon": 18.068581,
    "lat": 59.329323,
    "exclude": "current,minutely,daily",
    "units": "metric"
}

# Gets the data from the api
api = "https://api.openweathermap.org/data/2.8/onecall"
data = requests.get(api,params)
data.raise_for_status()
data = data.json()

# Makes a function that can check if it rains in the next 12 hrs using the api above
def rainingNext12Hrs():
    # Gets the weather id for the specified hr
    def getID(hr):
        return data["hourly"][hr]["weather"][0]["id"]

    # Goes thru the next 12 hrs and checks if any id is less than 700. If any id is less than 700
    # then return True else False.
    # under 700 means its some sort of rain or snow
    start = None
    end = None
    tms = {}
    for i in range(12):
        id = getID(i)
        if(id<700):
            if(start == None):
                start = i
                continue
            end = i
            continue
        if(start != None and end!=None):
            tms[start] = end
            start = None
            end = None
    return tms

# Makes a function to send emails
def send(email, mail):
    from smtplib import SMTP
    sender = "pythondev1233@gmail.com"
    with SMTP("smtp.gmail.com", 587) as c:
        c.starttls()
        c.login(sender, "zvbdbylnspmsnvzt")
        c.sendmail(sender, email,mail)

# Makes a function to send emails in a specific way
def sendEmails(mail):
    for i in users:
        send(i, mail.send())

# If it is or isn't raining this if statement handles it correctly
def times(tms:dict):
    result = "It's going to rain from ca: "
    now = datetime.now()
    hr = now.hour
    m = now.minute
    for start,end in tms.items():
        result+=f"{(start+hr)%24}:{m}-{(end+hr)%24}:{m}, "
    result = result[:-2]+"."
    return result


raining = rainingNext12Hrs()
if(raining != {}):
    print("Bring umbrella.")
    mail = Email("Notis", "It's going to rain today, so dont forget to bring an umbrella.\n"+
        times(raining))
    sendEmails(mail)
    sys.exit()
print("It's not going to rain today")
mail = Email("Notis", "It's not going to rain today.")
sendEmails(mail)

