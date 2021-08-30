from tkinter import Tk, Frame, Label


class Right(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind('<Motion>', self.mouse)
        self.lbl_77 = Label(self, text='Hellow', bg='green', fg='black')

    def mouse(self, event):
        x, y = event.x, event.y
        print(x,y)
        x1, x2 = 0, 50
        y1, y2 = 0, 50
        if x1 < x < x2 and y1 < y < y2:
            self.lbl_77.place(x=90, y=0)
        else:
            self.lbl_77.place_forget()


root = Tk()
root.geometry('500x500')
frame = Right(root)
frame.pack(fill='both', expand=True)
root.mainloop()

  