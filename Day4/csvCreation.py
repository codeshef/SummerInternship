## Creating csv file using python


fileName = "project.csv"

# open file for writing

fileOpen = open(fileName, "w")

# Give title to our columns and write that data on csv

fileOpen.write("name,branch,phoneNo\n")

# Adding data to rows

fileOpen.write("abc,cse,1234567890\n")

fileOpen.close()


