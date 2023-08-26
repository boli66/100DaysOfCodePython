heights = input("Enter a all the students heights separated py spaces.\n").split(" ")

people = 0
total = 0
for i in heights:
    total += int(i)
    people+=1

total/=people
total = round(total)
print(f"The average length was {total}")