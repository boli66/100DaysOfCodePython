import os

import coffee_maker
import menu
import money_machine
coffeeMaker = coffee_maker.CoffeeMaker()
moneyMachine = money_machine.MoneyMachine()
coffees = menu.Menu()

# Coverts the coffee object into something readable
def _str(coffee):
    return f'\t{coffee.name} costs: ${coffee.cost}.'
def printMenu():
    print("Menu:")
    for i in coffees.menu:
        if(coffeeMaker.canMakeThis(i)):
            print(_str(i))
        else:
            print(f"{_str(i)} Out if stock. Select this to call a staff.")
def end():
    input("Press enter to finish.")
    os.system("cls")
class res:
    max={
        "water": 2500,
        "milk": 1500,
        "coffee": 200
    }
def refill(things):
    for i in things:
        coffeeMaker.resources[i] = res.max[i]
    print("Refilled")


while True:
    printMenu()
    coffee = input("What would you like: ").lower()
    if(coffee == "report"):
        coffeeMaker.report()
        moneyMachine.report()
        end()
        continue
    coffeeObj = coffees.find_drink(coffee)

    if(coffeeMaker.is_resource_sufficient(coffeeObj)):
        if(moneyMachine.make_payment(coffeeObj.cost)):
            coffeeMaker.make_coffee(coffeeObj)
    else:
        def check(ingredient):
            if(coffeeObj.ingredients[ingredient] > coffeeMaker.resources[ingredient]):
                return True
            else:
                return False
        things = []
        for i in ["water", "milk", "coffee"]:
            if(check(i)):
                things.append(i)
        refill(things)
    end()

