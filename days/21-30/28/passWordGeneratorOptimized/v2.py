#Password Generator Project
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
password = []

# adds the amount of letters the user wants to the password
temp = (letters,nr_letters)
password.extend([r.choice(temp[0]) for _ in range(temp[1])])

# adds the amount of symbols the user wants to the password
temp = (symbols, nr_symbols)
password.extend([r.choice(temp[0]) for _ in range(temp[1])])

# adds the amount of numbers the user wants to the password
temp = (numbers, nr_numbers)
password.extend([r.choice(temp[0]) for _ in range(temp[1])])

# Randomises the password
r.shuffle(password)
password = "".join(password)

print(password)

# 6 r 2