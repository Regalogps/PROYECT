



from tkinter import *

class A (Frame):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self._open_1 = False
        self._open_2 = False
        self.btn = Button(self, text='create winoows', command= self.create)
        self.btn .pack()

    def create(self):
        if self._open_1 is False:
            self.w1 = Toplevel(self.master)
            self.w1 .title('window 1')
            self.w1 .bind('<Destroy>',lambda f: self.close_windows(1))
        
        if self._open_2 is False:
            self.w2 = Toplevel(self.master)
            self.w2 .title('window 2')
            self.w2 .bind('<Destroy>',lambda f: self.close_windows(2))

        self._open_1 = True
        self._open_2 = True

    def close_windows(self,  number, event=None):
        if number is 1:
            event.widget.destroy()
            self._open_1 = False

        if number is 2: pass #......


root = Tk()
a = A(root)
a .pack()
root .mainloop()