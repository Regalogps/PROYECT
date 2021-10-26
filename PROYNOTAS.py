#___< B U T T O N - 1 >
    def open_text_flecha(self, event): 

        # Convierte el tamaño total de la ventana en porcentaje:  100 %
        self.porcentage_total_x = event.x / self.master.winfo_width() * 100              # ---> winfo_width() : Devuelve el ancho actual del widget(Toplevel) en pixeles
        self.porcentage_total_y = event.y / self.master.winfo_height() * 100             # ---> event.x/y     : Devuelve la posicion del mouse en pixeles (click/movimiento)
        x1, x2 = 0, 100
        y1, y2 = 67, 100  
      
        if x1 <(self.porcentage_total_x)< x2  and  y1 <(self.porcentage_total_y)< y2: 

            if not self._open1 == True:                                               # ---> Si self.test es Falso:   ---> Predeterminado: False
                self._open1 = True
                self.motion.set('of')

                self.frame_image_base_77 .grid(column=0, row=0)                      # Posiciona                  # == {} (no mapeado)  
                self.lbl_text_flecha     .grid(column=0, row=0, ipadx=5, sticky=SE) # VER SI ACEPTA VARIABLES

                self.lbl_text_mostrar_77 .grid_forget()

                #print('se cambio de --ON-- a --OF-- ')              
            else:
                #print('se cambio de --OF-- a --ON-- ')
                self._open1 = False

                self.frame_image_base_77 .grid_forget()
                self.after(0, lambda e = self.motion: self.motion.set('on'))  ## analizae

                self.lbl_text_mostrar_77 .grid (column=0, row=0, ipadx=5, ipady=5, sticky=N,)
                
                self.lbl_text_flecha.grid_forget()


    #_______M E T O D O   < M O T I O N >
    def motion(self, event):      
 
        self.pointer_width_2 = event.x / self.master.winfo_width() * 100
        self.pointer_height_2 = event.y / self.master.winfo_height() * 100
        x1, x2 = 0, 100
        y1, y2 = 67, 100
        
        if self.motion.get()=='on':    
            if x1 < (self.pointer_width_2) < x2  and  y1 < (self.pointer_height_2) < y2:        
                self.lbl_text_mostrar_77 .grid (column=0, row=0, ipadx=5, ipady=5, sticky=N,)
                #print(self.pointer_width_2)

            else:
                self.lbl_text_mostrar_77 .grid_forget()
                #print('entre ala sala motion')

        if self.frame_image_base_77 . grid_info() != {}:
            self.lbl_text_mostrar_77 .grid_forget() 