import sys

from expense import *
from iostream import *

expenses = ExpenseTracker("expenses.ex")
expenses.load()
printer = Printer()
actions = {
    "show": expenses.print,
    "add": expenses.Expense,
    "remove": expenses.remove
}
description = [
    "Valid Actions",
    "exit: Closes the program.",
    "show: Shows all the expenses.",
    "add: Adds an expense.",
    "remove: removes an expense."
]

def BadInput():
    print(f"\nInvalid Action!\n")
    for i in description:
        print(i)
    print("")

IN = ""
while IN != "exit":
    IN = input("What do you want to do: ").lower().strip()
    if not IN in actions:
        BadInput()
        continue
    if IN == "remove":
        actions[IN](printer.remove())
    elif IN == "add":
        actions[IN](printer.Expense())
    else:
        actions[IN]()

expenses.save()