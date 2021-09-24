class Aplicacion(Frame)
    def __init__(self, master, *args):
        Frame.__init__(self, master, *args)
        self.x = 0
        self.y = 0
        self.x0 = 50
        self.y0 = 50
        self.x1 = 100
        self.y1 = 100
        self.click = True
   
        self.ventana = Toplevel(self.master)
        self.ventana .overrideredirect(1)
        self.ventana .minsize(width=300, height=200)
        self.ventana .geometry('800x500+300+90')
       
        #__FRAME BARRA DE TITULO:
        self.frame_top = Frame (self.ventana, bg='blue', height=60)
        self.frame_top .grid_propagate(0)
        self.frame_top .grid (column=0, row=0, sticky='nsew')

        #__FRAME DEL CONTENIDO:
        self.frame_principal = Frame (self.ventana, bg='black')
        self.frame_principal .grid (column=0, row=1, sticky='nsew')

        self.ventana .columnconfigure(0, weight=1)
        self.ventana .rowconfigure(1, weight=1)

        self.frame_principal .columnconfigure(0, weight=1)
        self.frame_principal .columnconfigure(1, weight=1)
        self.frame_principal .columnconfigure(2, weight=1)
        self.frame_principal .rowconfigure(0, weight=1)
        self.frame_principal .rowconfigure(1, weight=1)

        self.frame_top .bind ('<ButtonPress-1>', self.start)
        self.frame_top .bind ('<B1-Motion>', self.mover)
        self.master .bind ('<Map>', self.on_deiconify)
        self.master .bind ('<Unmap>', self.on_iconify)








