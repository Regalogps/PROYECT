















from tkinter import *

class A(Frame):  #--------------------------> FRAME CONTROLADOR PRINCIPAL
    def __init__(self, master=None, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.container_A = Frame(root, bg='green')
        self.container_A .pack(fill=BOTH)
        btn = Button(self.container_A, text='__1__')
        btn.pack()

        self.container_B = Frame(self.container_A, bg='green2')
        self.container_B .pack(fill=BOTH)
        btn = Button(self.container_B, text='__2__')
        btn.pack()

        self.bind_all("<B1-Motion>", self.a)

    def a (self, event):
        event

root = Tk()
app = A (root)
app .pack()
root.mainloop()