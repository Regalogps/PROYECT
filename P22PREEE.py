
from tkinter import *

class TypeButton(Button):
    def __init__(self, parent, *args, **kwargs):
        kwargs = {'font':('Calibri',9,'bold'), 'bg': '#11161d', 'fg':'white',
                  'width':10, 'bd':0, 'activebackground':'#bdfe04', **kwargs}
        super().__init__(master, *args, **kwargs)

class Example(Frame):
    def __init__(self,parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.frame = Frame(self, bg='#11161d')
        self.frame .grid(padx=(10,10), pady=(6,6))
        self.creator_buttons()

    def creator_buttons(self):  

        mobiles = [['_0_', '_1_', '_2_', '_3_', '_4_', '_5_', '_6_', '_7_', '_8_', '_9_', '_10_', '_11_'],
                   ['_12_', '_13_', '_14_', '_15_', '_16_', '_17_', '_18_', '_19_', '_20_', '_21_']]
        mobiles2 = ['_1_', '_8_', '_12_', '_20_', '_21_'] 
        buttons = []
        for index1, mobil in enumerate(mobiles):
            for index2, texto in enumerate(mobil):
                number = 11 if index1 == 1 else 0
                btn = TypeButton (self.frame, text=texto)             
                n1 = 5 if index2 == 0 else 0        
                n2 = 5 if index2 == 10 else 0
                btn .grid(column=index2 , row=index1 , pady=3, padx=(n1,n2))
                if texto in mobiles2: btn.config(fg='yellow')
                btn.bind("<Enter>", self.mouse_move)
                btn.bind("<Leave>", self.mouse_stop)
                #btn.bind("<Button-1>", self.mouse_clic)   
                buttons.append(btn)

    def mouse_move(self, event):   # Change the color when hovering the mouse over the    # Color: Light blue off
        event.widget.config(bg="#24364a")

    def mouse_stop(self, event):   # Leave the color as it was by default                 # Color: Dark blue     
        event.widget.config(bg='#11161d')
    
    #def mouse_clic(self, event):
    #    event.widget.config(state='disabled', disabledforeground='green', )#bg='#bdfe04', fg='black')
 
root = Tk()
app = Example(root).pack()
root.mainloop()
