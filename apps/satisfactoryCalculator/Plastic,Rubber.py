from math import *

oil = int(input("How much crude oil do you have: "))

machines = floor(oil/20) # 20 is how much oil a machine needs to run
oil %= 20

plasticMachines = floor(machines/2)
rubberMachines = floor(machines/2)
machines -= machines%2

plastic = plasticMachines*20
rubber = rubberMachines*20
BiProduct = plasticMachines*10+rubberMachines*20

fuelMachines = ceil(BiProduct/60)
fuel = fuelMachines*40

print(f"Rubber machines: {rubberMachines}, Plastic machines: {plasticMachines}; Produces Rubber/Plastic: {plastic}")
print(f"Fuel machines: {fuelMachines}; Produces roughly: {fuel} fuel")
print(f"Total machines: {machines+fuelMachines}")
