# Features :
# In this we include Product Scanning
# show bill receipt (Show pending or extra balance)
# Handle Conversion
# Use isDigit in payment

from productFile import Product

pidNameDict = {1: 'bread', 2: 'butter'}
pnameCostDict = {'bread': 20.00, 'butter': 10.00}
cartStatus = {}


class checkoutClass:

    def __init__(self):
        self.amount = 0.0
        print(".....Welcome to Our Store.....")

    def addProducts(self):
        nObj = 0
        choice = 'Y'
        while choice == 'Y':

            self.pId = int(input('Enter Product Id  : '))
            self.pName = input('Enter Product Name : ')
            self.pCost = float(input('Enter Product Cost :$ '))

            if float(self.pCost):

                pObject = Product(self.pId, self.pName, self.pCost)
                pidNameDict[self.pId] = self.pName
                pnameCostDict[self.pName] = self.pCost
                choice = input("Add More Items Y or N : ")
            else:
                print('You enter invalid input...')


    def viewProducts(self):

        print("......Available items in Store ......")

        for key in sorted(pidNameDict):
            print("Product Id : ", key)
            print("Product Name : ", pidNameDict[key])
            print("Product Cost : $", pnameCostDict[pidNameDict[key]])

    def addToCart(self):


        self.amount = 0.0

        ch = 'Y'

        while ch == 'Y':

            self.name = input("Enter name of item you want to purchase : ")

            flag = False

            for key in pnameCostDict:

                if key == self.name.lower():

                    print('Item Name : ', key)
                    print('Item Cost : ', pnameCostDict[key])
                    value = pnameCostDict[key]

                    self.amount += value

                    cartStatus[key] = value
                    flag = True
                    print('Item successfully added to cart!!!')
                    break
                else:
                    flag = False

            if not flag:
                print('Item is not available\n')
            ch = input('Enter Y to purchase more and N to Exit : ')

    def payment(self):

        self.cost = float(input('Enter your amount $'))

        if float(self.cost):

            if self.cost < self.amount:

                extraAmount = self.amount - self.cost

                print("Your have to pay more $", extraAmount)


            elif self.cost > self.amount:

                extraAmount = self.cost - self.amount

                print("Amount Refunded $", extraAmount)

            else:
                print("Transaction Completed Order Placed Successfully!!\n")
        else:
            print('Error : You enter invalid amount\n')

    def viewBill(self):
        print("..... Your Bill .....")

        for key in cartStatus:
            print('Item Name : ', key)
            print('Item Cost : $', cartStatus[key])

        print('Total Amount : $', self.amount)
        print('\n')
        print('Thanks for visiting us!!!\n')

