from tkinter import Tk, Frame, Label, Spinbox, Listbox, StringVar
from tkinter import SINGLE, ANCHOR, END, S,N,E,W

class App(Frame):
    def __init__(self, parents, *args, **kwargs):
        Frame.__init__(self, parents, *args, kwargs)          
        frame_3 = B3_class (self)
        frame_3 .pack()
        #.........
#-------------------------
class B3_class(Frame):
    def __init__(self, parents, *args, **kwargs):
        Frame.__init__(self, parents, *args, kwargs)  
        #_____C O N T A I N E R:
        self.frm_B3 = Frame (self, bg='#31343a', width=172, height=65)
        self.frm_C1 = Frame (self, bg='#11161d', width=60, height=65)

        self.label_filas = Label (self.frm_B3, width=18, bg='#11161d', fg='#969696', bd=2, anchor= E)
        label_title = Label (self.frm_B3, text='Seleccione  Mobil :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        # self.label_miniature = Label (self.frm_C1, image=self.master.Miniatures[0], bd= 0)
        # This label is a container for the images that are changing ...
        self.listbox = Listbox_class (self.label_filas, width=11, height=1)
        self.spinbox = Spinbox_class (self.frm_B3, width=13, bd=0)

        #_____Position:
        self.frm_B3 .grid (column=0, row=0, padx=0, pady=0)
        self.frm_C1 .grid (column=1, row=0, padx=0, pady=0)

        self.label_filas .grid (column=0, row=0, padx=(0,5), pady=(0,2), sticky=N)
        label_title .grid (column=0, row=1, padx=10, pady=(0,0), sticky=W)

        self.listbox .grid ( padx=(19,0), pady=(0,5), sticky=N)
        self.spinbox .grid (column=0, row=2, padx=11, pady=(3,3), sticky=W)

        #__________Propagación:
        self.frm_B3 .grid_propagate(False)
        self.frm_C1 .grid_propagate(False)
        self.label_filas .grid_propagate(False)
        self.listbox .grid_propagate(False)

    def change_miniature(self):
        pass # This function is responsible for changing the images of self.label_miniature,
             # for reasons of verification the code was removed

#------------------------------------------
class Spinbox_class(Spinbox, B3_class):
    def __init__(self, master, **args):
        Spinbox.__init__(self, master, **args)
        self.spinbox_variable = StringVar()
        self.spinbox_values = ['Banana','Apple','Grapes','Lemon','Cherry'] ##################
        self.config (values=self.spinbox_values,
                     textvariable=self.spinbox_variable,
                     justify='center',
                     wrap=True,
                     bd=0)

        self.bind ('<Double-Button-1>', lambda *arg: self.delete(0, END))
        self.bind ('<Return>', self.bind_listbox)

        self.spinbox_variable .trace_add ('write', self.change_variable)  
        self.spinbox_variable .trace_add ('write', lambda *arg: self.spinbox_variable.set (self.spinbox_variable.get() .capitalize()))
       

    def bind_listbox(self, event):
        spinbox = self.get()
        listbox = self.master.master.listbox.get(0)
        if listbox != spinbox and listbox != '':
            self.delete(0, END)
            self.insert(0, listbox)
 
    def change_variable(self, *args):
        spinbox = self.get().capitalize()
        if spinbox == '':
            self.master.master.listbox .delete(0, END)
        else:
            list_new = []
            for i in self.spinbox_values:
                if spinbox in i:
                    list_new .append(i)
            if list_new != []:
                self.update(list_new)
            if spinbox == 'As':
                self.master.master.listbox .delete(0, 1) 
        self.master.master.change_miniature()

    def update(self, list, *args):
        self.master.master.listbox .delete(0, END)
        for i in list:
            self.master.master.listbox .insert(END, i)
        if self.master.master.listbox .get(0) == self.spinbox_variable.get():
            self.master.master.listbox .delete(0, END)

#------------------------------------------ 
class Listbox_class(Listbox, B3_class):
    def __init__(self, master, **kwargs):  #
        Listbox.__init__(self, master, **kwargs)
        self.config (font=('Calibri',9,'bold'),
                     bg='#11161d', fg='#00ff00', 
                     highlightthickness=0, bd=0,
                     activestyle='none',
                     justify='center',
                     selectmode=SINGLE,
                     takefocus=0)

        self.bind ('<<ListboxSelect>>', self.listbox_select)

    def listbox_select(self, event):       
        selection = self.get(ANCHOR)
        if self.get(0,END) != ():
            self.master.master.master.spinbox .delete(0, END)
        self.master.master.master.spinbox.insert(0, selection)
        self.selection_clear(0,END)
        
        self.after(100, lambda: self.master.master.master.spinbox.focus_set())


root = Tk()
root.geometry('250x130+200+200')   
app =   App (root)
app . pack()
root.mainloop()
