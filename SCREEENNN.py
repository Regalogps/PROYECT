




    def pantalla_completa(self):
        screen_x = self.master.winfo_screenwidth()
        screen_y = self.master.winfo_screenheight()

        width_1 = screen_x * 20 / 100   # Ancho de la ventana
        height_1 = screen_y - 50        # Alto de la ventana
        pos_x1 = 0                      # Posición en eje x
        pos_y1 = 20                     # Posición en eje y
        
        pos_x2 = width_1 * 4

        width_2 = screen_x *
        height_2 = screen_y 
        
        window_izq = ('{}x{}+{}+{}'.format(width_1, heigth_1, pos_x1, pos_y1))
        window_der = ('{}x{}+{}+{}'.format(width_1, height_1, pos_x2, pos_y1))
        window_stuf = ('{}x{}+{}+{}'.format(width_1, height_1, pos_x2, pos_y1))
        
        self.ventana .geometry('{0}x{1}+0+0' .format(self.ventana .winfo_screenwidth(),
                     self.ventana .winfo_screenheight () - 30))
   
        new_pos = "+{}+{}".format(self.winfo_x() + deltax, self.winfo_y() + deltay)
