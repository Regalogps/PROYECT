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

        self.grip = ttk.Sizegrip (self.frame_principal, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='se')
        self.grip .bind ('<B1-Motion>', self.redimencionar)
        ttk.Style().configure('TSizegrip', background='black')

        self.widgets()

    def redimencionar(self, event):
        self.x0 = self.ventana .winfo_rootx()
        self.y0 = self.ventana .winfo_rooty()
        self.x1 = self.ventana .winfo_pointerx()
        self.y1 = self.ventana .winfo_pointery()

        try:
        self.ventana . geometry('%sx%s' % ((self.x1 - self.x0),(self.y1 - self.y0)))
        except:
            pass

    def salir(self):
        self.ventana .destroy()
        self.ventana .quit()

    def start(self, event):
        self.x = event.x
        self.y = event.y

    def mover(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        if self.ventana .winfo_y() > 0:
            self.ventana . geometry('+%s+%s' % (self.ventana .winfo_x() +
                 deltax, self.ventana .winfo_y() + deltay))
            self.ventana .update()

        elif self.ventana .winfo_y() <= 1:
            self.ventana . geometry('+%s+%s' % (self.ventana .winfo_x() +
                 deltax, self.ventana .winfo_y() + deltay))
            self.ventana .update()

            self.pantalla_completa()
            self.cambiar_tamano .config(image= self.imagen_encogimiento)
            self.click = False
            
            if self.ventana .winfo_y() <= 50 and self.ventana .winfo_y() > 0::
                 self.click = TRUE
                 self.cambiar_tamano .config(image= self.imagen_maximizar)                                                           
                 self.ventana . geometry('%sx%s+%s+%s' %((self.x1 - self.x0), (self.y1 - self.y0), self.x0, self.y0))
                 self.ventana . geometry('+%s+%s' % (self.ventana .winfo_x() +
                      deltax, self.ventana .winfo_y() + deltay))
                 self.ventana .update()

    def pantalla_completa(self):
        self.ventana .geometry(
            








