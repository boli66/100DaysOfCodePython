nums = [n for n in range(1,10+1)]

new = []
for n in nums:
    if(n%2==0):
        new.append(n)

evenNumbers = [n for n in nums if n%2 == 0]
print(f"Before {nums}\nAfter {evenNumbers}")