numbers = [1,2,3]

# Old
"""
new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)"""
# New
new_list = [n+1 for n in numbers]
print(new_list)

