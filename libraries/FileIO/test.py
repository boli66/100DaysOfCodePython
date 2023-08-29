import file as f

file = f.writer("js.txt")

lines = [
    "Hello",
    "World",
    "With my new file I/O library"
]
file.lns(lines)
file.close()

file = f.reader("js.txt")

file.printLines()
file.close()