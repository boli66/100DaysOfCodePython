import random as r

people = input("Give me everybody's names, separated by a space: ")
people = people.split(" ")

person = people[r.randint(0,len(people)-1)]

print(f"{person} is going to pay for the meal today!")
