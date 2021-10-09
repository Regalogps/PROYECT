

from tkinter import *

#_____________________________________ aqui
class CButton(Button):
    def __init__(self, master, *args, **kwargs):
        kwargs = {"font":('Calibri',9,'bold'), 'bg': '#11161d', 'fg':'white', 'width':10, 'bd':0, 'activebackground':'#ebb015', **kwargs}
        super().__init__(master, *args, **kwargs) 

class Frame1Cls(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.frame_1 = Frame(self, bg='green')
        self.frame_1 .grid(padx=(10,10), pady=(6,6))
        #self.creator()
        self.bucle()

    def creator (self):

        self.Frog_1 = CButton        (self.frame_1, text='Frog', )
        self.Fox_2 = CButton         (self.frame_1, text='Fox',)
        self.Boomer_3 = CButton      (self.frame_1, text='Boomer', )
        self.Ice_4 = CButton         (self.frame_1, text='Ice', )
        self.JD_5 = CButton          (self.frame_1, text='J.D',  )
        self.Grub_6 = CButton        (self.frame_1, text='Grub', )
        self.Lightning_7 = CButton   (self.frame_1, text='Lightning' )
        self.Aduka_8 = CButton       (self.frame_1, text='Aduka',  )
        self.Knight_9 = CButton      (self.frame_1, text='Knight', )
        self.Kalsiddon_10 = CButton  (self.frame_1, text='Kalsiddon', )
        self.Mage_11 = CButton       (self.frame_1, text='Mage',  )

        self.Randomizer_12 = CButton (self.frame_1, text='Randomizer',  )
        self.Jolteon_13 = CButton    (self.frame_1, text='Jolteon',  )
        self.Turtle_14 = CButton     (self.frame_1, text='Turtle', )
        self.Armor_15 = CButton      (self.frame_1, text='Armor',  )
        self.Asate_16 = CButton      (self.frame_1, text='A.Sate', )
        self.Raon_17 = CButton       (self.frame_1, text='Raon', )
        self.Trico_18 = CButton      (self.frame_1, text='Trico', )
        self.Nak_19 = CButton        (self.frame_1, text='Nak', )
        self.Bigfoot_20 = CButton    (self.frame_1, text='Bigfoot', )
        self.Barney_21 = CButton     (self.frame_1, text='Barney',  )
        self.Dragon_22 = CButton     (self.frame_1, text='Dragon', )
                
        self.Frog_1 .grid (column= 0, row= 0, pady= 3, padx= (5,0))
        self.Fox_2 .grid (column= 1, row= 0, pady= 3, padx= (0,0))       
        self.Boomer_3 .grid (column= 2, row= 0, pady= 3, padx= (0,0))           
        self.Ice_4 .grid (column= 3, row= 0, pady= 3, padx= (0,0))
        self.JD_5 .grid (column= 4, row= 0, pady= 3, padx= (0,0))
        self.Grub_6 .grid (column= 5, row= 0, pady= 3, padx= (0,0))
        self.Lightning_7 .grid (column= 6, row= 0, pady= 3, padx= (0,0))
        self.Aduka_8 .grid (column= 7, row= 0, pady= 3, padx= (0,0))
        self.Knight_9 .grid (column= 8, row= 0, pady= 3, padx= (0,0))
        self.Kalsiddon_10 .grid (column= 9, row= 0, pady= 3, padx= (0,0))
        self.Mage_11 .grid (column= 10, row= 0, pady= 3, padx= (0,5))

        self.Randomizer_12 .grid (column= 0, row= 1, pady= 2, padx= (5,0))
        self.Jolteon_13 .grid (column= 1, row= 1, pady= 2, padx= (0,0))
        self.Turtle_14 .grid (column= 2, row= 1, pady= 2, padx= (0,0))
        self.Armor_15 .grid (column= 3, row= 1, pady= 2, padx= (0,0))
        self.Asate_16 .grid (column= 4, row= 1, pady= 2, padx= (0,0))
        self.Raon_17 .grid (column= 5, row= 1, pady= 2, padx= (0,0))
        self.Trico_18 .grid (column= 6, row= 1, pady= 2, padx= (0,0))
        self.Nak_19 .grid (column= 7, row= 1, pady= 2, padx= (0,0))
        self.Bigfoot_20 .grid (column= 8, row= 1, pady= 2, padx= (0,0))
        self.Barney_21 .grid (column= 9, row= 1, pady= 2, padx= (0,0))
        self.Dragon_22 .grid (column= 10, row= 1, pady= 2, padx= (0,5))

    def bucle (self):
        lst_1 = [['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub',
                  'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage'],
                 ['Randomizer', 'Jolteon', 'Turtle', 'Armor', 'A.sate',
                  'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']]

        lst_2 = [['Fox','Knight','Jolteon','Barney','Dragon']]  
    
        for index, i in enumerate(lst_1):
            print(i)
            for dex, x in enumerate(i):
                for dey in (lst_2):
                    btn = CButton (self.frame_1, text=x) #command=lambda:self.windows(
                                 # lambda top1:ShowImage1(top1, index_1, index_2, self.path_lst),
                                 # lambda top2:ShowImage2(top2, index_1, index_2, self.path_lst),
                                 # lambda top3:ShowImage3(top3, index_1, index_2, self.path_lst)))         
                    five = (5,0) if dex == 0 else 0
                    #print('indice:',dex,'es:', five)
                    five = (0,5) if dex == 10 else 0
                    #print('indice:',dex,'es:', five)
                    btn .grid(column=dex , row=index , pady=3 - index, padx=five)
                    #print('indice:',dex,'es:', five)

                    if x in dey: btn.config(fg='yellow', activebackground='#ebb015')
    
                  

root = Tk()
app = Frame1Cls (root)
app .pack()
root .mainloop()