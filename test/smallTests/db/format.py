import json

with open("olddb.json") as f:
    data = json.load(f)

newData = [{"question":i["question"], "correct_answer":i["answer"]} for i in data]

with open("db.json", "w") as f:
    json.dump(newData,f, indent=4)
