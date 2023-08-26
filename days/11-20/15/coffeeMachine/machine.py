import data
def check(coffee):
    def c(resorce):
        return data.resources[resorce] >= coffee["ingredients"][resorce]
    r = data.resources
    coffee = dict(coffee)
    if c("water") and c("milk") and c("coffee"):
        return True
    else:
        return False
def makeCoffee(flavor):
    if check(data.flavours[flavor]):
        i = data.flavours[flavor]["ingredients"]
        r = data.resources
        r["water"] -= i["water"]
        r["milk"] -= i["milk"]
        r["coffee"] -= i["coffee"]
        data.resources = r
        return True
    else:
        return False
def refill():
    r = data.resources["max"]
    d = data.resources
    def c(key):
        d[key] = r[key]
    c("water")
    c("milk")
    c("coffee")
