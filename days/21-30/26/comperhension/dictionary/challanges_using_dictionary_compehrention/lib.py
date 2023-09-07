def Format(dicts):
    out = "{\n"
    out += "".join([f"\t'{word}': {len}\n" for word, len in dicts.items()])
    return out + "}"