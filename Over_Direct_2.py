from tkinter import *
from tkinter import ttk

class Aplicacion(Frame):
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
       
        #__FRAME BARRA DE TITULO:aaaaaa
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

    def close(self):
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
            
            if self.ventana .winfo_y() <= 50 and self.ventana .winfo_y() > 0:
                 self.click = True
                 self.cambiar_tamano .config(image= self.imagen_maximizar)                                                           
                 self.ventana . geometry('%sx%s+%s+%s' %((self.x1 - self.x0), (self.y1 - self.y0), self.x0, self.y0))
                 self.ventana . geometry('+%s+%s' % (self.ventana .winfo_x() +
                      deltax, self.ventana .winfo_y() + deltay))
                 self.ventana .update()

    def pantalla_completa(self):
        self.ventana .geometry('{0}x{1}+0+0' .format(self.ventana .winfo_screenwidth(),
                               self.ventana .winfo_screenheight () - 30))
   
    def cambiar_dimencion(self):
        if self. click == True:
            self.cambiar_tamano .config(image= self.imagen_encogimiento)
            self.pantalla_completa()
            self.click = False
        else:
            self.cambiar_tamano .config(image= self.imagen_maximizar)
            self.ventana . geometry('%sx%s+%s+%s' %((self.x1 - self.x0), (self.y1 - self.y0), self.x0, self.y0))
            self.click = True

    def on_deiconify(self, event):
        self.ventana .deiconify()
        self.master .lower()

    def on_iconify(self, event):
        self.ventana .withdraw()
        self.master .iconify()

    def widgets(self):
        self.imagen_cerrar = PhotoImage(file= '11.png')
        self.imagen_maximizar = PhotoImage(file= '22.png') 
        self.imagen_minimizar = PhotoImage(file= 'mi.png')
        self.imagen_encogimiento = PhotoImage(file= 'ma2.png')

        self.cerrar = Button(self.frame_top, image=self.imagen_cerrar, bg='DarkOrchid1',
                             activebackground='DarkOrchid1', bd=0, command=self.close)
        self.cerrar .pack(ipadx=5,  padx=5, side='right')

        self.cambiar_tamano = Button(self.frame_top, image=self.imagen_maximizar, bg='DarkOrchid1',
                             activebackground='DarkOrchid1', bd=0, command=self.cambiar_dimencion)
        self.cambiar_tamano .pack(ipadx=5, padx=5, side='right')

        self.minimizar = Button(self.frame_top, image=self.imagen_minimizar, bg='DarkOrchid1',
                             activebackground='DarkOrchid1', bd=0, command= lambda: self.master .iconify())
        self.minimizar .pack(ipadx=5, padx=5, side='right')

        self.titulo = Label(self.frame_top, text='Aplicación de escritorio', bg='green2', fg='black',
                           font=('Calibri',12,'bold'))  
        self.titulo .pack(padx=10, side='left')
        self.titulo .bind ('<B1-Motion>', self.mover)
        self.titulo .bind ('<ButtonPress-1>', self.start)

        frame_1 = Frame (self.frame_principal, bg='spring green', width=00, height=200, highlightbackground ='gray25', highlightthickness=2)
        frame_1 .grid (padx=10, pady=10, columnspan=2, row=0, sticky='nsew')
        frame_2 = Frame (self.frame_principal, bg='spring green', width=00, height=200, highlightbackground='gray25', highlightthickness=2)
        frame_2 .grid (padx=10, pady=10, column=2, row=0, sticky='nsew')
        frame_3 = Frame (self.frame_principal, bg='magenta2', width=00, height=200, highlightbackground='gray25', highlightthickness=2)
        frame_3 .grid (padx=10, pady=10, column=0, row=1, sticky='nsew')
        frame_4 = Frame (self.frame_principal, bg='gold', width=00, height=200, highlightbackground='gray25', highlightthickness=2)
        frame_4 .grid (padx=10, pady=10, column=1, row=1, sticky='nsew')
        frame_5 = Frame (self.frame_principal, bg='tomato', width=00, height=200, highlightbackground='gray25', highlightthickness=2)
        frame_5 .grid (padx=10, pady=10, column=2, row=1, sticky='nsew')

if __name__=='__main__':
    root = Tk()
    root .title('Aplicación moderna')
    #icono
    root .wm_attributes("-alpha", 0.0 ) 
    root .config(bg='DarkOrchid1')
    app = Aplicacion (root)
    app .mainloop()




            








