# Gets the asks the user for their height and weight
height = input("What is your height in cm?: ")
weight = input("What is your weight in kg?: ")

# Converts the input to floats
weight = float(weight)
height = float(height)

# converts height from centimeters to meters
height = height/100

# Calculates the BMI
BMI = weight/(height*height)

# Prints the BMI
print(f"BMI is {int(BMI)}")