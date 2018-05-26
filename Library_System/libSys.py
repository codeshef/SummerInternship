# Creating library management system using python basic fundamentals

# Books related data

bookId = [1, 2, 3, 4, 5]
bookName = ['c', 'c++', 'python', 'java', 'css']
bookQuantity = [1, 2, 2, 3, 1]

bookIdName = dict(zip(bookId, bookName))
bookNameQuant = dict(zip(bookName, bookQuantity))

# Members related data

memberId = [1, 2, 3, 4, 5]
memberName = ['a', 'b', 'c', 'd', 'e']

memberDict = dict(zip(memberId, memberName))


# fun to increase quantity of books

def increaseQuantity(my_dic, name, quant):
    for key in my_dic:
        if key == name:
            value = my_dic[key]
            print(value)
            value = value + quant
            bookQuantity.append(value)
            my_dic[key] = value
            flag = True
            break
        else:
            flag = False
    if not flag:
        # new book is added
        bookQuantity.append(quant)
        my_dic[name] = quant


# fun to decrease quantity of books

def decreaseQuantity(my_dic, name, quant):
    for key in my_dic:
        if key == name:
            value = my_dic[key]
            print(value)
            value = value - quant
            bookQuantity.append(value)
            my_dic[key] = value
            flag = True
            break
        else:
            flag = False
    if not flag:
        bookQuantity.append(quant)
        my_dic[name] = quant


# fun to add Books

def addBooks():
    print("Add Books\n")

    id = int(input('Book Id : '))
    name = input("Book Name : ")
    quantity = int(input('Book Quantity : '))

    bookId.append(id)
    bookName.append(name)


    # add values in dictionary

    bookIdName[id] = name

    increaseQuantity(bookNameQuant, name, quantity)


# fun to add members

def addMembers():
    print("Add Members\n")

    memid = int(input('Enter member id : '))
    memName = input("Enter member name : ")

    # add value to lists
    memberId.append(memid)
    memberName.append(memName)

    # add value to dictionary
    memberDict[memid] = memName

# fun to Issue books

def issueBooks():
    print("Issue Books\n")



# fun  to View Books

def viewBooks():
    print("View Books\n")

    for key, value in bookIdName.items():

        print("Book id = ",  key)
        print("Book Name = ", value)
        print("Book Quantity = ", bookNameQuant[value])


# fun to View Members

def viewMembers():
    print("View Members\n")

    print("Total Number of Members : ", memberDict.__len__())
    print('\n')

    for key, value in memberDict.items():
        print("Member id : ", key)
        print("Member name : ", value)


# Menu Bar

print("Welcome to our Library Management System\n")
print("Press 1 : Add Books")
print("Press 2 : Add Members")
print("Press 3 : Issue Books")
print("Press 4 : View Books")
print("Press 5 : View Members")
print("Press 6 : Exit View\n")

# for while condition

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
    print("Do you want to continue.Press y for yes ")
    ch = input('Enter y or any other key : ')
