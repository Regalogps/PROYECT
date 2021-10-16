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
        widget1 = event.widget
        if widget1 != self.widget1:
            if widget1 .cget('text') in self.mobiles2:
                    widget1 .config (bg='#11161d', fg='yellow')         
            else:
                widget1 .config (bg='#11161d', fg='white')
        self.container2 = widget1


    # Deja el color como estaba por defecto, y reintegra el boton a la lista
    def active_reverse(self):
        if self.container1 is not None:
            if self.container1 .cget('text') in self.mobiles2:
                self.container1 .config (bg='#11161d', fg='yellow')         # Cambia el color del boton: (bg y fg) que tenian por defecto
            else:
                self.container1 .config (bg='#11161d', fg='white')          # Cambia el color del boton: (bg y fg) que tenian por defecto
        self.container1 = None
