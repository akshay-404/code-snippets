from tkinter import *
from datetime import datetime
import os, math

root = Tk()
root.title('Analog Clock')
root.resizable(width=False, height=False)
# --- Change icon path if needed ---
root.iconbitmap(r'Git\code-snippets\additional-files\clockico.ico')

length, radius = 200, 180
frm = Frame(root)
frm.pack(padx=20)
Label(frm, text='ANALOG CLOCK', font=('', 26, 'bold')).pack()

can = Canvas(frm, height=2*length, width=2*length, highlightthickness=2, highlightbackground='black')

x0, y0, x1, y1 = length-radius, length-radius, length+radius, length+radius
can.create_oval(x0, y0, x1, y1, width=4)

for t in range(12):
    x = math.cos(math.radians(t * 30))*(radius-22) + 200
    y = math.sin(math.radians(t * 30))*(radius-22) + 200
    can.create_text(x, y, text=f'{t-9 if t>9 else t+3}', font=('',25, 'bold'))

h_len = radius * 0.5
m_len = radius * 0.7
s_len = radius * 0.78

h_hand = can.create_line(length, length, length, length-h_len, width=6, arrow='last', fill='red')
m_hand = can.create_line(length, length, length+m_len, length, width=4, arrow='last', fill='black')
s_hand = can.create_line(length, length, length, length+s_len, width=2, arrow='last', fill='blue')

can.bind('<Button-1>', quit)
can.pack()

time_now = StringVar(root)
time = Label(textvariable=time_now, font=('Consolas', 15, 'bold'))
time.pack(pady=(10, 10))

def update_clock():
    time = datetime.now()
    hh, mm, ss = int(datetime.strftime(time, '%I')), time.minute, time.second

    s_r = math.radians(ss*6 - 90)
    m_r = math.radians(mm*6 - 90)
    h_r = math.radians(hh*30 + mm/2 - 90)

    h_x, h_y = math.cos(h_r)*h_len + 200, math.sin(h_r)*h_len + 200
    m_x, m_y = math.cos(m_r)*m_len + 200, math.sin(m_r)*m_len + 200
    s_x, s_y = math.cos(s_r)*s_len + 200, math.sin(s_r)*s_len + 200

    can.coords(h_hand, length, length, h_x, h_y)
    can.coords(m_hand, length, length, m_x, m_y)
    can.coords(s_hand, length, length, s_x, s_y)
    time_now.set(datetime.strftime(datetime.now(), '%A, %d %b %Y -- %I:%M:%S %p'))

    root.after(1000, update_clock)

update_clock()

root.mainloop()
