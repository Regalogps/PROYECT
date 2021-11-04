
from tkinter import *

class Interface(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self._motion_1 = False
        self.x1 = 0
        self.x2 = 100
        self.y1 = 0
        self.y2 = 100

        self.control = Frame(self, bg='green')
        self.control .pack(fill= 'both', expand= True)  

        self.lbl_change1 = Label(self.control, text='text 1', bg='black', fg='white', bd=0)
        self.lbl_change1   .pack(side=LEFT, fill='both', expand=True, padx=10)
        self.lbl_change2 = Label(self.control, text='text 2', bg='black', fg='white', bd=0)
        self.lbl_change2   .pack(side=LEFT, fill='both', expand=True, padx=10)
    
        #_______________
        self.master.bind('<Motion>',self.open_frame)
        self.master.bind('<Leave>', lambda arg: self.control .pack_forget())


    def open_frame(self, event):
        self.pointer_width_2  = event.x / self.master.winfo_width() * 100
        self.pointer_height_2 = event.y / self.master.winfo_height() * 100

        if not self._motion_1 == True:
            if self.x1 <(self.pointer_width_2)< self.x2  and  self.y1 <(self.pointer_height_2)< self.y2: 
                self.control .pack(fill= 'both', expand= True)
                print(111)
            else:
                print(222)
                self.control .pack_forget()
 
root = Tk()
root .geometry('200x600+300+0')
root .config(bg='gray22')
frame = Interface(root)
frame .pack()
root .mainloop()