import os

# Get Path with: path = f"{os.path.dirname(__file__)}/"

def run(s: list):
    for i in s:
        os.system(i)
def run(s: str):
    os.system(s)

"""def getPath():
    return f'{os.path.dirname(__file__)}/'"""