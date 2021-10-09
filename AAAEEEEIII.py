def bucle (self):
        lst_1 = [['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub',
                  'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage'],
                 ['Randomizer', 'Jolteon', 'Turtle', 'Armor', 'A.sate',
                  'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']]

        lst_2 = [['Fox','Knight','Jolteon','Barney','Dragon']]  
    
        for index, i in enumerate(lst_1):
            for index2, e in enumerate(lst_2):
                btn = CButton (self.frame_1, text=i) 

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
    
