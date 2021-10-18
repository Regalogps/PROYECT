from tkinter import *

class TypeButton(Button):
    def __init__(self, parent, *args, **kwargs):
        kwargs = {'font':('Calibri',9,'bold'), 'bg': '#11161d', 'fg':'white',
                  'width':10, 'bd':0, 'activebackground':'#bdfe04', **kwargs}
        super().__init__(parent, *args, **kwargs)

class Example(Frame):
    def __init__(self,parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.frame = Frame(self, bg='#11161d')
        self.frame .grid(padx=(10,10), pady=(6,6))
        self.container1 = None

        self.creator_buttons()
        #????????????????
        #self.bind_all("<B1-Motion>", self.callback)

    def creator_buttons(self):  

        mobiles = [['Persona1', 'Persona2', 'Persona3', 'Persona4', 'Persona5', 'Persona6', 'Persona7', 'Persona8', 'Persona9', 'Persona10', 'Persona11'],
                   ['Persona12', 'Persona13', 'Persona14', 'Persona15', 'Persona16', 'Persona17', 'Persona18', 'Persona19', 'Persona20', 'Persona21', 'Persona22']]                
        self.mobiles2 = ['Persona2','Persona9','Persona13','Persona21','Persona22'] 

        self.buttons22 = []
        for index1, mobil in enumerate(mobiles):
            for index2, texto in enumerate(mobil):
                number = 11 if index1 == 1 else 0

                btn = TypeButton (self.frame, text=texto, command= self.callback)            
                n1 = 5 if index2 == 0 else 0        
                n2 = 5 if index2 == 10 else 0
                btn .grid(column=index2 , row=index1 , pady=3, padx=(n1,n2))

                btn.bind("<Enter>", self.enter_mouse)
                btn.bind("<Leave>", self.leave_mouse)
                btn.bind("<Button-1>", self.clic_mouse)

                if texto in self.mobiles2: btn.config(fg='yellow')
                self.buttons22.append(btn)   

    def enter_mouse(self, event):
        widget1 = event.widget
        if not widget1 .cget('bg') == '#bdfe04': 
            widget1 .config(bg="#24364a")

    def leave_mouse(self, event):
        if not event.widget .cget('bg') == '#bdfe04':
            event.widget.config(bg='#11161d')                               

    def clic_mouse(self, event):
        widget1 = event.widget
        widget1.config(bg='#bdfe04', fg='black')
            
        if self.container1 is not None and self.container1 != widget1:
            if self.container1 .cget('text') in self.mobiles2:
                self.container1 .config (bg='#11161d', fg='yellow')
            else:
                self.container1 .config (bg='#11161d', fg='white')          
        self.container1 = widget1
    
    def callback(self):
        print('Closed')
 
root = Tk()
app = Example(root).pack()
root.mainloop()