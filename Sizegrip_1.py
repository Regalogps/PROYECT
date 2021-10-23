from tkinter import *
from tkinter import ttk

class App(Frame):
    def __init__(self, parent):
        mframe = Frame.__init__(self, parent)
        self.pack(fill = 'both', expand = True)
        ttk.Sizegrip(mframe).pack(side = 'right')

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        Text(self, width = 20, height = 2).grid(row = 0, column = 0, sticky = 'nsew')

root = Tk()
root .overrideredirect(1)
App(root)

root.mainloop()
