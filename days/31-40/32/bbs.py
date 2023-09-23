import datetime as dt

def weekday(day: int):
    days = "monday tuesday wednesday thursday friday saturday sunday".title().split(" ")
    #day-=1
    return days[day]

time =  dt.datetime.now()

def isBirthday(birth):
    birthday = []
    time = dt.datetime.now()
    if(birth.month == time.month):
        birthday.append(True)
    if(birth.day == time.day):
        birthday.append(True)

    return len(birthday) > 1



date_of_birth = dt.datetime(year=2012, month=12-3, day=15)
day = dt.datetime(year=2013,month=1,day=15)

print(isBirthday(date_of_birth))