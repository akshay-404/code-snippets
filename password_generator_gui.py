from tkinter import *
import pyperclip as py
import random

root = Tk()
root.title('PASSWORD GENERATOR')
num = Label(root, text='Password Length', font=10, padx=10)
num.grid(row=0, column=0)
e = Entry(root, width=5, borderwidth=2, font=10, justify='center')
e.grid(row=0, column=1, padx=10, sticky=E)
e.insert(0, 8)

frame = LabelFrame(root, text='Password Characters', font=10, width=100, padx=40)
frame.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

one = BooleanVar()
two = BooleanVar()
three = BooleanVar()
four = BooleanVar()
checkOne = Checkbutton(frame, text='Upper Case', variable=one, onvalue=True, offvalue=False, font=10, anchor='w')
checkOne.grid(row=1, column=0)
checkTwo = Checkbutton(frame, text='Lower Case', variable=two, onvalue=True, offvalue=False, font=10, anchor='w')
checkTwo.grid(row=2, column=0)
checkThree = Checkbutton(frame, text='Numbers', variable=three, onvalue=True, offvalue=False, font=10, anchor='w')
checkThree.grid(row=3, column=0)
checkFour = Checkbutton(frame, text='Symbols', variable=four, onvalue=True, offvalue=False, font=10, anchor='w')
checkFour.grid(row=4, column=0)

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
sym = "!()-.?[]_`~;\\/:@#$%^&*+="

global password

def generate():
    seq = []
    global temp, label, copy
    try:
        temp.grid_remove()
        label.grid_remove()
        copy.grid_remove()
    except NameError:
        pass
    try:
        N = int(e.get())
        if N>32 or N<8:
            temp = Label(root, text='Password length should be between 8 and 32 !')
            temp.grid(row=6, column=0, columnspan=2, pady=5)
            return           
    except ValueError:
        temp = Label(root, text='Choose valid password length !')
        temp.grid(row=6, column=0, columnspan=2)
        return
    if one.get():
        seq.append(caps)
    if two.get():
        seq.append(low)
    if three.get():
        seq.append(num)
    if four.get():
        seq.append(sym)
    if seq == []:
        temp = Label(root, text='No characters chosen !')
        temp.grid(row=6, column=0, columnspan=2)
        return
    
    global password
    password = ''
    for i in range(N):
        password += ''.join(random.sample(seq[i%len(seq)], 1))
    password = list(password)
    for i in range(random.randint(0,N)):
        random.shuffle(password)
    password = ''.join(password)

    try:
        label.grid_remove()
        label = Label(root, text=password, font=10, relief='sunken', pady=5, width=20)
        label.grid(row=6, column=0, columnspan=2, pady=5, padx=5)
    except NameError:
        label = Label(root, text=password, font=10, relief='sunken', pady=5, width=20)
        label.grid(row=6, column=0, columnspan=2, pady=5, padx=5)

    copy = Button(root, text='Copy to Clipboard', command=lambda: py.copy(password), width=20, font=10)
    copy.grid(row=7, column=0, columnspan=2)
    
    global close
    close.grid_remove()
    close = Button(root, text='Exit', command=root.quit, width=20, font=10)
    close.grid(row=8, column=0, columnspan=2)

button = Button(root, text='Generate Password', width=20, font=10, command=generate)
button.grid(row=5, column=0, columnspan=2)

try:
    close = Button(root, text='Exit', command=root.quit, width=20, font=10)
    close.grid(row=7, column=0, columnspan=2)
except UnboundLocalError:
    pass

root.mainloop()