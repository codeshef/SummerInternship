# Date and Tie built in functions
# import datetime as dt
# print(dt.datetime.now())

# print(dt.datetime.now().date())

# print(dt.datetime.now().day)

# print(dt.datetime.now().weekday())

# print(dt.datetime.now().month)

# print(dt.datetime.now().time())

# Using csv module

import csv

a = open("file1.csv", "w")

a.write("name,city\n")

a.write("abc,chd")

a.close()

# Read using reader function

csv_reader = csv.reader(open('file1.csv'), delimiter=',')

for row in csv_reader:
    print(row)
