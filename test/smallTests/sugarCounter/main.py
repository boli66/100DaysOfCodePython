def chocolateMilk(sugarGPer100ml,wholeBottleInLiters):
    bottle = wholeBottleInLiters*1000
    times = bottle/100
    sugar = sugarGPer100ml
    result = sugar
    result*=times

    return result

sugar = input("How much sugar in grams is in the drink every 100ml: ")
bottle = input("How big is the drink in liters: ")

sugar, bottle = float(sugar), float(bottle)

print("There is",chocolateMilk(sugar,bottle), "grams of sugar in this drink.")