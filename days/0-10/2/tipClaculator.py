# Greets the user
print("Welcome to the tip Calculator.")

# Asks the user for all the things we need
bill = input("What is the total bill? ")
precentOfBillToPay = input("What percentage tip would you like to give? 10, 12, 15? ")
split = input("How many people to split the bill? ")

# Covert the variables
precentOfBillToPay = "0."+precentOfBillToPay
bill = float(bill)
precentOfBillToPay = float(precentOfBillToPay)
split = int(split)

# Math
eachPerson = bill/split
eachPerson += eachPerson*precentOfBillToPay
eachPerson = round(eachPerson,2)


# Show the result
print(f"Each person should pay: ${eachPerson}")
