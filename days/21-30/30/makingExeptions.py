height = float(input("Height: "))
weight = float(input("Weight: "))
height /=100

if height > 3:
    raise ValueError("Your height is humanly impossible")

bmi = weight/height**2

print(bmi)