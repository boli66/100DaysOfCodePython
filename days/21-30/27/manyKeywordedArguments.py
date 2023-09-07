def calculate(**ops):
    result = 0
    operations = {
        "add": lambda a: result + a,
        "sub": lambda a: result - a,
        "multiply": lambda a: result * a,
        "divide": lambda a: result / a,
    }
    for i in ops:
        result = operations[i](ops[i])
    return result


# print(calculate(add=3, multiply=5))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
        s = lambda: vars(self)
        for var,value in s().items():
            if(value== None):
                s()[var] = "Not Specified"


car = Car(make="Nissan", model="NT-R")
print(car.color)
print()
