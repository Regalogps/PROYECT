
self.button1 = tk.Button(self, text='pack 1',
                      command=lambda:self.windows(lambda top:ShowImage(top, index_1, index_2, self.path_lst),


def bucle (self):
        lst_1 = [['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub',
                  'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage'],
                 ['Randomizer', 'Jolteon', 'Turtle', 'Armor', 'A.sate',
                  'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']]

        lst_2 = [['Fox','Knight','Jolteon','Barney','Dragon']]  
    
        for index, i in enumerate(lst_1):
            for dex, x in enumerate(i):
                for dey in (lst_2)
                    btn = CButton (self.frame_1, text=x)
                    five = (5,0) if dex == 0 else five = 0
                    five = (0,5) if dex == 10 else five = 0
                    btn .grid(columna=dex , row=index , pady=3-index , padx=five)

                    if x in dey: btn.config(fg='yellow', activebackground='#ebb015')


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
