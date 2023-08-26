import random as r

flip = r.randint(0,1)
if flip == 1:
    flip = "Tails"
else:
    flip = "Heads"

print(flip)
