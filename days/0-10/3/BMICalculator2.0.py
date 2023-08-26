# Welcomes the user
print("Welcome to the BMI Calculator")
# Gets the input
weight = float(input("What is your weight kg: "))
height = int(input("What is your height cm: "))

# Math
height /= 100
BMI = round(weight / (height*height))
start = f"Your BMI is {BMI}. "

# Give the values
# example: Your BMI is 28, you are slightly overweight.
if BMI < 18.5:
    if BMI >= 16.5:
        print(f"{start}you are slightly underweight.")
    else:
        print(f"{start}you are underweight.")
elif BMI < 25:
    print(f"{start}you are normal weight.")
elif BMI < 30:
    if BMI <= 27:
        print(f"{start}you are slightly overweight.")
    else:
        print(f"{start}you are overweight.")
elif BMI < 35:
    if BMI <= 32:
        print(f"{start}you are slightly obese.")
    else:
        print(f"{start}you are obese.")
else:
    print(f"{start}you are clinically obese.")
