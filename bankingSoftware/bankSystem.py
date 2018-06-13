# Banking software using python

import tkinter as t
import os

from tkinter import E, INSERT
from tkinter import W
from tkinter import S
from tkinter import N
from tkinter import messagebox

global count1, count2, root, root2, text1, text2, length
count1 = 0
count2 = 0
length = 1

global currentBalance
global lab3, amountField
global accountNo
global textField

currentBalance = 0.0


# Writing data into textBox

def writeTextBox():
    global textField
    global accountNo
    list = []
    file = open(accountNo, "r")
    data = file.readlines()
    list.extend(data)
    print(list[3:])

    textField.delete('1.0', 'end')
    for i in list[3:]:
        textField.insert(INSERT, i)


# write content into text file

def writeFile(action):
    print("Writing into file ...")
    global accountNo
    global length

    file = open(accountNo, "r")
    data = file.readlines()

    data[2] = str(currentBalance) + '\n'
    file = open(accountNo, "w")
    file.writelines(data)
    file.close()

    file = open(accountNo, "a")
    file.write(action + '\n')
    file.write(amountField.get() + '\n')
    file.close()
    writeTextBox()


# Close current window

def closeFrame(frame):
    frame.destroy()


def depositMoney():
    global lab3
    print("Deposit Money")
    global currentBalance

    amt = float(amountField.get())
    currentBalance = currentBalance + amt
    lab3.configure(text="Balance: $" + str(currentBalance) + "")
    writeFile("Deposit")
    amountField.delete(0, 'end')


def withdrawMoney():
    global lab3
    print('Withdraw Money')

    global currentBalance

    amt2 = float(amountField.get())

    if amt2 > currentBalance:
        messagebox.showinfo("Error", "Insufficent Amount!!")
        amountField.delete(0, 'end')
    else:
        currentBalance = currentBalance - amt2
        lab3.configure(text="Balance: $" + str(currentBalance) + "")
        writeFile("Withdraw")
        amountField.delete(0, 'end')


# Show new window

def showNewWindow(userAccount, userPin):
    global root2
    global currentBalance, amountField
    global lab3
    global textField

    root2 = t.Tk()
    root2.title('Banking System')
    root2.geometry("500x500")
    root2.resizable(0, 0)
    root2.configure(bg="white")

    file = open(userAccount, 'r')
    data = file.readlines()
    currentBalance = float(data[2])
    file.close()

    lab1 = t.Label(root2, text="Account Summary", fg="blue", bg='white', font=("Comic Sans MS Bold", 20))
    lab1.grid(row=0, columnspan=4, sticky=N + S + W + E, padx=5, pady=10)

    lab2 = t.Label(root2, text="Account Number : " + userAccount + "", fg="black", bg='white',
                   font=("Comic Sans MS Bold", 11))
    lab2.grid(row=2, column=0, padx=4, sticky=N + S + E + W)

    lab3 = t.Label(root2, text="Balance: $" + str(currentBalance) + "", fg="black", bg='white',
                   font=("Comic Sans MS Bold", 11))
    lab3.grid(row=2, column=1, padx=4, sticky=N + S + E + W)

    btn1 = t.Button(root2, text="LogOut", width=10, fg="white", bg='Green', command=lambda: closeFrame(root2))
    btn1.grid(row=2, column=2, sticky=E + W)

    lab4 = t.Label(root2, text="Amount($) : ", fg="black", bg='white', font=("Comic Sans MS Bold", 11))
    lab4.grid(row=3, column=0, pady=4)

    amountField = t.Entry(root2)
    amountField.grid(row=3, column=1, pady=4)

    btn2 = t.Button(root2, text="Deposit", width=10, fg="white", bg='Green', command=lambda: depositMoney())
    btn2.grid(row=3, column=2, padx=4)

    btn3 = t.Button(root2, text="Withdraw", width=10, fg="white", bg='Green', command=lambda: withdrawMoney())
    btn3.grid(row=4, column=2)

    textField = t.Text(root2, width=30, font=("Comic Sans MS Bold", 11))
    textField.grid(row=5, columnspan=4, sticky=N + S + E + W)

    writeTextBox()

    root2.mainloop()


# Cancel/Clear function

def clearButton():
    global count1, count2
    print('Inside Clear function')
    text1.delete('1.0', 'end')
    text2.delete('1.0', 'end')
    count1 = 0
    count2 = 0


# Login function

