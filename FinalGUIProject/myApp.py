import tkinter as t

from tkinter import E
from tkinter import S
from tkinter import W
from tkinter import N

from tkinter.filedialog import *
from tkinter import messagebox

global filename
filename ='untitled-Notepad'


# functions

# message Box
def dialogBox1():
    print('Printing message.....')
    ans = t.messagebox.askquestion("Message Box", 'File is not saved want to save??')
    if ans == 'yes':
        print('Yes')
        saveAsFile()
    else:
        print('Do Nothing...')





# kill func
def kill():
    root.destroy()


# about function
def about():
    print('Implement Notepad using python......')
    name = '/home/anchal/SummerInternship/FinalGUIProject/about'
    f = open(name, 'r')
    print(f)
    if f:
        text = f.read()
        f.close()
        textBar.insert('1.0', text)
    else:
        print('Unable to open file')


# open file
def openFile():
    print("Opening File ......")
    dialogBox1()
    filename = askopenfilename(parent=root)
    print("Name : ", filename)
    f = open(filename, 'r')
    print(f)
    if f:
        root.title(filename)
        textBar.delete('1.0', 'end')
        text = f.read()
        f.close()
        textBar.insert('1.0', text)
    else:
        print('Unable to open file')


# Clear func
def clear():
    textBar.delete(1.0, END)


# Undo fun
def undo():
    print('Undo function ...')
    textBar.config(undo=True, autoseparators=True, maxundo=-1)
    textBar.edit_undo()


# cut fun
def cut():
    print('Cut function ...')

    try:
        textBar.event_generate("<<Cut>>")
    except:
        print('Error')


# copy fun
def copy():
    print('Copy Function ...')
    textBar.clipboard_clear()
    textBar.clipboard_append(textBar.selection_get())


# Paste fun
def paste():
    print('Print function ...')

    try:
        text = textBar.selection_get(selection='CLIPBOARD')
        textBar.insert(INSERT, text)
    except:
        print('Error')


# NewFile fun
def newFile():
    dialogBox1()
    print("Creating new file ....")
    root.title("Untitled - Notepad")
    textBar.delete('1.0', END)


# Save File
def saveFile():
    print('Save File ...')
    root.title(filename)
    a = open(filename, 'w')
    b = textBar.get("1.0", "end")
    a.write(b)
    a.close()


# SaveAs File
def saveAsFile():
    print('Save As file ....')
    filename = asksaveasfilename(initialdir='/home/anchal/SummerInternship/FinalGUIProject/UserFiles',
                                 initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if filename:
        root.title(filename)
        a = open(filename, 'w')
        b = textBar.get("1.0", "end")
        a.write(b)
        a.close()


# main window
root = t.Tk()
root.title('Untitled-Notepad')
root.configure(bg="white")
root.geometry("800x700")
img = t.Image("photo", file="index.ico")
root.tk.call('wm', 'iconphoto', root._w, img)
root.resizable(0, 0)

# Adding text bar
textBar = t.Text(root, width=800, height=700, font=("Comic Sans MS Bold", 11))
textBar.grid(row=1, column=0, sticky=N + S + E + W)

# adding label
lab1 = t.Label(root, text="hello", fg='black', bg='white', font=("Comic Sans MS Bold", 11))
lab1.grid(row=0, column=0, sticky=N + S + E + W)

# Adding menu in window
menuBar = t.Menu(root)

# Creating File Menu
fileMenu = t.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=newFile, accelerator="Ctrl+N")
fileMenu.add_command(label="Open", command=openFile, accelerator="Ctrl+O")
fileMenu.add_command(label="Save", command=saveFile, accelerator="Ctrl+S")
fileMenu.add_command(label="SaveAs", command=saveAsFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=kill)

# Creating Edit Menu
editMenu = t.Menu(menuBar, tearoff=0)
editMenu.add_command(label="Undo", command=undo, accelerator="Ctrl+Z")
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy, accelerator="Ctrl+C")
editMenu.add_command(label="Paste", command=paste, accelerator="Ctrl+P")
editMenu.add_command(label="Delete", command=clear)

# Creating help menu
helpMenu = t.Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About', command=about)

# adding subMenus to main menu bar
menuBar.add_cascade(label='File', menu=fileMenu)
menuBar.add_cascade(label='Edit', menu=editMenu)
menuBar.add_cascade(label="Help", menu=helpMenu)

root.configure(menu=menuBar)
root.mainloop()
