# Asks the user for its age
age = input("What is your age?: ")

# Converting the necessary variables
age = int(age)

# Does the necessary calculations
maxAge = 90

years = maxAge-age
months = years*12
weeks = years*52
days = years*365

print(f"You have {years} years, {months} months, {weeks} weeks or {days} days left")
