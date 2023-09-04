import pandas
# Primary Fur Color

data = pandas.read_csv("squirrel.csv")["Primary Fur Color"]
table = {
    "Fur Color":{
        "Gray": 0,
        "Cinnamon": 0,
        "Black": 0,
    }
}
for i in data:
    if(type(i) != type(1.1)):
        table["Fur Color"][i]+=1

out = {}

def keys(dictionary):
    keys = []
    for i in dictionary:
        keys.append(i)
    return keys
def values(dictionary):
    values = []
    for i in dictionary:
        values.append(dictionary[i])
    return values

out["Fur Color"] = keys(table["Fur Color"])
out["count"] = values(table["Fur Color"])

s = pandas.DataFrame(out)
s.to_csv("squirrels.csv")
