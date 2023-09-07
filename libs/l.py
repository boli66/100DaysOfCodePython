def negative(IN: int) -> int:
    s = f"-{IN}"
    return int(s)

def backToFront(index: int, length: int):
    return (negative(index)) + length


def numWithSpaces(num: int) -> str:
    num = str(num)
    out = []
    space = 0
    for i in range(len(num)):
        if (space == 3):
            out.append(" ")
            space = 0
        else:
            space+=1
        out.append(num[i])
    return "".join(out).strip()
