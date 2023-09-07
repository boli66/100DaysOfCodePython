sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
from lib import *
result = {w: len(w) for w in sentence.split(" ")}


print(Format(result))
