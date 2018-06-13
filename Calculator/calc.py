import tkinter as t
from tkinter import W
from tkinter import S
from tkinter import E

root = t.Tk()

root.title('Calculator')

display = t.Entry(root)

display.grid(row=1, column=6, sticky=W + E)

t.Button(root, text='MC').grid(row=2, column=1)
t.Button(root, text='MR').grid(row=2, column=2)
t.Button(root, text='MS').grid(row=2, column=3)
t.Button(root, text='M+').grid(row=2, column=4)
t.Button(root, text='M- ').grid(row=2, column=5)

t.Button(root, text=' AC').grid(row=3, column=1)
t.Button(root, text=' CE').grid(row=3, column=2)
t.Button(root, text='  pi ').grid(row=3, column=3)
t.Button(root, text='+/-').grid(row=3, column=4)
t.Button(root, text='  C  ').grid(row=3, column=5)

t.Button(root, text='  7  ').grid(row=4, column=1)
t.Button(root, text='  8  ').grid(row=4, column=2)
t.Button(root, text='  9  ').grid(row=4, column=3)
t.Button(root, text='  /  ').grid(row=4, column=4)
t.Button(root, text='  %  ').grid(row=4, column=5)

t.Button(root, text='  4  ').grid(row=5, column=1)
t.Button(root, text='  5  ').grid(row=5, column=2)
t.Button(root, text='  6  ').grid(row=5, column=3)
t.Button(root, text='  *  ').grid(row=5, column=4)
t.Button(root, text='  1/x').grid(row=5, column=5)

t.Button(root, text='  1  ').grid(row=6, column=1)
t.Button(root, text='  2  ').grid(row=6, column=2)
t.Button(root, text='  3  ').grid(row=6, column=3)
t.Button(root, text='  -  ').grid(row=6, column=4)
t.Button(root, text='   !   ').grid(row=6, column=5)

t.Button(root, text='exp').grid(row=7, column=1)
t.Button(root, text='  0  ').grid(row=7, column=2)
t.Button(root, text='  .  ').grid(row=7, column=3)
t.Button(root, text='  +  ').grid(row=7, column=4)
t.Button(root, text='  =  ').grid(row=7, column=5)

root.mainloop()
