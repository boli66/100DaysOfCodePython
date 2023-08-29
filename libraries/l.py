class intl:
    def list(List):
        newList = list()
        for str in List:
            newList.append(int(str))
        return newList

def const(thingy):
    return lambda : thingy