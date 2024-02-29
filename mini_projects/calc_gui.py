from tkinter import *

root = Tk()

root.title('Calculator')
e = Entry(root, width=20, borderwidth=5, font=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
n1 = None
op = None

def click(num):
    global op
    if op == 0:
        e.delete(0, END)
        op = None
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def add():
    global n1
    global op
    op = '+'
    n1 = int(e.get())
    e.delete(0, END)

def subtract():
    global n1
    global op
    op = '-'
    n1 = int(e.get())
    e.delete(0, END)

def multiply():
    global n1
    global op
    op = '*'
    n1 = int(e.get())
    e.delete(0, END)

def divide():
    global n1
    global op
    op = '/'
    n1 = int(e.get())
    e.delete(0, END)

def equal():
    global n1
    global op
    n2 = int(e.get())
    if op == '+':
        e.delete(0, END)
        e.insert(0, n1 + n2)
    if op == '-':
        e.delete(0, END)
        e.insert(0, n1 - n2)
    if op == '*':
        e.delete(0, END)
        e.insert(0, n1 * n2)
    if op == '/':
        e.delete(0, END)
        e.insert(0, n1 / n2)
    n1 = None
    op = 0
    
def clear():
    e.delete(0, END)    

button1 = Button(root, text='1', width=12, height=3, command=lambda: click(1))
button2 = Button(root, text='2', width=12, height=3, command=lambda: click(2))
button3 = Button(root, text='3', width=12, height=3, command=lambda: click(3))
button4 = Button(root, text='4', width=12, height=3, command=lambda: click(4))
button5 = Button(root, text='5', width=12, height=3, command=lambda: click(5))
button6 = Button(root, text='6', width=12, height=3, command=lambda: click(6))
button7 = Button(root, text='7', width=12, height=3, command=lambda: click(7))
button8 = Button(root, text='8', width=12, height=3, command=lambda: click(8))
button9 = Button(root, text='9', width=12, height=3, command=lambda: click(9))
button0 = Button(root, text='0', width=12, height=3, command=lambda: click(0))

button_p = Button(root, text='+', width=12, height=3, command=add)
button_m = Button(root, text='-', width=12, height=3, command=subtract)
button_c = Button(root, text='Clear All',width=36, height=3, command=clear)
button_e = Button(root, text='=', width=12, height=3, command=equal)
button_x = Button(root, text='x', width=12, height=3, command=multiply)
button_d = Button(root, text='/', width=12, height=3, command=divide)

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
button_x.grid(row=5, column=0)
button_d.grid(row=5, column=1)
button_e.grid(row=5, column=2)
button_c.grid(row=6, column=0, columnspan=3)

root.mainloop()