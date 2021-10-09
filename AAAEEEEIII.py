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

        #lst_2 = [['Fox','Knight','Jolteon','Barney','Dragon']]  
    
        for index, i in enumerate(lst_1):
            for indexe, e in enumerate(i):
                btn = CButton (self.frame_1, text=e)
                cinco = (5,0) if indexe == 0 else exc = 0
                btn .grid(columna=indexe , row=index , pady=3-index , padx=exc)


                if index < 11 and index != 0 and index != 10:
                    btn .grid(column= index, row= 0, pady= 3, padx= (0,0))               
                if index > 10 and index != 11 and index != 21:
                    index = index - 11
                    btn .grid(column= index, row= 1, pady= 2, padx= (0,0)) 
                if index == 0:
                    btn .grid (column= 0, row= 0, pady= 3, padx= (5,0))
                if index == 10:
                    btn .grid (column= 10, row= 0, pady= 3, padx= (0,5))
                if index == 11:
                    btn .grid (column= 0, row= 1, pady= 2, padx= (5,0))
                if index == 21:  
                    btn .grid (column= 10, row= 1, pady= 2, padx= (0,5))

                if i in e:
                  btn.config(fg='yellow', activebackground='#ebb015')
    
