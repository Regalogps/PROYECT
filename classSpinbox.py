class Spinbox_class(Spinbox)
    def __init__(self, master, *arg)
        súper().__init__(self, master, width=13)
        self.spinbox_variable = StringVar() # ?poner padre?
        self.spinbox_values = ['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage', 'Randomizer', 'Jolteon', 'Turtle', 'Armor','A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']
        

        #_____C O N T E N E D O R E S:
        self.frm_B3 = Frame (self, bg='#31343a', width=172, height=65)   # NO POSICIONADO     # Color: Plomo       
        self.frm_C1 = Frame (self, bg='#11161d', width=60, height=65)    # NO POSICIONADO     # Color: Azul  #11161d

        #_____L A B E L:  NUMERO DE FILAS EXISTENTES   #|||||
        self.label_filas = Label (self.frm_B3, width=18, bg='#11161d', fg='#969696', bd=2, anchor= E) #|||||

        #_____L A B E L:  SELECCIONE MOBIL
        label_title = Label (self.frm_B3, text='Seleccione  Mobil :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)      # POSICIONADO

        #_____L A B E L:  MINIATURAS
        self.label_miniature = Label (self.frm_C1, image=self.Miniatures[0], bd= 0)                                                  # POSICIONADO

        #__________V A L I D A C I O N E S:  DE ENTRADA DE TEXTO DEL SPINBOX
        self.all_register = (self.register(self.validate_text), '%P', '%S')

        #_____L I S T B O X  / POSICIONADO
        self.listbox = Listbox (self.label_filas, font=('Calibri',9,'bold'), bg='#11161d', fg='#00ff00', width=11, height=1,  
                                justify='center', highlightbackground='#11161d', highlightthickness=0, borderwidth=0, bd=0,
                                selectbackground='#11161d', highlightcolor='#11161d', selectforeground='#ff8000', activestyle='none',                                        
                                takefocus=0, selectmode=SINGLE)  #|||||
                           
        #_____S P I N B O X  / POSICIONADO
        self.spinbox = Spinbox (self.frm_B3, width=13, bd=0, justify='center', wrap=True,
                                values=self.spinbox_values,                                      # DESDE AQUI PARA ABAJO SE HACEN LLAMADAS
                                textvariable=self.spinbox_variable, 
                                validate='key', validatecommand=self.all_register)                             
        
        #_____B I N D - L I S T B O X - E V E N T:  1
        self.listbox .bind ('<<ListboxSelect>>', self.listbox_select)   # ACTIVA: CON CLICK IZQUIERDO EN EL LISTBOX - SELECCIONA 1 ITEM

        #_____B I N D - S P I N B O X - E V E N T:  2
        self.spinbox .bind ('<Return>', self.bind_spinbox)  # ACTIVA: CON TECLA ENTER - ABRE LAS VENTANAS
        self.spinbox .bind ('<Double-Button-1>', lambda *arg: self.spinbox.delete(0, END))   # ACTIVA: CON DOBLE CLICK EN SPINBOX - LIMPIA SPINBOX
        self.spinbox .bind ('<Return>', self.bind_listbox)  # ACTIVA: CON TECLA ENTER - SELECCIONA EL INDICE 0 DEL LISTBOX   #||||||
       
        #_____T R A C E__A D D - S P I N B O X:     ACTIVA: SI SPINBOX_VARIABLE CAMBIA DE VALOR
        self.spinbox_variable .trace_add ('write', self.change_miniature)  
        self.spinbox_variable .trace_add ('write', lambda *arg: self.spinbox_variable.set (self.spinbox_variable.get() .capitalize()))   # INSERTA EL VALOR OBTENIDO EN MAYUSCULA EL PRIMER STRING


        #__________Posicionamientos:
        self.label_filas .grid (column=0, row=0, padx=(0,5), pady=(0,2), sticky=N)  #|||||
        label_title .grid (column=0, row=1, padx=10, pady=(0,0), sticky=W)
        self.label_miniature .grid (padx=2, pady=3)

        self.listbox .grid ( padx=(19,0), pady=(0,5), sticky=N)
        self.spinbox .grid (column=0, row=2, padx=11, pady=(3,3), sticky=W)   

        #__________Propagación:
        self.frm_B3 .grid_propagate(False)
        self.frm_C1 .grid_propagate(False)
        self.label_filas .grid_propagate(False)
        self.listbox .grid_propagate(False)
    


#__________________G L O S A R I O:
        # LISTBOX:    
        # width= 15 ---> NUMEROS DE CARACTERES PERMITIDOS
        # height= 1 ---> NUMERO DE FILAS OBSERVABLES
        # justify= 'center' ---> CENTRAR TEXTO INTERNO
        # highlightbackground= '#11161d' ---> COLOR DEL BORDE SIN FOCO
        # highlightthickness= 4 ---> TAMAÑO DEL BORDE EN PIXELES SIN FOCO
        # selectbackground= '#11161d' ---> COLOR DE BORDE CON FOCO
        # selectforeground= 'green2' ---> COLOR DE FONDO CON FOCO
        # activestyle= 'none' ---> SUBRAYADO DEL TEXTO CUANDO ES SELECCIONADO DESACTIVADO:'none'
#__________________

    def validate_text(self, text, arg):   # ACTIVA: SIEMPRE QUE INSERTE TEXTO EN SPINBOX - NO PERMITE NUMEROS,SIMBOLOS,ESPACIOS Y CONTROLA LA CANTIDAD

        if all (i not in "0123456789[{!¡¿?<>(|#$%&),_-°'´}] +-*/=" for i in text) and len(text) < 14:   
                return True                                                 
        return False  

        
        # TRUE = PERMITIR
        # FALSE = DENEGAR                                                  
                  
    def gear_stacking(self):   # ACTIVA: CON CLICK IZQUIERDO EN LA RUEDA DE CONFIGURACION - QUITA Y PONE WIDGET, REDIMENSIONA LA VENTANA PRINCIPAL,ETC

        if  self.gear == True:          # PREDETERMINADO: TRUE
            self.frm_B1 .grid_remove()  # B1: BOTONES          
            self.frm_B3 .grid_remove()  # B3: LISTBOX    ###??? necesita if?
            self.frm_C1 .grid_remove()  # C1: MINIATURA

            self.frm_B2 .focus_set()    # NECESARIO 
            self.frm_B2 .grid (column=1, row=0, padx=0, pady=0, sticky=N)               
            self.gear = False
            self.geometry ('816x65')       
    
        else:
            self.frm_B2 .grid_remove()
            self.gear = True   #@@@# ESTO ESTABA AL FINAL
            if self.checkbutton5 .variable.get() == True:   
                self.frm_B3 .grid (column=1, row=0, padx=0, pady=0, sticky=NW)
                self.frm_C1 .grid (column=1, row=0, padx=0, pady=0, sticky=NE)
                self.spinbox .focus_set()
                self.spinbox .icursor(END)
                self.geometry ('232x65')
            else:
                self.frm_B1 .grid()
                self.frm_B3 .grid_remove()
                self.frm_C1 .grid_remove()
                            
    def change_miniature(self, *args):   # ACTIVA: SI SPINBOX_VARIABLE CAMBIA DE VALOR - BORRA LA LISTA DE LISTBOX, MANDA A LLAMAR A UPDATE Y CAMBIA LAS MINIATURAS

        value = self.spinbox.get() .capitalize()

        if value == '':                                              # 1- SI SPINBOX ESTA VACIO.  2- BORRA LA LISTA DE LISTBOX.  3- DESHABILITA LISTBOX.
            self.listbox .delete(0, END)
        else:                                                        # 1- HABILITA LISTBOX.  2- CREA LISTA VACIA.  3- ITERANDO: 'self.spinbox_values'.
            list_new = []                                            # 4- SI COINCIDE 'value' EN 'self.spinbox_values'.  5- AGREGA VALUE A LISTA.  6- SI LA LISTA NO ESTA VACIA.
            for i in self.spinbox_values:                            # 10- LLAMA AL METODO: 'def update' Y PASA LA LISTA DE ARGUMENTO. 
                if value in i:
                    list_new .append(i)

            if list_new != []:   ##@@@@@## PROBAR SIN IF, SI ES ELEGIBLE ''
                print("mando lista", list_new)          
                self.update(list_new)

            if self.spinbox_variable.get() == 'As':  #|||
                self.listbox.see(2) ##@@@@@## PROBAR SIN.SEE, YA QUE SOLO QUEDARIA ASATE 
                self.listbox.delete(0,1)
       
        for index, i in enumerate(self.spinbox_values):      
            if self.spinbox.get() .capitalize() == i:                           
                self.label_miniature .config(image= self.Miniatures[index])
                self.spinbox .icursor(END)
            
        listbox = self.listbox.get(0)
        spinbox = self.spinbox.get()
        print('valor de list:', listbox)
        print('valor de spin:', spinbox)


        if listbox != spinbox and listbox != '': 
            self.label_miniature .config(image= self.Miniatures[22])
        if spinbox == '':
            self.label_miniature .config(image= self.Miniatures[22])

        # print('111', self.spinbox_variable.get()) # DEVUELVE: PRIMER CARACTER EN MAYUSCULA
        # print('222', self.spinbox.get())          # DEVUELVE: PRIMER CARACTER EN MINUSCULA
 
    def cheeck_5 (self):   # SIN USOOOOOOOOOOOOOOOOOO
        self.checkbutton5.value()

    def bind_spinbox(self, event):  # ACTIVA: CON TECLA ENTER SI SPINBOX TIENE FOCO - ABRE LAS VENTANAS
        
        left = [Frog_left_off, Fox_left_off, Boomer_left_off, Ice_left_off, Jd_left_off, Grub_left_off, Lightning_left_off, Aduka_left_off, Knight_left_off, Kalsiddon_left_off, Mage_left_off, Randomizer_left_off, Jolteon_left_off, Turtle_left_off, Armor_left_off, Asate_left_off, Raon_left_off, Trico_left_off, Nak_left_off, Bigfoot_left_off, Barney_left_off, Dragon_left_off,]
        right = [Frog_right, Fox_right, Boomer_right, Ice_right, Jd_right, Grub_right, Lightning_right, Aduka_right, Knight_right, Kalsiddon_right, Mage_right, Randomizer_right, Jolteon_right, Turtle_right, Armor_right, Asate_right, Raon_right, Trico_right, Nak_right, Bigfoot_right, Barney_right, Dragon_right]
        stuf = [Frog_stuf, Fox_stuf, Boomer_stuf, Ice_stuf, Jd_stuf, Grub_stuf, Lightning_stuf, Aduka_stuf, Knight_stuf, Kalsiddon_stuf, Mage_stuf, Randomizer_stuf, Jolteon_stuf, Turtle_stuf, Armor_stuf, Asate_stuf, Raon_stuf, Trico_stuf, Nak_stuf, Bigfoot_stuf, Barney_stuf, Dragon_stuf]

        for index, i in enumerate(self.spinbox_values):
            if self.spinbox.get() == i:
                self.windows_123(left[index], right[index], stuf[index]) 
                self.spinbox .icursor(END)  # ESTA APRUEBA SI ES TOTLAMENTE NECESARIO 
                
    def minimize_windows(self):   # ACTIVA: CON CLICK IZQUIERDO AL LOGO - MINIMIZA LAS VENTANAS

        if self.open_1 == True or self.open_2 == True or self.open_3 == True:

            if self.minimize == False:
                if self.open_1 == True:
                    self.toplevel_LEFT .deiconify()   # MOSTRAR VENTANAS  
                if self.open_2 == True:
                    self.toplevel_RIGHT .deiconify()
                if self.open_3 == True:
                    self.toplevel_STUF .deiconify()

                self.minimize = True

            else: 
                if self.open_1 == True:
                    self.toplevel_LEFT .iconify()     # OCULTAR VENTANAS
                if self.open_2 == True:
                    self.toplevel_RIGHT .iconify() 
                if self.open_3 == True:    
                    self.toplevel_STUF .iconify()

                self.minimize = False

    def ash_close_windows(self, event):   # ACTIVA: CON DOBLE CLICK DERECHO EN EL LOGO - CIERRA LAS VENTANAS 

        self.toplevel_LEFT .destroy() 
        self.open_1 = False

        self.toplevel_RIGHT .destroy()
        self.open_2 = False

        self.toplevel_STUF .destroy()
        self.open_3 = False

    def update(self, list):  # ACTIVA: SI EL METODO CHANGE_MINIATURE LA MANDA A LLAMAR - BORRA LA LISTA DE LISTBOX EXISTENTE, AGREGA NUEVOS VALORES A LISTA Y BORRA DE NUEVO SI SE CUMPLE LA CONDICION
        
        self.listbox .delete(0, END)                                    # 1- BORRA LA LISTA DE LISTBOX
        
        for i in list:                                                  # 1- ITERANDO: 'list_new'.  2- INSERTANDO ITERADOR 'i' A LISTBOX.  
            self.listbox .insert(END, i) 
        if self.listbox.get(0) == self.spinbox_variable.get():  #|||
            self.listbox .delete(0, END) 

    def listbox_select(self,event):   # ACTIVA: CON CLICK IZQUIERDO EN LISTBOX - 
       
        selection = self.listbox .get(ANCHOR)                                                           # 1- BORRA EL CONTENIDO DE SPINBOX.  2- INSERTA EL ITEM SELECCIONADO DEL LISTBOX A SPINBOX                         
        
        if self.listbox.get(0,END) != ():      
            self.spinbox .delete(0, END) 
        self.spinbox .insert(0, selection)
        self.listbox .selection_clear(0,END)
 
        self.after(100, lambda: self.spinbox.focus_set())

        print('numero',self.listbox.size())
        
    
    def bind_listbox(self, event):
 
        print('QUERIENDO ENTRAR A IFF BIND')
        listbox = self.listbox.get(0)
        spinbox = self.spinbox.get()
        #print('valor de list:', listbox)
        #print('valor de spin:', spinbox)


        if listbox != spinbox and listbox != '':
            self.spinbox.delete(0, END)
            self.spinbox.insert(0, listbox)
            
        self.bind_spinbox(event)    

            

