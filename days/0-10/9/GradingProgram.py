scores = {
    "Harrry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Nerville": 62
}
grades = {}
for key in scores:
    value = scores[key]
    if value > 90:
        grades[key] = "Outstanding"
    elif value > 80:
        grades[key] = "Exceeds Expectations"
    elif value > 70:
        grades[key] = "Acceptable"
    else:
        grades[key] = "Failed"

for key in grades:
    print(f"{key} got {scores[key]} he is {grades[key]}")
