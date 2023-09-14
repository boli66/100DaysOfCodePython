def Format(dicts):
    out = "{\n"
    out += "".join([f"\t'{word}': {length}\n" for word, length in dicts.items()])
    return out + "}"