import json
class Expense:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
def expense(dict):
    return Expense(dict["name"], dict["cost"])


class ExpenseTracker:
    def __init__(self, path):
        self.expenses = []
        self.path = path

    def Expense(self, expence: Expense):
        self.expenses.append(expence)

    def total(self):
        return sum([i.cost for i in self.expenses])
    def print(self):
        print(str(self))

    def remove(self, name):
        for i in self.expenses:
            if(i.name == name):
                self.expenses.remove(i)
                return i
        return False

    def __str__(self):
        result = ""
        def l(s):
            nonlocal result
            result+=f"{s} kr\n"

        for i in self.expenses:
            l(f"\t{i.name}: {i.cost}")
        l(f"Total: {self.total()}")
        return result

    def load(self):
        try:
            with open(self.path) as f:
                self.expenses = [expense(i) for i in json.load(f)]
        except FileNotFoundError:
            self.expenses = []

    def dict(self):
        return [vars(i) for i in self.expenses]
    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.dict(), f, indent=4)