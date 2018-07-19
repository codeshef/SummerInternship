# file handling exercise

import os

# print(os.getcwd())

# take user input

name = input("Enter your name")
age = input("Enter your age")
phoneNo = input("Enter your phoneNo")

# change directory

os.chdir("/home/anchal/Desktop/userDirectory")

# print(os.getcwd())

if os.path.isdir(name):
    print("Directory already exist")
else:
    os.mkdir(name)

print(name)

os.chdir("/home/anchal/Desktop/userDirectory/" + name)

# write user data into file
data = open("userFile", "w")
data.write(name)
data.write(age)
data.write(phoneNo)
data.close()

# read data from file
data = open("userFile", "r")
text = data.read()
print(text)
data.close()
