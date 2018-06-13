from tkinter import *
import math

root = Tk()

global x, y, r, b, c

x = 0
y = 0
r = 0
b = 0
c = ''

global clrscr
clrscr = True
op = False
fstage = True
global temp
temp = ""
dotcl = True
root.title("Calculator")
root.resizable(0, 0)
global newText
newText = ""

# Memory varibles
global M
M = 0

# Functions


text1 = Text(root, width=30, height=3, font='arial 10 bold')
text1.insert(INSERT, '0')
text1.grid(row=1, columnspan=5, sticky=N + S + W + E, padx=5, pady=5)
text1.configure(background='powder blue')


# For normal working of textbox
def normal():
    text1.config(state=NORMAL)
    return


# To disable textbox but issue arise during insert operation
def disable():
    text1.config(state=DISABLED)
    return


# To shift alignment of text to right in textBox
# def justify():


# '+' is clicked

def addClicked(first, second):
    global r

    r = first + second

    print("Result in addition fun", r)
    text1.delete('1.0', 'end')
    text1.insert(INSERT, r)


# '=' is clicked

def equalToClicked():
    global r
    print(r)
    text1.delete('1.0', 'end')
    text1.insert(INSERT, r)


# '*' is clicked

def multiClicked(first, second):
    global r
    r = first * second
    print("Result in Multiply fun", r)
    text1.delete('1.0', 'end')
    text1.insert(INSERT, r)


# '-' is clicked

def subClicked(first, second):
    global r
    r = first - second
    print("Result in Sub fun", r)
    text1.delete('1.0', 'end')
    text1.insert(INSERT, r)


# '/' is clicked

def divClicked(first, second):
    global r
    r = float(first / second)
    print("Result in  Div fun", r)
    text1.delete('1.0', 'end')
    text1.insert(INSERT, r)


# '%' is clicked

def percentageFun(first):
    global r
    r = float(first / 100.0)
    print("Result in  percentage fun", r)
    text1.delete('1.0', 'end')
    text1.insert(INSERT, r)
    op = False


# '√' is clicked

def sqrtFun(first):
    global r
    r = math.sqrt(first)
    print("Result in  Sqrt fun", r)
    text1.delete('1.0', 'end')
    text1.insert(INSERT, r)
    op = False


# '1/x' is clicked

def reciprocalFun(first):
    global r
    r = float(1 / first)
    print("Result in  Reciprocal  fun", r)
    text1.delete('1.0', 'end')
    text1.insert(INSERT, r)
    op = False


# '±' is clicked

def signFun(first):
    global r
    r = (-1) * first
    print("Result in sign  fun", r)
    text1.delete('1.0', 'end')
    text1.insert(INSERT, r)
    op = False


# 'C' is clicked

def clearScreen():
    global x, y, r, c
    global clrscr, op
    text1.delete('1.0', 'end')
    clrscr = True
    x = 0
    y = 0
    r = 0
    c = ''
    op = False
    text1.insert(INSERT, '0')


# 'MS' is clicked

def storeInMem(first):
    global M, op
    M = first
    print(M)
    op = False


# 'MC' is clicked

def clearMem():
    global M, op
    M = 0
    op = False


# 'MR' is clicked

def useMem():
    global M, op


# operation function

def operationFun():
    if c == '+':
        addClicked(x, y)
    elif c == '=':
        equalToClicked()
    elif c == '-':
        subClicked(x, y)
    elif c == '*':
        multiClicked(x, y)
    elif c == '/':
        divClicked(x, y)
    elif c == 'C':
        clearScreen()
    elif c == '%':
        percentageFun(x)
    elif c == '√':
        sqrtFun(x)
    elif c == '1/x':
        reciprocalFun(x)
    elif c == '±':
        signFun()
    elif c == 'MS':
        storeInMem(x)
    elif c == 'MC':
        clearMem()


# single operand operations(%,√,1/x)
def singleOperand():
    if c == 'C':
        clearScreen()
    elif c == '%':
        percentageFun(x)
    elif c == '√':
        sqrtFun(x)
    elif c == '1/x':
        reciprocalFun(x)
    elif c == '±':
        signFun(x)
    elif c == 'MS':
        storeInMem(x)
    elif c == 'MC':
        clearMem()


