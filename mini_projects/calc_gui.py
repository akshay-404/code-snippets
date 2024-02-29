from tkinter import *

root = Tk()

root.title('Calculator')
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
n1 = None
n2 = None
def click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def add():
    global n1
    n1 = int(e.get())
    e.delete(0, END)

def subtract():
    global n2
    n2 = int(e.get())
    e.delete(0, END)

def equal():
    global n1
    global n2
    n = int(e.get())
    if n1 != None:
        e.delete(0, END)
        e.insert(0, n1 + n)
    if n2 != None:
        e.delete(0, END)
        e.insert(0, n2 - n)
    n1 = None
    n2 = None

def clear():
    e.delete(0, END)    

button1 = Button(root, text='1', padx=40, pady=20, command=lambda: click(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: click(2))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: click(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: click(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: click(5))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: click(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: click(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: click(8))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: click(9))
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: click(0))

button_p = Button(root, text='+', padx=40, pady=20, command=add)
button_m = Button(root, text='-', padx=40, pady=20, command=subtract)
button_c = Button(root, text='Clear All', padx = 70, pady=20, command=clear)
button_e = Button(root, text='=', padx=40, pady=20, command=equal)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
button_p.grid(row=4, column=1)
button_m.grid(row=4, column=2)
button_c.grid(row=5, column=0, columnspan=2)
button_e.grid(row=5, column=2)

root.mainloop()