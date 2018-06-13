from tkinter import *
import mysql.connector
from tkinter import messagebox

conn = mysql.connector.connect(user='root', password='anchal', host='127.0.0.1')

myCursor = conn.cursor()

# myCursor.execute('CREATE DATABASE loginApp')
myCursor.execute('Use loginApp')
# myCursor.execute(
# "CREATE TABLE loginTbl(id int primary key AUTO_INCREMENT, name varchar(30),email varchar(100),password varchar(50),branch varchar(50),gender varchar(20),course varchar(20))"
# )


# global variables

global gen
global crs
global v, v1, v2
gen = ''
crs = ''


# Main layout

def mainWindow():

    global v, v1, v2
    root = Tk()
    root.title("New Account")
    root.geometry("500x500")
    root.resizable(0, 0)
    root.configure(bg="White")

    # Widgets

    lab1 = Label(root, text="Name :  ", fg="black", bg='white', font=("Comic Sans MS Bold", 12))
    lab1.grid(row=1, column=0, padx=10, pady=15, sticky=W)

    nameField = Entry(root, bg="white", fg="black")
    nameField.grid(row=1, column=1, padx=10, pady=15)

    lab2 = Label(root, text="Email :  ", fg="black", bg='white', font=("Comic Sans MS Bold", 12))
    lab2.grid(row=2, column=0, padx=10, pady=15, sticky=W)

    emailField = Entry(root, bg="white", fg="black")
    emailField.grid(row=2, column=1, padx=10, pady=15)

    lab3 = Label(root, text="Password :  ", fg="black", bg='white', font=("Comic Sans MS Bold", 12))
    lab3.grid(row=3, column=0, padx=10, pady=15, sticky=W)

    passField = Entry(root, bg="white", fg="black")
    passField.grid(row=3, column=1, padx=10, pady=15)

    lab4 = Label(root, text="Branch :  ", fg="black", bg='white', font=("Comic Sans MS Bold", 12))
    lab4.grid(row=4, column=0, padx=10, pady=15, sticky=W)

    branchField = Entry(root, bg="white", fg="black")
    branchField.grid(row=4, column=1, padx=10, pady=15)

    lab5 = Label(root, text="Gender :  ", fg="black", bg='white', font=("Comic Sans MS Bold", 12))
    lab5.grid(row=5, column=0, padx=10, pady=15, sticky=W)

    v = IntVar()

    maleButton = Radiobutton(root, bg="white", fg="black", width=6, text="Male", variable=v, value=1,
                             command=lambda: getValue())
    maleButton.grid(row=5, column=1, padx=10, pady=15, sticky=W)

    femaleButton = Radiobutton(root, bg="white", fg="black", width=6, text="Female", variable=v, value=2,
                               command=lambda: getValue())
    femaleButton.grid(row=6, column=1, padx=10, pady=15, sticky=W)

    lab6 = Label(root, text="Courses:  ", fg="black", bg='white', font=("Comic Sans MS Bold", 12))
    lab6.grid(row=7, column=0, padx=10, pady=15, sticky=W)

    v1 = IntVar()
    v2 = IntVar()

    javaButton = Radiobutton(root, bg="white", fg="black", text="Java", variable=v1, width=6,
                             )
    javaButton.grid(row=7, column=1, padx=10, pady=15, sticky=W)

    pythonButton = Radiobutton(root, bg="white", fg="black", text="Python", variable=v2, width=6,
                               )
    pythonButton.grid(row=8, column=1, padx=10, pady=15, sticky=W)

    btn1 = Button(root, text="Submit", width=10, fg="white", bg='Blue', command=lambda: submitData())
    btn1.grid(row=9, column=1, padx=10, pady=20, sticky=W)


    # get Value function

    def getValue():
        global v
        print("Inside getValue function")
        global gen
        val = v.get()
        if val == 1:
            gen = 'Male'
            print('You selected Male')
        elif val == 2:
            gen = 'Female'
            print('You selected Female')

    # seValue function

    global crs
    if v1.get():
        crs = 'Java'
    elif v2.get():
        crs = 'python'

    # submit data into database

    def submitData():
        print("Submit Data into Database... ")

        name = nameField.get()
        email = emailField.get()
        password = passField.get()
        branch = branchField.get()

        myCursor.execute(
            "Insert into loginTbl(name,email,password,branch,gender,course) values('" + name + "','" + email + "', '" + password + "', '" + branch + "','" + gen + "', '" + crs + "')")
        print('Inserted Successfully into database!!')
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Inserted Successfully")
        resetField()

    # Reset Field
    def resetField():
        global v, v1, v2
        nameField.delete('0', 'end')
        emailField.delete('0', 'end')
        passField.delete('0', 'end')
        branchField.delete('0', 'end')
        v = 0
        v1 = 0
        v2 = 0

    root.mainloop()


if __name__ == "__main__":
    mainWindow()
