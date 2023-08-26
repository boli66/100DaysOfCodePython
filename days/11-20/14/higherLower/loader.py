import random

import data


def getThing(index):
    thing = data.data[index]
    out = ""
    out += thing["name"]
    out += ", "
    out += f'a {thing["description"]}'
    out += ", "
    out += f'from {thing["country"]}.'
    return out
def getDict(index):
    return data.data[index]
