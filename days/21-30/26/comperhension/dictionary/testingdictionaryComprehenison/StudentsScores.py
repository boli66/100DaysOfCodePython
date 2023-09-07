import random as r

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

scores = {n: r.randint(0, 100) for n in names}

passed = {key:value for key,value in scores.items() if value >=60}

failed = {key:value for key,value in scores.items() if not key in passed}

def Format(dicts: dict):
    return "".join([f"{i} : {dicts[i]}\n" for i in dicts])


print("All Students")
print(Format(scores))

print("Students passed")
print(Format(passed))

print("Students failed")
print(Format(failed))
