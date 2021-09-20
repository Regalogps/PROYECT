from tkinter import *

class Frame_class(Frame):
    def __init__(self, parents, *args, **kwargs):
        Frame.__init__(self, parents, *args, kwargs)
        self.listbox = Listbox_class (self, width=11, height=1)
        self.listbox .pack() 

        self.spinbox = Spinbox_class (self, width=11)
        self.spinbox .pack()
        
        # from here I want to get the value of 
        # the first item of listbox or delete it     

    def delete(self, number):
        if number == 1:
            self.listbox.delete(0, END)
        if number == 2:
            self.listbox.delete(0, 1)


class Listbox_class(Listbox, Frame_class):

    def __init__(self, master, **kwargs):
        Listbox.__init__(self, master, **kwargs)       
        self.config (font=('Calibri',9,'bold'))
        self.insert(0, 'banana1')
        self.insert(0, 'orange1')



class Spinbox_class(Spinbox, Frame_class):

    def __init__(self, master, **kwargs):
        Spinbox.__init__(self, master, **kwargs)
        self.var = StringVar() 
        self.val = [1,2,3,4,5,6,7,8,9]      
        self.config (font=('Calibri',9,'bold'), textvariable= self.var, values= self.val)
        self.var.trace_add ('write', self.change)
        
      
    def change(self, *args):
        spinbox = self.get()

        if spinbox == '':                                                          
            self.master.delete(1)  
        else:  
            pass

root = Tk()
root.geometry('250x130+100+100')   
app =  Frame_class (root)
app . pack()
root.mainloop()   