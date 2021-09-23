 #_____C O N T E N E D O R E S:
        self.frame_B3 = Frame (self, bg='#31343a', width=172, height=65)   # NO POSICIONADO     # Color: Plomo       
        self.frame_C1 = Frame (self, bg='#11161d', width=60, height=65)    # NO POSICIONADO     # Color: Azul  #11161d

        #_____L A B E L: 
        self.label_listbox = Frame (self.frame_B3, width=18, bg='green', bd=2, )   # #11161d
        label_title = Label (self.frame_B3, text='Seleccione  Mobil :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0) 

        #_____L A B E L:  MINIATURAS
        self.label_miniature = Label (self.frame_C1, bd= 0,
                                        image=self.master.Miniatures[0]) # image=self.master.Miniatures[0],


        #_____L I S T B O X  
        self.create_listbox (width=10, height=1)
        #_____S P I N B O X 
        self.create_spinbox (width=13)


        #self.radio_listbox = Radiobutton (self.label_listbox, borderwidth=0, bd=0 , height=0)
        #self.radio_listbox .grid(column=0, row=0)
        #self.radio_listbox .place (x=0 ,y=0)


        #__________Posicionamientos:
        self.frame_B3 .grid (column=0, row=0, padx=0, pady=0, )
        self.frame_C1 .grid (column=1, row=0, padx=0, pady=0, )


        self.label_listbox .grid (column=0, row=0, padx=(0,5), pady=(0,2), sticky=N)  
        label_title .grid (column=0, row=1, padx=10, pady=0)
        self.label_miniature .grid (padx=2, pady=3)

        self.listbox .grid(column=1, row=0)
        self.spinbox .grid (column=0, row=2, padx=11, pady=(3,3), sticky=W)   

        #__________Propagación:
        self.frame_B3 .grid_propagate(False)
        self.frame_C1 .grid_propagate(False)

        self.label_listbox .grid_propagate(False)
        self.listbox .grid_propagate(False)