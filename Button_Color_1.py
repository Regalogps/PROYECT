                btn.bind("<Enter>", self.enter_mouse)
                btn.bind("<Leave>", self.leave_mouse)
                btn.bind("<Button-1>", self.clic_mouse)
                btn.bind("<B1-Motion>", self.motion_mouse)

                if texto in self.mobiles2: btn.config(fg='yellow')
                self.buttons22.append(btn)   # Examinar si borrar porque no tiene uso la lista



    # Cambia el color al pasar el mouse sobre el, en este caso: [ Celeste Apagado ]  AL ENTRAR
    def enter_mouse(self, event):
        widget1 = event.widget
        if not widget1 .cget('bg') == '#bdfe04':                            # Si el background no es verde:    
            widget1 .config(bg="#24364a")                                   # Color:  bg= #24364a  -->  Celeste apagado

 
    # Deja el color como estaba por defecto, en este caso: [ Azul Marino]  AL SALIR
    def leave_mouse(self, event):
        if not event.widget .cget('bg') == '#bdfe04':                       # Si el background no es verde:  
            event.widget.config(bg='#11161d')                               # Color:  #11161d   -   Defecto  Azul Marino


    # Cambia el color por defecto al hacerle click, en este caso: [ Verde ]
    def clic_mouse(self, event):
        widget1 = event.widget
        widget1.config(bg='#bdfe04', fg='black')                            # Color:  bg= #bdfe04  --> Verde
            
        if self.container1 is not None and self.container1 != widget1:
            if self.container1 .cget('text') in self.mobiles2:
                self.container1 .config (bg='#11161d', fg='yellow')         # Cambia el color del boton: (bg y fg) que tenian por defecto
            else:
                self.container1 .config (bg='#11161d', fg='white')          # Cambia el color del boton: (bg y fg) que tenian por defecto
        self.container1 = widget1                                           # Almacena el boton actual en otra variable
    

    def release_mouse(self, event):
        widget1 = event.widget    # Este event.widget tiene q detectar al WIDGET que precisamente esta debajo del mouse cuando este es soltado, para compararlo con el último botón presionado
        if self.container1 is not None and self.widget1 != widget1:
            if self.widget1 .cget('text') in self.mobiles2:
                    widget1 .config (bg='#11161d', fg='yellow')         
            else:
                self.widget1 .config (bg='#11161d', fg='white')


    # Deja el color como estaba por defecto, y reintegra el boton a la lista
    def active_reverse(self):
        if self.container1 is not None:
            if self.container1 .cget('text') in self.mobiles2:
                self.container1 .config (bg='#11161d', fg='yellow')         # Cambia el color del boton: (bg y fg) que tenian por defecto
            else:
                self.container1 .config (bg='#11161d', fg='white')          # Cambia el color del boton: (bg y fg) que tenian por defecto
        self.container1 = None









    #_______________________________________
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



###______________________________________________________





def focus_out(self, event):

        if self.focus_get() == None and self._button_selection is not None:
            print('saliendo',self.focus_get() )

            for btn in (self.frame_botones. buttons22):                       #

                if self._button_selection == btn.cget('text'):                #
                    btn .config(bg='#bdfe04', fg='black')                     #
                """ else:                                                         #
                    if btn .cget('text') in self.frame_botones .mobiles2:     #
                        btn .config (bg='#11161d', fg='yellow')               #
                    else:                                                     #
                        btn .config (bg='#11161d', fg='white') """                #



    # TAREA:
    #   1- Cambia el color del boton presionado actual a [VERDE-NEGRO]
    def press_mouse(self, event):
        widget_press = event.widget                                            # -1
        widget_press .config(bg='#bdfe04', fg='black')                         # -2
            
        #if self.container1 is not None and self.container1 != widget_press:    # -3
            #if self.container1 .cget('text') in self.mobiles2:                       # -3.1
            #    self.container1 .config (bg='#11161d', fg='yellow')                   # >>>>
            #else:                                                                    # -3.2
            #    self.container1 .config (bg='#11161d', fg='white')                    # >>>>  
                     
        for btn in (self.buttons22):
            if btn != widget_press:
                if btn .cget('text') in self.mobiles2:
                    btn .config (bg='#11161d', fg='yellow')
                else:
                    btn .config (bg='#11161d', fg='white') 

        self.container1 = widget_press                                         # -4


        # 1-  Atrapa al boton clickeado [ Nombre ]
        # 2-  Cambia el background y foreground del boton clikeado a un --> [ VERDE - NEGRO ]_________

        # 3-  Si [self.container1 = boton clickeado anterior] deja de ser [None] y es diferente al boton clickeado actual :▼▼▼▼
            # 3.1-  [self.container1 = boton clickeado anterior] tiene de texto algunas de las cadenas de la lista, self.mobiles2 :▼▼▼▼
                # >>>>  Cambia el background y foreground del boton clikeado anterior a un --> [ AZULINO - AMARILLO ]
            # 3.2-  Entonces :▼▼▼▼
                # >>>>  Cambia el background y foreground del boton clikeado anterior a un --> [ AZULINO - BLANCO ]
        
        # 4-  Almacena el boton actual en una variable   

