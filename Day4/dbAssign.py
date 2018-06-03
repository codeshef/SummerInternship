# Assignment : 2

import mysql.connector

conn = mysql.connector.connect(user='root', password='anchal', host='127.0.0.1')

myCursor = conn.cursor()
myCursor.execute("Use studentDb")


# Functions

def insertData():
    print('Insert data')

    name = input('Enter Name : ')
    salary = input('Enter Salary : ')
    myCursor.execute("Insert into userTbl(name,salary) values('" + name + "','" + str(salary) + "')")

    print('Data successfully inserted!!')

    conn.commit()


def updateData():
    print('Update data')

    Id = int(input('Enter Id'))
    choiceU = input("you want to update name ,salary or both")

    if choiceU == 'name':
        updatedName = input('Enter updated Name : ')
        myCursor.execute(
            "Update userTbl Set name = '" + updatedName + "' where id='" + str(Id) + "'")

        conn.commit()
        print("Updated Successfully !!!")

    elif choiceU == 'salary':
        updatedSalary = int(input('Enter updated Salary: '))
        myCursor.execute("Update userTbl Set salary = '" + str(updatedSalary) + "' where id='" + str(Id) + "'")
        conn.commit()
        print("Updated Successfully !!!")

    else:
        updatedName = input('Enter updated Name : ')
        updatedSalary = int(input('Enter updated Salary : '))

        myCursor.execute(
            "Update userTbl Set name = '" + updatedName + "', salary = '" + str(
                updatedSalary) + "' where id='" + str(
                Id) + "'")

        conn.commit()
        print("Updated Successfully !!!")


def deleteData():
    print('Delete data')

    data = input("Whether you want to  delete from salary col,name col,entire row")

    print('Press 1 : To delete from salary col...')
    print('Press 2 : To delete from name col...')
    print('Press 3 : To delete entire row')

    choiceD = int(input('Enter your choice'))
    Id = input('Enter Id you want to delete')

    if choiceD == 1:
        myCursor.execute("Delete salary from userTbl where id='" + Id + "'")
        conn.commit()
        print("Deleted Successfully!!")
    elif choiceD == 2:
        myCursor.execute("Delete name from userTbl where id='" + Id + "'")
        conn.commit()
        print("Deleted Successfully!!")
    elif choiceD == 3:
        myCursor.execute("Delete from userTbl where id='" + Id + "'")
        conn.commit()
        print("Deleted Successfully!!")
    else:
        print('That id is no longer available')


def readData():
    print('Read data')

    myCursor.execute('Select*from userTbl')
    myList = myCursor.fetchall()
    for i in myList:
        j = int(i[0])
        print(str(j) + " " + i[1] + " " + str(i[2]))

        conn.commit()


print("Welcome to our portal")
print("Press 1 : Insert")
print("Press 2 : Update")
print("Press 3 : Delete")
print("Press 4 : Read")
print("Press 5 : Exit")

ch = 'y'

while ch == 'y':

    choice = int(input("Enter your choice"))

    if choice == 1:
        insertData()
    elif choice == 2:
        updateData()
    elif choice == 3:
        deleteData()
    elif choice == 4:
        readData()
    elif choice == 5:
        conn.close()
        break
    else:
        print("Invalid NUmber")

    ch = input('Do you want to continue press y')
