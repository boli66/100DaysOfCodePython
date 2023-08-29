class writer:
    def __init__(self, path):
        self.path = path
        self.do = "w"
        self.file = open(path, self.do)
    def ln(self, line):
        self.file.write(f"{line}\n")
    def lns(self, lines):
        for i in lines:
            self.ln(i)

    def close(self):
        self.file.close()

class reader:
    def __init__(self, path):
        self.path = path
        self.do = "r"
        self.file = open(path,self.do)

    def getLines(self):
        lines = self.file.readlines()
        l = ""
        for i in lines:
            l+=i
        lines = l.split("\n")
        return lines
    def printLines(self):
        lines = self.getLines()
        for i in lines:
            print(i)
    def close(self):
        self.file.close()