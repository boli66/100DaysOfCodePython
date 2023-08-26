class CarBlueprint:
    color = ""
    name = ""
    def __str__(self):
        return f"name = {self.name}, color = {self.color}."
    def __init__(self, name, color):
        self.color = color
        self.name = name

car = CarBlueprint("Nican", "Blue")
print(car)