def assignText(button):
    print('Assign numbers to text block....')

    global clrscr
    global op
    global x, y, c

    enteredText = button["text"]

    if enteredText == "0":
        if clrscr:
            # Case when 0 present in front

            text1.delete('1.0', 'end')
            text1.insert(INSERT, '0')
        else:

            # Case when 0 present in middle
            text1.insert(INSERT, enteredText)

    elif enteredText != '0' and enteredText != 'MC' and enteredText != 'MR' and enteredText != 'MS' and enteredText != 'M+' and enteredText != 'M-' and enteredText != '←' and enteredText != 'CE' and enteredText != 'C' and enteredText != '±' and enteredText != '√' and enteredText != '/' and enteredText != '%' and enteredText != '*' and enteredText != '1/x' and enteredText != '+' and enteredText != '-' and enteredText != '=' and enteredText != '*':

        # Remove initially add  zero to add new number

        input1 = text1.get('1.0', 'end-1c')
        print(input1)
        if input1 == "0":
            text1.delete('1.0', 'end-1c')
        text1.insert(INSERT, enteredText)
        clrscr = False


    elif not op:
        clrscr = False
        x = float(text1.get('1.0', 'end-1c'))
        print("x : ", x)
        text1.delete('1.0', 'end')
        clrscr = True

        text1.insert(INSERT, enteredText)
        op = True
        c = text1.get('1.0', 'end-1c')
        print("c : ", c)
        text1.delete('1.0', 'end')

        # operation that don't require operand
        singleOperand()

    elif op:

        clrscr = False
        y = float(text1.get('1.0', 'end-1c'))
        print("y : ", y)
        text1.delete('1.0', 'end')
        clrscr = True
        operationFun()

        if enteredText == 'MC' or enteredText == 'MR' or enteredText == 'MS' or enteredText == 'M+' or enteredText == 'M-' or enteredText == '←' or enteredText == 'CE' or enteredText == 'C' or enteredText == '±' or enteredText == '√' or enteredText == '/' or enteredText == '%' or enteredText == '*' or enteredText == '1/x' or enteredText == '+' or enteredText == '-' or enteredText == '=' or enteredText == '*':

            c = enteredText
            op = False

        else:
            op = True


button1 = Button(root, text="MC", width=6, command=lambda: assignText(button1))
button1.grid(row=2, column=0, padx=4)

button2 = Button(root, text="MR", width=6, command=lambda: assignText(button2))
button2.grid(row=2, column=1, padx=4)

button3 = Button(root, text="MS", width=6, command=lambda: assignText(button3))
button3.grid(row=2, column=2, padx=4)

button4 = Button(root, text="M+", width=6, command=lambda: assignText(button4))
button4.grid(row=2, column=3, padx=4)

button5 = Button(root, text="M-", width=6, command=lambda: assignText(button5))
button5.grid(row=2, column=4, padx=4)

button6 = Button(root, text="←", width=6, command=lambda: assignText(button6))  # alt27(23 to 27)
button6.grid(row=3, column=0, padx=4, pady=4)

button7 = Button(root, text="CE", width=6, command=lambda: assignText(button7))
button7.grid(row=3, column=1, padx=4, pady=4)

button8 = Button(root, text="C", width=6, command=lambda: assignText(button8))
button8.grid(row=3, column=2, padx=4, pady=4)

button9 = Button(root, text="±", width=6, command=lambda: assignText(button9))  # alt+0177
button9.grid(row=3, column=3, padx=4, pady=4)

button10 = Button(root, text="√", width=6, command=lambda: assignText(button10))  # alt+251
button10.grid(row=3, column=4, padx=4, pady=4)

button11 = Button(root, text="7", width=6, command=lambda: assignText(button11))
button11.grid(row=4, column=0, padx=4, pady=4)

button12 = Button(root, text="8", width=6, command=lambda: assignText(button12))
button12.grid(row=4, column=1, padx=4, pady=4)

button13 = Button(root, text="9", width=6, command=lambda: assignText(button13))
button13.grid(row=4, column=2, padx=4, pady=4)

button14 = Button(root, text="/", width=6, command=lambda: assignText(button14))
button14.grid(row=4, column=3, padx=4, pady=4)

button15 = Button(root, text="%", width=6, command=lambda: assignText(button15))
button15.grid(row=4, column=4, padx=4, pady=4)

button16 = Button(root, text="4", width=6, command=lambda: assignText(button16))
button16.grid(row=5, column=0, padx=4, pady=4)

button17 = Button(root, text="5", width=6, command=lambda: assignText(button17))
button17.grid(row=5, column=1, padx=4, pady=4)

button18 = Button(root, text="6", width=6, command=lambda: assignText(button18))
button18.grid(row=5, column=2, padx=4, pady=4)

button19 = Button(root, text="*", width=6, command=lambda: assignText(button19))
button19.grid(row=5, column=3, padx=4, pady=4)

button20 = Button(root, text="1/x", width=6, command=lambda: assignText(button20))
button20.grid(row=5, column=4, padx=4, pady=4)

button21 = Button(root, text="1", width=6, command=lambda: assignText(button21))
button21.grid(row=6, column=0, padx=4, pady=4)

button22 = Button(root, text="2", width=6, command=lambda: assignText(button22))
button22.grid(row=6, column=1, padx=4, pady=4)

button23 = Button(root, text="3", width=6, command=lambda: assignText(button23))
button23.grid(row=6, column=2, padx=4, pady=4)

button24 = Button(root, text="-", width=6, command=lambda: assignText(button24, ))
button24.grid(row=6, column=3, padx=4, pady=4)

button25 = Button(root, text="=", width=6, command=lambda: assignText(button25))
button25.grid(row=6, column=4, rowspan=2, sticky=N + S + W + E, padx=4, pady=4)

button26 = Button(root, text="0", width=6, command=lambda: assignText(button26))
button26.grid(row=7, column=0, columnspan=2, sticky=N + S + W + E, padx=4, pady=4)

button27 = Button(root, text=".", width=6, command=lambda: assignText(button27))
button27.grid(row=7, column=2, padx=4, pady=4)

button28 = Button(root, text="+", width=6, command=lambda: assignText(button28))
button28.grid(row=7, column=3, padx=4, pady=4)

root.mainloop()
