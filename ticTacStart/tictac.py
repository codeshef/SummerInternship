import tkinter as t

from tkinter import E
from tkinter import N
from tkinter import S
from tkinter import W

from tkinter import messagebox

import ctypes

# from gtts import gTTS


root = t.Tk()
root.title("Tic Tac Toe")

global bClick
bClick = True


def close():
    exit()


def reset():
    button1["text"] = ""
    button2["text"] = ""
    button3["text"] = ""
    button4["text"] = ""
    button5["text"] = ""
    button6["text"] = ""
    button7["text"] = ""
    button8["text"] = ""
    button9["text"] = ""


def gameStart(buttons):
    print("Game Started!!")

    global bClick

    if bClick == True and buttons["text"] == "":
        print("User1")
        buttons["text"] = "X"
        checkConditions()
        bClick = False
    elif bClick == False and buttons["text"] == "":
        print("User2")
        buttons["text"] = "O"
        checkConditions()
        bClick = True


def user1Wins():
    messagebox.showinfo("Result", "User1 Wins!!")
    reset()


def user2Wins():
    messagebox.showinfo("Result", "User2 Wins!!")
    reset()


def drawMatch():
    messagebox.showinfo("Result", "Match Draw!!")
    reset()


def checkConditions():
    print("Checking Conditons")

    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        print("User1 Wins")
        user1Wins()
    elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        print("User1 Wins")
        user1Wins()
    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        print("User1 Wins")
        user1Wins()
    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        print("User1 Wins")
        user1Wins()
    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        print("User1 Wins")
        user1Wins()
    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        print("User 1 Wins")
        user1Wins()
    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        print("User1 Wins")
        user1Wins()
    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        print("User1 Wins")
        user1Wins()
    if button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        print("User2 Wins")
        user2Wins()
    elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        print("User2 Wins")
        user2Wins()
    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        print("User2 Wins")
        user2Wins()
    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        print("User2 Wins")
        user2Wins()
    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        print("User2 Wins")
        user2Wins()
    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        print("User 2 Wins")
        user2Wins()
    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        print("User2 Wins")
        user2Wins()
    elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        print("User2 Wins")
        user2Wins()
    elif button1["text"]!="" and button2["text"]!="" and button3["text"]!="" and button4["text"]!="" and button5["text"]!="" and button6["text"]!="" and button7["text"]!="" and button8["text"]!="" and button9["text"]!="":
        print("Match Draw")
        drawMatch()


button1 = t.Button(root, text="", font='Arial 30 bold', height=1, width=2, command=lambda: gameStart(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)
button2 = t.Button(root, text="", font='Arial 30 bold', height=1, width=2, command=lambda: gameStart(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)
button3 = t.Button(root, text="", font='Arial 30 bold', height=1, width=2, command=lambda: gameStart(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)
button4 = t.Button(root, text="", font='Arial 30 bold', height=1, width=2, command=lambda: gameStart(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)
button5 = t.Button(root, text="", font='Arial 30 bold', height=1, width=2, command=lambda: gameStart(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)
button6 = t.Button(root, text="", font='Arial 30 bold', height=1, width=2, command=lambda: gameStart(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)
button7 = t.Button(root, text="", font='Arial 30 bold', height=1, width=2, command=lambda: gameStart(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)
button8 = t.Button(root, text="", font='Arial 30 bold', height=1, width=2, command=lambda: gameStart(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)
button9 = t.Button(root, text="", font='Arial 30 bold', height=1, width=2, command=lambda: gameStart(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)

button10 = t.Button(root, text="Reset Game ", font='Arial 9 bold', height=1, width=6, command=reset)
button10.grid(row=4, column=0, columnspan=3, sticky=S + N + E + W)
button11 = t.Button(root, text="Exit Game ", font='Arial 9 bold', height=1, width=6, command=close)
button11.grid(row=5, column=0, columnspan=3, sticky=S + N + E + W)

root.resizable(0, 0)  # Dsabling WIndow REsize

checkConditions()

root.mainloop()
