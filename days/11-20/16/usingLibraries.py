from  prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Person", "Good"]
x.add_row(["Ronaldo", True])
x.add_row(["Messi", True])
x.add_row(["Ariana Grande", False])

print(x)
