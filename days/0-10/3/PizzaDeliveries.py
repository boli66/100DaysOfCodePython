# Greets the user
print("Welcome to Python Pizza Deliveries!")

# Gets inputs
size = input("What size do you want S, M, L: ")
peperoni = input("Do you want peperoni Y or N: ")
extra_Cheese = input("Do you want extra cheese Y or N: ")
bill = 0
class costs:
    size = [15,20,25]
    extraCheese = 1
    peperoni = [2,3]


# Ifs
#Size
if size == "S":
    bill = costs.size[0]
    size = 0
elif size == "M":
    bill = costs.size[1]
    size = 1
elif size == "L":
    bill = costs.size[2]
    size = 1

# Peperoni
if peperoni == "Y":
    bill += costs.peperoni[size]

# Extra cheese
if extra_Cheese == "Y":
    bill += costs.extraCheese
print(f"Your final bill is: ${bill}")

