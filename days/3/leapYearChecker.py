# Gets the year
year = int(input("What year do you want to check: "))

# Math
isLeap = False

if year % 4 == 0:
    isLeap = True

    if year % 100 == 0:
        isLeap = False

        if year%400 == 0:
            isLeap = True


if isLeap:
    print("Leap year.")
else:
    print("Not leap year.")
