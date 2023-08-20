to = input("Binary to decimal or Decimal to binary 1/2: ")
def toDecimal(bin):
    add = 1
    result = 0
    for i in range(0,len(bin)):
        if bin[i] == "1":
            result += add
        add *= 2
    return result
def toBinary(dec):
    bin = ""
    while(not(dec < 1)):
        bin += str(round(dec % 2))
        dec = dec / 2
    return bin

if to == "1":
    bin = input("What is the binary number: ")
    print(toDecimal(bin))

if to == "2":
    dec = input("What is the decial number: ")
    print(toBinary(int(dec)))