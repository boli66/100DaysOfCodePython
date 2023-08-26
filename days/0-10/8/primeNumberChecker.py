def prime(num):
    isPrime = True
    for i in range(2,num):
        if(num%i == 0):
            isPrime = False
            break
    return isPrime

num = int(input("What number do you want to check: "))
print(f'The number is{"" if prime(num) else " not"} a prime number.')