def loginButton():
    print('Inside Login Method')
    global count1, count2, root
    global accountNo

    if count1 == 6 and count2 == 4:

        print('Check validity of account No and Pin')

        print(os.getcwd())

        accountNo = text1.get('1.0', 'end')
        pinNo = text2.get('1.0', 'end')

        print(accountNo)
        print(pinNo)

        os.chdir("/home/anchal/SummerInternship/bankingSoftware")

        if os.path.isdir(accountNo):

            print("File already present!!")
            os.chdir("/home/anchal/SummerInternship/bankingSoftware/" + accountNo)
            accountFile = open(accountNo, "r")
            data = accountFile.readlines()
            acNo = int(data[0])
            pNo = int(data[1])
            accountFile.close()
            print(acNo)

            print(pNo)

            if acNo == int(accountNo) and pNo == int(pinNo):
                print("Valid input jump to next page")
                closeFrame(root)
                showNewWindow(accountNo, pinNo)

            elif acNo == int(accountNo) and pNo != int(pinNo):
                messagebox.showinfo("Error", "Invalid Pin No!!")
                text2.delete('1.0', 'end')
            elif acNo != int(accountNo) and pNo == int(pinNo):
                messagebox.showinfo("Error", "Invalid Account No!!")
                text1.delete('1.0', 'end')
            else:
                messagebox.showinfo("Error", "Invalid Account and Pin no!!")
                text1.delete('1.0', 'end')
                text2.delete('1.0', 'end')
        else:
            os.mkdir(accountNo)
            os.chdir("/home/anchal/SummerInternship/bankingSoftware/" + accountNo)

            accountFile = open(accountNo, "w")
            accountFile.write(accountNo)
            accountFile.write(pinNo)
            accountFile.write('0.0')
            accountFile.close()
            showNewWindow(accountNo, pinNo)

    else:
        print("Something went wrong !!")


def assignText(button):
    print("Button Clicked!! ", button)
    global count1, count2
    enteredText = button['text']

    if count1 < 6:
        text1.insert(INSERT, enteredText)
        count1 = count1 + 1
    else:
        if count2 < 4:
            text2.insert(INSERT, enteredText)
            count2 = count2 + 1
        else:
            messagebox.showinfo("Error", "Pin number must contain 4 digits")
            text2.delete('1.0', 'end-1c')
            count2 = 0


# Layout

def mainWindow():
    global root, text1, text2
    root = t.Tk()
    root.title('Banking Software')
    root.resizable(0, 0)
    root.configure(bg="white")
    label1 = t.Label(root, text="Banking System", fg="blue", bg='white', font=("Comic Sans MS Bold", 25))
    label1.place(x=140, y=25)
    label2 = t.Label(root, text="Account Number/Pin : ", fg="black", bg='white', font=("Comic Sans MS", 12))
    label2.grid(row=0, column=0, padx=10, pady=80, sticky=E + W)
    text1 = t.Text(root, width=20, height=2, font=("Comic Sans MS", 10))
    text1.grid(row=0, column=1, sticky=E + W)
    text2 = t.Text(root, width=20, height=2, font=("Comic Sans MS", 10))
    text2.grid(row=0, column=2, sticky=E + W)
    button1 = t.Button(root, text="1", width=6, height=4, fg="white", bg='Green', command=lambda: assignText(button1))
    button1.grid(row=1, column=0, sticky=S + N + E + W)
    button2 = t.Button(root, text="2", width=6, height=4, fg="white", bg='Green', command=lambda: assignText(button2))
    button2.grid(row=1, column=1, sticky=S + N + E + W)
    button3 = t.Button(root, text="3", width=7, height=4, fg="white", bg='Green', command=lambda: assignText(button3))
    button3.grid(row=1, column=2, sticky=S + N + E + W)
    button4 = t.Button(root, text="4", width=6, height=4, fg="white", bg='Green', command=lambda: assignText(button4))
    button4.grid(row=2, column=0, sticky=S + N + E + W)
    button5 = t.Button(root, text="5", width=6, height=4, fg="white", bg='Green', command=lambda: assignText(button5))
    button5.grid(row=2, column=1, sticky=S + N + E + W)
    button6 = t.Button(root, text="6", width=7, height=4, fg="white", bg='Green', command=lambda: assignText(button6))
    button6.grid(row=2, column=2, sticky=S + N + E + W)
    button7 = t.Button(root, text="7", width=6, height=4, fg="white", bg='Green', command=lambda: assignText(button7))
    button7.grid(row=3, column=0, sticky=S + N + E + W)
    button8 = t.Button(root, text="8", width=6, height=4, fg="white", bg='Green', command=lambda: assignText(button8))
    button8.grid(row=3, column=1, sticky=S + N + E + W)
    button9 = t.Button(root, text="9", width=7, height=4, fg="white", bg='Green', command=lambda: assignText(button9))
    button9.grid(row=3, column=2, sticky=S + N + E + W)
    button10 = t.Button(root, text="Clear/Cancel", width=6, height=4, fg="white", bg='Black',
                        command=lambda: clearButton())
    button10.grid(row=4, column=0, sticky=S + N + E + W)
    button11 = t.Button(root, text="0", width=6, height=4, fg="white", bg='green', command=lambda: assignText(button11))
    button11.grid(row=4, column=1, sticky=S + N + E + W)
    button12 = t.Button(root, text="Login", width=6, height=4, fg="white", bg='Black', command=lambda: loginButton())
    button12.grid(row=4, column=2, sticky=S + N + E + W)
    root.mainloop()


if __name__ == "__main__":
    mainWindow()
