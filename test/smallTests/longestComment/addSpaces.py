with open("message.txt") as f:
    lines = f.read().split("\n")

s = [lines[0]]
nls_per_line = 1000
for i in lines[1:]:
    s.extend(["\n" for _ in range(nls_per_line-1)])
    s.append(i)

with open("final.txt", "w") as f:
    f.writelines(s)