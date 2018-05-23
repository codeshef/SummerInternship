
# File Handling in python

import os

print(os.getcwd())

# to change directory

os.chdir("/home/anchal/Desktop/pythonProjects/student")

#mode = w,r,a,r+,w+
a = open("file1.txt","w")
a.write("Hello everyone")
a.close()
print("file created")

a = open("file1.txt","r")
text = a.read()
print(text)
a.close()










