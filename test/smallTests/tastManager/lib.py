# Saves the inputted tasks to a txt file
def prints(l:list):
    for i in l:
        print(i)
def index(l: list) -> list:
    s = range(1,len(l)+1)
    out = [f"{s[i]}: {l[i]}" for i in range(len(l))]
