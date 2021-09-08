class SpinboX (Spinbox):
    
    def__init__(self, *arg, **kwarg)
        Spinbox.__init__(self, *arg, **kwarg)

        #####self.frm_B3 = Frame (self, bg='#31343a', width=174, height=65)  # Color: Plomo
        #####self.frm_B3 .grid_propagate(False)
        #####self.frm_C1 = Frame (self, bg='green2', width=60, height=65)
        #####self.frm_C1 .grid_propagate(False)
        
        self.spinbox_variable = StringVar()
        self.spinbox_variable .trace_add ('write', lambda *arg: self.spinbox_variable.set (self.spinbox_variable.get() .capitalize()))  # SE ACTIVA SI INTRODUCE TEXTO: CAMBIA POR MAYUSCULA

        #####label_title = Label (self.frm_B3, text='Seleccione  Mobil :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)

        self.spinbox_values = ['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage', 'Randomizer', 'Jolteon', 'Turtle', 'Armor','A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Dragon 1', 'Dragon 2']
        self.spinbox = Spinbox (self.frm_B3, width=13, values= self.spinbox_values, textvariable=self.spinbox_variable, wrap= True)    

        self.spinbox .bind ('<Return>', self.bind_spinbox)  # SE ACTIVA SI SPINBOX TIENE FOCO, Y SE PRESIONA LA TECLA ENTER: ABRE LAS VENTANAS
        
        #self.spinbox .icursor(END)

        #####______Posicionamientos:
        #####label_title .grid (column= 0, row=0, padlx=10, pady=(10,5), sticky= W)
        self.spinbox .grid (column= 0, row=1, padx=10, pady=(0,6), sticky= W)