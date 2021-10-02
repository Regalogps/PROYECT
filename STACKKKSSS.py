from tkinter import *

class Move():
    def __init__(self):
        self._x = 0
        self._y = 0

    def start_move2(self, event):        
        self._x = event.x
        self._y = event.y

    def stop_move2(self, event):
        self._x = None
        self._y = None

    def on_move2(self, event):
        deltax = event.x - self._x
        deltay = event.y - self._y
        win = event.widget.winfo_toplevel()
        new_position = "+{}+{}".format(win.winfo_x() + deltax, win.winfo_y() + deltay)

        win.geometry(new_position) 


class A (Frame, Move):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.btn = Button(self, text='opens', command=self.open)
        self.btn .pack()

        self.bind_all("<ButtonPress-1>", self.start_move2)
        self.bind_all("<B1-Motion>", self.on_move2)
        self.bind_all("<ButtonRelease-1>", self.stop_move2)

    def open(self):
        self.w1 = Toplevel(self.master)
        self.w2 = Toplevel(self.master)
        self.w1 .geometry('300x300')
        self.w2 .geometry('300x300')
        self.frm1 = Frame(self.w1, bg='green')
        self.frm2 = Frame(self.w2, bg='blue')
        self.lbl1 = Label(self.frm1, text='windows 1', bg='green2')
        self.lbl2 = Label(self.frm2,  text='windows 2', bg='gray')
        
        self.frm1 .pack()
        self.frm2 .pack()
        self.lbl1 .pack()
        self.lbl2 .pack()

root = Tk()
app = A(root, bg='black')
app .pack()
root .mainloop()