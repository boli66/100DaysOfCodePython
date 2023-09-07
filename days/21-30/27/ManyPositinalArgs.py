def add(*nums: int):
    result = 0
    for i in nums:
        result+=int(i)
    return result

print(add(1,2,3,4,5,6,7,"8"))