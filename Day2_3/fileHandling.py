
# File Handling in python

import os

print(os.getcwd())

# to change directory

os.chdir("/home/anchal/Desktop/pythonProjects")

print(os.getcwd())

if(os.path.isdir("student")):
    print("Directory already exist")
else:
    os.mkdir("student")

# to remove os.rmdir("")

print("Directory Created")








