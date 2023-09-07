names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [n for n in names if len(n)<5]
long_names = [n.upper() for n in names if len(n)>5]
print(long_names)