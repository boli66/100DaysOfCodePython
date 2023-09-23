import requests
from tkinter import *

iss_now = "http://api.open-notify.org/iss-now.json"




window = Tk()

r = Canvas(width=500,height=500)
lbl = r.create_text(250,250, font=("arial",20,"bold"), text="")
r.create_text(250,20, font=("arial", 20, "bold"), text="ISS Position Live")

def log(func):
    def wrapper():
        print(f"Started {func.__name__}")
        func()
        print(f"Finished {func.__name__}")
    return wrapper

# @log
def update():
    data = requests.get(url=iss_now).json()
    data = data['iss_position']
    print(f"latitude = {data['latitude']}, longitude = {data['longitude']}")
    r.itemconfig(lbl, text=f"latitude = {data['latitude']}\nlongitude = {data['longitude']}")

    window.after(100,update)

r.pack()
window.after(100,update)
window.mainloop()
