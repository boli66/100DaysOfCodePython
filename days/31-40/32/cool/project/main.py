from path import IN as ss
import mains
import os
def IN(path):
    return "./"+ss+path
# Put your code here
with open(IN("emails.txt")) as f:
    emails = f.read().split("\n")

for i in emails:
    mains.send(i)
