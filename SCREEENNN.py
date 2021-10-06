




    def pantalla_completa(self):
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        tplvl_w = width * 20 / 100
        tplvl_h = height - 50
        
        
        self.ventana .geometry('{0}x{1}+0+0' .format(self.ventana .winfo_screenwidth(),
                     self.ventana .winfo_screenheight () - 30))
   
