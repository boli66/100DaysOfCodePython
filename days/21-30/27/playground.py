import random as r

def addFunc():
    def add(*nums: int):
        result = 0
        for i in nums:
            result += int(i)
        return result
    print(add(1,23,4,5,235,523,5,243,22,5,6,4,23,345))


def shuffleFunc():
    Founder = "Angela Yu"
    def shuffle(string: str):
        string = [c for c in string]
        r.shuffle(string)
        return "".join(string)

    newFounder = shuffle(Founder)
    tries = 0
    while newFounder != Founder:
        newFounder = shuffle(Founder)
        tries +=1

    print(f"Got this after {tries} tries.")
    print(f"Before {Founder}")
    print(f"After {newFounder}")
