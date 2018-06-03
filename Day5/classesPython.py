
# <------- Day 8 work ------->

# classes in python

class User:

    def __init__(self):
        print("Hello!! I am constructor of class user")

    def setUserName(self, fn, ln):

        print("I am inside setUserNameFunc")
        self.firstName = fn
        self.lastName = ln

    def printData(self):

        print(self.firstName+" "+self.lastName)


## Creating objects

objUser = User()

## Calling class functions

objUser.setUserName("abc", "xyz")
objUser.printData()

