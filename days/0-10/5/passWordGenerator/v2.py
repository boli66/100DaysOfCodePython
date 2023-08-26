#Password Generator Project
import random
import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '16', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Gets the inputs
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Creates the password variable
password = ""

# adds the amount of letters the user wants to the password
for i in range(0,nr_letters):
    password += r.choice(letters)

# adds the amount of symbols the user wants to the password
for i in range(0, nr_symbols):
    password+= r.choice(symbols)

# adds the amount of numbers the user wants to the password
for i in range(0,nr_numbers):
    password+= r.choice(numbers)

# Randomizes the password
rPassword = ""
badNums = []
for i in range(0,len(password)):
    while True:
        rand = r.randint(0,len(password)-1)
        if(not badNums.__contains__(rand)):
            rPassword+=password[rand]
            badNums.append(rand)
            break
print(rPassword)