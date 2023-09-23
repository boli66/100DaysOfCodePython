import json, requests
from datetime import datetime

api = "https://api.sunrise-sunset.org/json"

parameters = {
    "lat": 59.335060,
    "lang": 18.296930
}
response = requests.get(api, params=parameters)
response.raise_for_status()
rawData = response.json()["results"]
def APIWithParams(api, params):
    url = api+"?"
    def add(name,value):
        url = ""
        url+=name
        url+="="+str(value)
        url+="&"
        return url
    for i in [i for i in params][:-1]:
        url += add(i,params[i])
    url+=f"{[i for i in params][-1]}={params[[i for i in params][-1]]}"
    return url


data = {
    "sunset": rawData["sunset"],
    "sunrise": rawData["sunrise"]
}

def s(d:str):
    date = d
    rawdate = date.split(" ")
    date = rawdate[0]
    date = date.split(":")
    date = [int(i) for i in date]
    if(rawdate[1] == "PM"):date[0]+=12
    return date

now = datetime.now()
sun = s(data["sunset"])
sunset = datetime(now.year,now.month,now.day,sun[0],sun[1],sun[2])
print(sunset-now)