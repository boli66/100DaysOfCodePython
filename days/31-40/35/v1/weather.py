import sys

import requests
#"lon": 18.068581,
#"lat": 59.329323,
params = {
    "appid": "0c2f4c869a8ac08544b22b8472306bf6",
    "lon": 18.068581,
    "lat": 59.329323,
    "exclude": "current,minutely,daily",
    "units": "metric"
}
api = "https://api.openweathermap.org/data/2.8/onecall"
data = requests.get(api,params)
data.raise_for_status()
data = data.json()
def rainingNext12Hrs():
    def getID(hr):
        return data["hourly"][hr]["weather"][0]["id"]

    for i in range(12):
        id = getID(i)
        if(id<700):
            return True
    return False

def send(email, mail):
    from smtplib import SMTP
    sender = "pythondev1233@gmail.com"
    with SMTP("smtp.gmail.com", 587) as c:
        c.starttls()
        c.login(sender, "zvbdbylnspmsnvzt")
        c.sendmail(sender, email,mail)


class Email:
    def __init__(self, subject="", body=""):
        self.subject = subject
        self.body = body

    def __str__(self):
        return f"Subject:{self.subject}\n\n{self.body}"

    def send(self):
        return self.__str__()

if(rainingNext12Hrs()):
    print("Bring umbrella.")
    mail = Email("Notis", "It's going to rain today dont forget to bring an umbrella.")
    send("leo@orr.nu", mail)
    sys.exit()
print("It's not going to rain today")
mail = Email("Notis", "It's not going to rain today.")
send("leo@orr.nu", mail.send())

