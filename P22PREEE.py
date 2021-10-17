
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
        self.creator_buttons()

    def creator_buttons(self):  

        mobiles = [['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage'],
                   ['Randomizer', 'Jolteon', 'Turtle', 'Armor', 'A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']]                  
        mobiles2 = ['Fox','Knight','Jolteon','Barney','Dragon'] 
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

    def mouse_move(self, event):
        event.widget.config(bg="#24364a")

    def mouse_stop(self, event): 
        event.widget.config(bg='#11161d')
    
    #def mouse_clic(self, event):
    #    event.widget.config(state='disabled', disabledforeground='green', )#bg='#bdfe04', fg='black')
 
root = Tk()
app = Example(root).pack()
root.mainloop()
