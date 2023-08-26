import os
import ASCII

def getInt(prompt, errorMessage):
    on = True
    while on:
        num1 = ""
        while type(num1) != type(1.1):
            num1 = input(prompt)
            try:
                num1 = float(num1)
                return num1
            except:
                print(f"{errorMessage}\n")

oprations = {
    "+": lambda a,b : a+b,
    "-": lambda a,b : a-b,
    "*": lambda a,b : a*b,
    "/": lambda a,b : a/b
}
def getOperator():
    while True:
        for i in oprations:
            print(i)
        op = input("What operation do you want to use?: ")
        if op in oprations:
            return op
        else:
            print("Invalid operation!")

def main():
    ASCII.printLogo("Logo.txt")
    num1 = getInt("What's the first number?: ", "Not a Valid Number!\n")
    print("")
    while True:
        op = getOperator()
        print("")
        num2 = getInt("What's the second number?: ", "Not a Valid Number!\n")
        answer = oprations[op](num1,num2)
        print(f"{num1} {op} {num2} = {answer}")
        again = input(f"Do you want to continue calculating with {answer} or do you want to create a new calculation [Y/n]: ")
        if(again != "n"):
            num1 = answer
            print("")
        else:
            os.system("cls")
            main()


main()