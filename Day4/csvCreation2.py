

import os

print(os.getcwd())

os.chdir("/home/anchal/SummerInternship/Day4")

fileOpen = open("project1.csv", "w")

# Adding column title
fileOpen.write("name,email,contactNo\n")

# Adding row data

name = input('Enter name')
email = input('Enter email')
contactNo = input('Enter contact details')

# Writing to file
rowData = name+","+email+","+contactNo+"\n"

fileOpen.write(rowData)




