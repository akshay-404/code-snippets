from tkinter import *

root = Tk()
root.title('Calculator Project')
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

button1 = Button(root, text='1', width=12, height=3, command=lambda: click(1), font='bold')
button2 = Button(root, text='2', width=12, height=3, command=lambda: click(2), font='bold')
button3 = Button(root, text='3', width=12, height=3, command=lambda: click(3), font='bold')
button4 = Button(root, text='4', width=12, height=3, command=lambda: click(4), font='bold')
button5 = Button(root, text='5', width=12, height=3, command=lambda: click(5), font='bold')
button6 = Button(root, text='6', width=12, height=3, command=lambda: click(6), font='bold')
button7 = Button(root, text='7', width=12, height=3, command=lambda: click(7), font='bold')
button8 = Button(root, text='8', width=12, height=3, command=lambda: click(8), font='bold')
button9 = Button(root, text='9', width=12, height=3, command=lambda: click(9), font='bold')
button0 = Button(root, text='0', width=12, height=3, command=lambda: click(0), font='bold')

button_p = Button(root, text='+', width=12, height=3, command=add, font='bold')
button_m = Button(root, text='-', width=12, height=3, command=subtract, font='bold')
button_c = Button(root, text='Clear All', width=24, height=3, command=clear, font='bold')
button_e = Button(root, text='=', width=12, height=3, command=equal, font='bold')

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