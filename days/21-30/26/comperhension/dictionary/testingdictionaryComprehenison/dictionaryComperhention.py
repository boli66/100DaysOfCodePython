dicti = {
    "txt": "What does idk stand for: ",
    "answer": "i dont know"
}
answers = [
    ""
]


def kv(dicti: dict):
    return [(d, dicti[d]) for d in dicti]


def range(start=0, end: int = False, step=1):
    s = []
    if (end == False):
        end = start
        start = 0
    while start < end:
        s.append(start)
        start += step
    return s


new = {key: value for key, value in dicti.items()}


def isPrime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True


def squareRoot(num):
    num = int(num)
    for i in range(1, num):
        if i ** 2 == num:
            return i


def show(num):
    print(f"The square root of {num} is {squareRoot(num)}.")


while True:
    show(input("Write a number: "))
