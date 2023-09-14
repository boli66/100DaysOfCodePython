import pandas
import json
data = pandas.read_csv("data.csv")
#print([i for i in data.iterrows()])
data = {row["English"]:row["Swedish"] for index,row in data.iterrows()}

with open("data.json", "w") as f:
    json.dump(data,f, indent=4)

for en,sv in data.items():
    print(en,sv)