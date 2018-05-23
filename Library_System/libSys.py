# Creating library management system using python

print("Welcome to our Library Management System\n")
print("Press 1 : Add Books")
print("Press 2 : Add Members")
print("Press 3 : Issue Books")
print("Press 4 : View Books")
print("Press 5 : View Members")
print("Press 6 : Exit View\n")

ch = 'y'

while(ch == 'y'):
    choice = int(input("Enter Your choice : "))
    # print(choice)
    if(choice==1):
        print("Add Books")
    elif(choice==2):
        print("Add Members")
    elif(choice==3):
        print("Issue Books")
    elif(choice==4):
        print("View Books")
    elif(choice==5):
        print("View Members")
    elif(choice==6):
        print("Exist")
    print("Do you want to continue.Press y for yes and n for no")
    ch = input('Enter y or n')

