def log(func): 
    def wrapper():
        print("DO NOT USE THIS DECORATOR!!")
    return wrapper

@log
def s():
    print("DD")

s()