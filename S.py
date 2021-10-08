






from tkinter import *
from tkinter import ttk


def a (ev):
    _event = ev.widget
    if isinstance(_event, Button, Frame):
        print(55555)
        print('hellow')

root = Tk()
root.geometry('200x200')
frame = Frame (root)
frame .pack(side=BOTTOM,  fill=BOTH)

btn = Button(frame, text='heyyyy').pack()

grip = ttk.Sizegrip(frame, style='TSizegrip')
grip .place (relx=1.0, rely=1.0, anchor='center')
ttk.Style().configure('TSizegrip', bg='black')

root.bind("<B1-Motion>", a)
root .mainloop()


