from tkinter import Tk, StringVar, ttk

def getValue():
    var = value.get()
    print("You selected : ", var)



root = Tk()
root.geometry('500x500')
value = StringVar()

box = ttk.Combobox(root, textvariable=value, state='readonly')
box['values'] = ('Perl', 'Python', 'Java', 'C++')
box.current(0)
getValue()
box.grid(column=0, row=0)
root.mainloop()


