def is_leap(year):
    isLeap = False
    if year % 4 == 0:
        isLeap = True
        if year % 100 == 0:
            isLeap = False
            if year % 400 == 0:
                isLeap = True
    return isLeap


def days_in_month(year, month):
    "Takes a year and a month and returns the correct days in a month depending on if it is a leap year or not."
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(month>12 or month<1):
        return "Invalid month entered."
    if is_leap(year):
        month_days[1] +=1
    return month_days[month-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

