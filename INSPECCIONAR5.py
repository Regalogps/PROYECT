
from tkinter import *

parent = Tk()
parent.title("Parent Widget")
frame = Frame(parent)
frame.grid(row = 0, column = 0, sticky = NSEW)

def printy():
    print(4444)

def press(ev):
    if ev.widget.master == frame:
        print(ev)
        ev.widget["state"] = "disabled"

def release(ev):
    if ev.widget.master == frame:
        ev.widget["state"] = "normal"

for a in range(10):
    BUT = Button(frame, text = "Press and D", command= printy)
    BUT.grid(row = a, column = 0, sticky = NSEW)

frame.bind_all("<B1-Motion>", press)
frame.bind_all("<ButtonRelease-1>", release)

label = Frame(parent)
label.grid(row = 0, column = 1, sticky = NSEW)
for a in range(10):
    BUT = Button(label, text = "Press and Drag", command= printy)
    BUT.grid(row = a, column = 0, sticky = NSEW)

parent.mainloop()


""" from tkinter import *
import time

F = None

def on_press(x):
    global F
    F = time.time()

def on_release(x):
    print(444888)
    if F is None: 
        print('Noneeeeeeeee')
    if time.time() - F > 0.5: 
        print(4444)

    print(F)
    """


""" root = Tk()

frm = Frame(root, bg='gray')
frm.pack()
btn = Button(frm, text='Closed')
btn.pack()

btn.bind('<ButtonPress-1>', on_press)
btn.bind('<ButtonRelease-1>', on_release)

root.mainloop() """