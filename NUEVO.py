

from tkinter import *

class A(Frame):  #--------------------------> FRAME CONTROLADOR PRINCIPAL
    def __init__(self, master=None, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.frame = Frame(self, bg='yellow')
        self.frame .pack(side=TOP, fill=BOTH)
         
        self.cnt = Frame(self.frame, bg='green2')
        self.cnt .pack(side=TOP, fill=BOTH)

        btn = Button(self.cnt, text='Hellow')
        btn.pack()

        self.bind_all('<Motion-1>', self.hellow)

    def hellow(self, event):
        print('I always run how I want')

root = Tk()
app = A (root)
app .pack(side=TOP, fill=BOTH)
root.mainloop()
