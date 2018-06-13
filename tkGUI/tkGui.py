import tkinter as t
import mysql.connector
from tkinter import messagebox

conn = mysql.connector.connect(user='root', password='anchal', host='127.0.0.1')

myCursor = conn.cursor()

# myCursor.execute('CREATE DATABASE tkDB')
myCursor.execute('Use tkDB')

# myCursor.execute(
# 'CREATE TABLE tkTbl(id int primary key AUTO_INCREMENT, name varchar(30), contactNo varchar(30),email varchar(100))')


# Window created
# Form using tkinter


# Window created


wind1 = t.Tk()

# Change the title of Window

wind1.title('Form')
wind1.geometry("500x500")
wind1.configure(bg="white")
## wind1.wm_iconbitmap('1.ico')

# Add text

label1 = t.Label(wind1, text=" Name : ", fg="black", bg='white', font=("Comic Sans MS", 15))
label1.grid(row=0, column=0, padx=120, pady=50, sticky='E')

nameInput = t.Entry(wind1)
nameInput.grid(row=0, column=1, padx=120, pady=50)

label2 = t.Label(wind1, text="ContactNo : ", fg="black", bg='white', font=("Comic Sans MS", 15))
label2.grid(row=1, column=0, padx=120, pady=50, sticky='E')

contactNo = t.Entry(wind1)
contactNo.grid(row=1, column=1, padx=120, pady=50)

label3 = t.Label(wind1, text="Email : ", fg="black", bg='white', font=("Comic Sans MS", 15))
label3.grid(row=2, column=0, padx=120, pady=50, sticky='E')

emailInput = t.Entry(wind1)
emailInput.grid(row=2, column=1, padx=120, pady=50)


def insertDb(name, cN, email):
    myCursor.execute("Insert into tkTbl(name,contactNo,email) values('" + name + "','" + cN + "', '" + email + "')")
    print('Inserted Successfully into database!!')
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Inserted Successfully")


def buttonClick():
    # submitBtn["text"] = "Clicked"
    # label3.configure(text ="Hello")

    print("Button Clicked")
    name = nameInput.get()
    print(name)
    cN = contactNo.get()
    print(cN)
    email = emailInput.get()
    print(email)

    insertDb(name, cN, email)

    # Add Button


submitBtn = t.Button(wind1, text="Submit", bg='black', fg='white', command=buttonClick, font=("Comic Sans MS", 15))
submitBtn.grid(row=3, column=1, padx=80, pady=50)

# show window and begin main loop

wind1.mainloop()
