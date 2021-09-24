class Aplicacion(Frame)
    def __init__(self, master, *args)
        Frame.__init__(self, master, *args)
        self.x = 0
        self.y = 0
        self.x0 = 50
        self.y0 = 50
        self.x1 = 100
        self.y1 = 100
        self.click = TRUE
   
        self.ventana = Toplevel(self.master)
        self.ventana .overrideredirect(1)
        self.ventana .minsize(width=300, height=200)
        self.ventana .geometry('800x500+300+90')
       
        #__FRAME BARRA DE TITULO:
        self.Frame_top = Frame (self.ventana, bg='blue')
        self.Frame_top .grid_propagate(0)
        self.Frame_top .grid (column=0, row=0, 
        self.Frame_top
