class B1FrameCls(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #_____C O N T E N E D O R E S:   [ 1 ]
        self.frame_1 = Frame (self, bg='#11161d')          # Color: Azul '#11161d'
        self.frame_1 .grid (padx=(10,10), pady=(6,6))

        #_____Métodos Llamados:
        self.creator_buttons()

        #_____Variables de Control para los Botones
        self.container1 = None
        self.container2 = None

        
    # Manda los indices para abrir las imagenes en las ventanas:
    def indices(self, indice):
        # I N D I C E S :
        arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, = 0, 1, 2, 3, 4, 5, 6, 7 

        return  lambda: self.master.windows_123(
                lambda top1: TopIzqCls  (top1, indice, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst),
                lambda top2: TopDerCls  (top2, indice, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst),
                lambda top3: TopStufCls (top3, indice, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst))

        
    # Crea los 22 botones y las posiciona:
    def creator_buttons(self):  
        mobiles = [['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage'],
                   ['Randomizer', 'Jolteon', 'Turtle', 'Armor', 'A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']]                  
        self.mobiles2 = ['Fox','Knight','Jolteon','Barney','Dragon'] 

        self.buttons22 = []                                     # Lista: Sirve para condicionar las funciones vinculadas a eventos: bind -->  mouse_move, mouse_stop, mouse_clic  
        for index1, mobil in enumerate(mobiles):                # Iterador: (mobil) = 11 elementos: 1 sublistasssss
            for index2, texto in enumerate(mobil):              # Iterador: (texto) = 1  elemento:  'Frog'
                number = 11 if index1 == 1 else 0               # number: cambie su valor de 0 a 11 si su condicion se cumple

                btn = DefaultButtonCls (self.frame_1, text=texto, command= self.indices(index2 + number))             
                n1 = 5 if index2 == 0 else 0        
                n2 = 5 if index2 == 10 else 0
                btn .grid(column=index2 , row=index1 , pady=3, padx=(n1,n2))

                btn.bind("<Enter>", self.enter_mouse)
                btn.bind("<Leave>", self.leave_mouse)
                btn.bind("<ButtonPress-1>", self.press_mouse)
                btn.bind("<ButtonRelease-1>", self.release_mouse)

                if texto in self.mobiles2: btn.config(fg='yellow')
                self.buttons22.append(btn)   # Examinar si borrar porque no tiene uso la lista



    # Cambia el color al pasar el mouse sobre el, en este caso: [ Celeste Apagado ]  AL ENTRAR
    def enter_mouse(self, event):
        if not event.widget .cget('bg') == '#bdfe04':                            # Si el background no es verde:    
            event.widget .config(bg="#24364a")                                   # Color:  bg= #24364a  -->  Celeste apagado

 
    # Deja el color como estaba por defecto, en este caso: [ Azul Marino]  AL SALIR
    def leave_mouse(self, event):
        if not event.widget .cget('bg') == '#bdfe04':                       # Si el background no es verde:  
            event.widget.config(bg='#11161d')                               # Color:  #11161d   -   Defecto  Azul Marino


    # Cambia el color por defecto al hacerle click, en este caso: [ Verde ]
    def press_mouse(self, event):
        self.widget_press = event.widget
        self.widget_press .config(bg='#bdfe04', fg='black')                             # Color:  bg= #bdfe04  --> Verde
            
        if self.container1 is not None and self.container1 != self.widget_press:
            if self.container1 .cget('text') in self.mobiles2:
                self.container1 .config (bg='#11161d', fg='yellow')         # Cambia el color del boton: (bg y fg) que tenian por defecto
            else:
                self.container1 .config (bg='#11161d', fg='white')          # Cambia el color del boton: (bg y fg) que tenian por defecto
        self.container1 = self.widget_press                                            # Almacena el boton actual en otra variable
    

    def release_mouse(self, event):
        widget_release = event.widget.winfo_containing(event.x_root, event.y_root)
        if widget_release != self.widget_press:
            if self.widget_press .cget('text') in self.mobiles2:
                self.widget_press .config (bg='#11161d', fg='yellow')
            else:
                self.widget_press .config (bg='#11161d', fg='white')


            if self.container2 is not None:
                self.container2 .config(bg='#bdfe04', fg='black')
        self.container2 = self.container1


    # Deja el color como estaba por defecto, y reintegra el boton a la lista
    def uncheck_selection(self):
        if self.container1 is not None:
            if self.container1 .cget('text') in self.mobiles2:
                self.container1 .config (bg='#11161d', fg='yellow')         # Cambia el color del boton: (bg y fg) que tenian por defecto
            else:
                self.container1 .config (bg='#11161d', fg='white')          # Cambia el color del boton: (bg y fg) que tenian por defecto
        self.container1 = None

