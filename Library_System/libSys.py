# Creating library management system using python


# func to add Books
def addBooks():
    print("Add Books")


# func to add members
def addMembers():
    print("Add Members")


# func to Issue books
def issueBooks():
    print("Issue Books")


# func  to View Books
def viewBooks():
    print("View Books")


# func to View Members

def viewMembers():
    print("View Members")


print("Welcome to our Library Management System\n")
print("Press 1 : Add Books")
print("Press 2 : Add Members")
print("Press 3 : Issue Books")
print("Press 4 : View Books")
print("Press 5 : View Members")
print("Press 6 : Exit View\n")

ch = 'y'

while ch == 'y':
    choice = int(input("Enter Your choice : "))
    # print(choice)
    if choice == 1:
        addBooks()
    elif choice == 2:
        addMembers()
    elif choice == 3:
        issueBooks()
    elif choice == 4:
        viewBooks()
    elif choice == 5:
        viewMembers()
    elif choice == 6:
        print("Exist")
        break
    print("Do you want to continue.Press y for yes and n for no")
    ch = input('Enter y or n')
