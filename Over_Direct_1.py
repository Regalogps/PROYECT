from tkinter import *
from tkinter import ttk

class Aplicacion(Frame):
    def __init__(self, master, *args):
        Frame.__init__(self, master, *args)
        self.x = 0
        self.y = 0
        
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

        self.frame_top .bind ('<ButtonPress-1>', self.start)
        self.frame_top .bind ('<B1-Motion>', self.mover)
        self.master .bind ('<Map>', self.on_deiconify)
        self.master .bind ('<Unmap>', self.on_iconify)                       

        self.grip = ttk.Sizegrip (self.frame_principal, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='se')
        ttk.Style().configure('TSizegrip', background='black')

        self.widgets()



    def close(self):
        self.ventana .destroy()
        self.ventana .quit()

    def start(self, event):
        self.x = event.x
        self.y = event.y

    def mover(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        new_pos = "+{}+{}".format(self.ventana.winfo_x() + deltax, self.ventana.winfo_y() + deltay)

        self.ventana.geometry(new_pos)
        #self.master.geometry(new_pos)
   
    def on_deiconify(self, event):
        self.ventana .deiconify()
        self.master .lower()

    def on_iconify(self, event):
        self.ventana .withdraw()
        self.master .iconify()

    def widgets(self):
        self.imagen_cerrar = PhotoImage(file= '11.png')
        self.imagen_maximizar = PhotoImage(file= '22.png') 
        self.imagen_minimizar = PhotoImage(file= '33.png')

        self.cerrar = Button(self.frame_top, image=self.imagen_cerrar, bg='DarkOrchid1',
                             activebackground='DarkOrchid1', bd=0, command=self.close)
        self.cerrar .pack(ipadx=5,  padx=5, side='right')

        self.minimizar = Button(self.frame_top, image=self.imagen_minimizar, bg='DarkOrchid1',
                             activebackground='DarkOrchid1', bd=0, command= lambda: self.master .iconify())
        self.minimizar .pack(ipadx=5, padx=5, side='right')

        self.titulo = Label(self.frame_top, text='Aplicación de escritorio', bg='green2', fg='black',
                           font=('Calibri',12,'bold'))  
        self.titulo .pack(padx=10, side='left')
        self.titulo .bind ('<B1-Motion>', self.mover)
        self.titulo .bind ('<ButtonPress-1>', self.start)


if __name__=='__main__':
    root = Tk()
    root .title('Aplicación moderna')
    #icono
    root .wm_attributes("-alpha", 0.0 ) 
    root .config(bg='DarkOrchid1')
    app = Aplicacion (root)
    app .mainloop()




            








