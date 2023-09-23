import datetime as dt

def isBirthday(birthday: dt.datetime):
    t = dt.datetime.now()
    if(birthday.day == t.day and birthday.month == t.month):
        return True
    return False
