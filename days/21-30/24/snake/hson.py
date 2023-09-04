import json

import file

class hson:
    def save(self):
        f = file.writer(self.path)
        f.ln(str(self.obj))
    def get(self):
        f=file.reader(self.path)
        s = f.getLines()
        lines = ""
        for i in s:
            lines+=i
        self.obj = eval(lines)
        return eval(lines)
    def __init__(self, path, obj):
        self.path = path
        self.obj = obj
