





from tkinter import Tk, Frame, Button



class Example(Frame):
    def __init__(self,master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.f = Frame(self)
        self.f .pack()

        self.btn1 = Button(self.f, text='Change', bg='red', command= self.disable)
        self.btn1.pack()
        self.btn = Button(self.f, text='Disabled', bg='green')
        self.btn .pack()

    def disable(self):
        self.btn.config(state='disabled', disabledbackground='blue')



root = Tk()
root.geometry("300x300+300+300")
app = Example(root)
app.pack()

root.mainloop()