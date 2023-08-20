print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride this rollercoaster")
    age = int(input("What is your age? "))
    bill = 0
    if age < 12:
        print("The ride will cost $5")
        bill = 5
    elif age <= 18:
        print("The ride will cost $7")
        bill = 7
    elif age >= 45 and age <= 55:
        print("The ride is free because you have a midlife crisis.")
    else:
        print("The ride will cost $12")
        bill = 9

    photos = str.lower(input("Do you want photos for $3? Y or N: "))
    if photos == "y":
        bill += 3
    print(f"The total bill is ${bill}")
        
else:
    print("You are to short :(")
