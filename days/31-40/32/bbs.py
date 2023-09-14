import datetime as dt

def weekday(day: int):
    days = "monday tuesday wednesday thursday friday saturday sunday".title().split(" ")
    #day-=1
    return days[day]

time =  dt.datetime.now()

print(weekday(time.weekday()))