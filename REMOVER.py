   def remover_frame(self):  # Metodo para Remover Frame ----------------------------NO TOCAR

        if self.frame_plomo.winfo_ismapped():      
            self.frame_plomo.grid_remove()   
        else:
            self.frame_plomo.grid()  

        global is_on
        '''
        if is_on:
            self.img_ash . config (image = Imagenes[107])  
            is_on = False

        else:
            self.img_ash . config (image = Imagenes[109]) 
            is_on = True
        '''

