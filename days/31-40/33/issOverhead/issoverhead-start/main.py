import smtplib
import sys
import time

from emailMaker import *
import requests
from datetime import datetime
def log(*args):
    line = ""
    for i in args:
        line+=i
    print(line)

while True:
    # MY_LAT = 51.507351 # Your latitude
    # MY_LONG = -0.127758 # Your longitude
    MY_LAT, MY_LONG = (59.335060, 18.296930)

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sun = response.json()
    sunrise = int(sun["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun["results"]["sunset"].split("T")[1].split(":")[0])

    now = datetime.now()

    if (now.hour < sunrise or now.hour > sunset):
        night = True
    else:
        night = False
    if not night:
        log("Not Night")
        continue
    data = data["iss_position"]
    if (iss_latitude > MY_LAT - 5 and iss_latitude < MY_LAT + 5):
        if (iss_longitude > MY_LONG - 5 and iss_longitude < MY_LONG + 5):
            def send(reciver, mail):
                user = ["pythondev1233@gmail.com", "zvbdbylnspmsnvzt"]
                connection = smtplib.SMTP("smtp.gmail.com", 587)
                connection.starttls()
                connection.login(user[0], user[1])
                connection.sendmail(user[0], reciver, str(mail))
                connection.close()


            mail = Email()
            mail.subject = "LOOK UP"
            mail.body = "Look Up Because the ISS Space Station is over you."

            send("leo@orr.nu", mail)
            time.sleep(60)
    log(iss_latitude,iss_longitude)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
