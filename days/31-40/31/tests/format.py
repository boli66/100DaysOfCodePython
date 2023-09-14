with open("file.txt") as f:
    file = f.read()

file = [f'{j.split(" ")[0]}\n' for j in file.split("\n")]
with open("newfile.txt", "w") as f:
    f.writelines(file)