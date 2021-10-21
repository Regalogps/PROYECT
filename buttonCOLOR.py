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
        
        for index, i in enumerate(self.buttons22):
            if self.master._mobil == i.cget('text'):
                print('esss:', self.master._mobil)
                i.config(bg='#bdfe04', fg='black')              # Color:  bg= #bdfe04  --> Verde
            else:
                if i .cget('text') in self.mobiles2:
                    i .config (bg='#11161d', fg='yellow')
                else:
                    i .config (bg='#11161d', fg='white')
                #break
        print(111)



