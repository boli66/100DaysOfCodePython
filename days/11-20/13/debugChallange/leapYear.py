year = int(input("Which year do you want to check?"))
isleap = False
if year % 4 == 0:
    isleap = True
    if year % 100 == 0:
        isleap = False
        if year % 400 == 0:
            isleap = True
if(isleap):
    print("Leap year")
else:
    print("Not leap year")