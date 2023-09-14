import smtplib

my_email = "pythondev1233@gmail.com"
appPassword = "zvbdbylnspmsnvzt"
receiver = "leo@orr.nu"


connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=appPassword)
for i in range(10):
    connection.sendmail(from_addr=my_email, to_addrs=receiver, msg="Loops")
connection.close()
print("Email sent successfully")
