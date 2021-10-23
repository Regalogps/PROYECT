from tkinter import *

class A (Frame):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.image_close = PhotoImage(file= '11.png')
        self._open_1 = False
        self._open_2 = False
        self.btn = Button(self, text='create winoows', command= self.create)
        self.btn.pack()

    def create(self):
        if not self._open_1:
            self.w1 = Toplevel(self.master)
            self.w1 .geometry('200x200')
            self.w1.title('window 1')
            self.w1.bind('<Destroy>', lambda event: self.close_windows(1, event))
            f = Frame(self.w1)
            f.pack()
            a = Label(self.w1, image=self.image_close)
            a.pack()
        
        if not self._open_2:
            self.w2 = Toplevel(self.master)
            self.w2.title('window 2')
            self.w2 .geometry('200x200')
            self.w2.bind('<Destroy>', lambda event: self.close_windows(2, event))
            f = Frame(self.w2)
            f.pack()

        self._open_1 = True
        self._open_2 = True

    def close_windows(self, number, event=None):
        print(111)
        if number == 1:
            self._open_1 = False
            event.widget.destroy()
            print("DEBUG: Close 1", event)

        if number == 2: 
           self._open_2 = False
           #event.widget.destroy()
           print("DEBUG: Close 2", event)


root = Tk()
a = A(root)
a.pack()
root.mainloop()