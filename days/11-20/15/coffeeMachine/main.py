import math
import os
import sys
import time
import data
import machine

while True:
    coffees = "espresso/latte/cappuccino"
    # Ask the user what coffee they want:
    coffee = input(f"What would you like? ({coffees}): ")
    # print(f"What would you like? ({coffees}): {coffee}")

    # Checks if the user wants to see the resources the machine has left
    if(coffee == "off"):
        sys.exit()
    if(coffee == "report"):
        def c(r):
            return data.resources[r]
        def ad(r,unit):
            print(f"{r}: {c(r)}{unit}")

        ad("water","ml")
        ad("milk","ml")
        ad("coffee","g")
        print(f'money: ${c("money")}')

        input("Press enter to finish.")
        os.system("cls")
        continue

    print(f'That will be ${data.flavours[coffee]["price"]}.\n')

    # Get their coins
    print("Please enter your coins.")
    total = 0
    for i in data.coins:
        total += int(input(f"How many {i}s do you have?: "))*data.coins[i]

    # Calculate their change and see if they have enough or not
    price = data.flavours[coffee]["price"]

    # Checks if enough money was put in
    if price <= total:

        # Says the users change
        print(f"Here is ${round(total-price,2)} in change.")

        while True:
            # Checks if the required recources exists else it makes them
            if machine.check(data.flavours[coffee]):

                # Makes the coffee and resets
                print(f"Here is your {coffee} ☕. Enjoy!")
                machine.makeCoffee(coffee)
                data.resources["money"] +=price
                break

            else:
                # Gets a staff to refill the machine and then give the coffee
                print("There is not enough resources to make your coffee. Staff will come shortly.")
                time.sleep(3)
                machine.refill()
                print("Staff is refilling.")
                time.sleep(3)
                print("Staff is done making your coffee.")

    else:
        # Don't have enough money
        print("Sorry that's not enough money. Money refunded")

    # Waits until the user is finished then clears the screen
    input("Press enter to finish.")
    os.system("cls")