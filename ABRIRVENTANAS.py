    def listbox_enter(self, event):  # ACTIVA: CON TECLA ENTER - INSERTA EL VALOR DE LISTBOX A SPINBOX, MANDA LLAMAR A OPEN_WINDOWS  Y ABREN LAS VENTANAS
 
        listbx = self.listboxx.get(0)
        spinbx = self.spinboxx.get()

        if listbx != spinbx and listbx != '':
            self.spinboxx.delete(0, END)
            self.spinboxx.insert(0, listbx)
   
        self.open_windows() 
         
    def open_windows(self, event=None):  # ACTIVA: ** SI ES LLAMADO POR LISTBOX_SELECT ** - ABRE LAS VENTANAS
        
        left = [Frog_left_off, Fox_left_off, Boomer_left_off, Ice_left_off, Jd_left_off, Grub_left_off, Lightning_left_off, Aduka_left_off, Knight_left_off, Kalsiddon_left_off, Mage_left_off, Randomizer_left_off, Jolteon_left_off, Turtle_left_off, Armor_left_off, Asate_left_off, Raon_left_off, Trico_left_off, Nak_left_off, Bigfoot_left_off, Barney_left_off, Dragon_left_off,]
        right = [Frog_right, Fox_right, Boomer_right, Ice_right, Jd_right, Grub_right, Lightning_right, Aduka_right, Knight_right, Kalsiddon_right, Mage_right, Randomizer_right, Jolteon_right, Turtle_right, Armor_right, Asate_right, Raon_right, Trico_right, Nak_right, Bigfoot_right, Barney_right, Dragon_right]
        stuf = [Frog_stuf, Fox_stuf, Boomer_stuf, Ice_stuf, Jd_stuf, Grub_stuf, Lightning_stuf, Aduka_stuf, Knight_stuf, Kalsiddon_stuf, Mage_stuf, Randomizer_stuf, Jolteon_stuf, Turtle_stuf, Armor_stuf, Asate_stuf, Raon_stuf, Trico_stuf, Nak_stuf, Bigfoot_stuf, Barney_stuf, Dragon_stuf]
        # I N D I C E S :
        arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, = 0, 1, 2, 3, 4, 5, 6, 7 


        for index, i in enumerate(self.spinbox_values):     
            if self.spinbox_variable.get() == i:            # ANTES DABA ERROR CON: self.spinboxx .!toplvel.!frame,etc
                #self.master.windows_123(left[index], right[index], stuf[index]) 
                #break                                       # Sin breack el programa seguiria buscando coincidencias despues del enter, y guardaria un error           
                self.master.windows_123(
                lambda top1: TopIzqCls  (top1, index, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst),
                lambda top2: TopDerCls  (top2, index, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst),
                lambda top3: TopStufCls (top3, index, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst))
                break

        if self._change is not None:
            self.after(10000, self.automatic_deletion) 

    def automatic_deletion(self):  # ACTIVA: ** SI ES LLAMADO POR OPEN_WINDOWS ** Y SI LA VARIABLE DE CONTROL NO ES NONE - LIMPIA SPINBOX
        self.spinboxx .delete(0, END)    
 
##################
        self.creator_buttons()

    def indices(self, ind):
        # I N D I C E S :
        arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, = 0, 1, 2, 3, 4, 5, 6, 7 

        return  lambda: self.master.windows_123(
                lambda top1: TopIzqCls  (top1, ind, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst),
                lambda top2: TopDerCls  (top2, ind, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst),
                lambda top3: TopStufCls (top3, ind, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst))
    
    def creator_buttons(self):  
        mobiles = [['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage'],
                   ['Randomizer', 'Jolteon', 'Turtle', 'Armor', 'A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']]
        mobiles2 = ['Fox','Knight','Jolteon','Barney','Dragon'] 
        self.buttons = []                                       # Lista: Sirve para condicionar las funciones vinculadas a eventos: bind -->  mouse_move, mouse_stop, mouse_clic
        for index1, mobil in enumerate(mobiles):                # Iterador: (mobil) = 11 elementos: 1 sublistasssss
            for index2, texto in enumerate(mobil):              # Iterador: (texto) = 1  elemento:  'Frog'
                number = 11 if index1 == 1 else 0               # number: cambie su valor de 0 a 11 si su condicion se cumple
                btn = B1ButtonCls (self.frame_1, text=texto, command= self.indices(index2 + number))             
                n1 = 5 if index2 == 0 else 0        
                n2 = 5 if index2 == 10 else 0
                btn .grid(column=index2 , row=index1 , pady=3, padx=(n1,n2))
                if texto in mobiles2: btn.config(fg='yellow')
                btn.bind("<Enter>", self.mouse_move)
                btn.bind("<Leave>", self.mouse_stop)
                btn.bind("<Button-1>", self.mouse_clic)   
                self.buttons.append(btn)
