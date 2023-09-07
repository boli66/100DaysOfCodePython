def up(path):
    with open(path) as f:
        return [int(f.strip()) for f in f.readlines()]

file1 = up("file1.txt")

file2 = up("file2.txt")

out = [n for n in file1 if n in file2]

print(out)

