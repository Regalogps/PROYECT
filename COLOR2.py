                btn.bind("<Motion>", self.enter_mouse)
                btn.bind("<Leave>", self.leave_mouse)
                btn.bind("<ButtonPress-1>", self.press_mouse)
                btn.bind("<ButtonRelease-1>", self.release_mouse)

                if texto in self.mobiles2: btn.config(fg='yellow')
                self.buttons22.append(btn)   # Examinar si borrar porque no tiene uso la lista


    # TAREA:
    #   1- Cambia el color del boton al pasar el mouse sobre el
    def enter_mouse(self, event):
        if not event.widget .cget('bg') == '#bdfe04':           # -1  
            event.widget .config(bg="#24364a")                     # -1.1
        
        # 1-  Si el background del boton sobre el que se posa el mouse, NO ES VERDE:
            # 1.1-   Cambia el background del boton a ( Celeste Apagado )

    
    # TAREA:
    #   1- Cambia el color del boton al salir el mouse de el
    def leave_mouse(self, event):
        if not event.widget .cget('bg') == '#bdfe04':            # -1
            event.widget.config(bg='#11161d')                       # -1.1

        # 1-  Si el background del boton desde donde sale el mouse, NO ES VERDE:
            # 1.1-   Cambia el background del boton a ( Default: Azulino )


    # TAREA:
    #   1- Atrapa al boton clickeado
    def press_mouse(self, event):
        self.widget_press = event.widget                         # -1   
        #self.widget_press .config(bg='#bdfe04', fg='black')      # -2
            
        # 1-  Atrapa al boton clickeado [ Nombre ]
        # 2-  Cambia el background y foreground del boton clikeado a VERDE y NEGRO
        
        if self.container2 is not None:
            if self.container2 .cget('text') in self.mobiles2:
                self.container2 .config (bg='#11161d', fg='yellow')         # Cambia el color del boton: (bg y fg) que tenian por defecto
            else:
                self.container2 .config (bg='#11161d', fg='white')  

    # TAREA:
    #   1- Atrapa al widget sobre el que se solto el clic izquierdo
    def release_mouse(self, event):
        widget_release = event.widget.winfo_containing(event.x_root, event.y_root)      # -1
        
        """ if widget_release != self.widget_press:                                         # -2
            if self.widget_press .cget('text') in self.mobiles2:                           # -2.1
                self.widget_press .config (bg='#11161d', fg='yellow')                         # -2.2.1
            else:                                                                          # -2.2
                self.widget_press .config (bg='#11161d', fg='white') """                          # -2.2.1


        
        #print('releasee:::___:::  ',self.master._mobil)
        self.after(100, lambda :self.mobile(1))

        # 1-  Atrapa al widget sobre el que se solto el clic izquierdo [ Nombre ]
        # 2-  Si widget sobre el que se solto el clic, es diferente al boton clikeado:
            # 2.1-  Si el boton clikeado tiene de texto algunas de las cadenas de la lista, self.mobiles2:
                # 2.1.1-  Cambia el background y foreground del boton clikeado a AZULINO y AMARILLO
            # 2.2-  Entonces:
                # 2.2.1-  Cambia el background y foreground del boton clikeado a AZULINO y BLANCO

    # TAREA:
    #   1- SIN DEFINIR
    def mobile (self, number):
        
        for btn in (self.buttons22):
            if self.master._mobil == btn.cget('text'):
                #print('esss:', self.master._mobil)
                btn .config(bg='#bdfe04', fg='black')              # Color:  bg= #bdfe04  --> Verde
                self.container2 = btn
            else:
                #print('butonnnnn______',btn)
                if btn .cget('text') in self.mobiles2:
                    print('ifff', btn)
                    btn .config (bg='#11161d', fg='yellow')
                else:
                    print('else', btn)
                    btn .config (bg='#11161d', fg='white')
                #break
        #print(111)

