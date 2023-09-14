import json

path = "data/data.json"

with open(path) as f:
    data = json.load(f)

newData = []

for english,swedish in data.items():
    temp = {}
    temp["English"] = english
    temp["Swedish"] = swedish
    newData.append(temp)

with open("data/newData.json", "w") as f:
    json.dump(newData, f, indent=4)