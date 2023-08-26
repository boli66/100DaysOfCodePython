# Welcome the user
print("Welcome to the Band Name Genenrator")

# ask the user what city they grew up in and store it in a variable called city
print("What's the name of the city you grew up in?")
city = input("")

# ask the user what their pet's name is and store it in a variable called pet
print("What's the name of your pet's name?")
pet = input("")

# Add the two variables we created and print it as a band name the user could use
bandName = city + " " + pet
print(f"Your band name could be {bandName}")
