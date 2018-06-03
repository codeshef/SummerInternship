# Main Store File


from checkoutFile import checkoutClass

user = checkoutClass()


class mainStore:

    def menuUser(self):

        print(".....Menu.....")

        if self.category == 'c':
            print('Press 1 : View Products')
            print('Press 2 : Add Products To Cart')
            print('Press 3 : Payment')
            print('Press 4 : View Bill')
            print('Press 5 : Exit')
            print('\n')

            choiceC = 'y'

            while choiceC == 'y':

                keyC = int(input('Enter your choice : '))
                print('\n')
                if keyC == 1:
                    user.viewProducts()
                    print('\n')
                elif keyC == 2:
                    user.addToCart()
                    print('\n')
                elif keyC == 3:
                    user.payment()
                    print('\n')
                elif keyC == 4:
                    user.viewBill()
                    print('\n')
                elif keyC == 5:
                    break
                else:
                    print('You enter invalid input!!!')

                choiceC = input('Want to continue.Press y or n : ')


        else:
            print('Press 1 : Add Products')
            print('Press 2 : View Products')
            print('Press 3 : Exit')

            choiceA = 'y'

            while choiceA == 'y':
                keyA = int(input('Enter your choice : '))
                if keyA == 1:
                    user.addProducts()
                elif keyA == 2:
                    user.viewProducts()
                elif keyA == 3:
                    break
                else:
                    print('You enter invalid input!!!')


                choiceA = input('Want to continue.Press y or n : ')

    def __init__(self):

        self.category = input('Enter whether you are customer or admin. Press c for customer and a for admin : ')
        if self.category.lower() == 'c':
            print('.....Enter as Customer.....')

        elif self.category.lower() == 'a':
            print('.....Enter as Admin.....')

        else:
            print('You enter invalid input!!!')





if __name__ == '__main__':
    mainStoreObj = mainStore()
    mainStoreObj.menuUser()
