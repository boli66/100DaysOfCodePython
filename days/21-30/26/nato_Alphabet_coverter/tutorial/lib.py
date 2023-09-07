
def FormatDict(dicts: dict):
    out = "{\n"
    out += "".join([f"\t'{word}': {len}\n" for word, len in dicts.items()])
    return out + "}"


def FormatList(dicts: list):
    out = "{\n"
    out += "".join([f"\t'{word}'\n" for word in dicts])
    return out + "}"