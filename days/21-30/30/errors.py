s = [12345,123,54,7,87,342,65,675,876]
d = 2
try:
    d = s[3]

except IndexError:
    print(F"You cant go that far man.")
else:
    pass
    # d = 0
print(d)