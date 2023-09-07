import os

if(not os.path.exists("./pr/user/dd")):
    os.makedirs("./pr/user/dd")
os.chdir("./pr/user/dd")
with open("ChangedWorkingDir.txt", "w")as f:
    f.writelines(["Hello\n", "World\n"])