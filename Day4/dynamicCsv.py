# A program to create csv file in python

import os

print(os.getcwd())

os.chdir("/home/anchal/SummerInternship/Day4")

fileName = input('Enter the name of your file with.csv extension')


def writeFile():
    print("<<<<< Writing  your file >>>>>")

    choiceW = 'y'

    # Create empty list for column and row data

    columnList = []

    rowList = []

    choiceW = 'y'
    choiceR = 'y'

    print('Adding Column Data : ')

    while choiceW == 'y':
        columnData = input('Enter Column Data : ')

        columnList.append(columnData)
        (',').join(columnList)

        print(columnList)

        choiceW = input('Want to add more columns press y')

    print("Adding Row Data : ")

    while choiceR == 'y':
        for i in range(len(columnList)):
            print('Enter ' + columnList[i] + ' : ')
            rowData = input()
            rowList.append(rowData)
            (',').join(rowList)

            print(rowList)
        choiceR = input('Want to add more data press y')


    #open file created by user in writing mode
    fileOpen = open(fileName, "w")
    # start writing column data
    fileOpen.write(columnList)
    # start writing row data
    fileOpen.write(rowList)

    fileopen.close()



def readFile():
    print("<<<<< Reading your file >>>>>")


print("......Create your own csv file.......")
print("Press 1 : Write")
print("Press 2 : Read")
print("Press 3 : Exit")

ch = 'y'

while ch == 'y':

    choice = int(input("Enter your choice"))

    if choice == 1:
        writeFile()
    elif choice == 2:
        readFile()
    elif choice == 3:
        break
    else:
        print("Invalid NUmber")

    ch = input('Do you want to continue press y')
