from expense import *
class Printer:
    def __init__(self):
        pass

    def remove(self):
        return input("What is the name of the item you want to remove: ")

    def Expense(self):
        name = input("What do you want to call this expense: ")
        amount = ""
        def am():
            nonlocal amount
            try:
                amount = int(input("How expensive is it: "))
            except ValueError:
                print(f"Please put in a number.\n")
                am()
            print("")
        am()
        return Expense(name,amount)

