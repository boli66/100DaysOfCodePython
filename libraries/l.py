class intl:
    def list(List):
        newList = list()
        for str in List:
            newList.append(int(str))
        return newList

def const(thingy):
    return lambda : thingy

def addTabs(tabs:int):
    return "".join(["\t" for _ in range(tabs)])

def formatList(l:list, tabs:int=1):
    lines = [addTabs(tabs-1)+"{\n"]
    for value in l:
        line = addTabs(tabs)
        if (type(value) == type([])):
            value = formatList(value, 2)
        elif (type(value) == type({})):
            value = formatDict(value)

        line+=f"{str(value)}\n"
        lines.append(line)
    return addTabs(tabs-1)+"}"


def formatDict(d:dict, tabs:int=1):
    lines = [addTabs(tabs-1)+"{\n"]
    for key, value in d.items():
        if(type(value) == type([])):
            value = "\n"+formatList(value,2)
        elif(type(value) == type({})):
            value = "\n"+formatDict(value,2)

        line = addTabs(tabs)
        line+=f"{key}: {str(value)}\n"
        lines.append(line)

    return ("".join(lines)+addTabs(tabs-1)+"}")
