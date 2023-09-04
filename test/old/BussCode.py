import os

s=""
a = [3, 8, 5, 1, 8, 5, 3, 2, 7,1]
i=0
while i < len(a):
  if a[i] % 2 != 0:
    s += f"{a[i]+a[a[i]]}"
    i+= 2
  else:
    i -= 1
def goto_url(url):
  os.system(f"start {url}")
goto_url(f"www.multisoft.se/{s}")