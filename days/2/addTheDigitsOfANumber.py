# This program will get a number.
# Get the digits of the number.
# Then add those digits together and print the number

# gets the 2 digit number to work with
Input = input("Write a 2 digit number: ")
number = 0

# adds the first digit to the total value
inty = int(Input[0])
number += inty

# adds the second digit to the total value
inty = int(Input[1])
number += inty

print(number)