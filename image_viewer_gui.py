from tkinter import *
from PIL import ImageTk, Image
import os

fileType = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
root = Tk()
root.title('Image Viewer')
root.iconbitmap(os.path.dirname(__file__) + r'\imgicon.ico')
e = Entry(root, width=40, font='bold', borderwidth=5, justify='center')
e.grid(row=0, column=0, columnspan=2)

height = root.winfo_height()
width = root.winfo_width()

def image_resize(img_path):
    img = Image.open(img_path)
    h_f = height / float(img.height)
    w_f = width / float(img.width)
    scaleFactor = 3*min(h_f, w_f)
    img = img.resize((int(img.width*scaleFactor), int(img.height*scaleFactor)))
    return ImageTk.PhotoImage(img)

def getList():
    global imgList, myEnter, myExit, inValid, directory
    try:
        inValid.grid_remove()
    except NameError:
        pass
    directory = e.get()
    directory = directory.replace("\"", "")
    imgList = []
    imgList = [os.path.join(fileRoot, file) for fileRoot, _, files in os.walk(directory)
            for file in files if any(file.endswith(t) for t in fileType)]
    if imgList == []:
        inValid = Label(root, text='Invalid or Empty Directory !', fg='red', font='bold')
        inValid.grid(row=4, column=0, columnspan=3)
        return None
    myEnter.grid_remove()
    myExit.grid_remove()
    e.grid_remove()

    global next, p_exit, prev, myImg, index, pic, status
    index = 0
    pic = image_resize(imgList[index])
    myImg = Label(image=pic)
    myImg.grid(row=0, column=0, columnspan=3)

    prev = Button(root, text='<<<', font='bold', borderwidth=5, command=funcPrev)
    prev.grid(row=1, column=0)
    p_exit = Button(root, text='EXIT PROGRAM', padx=25, font='bold', command=root.quit, borderwidth=5)
    p_exit.grid(row=1, column=1)
    next = Button(root, text='>>>', font='bold', borderwidth=5, command=funcNext)
    next.grid(row=1, column=2)
    status = Label(root, text=f'{os.path.basename(imgList[index])}\t\t\t\t\t\t\t\tImage {index+1} of {len(imgList)}', bd=2, relief=SUNKEN, anchor='center')
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def funcNext():
    global imgList, myImg, index, pic, status
    myImg.grid_remove()
    if index == len(imgList)-1:
        index = 0
    else:
        index += 1
    pic = image_resize(imgList[index])
    myImg = Label(image=pic)
    myImg.grid(row=0, column=0, columnspan=3)
    status = Label(root, text=f'{os.path.basename(imgList[index])}\t\t\t\t\t\t\t\tImage {index+1} of {len(imgList)}', bd=2, relief=SUNKEN, anchor='center')
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def funcPrev():
    global imgList, myImg, index, pic, status
    myImg.grid_remove()
    if index == 0:
        index = len(imgList)-1
    else:
        index -= 1
    pic = image_resize(imgList[index])
    myImg = Label(image=pic)
    myImg.grid(row=0, column=0, columnspan=3)
    status = Label(root, text=f'{os.path.basename(imgList[index])}\t\t\t\t\t\t\t\tImage {index+1} of {len(imgList)}', bd=2, relief=SUNKEN, anchor='center')
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

myEnter = Button(root, text='ENTER', width=15, font='bold', command=getList)
myExit = Button(root, text='EXIT', width=15, font='bold', command=root.quit)
myEnter.grid(row=1, column=1)
myExit.grid(row=1, column=0)

root.mainloop()