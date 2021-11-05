from tkinter import *

class Interface(Tk):
    def __init__(self):
        super().__init__()

        self.control1 = Frame(self, bg='green')
        self.control1 .pack(fill= 'both', expand= True) 

        self.control2 = Frame(self,  bg='red')
        self.control2 .pack(fill= 'both', expand= True)
    
        self.bind('<Enter>',self.open)
        self.bind('<Leave>',self.closed)

    def open(self, event):
        self.control1 .pack(fill= 'both', expand= True)
        print('Posicionado widget: FRAME 1')
    def closed(self, event):        
        self.control1 .pack_forget()
        print('Ocultando widget: FRAME 1')
 
root = Interface()
root .geometry('200x200+200+0')
root .config(bg='blue')

root .mainloop()