import smtplib

my_email = "pythondev1233@gmail.com"
password = "pythondev"

reciver = "leo@orr.nu"

appPassword = "zvbdbylnspmsnvzt"
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=appPassword)
for i in range(1):
    connection.sendmail(from_addr=my_email, to_addrs=reciver, msg="Subject:Happy Birthday\n\nBody")
connection.close()