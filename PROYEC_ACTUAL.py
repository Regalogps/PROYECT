from tkinter import Tk, ttk, Toplevel, PhotoImage, Frame, Label, Button, Spinbox, Listbox, Checkbutton, StringVar, IntVar, BooleanVar
from tkinter import SINGLE, ANCHOR, END, S,N,E,W, RIGHT, BOTTOM, BOTH, SE, TOP, LEFT
from tkinter.constants import NSEW
from PIL import ImageTk, Image
import cv2
import imutils
import numpy as np
import os 
#import sys

class Interface(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        """ path = 'E:/1-RICHI/MovilesDB'
        #____Coleccion de imagenes:
        self.Images_1 = self.generate_list (path, 'I') """
        #____Variables de control para las ventanas:  [ 1,2,3 ]
        self._frame_1 = None
        self._frame_2 = None
        self._frame_3 = None

        self._open_1 = False  
        self._open_2 = False 
        self._open_3 = False

        #____Variables de control secundarias:
        self._gear = True
        self._minimize = True
        
        #_____Métodos de Configuración y Posicionamiento de Widget: [Interface]
        #geo = self.geometry_(816, 65)   #NEW
        self. configure_interface()     # NEW EL ARGUMENTO geo     
        self. widgets()


    def configure_interface(self):   # CONFIGURA VENTANA PRINCIPAL
      
        #ventana.overrideredirect(1)
        #ventana.attributes("-toolwindow",-1)
        self.master.title ('_AshmanBot_')                                 #  BORRAR
        self.master.geometry ('830x65')                                 # TAMANIO DE LA VENTANA  ('816x65')   ---self.master.geometry (geometry)  
        self.master.resizable (1,1)                                       # OTORGA PERMISO PARA CAMBIAR DE TAMANIO ALA VENTANA
        self.master.config (bg='magenta2')                                # CONFIGURA EL FONDO DE LA VENTANA, etc
        self.master.attributes ('-topmost', True)                         # SUPERPONE LA VENTANA A OTRAS APLICACIONES ABIERTAS
        self.master.wm_attributes ('-transparentcolor', 'magenta2')       # BORRA EL COLOR SELECCIONADO DE LA VENTANA
        #root.attributes("-alpha", 0.5 ) 
        #self.eval('tk::PlaceWindow . center')    ######%%%%%%%%%%%%%%%%%%%%%%%%%

    def generate_list(self, file, option):   # INICIALIZA IMAGENES

        ouput = os.listdir (file)
        empty = []                    
        if option == 'I': 
            _lst = [[] for x in range(22)]
            _str = ['Fro','Fox','Boo','Ice','JD','Gru','Lig','Adu','Kni','Kal','Mag','Ran','Jol','Tur','Arm','Asa','Rao','Tri','Nak','Big','Dr1','Dr2']
            for i in ouput:               
                for index,iter in enumerate(_str):
                    if iter in i: 
                        full = file + '/' + i
                        open = cv2.imread (full)
                        RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB) 
                        _lst[index].append(RGB)               
            return _lst        
       
    def widgets(self):

        #____I N S T A N C I A S:  [ 4 ]
        self.frame_controller = A1_class (self, bg='#11161d', width=60, height=65)  # POSICIONADO       # Color: Azul         --- Frame contenedor de ash y gear
        self.frame_botones = B1_class (self, bg='#31343a', width=756, height=65)    # POSICIONADO       # Color: Plomo        --- Frame contenedor de botones
        self.frame_config = B2_class (self, bg='#31343a', width=756, height=65)     # NO POSICIONADO    # Color: Plomo        --- Frame contenedor de checkbuttons y labels
        self.frame_listmode = B3_class (self)                                       # NO POSICIONADO    # Color: Azul y Plomo --- Frame Contenedor de Spinbox y Listbox
         
        #____G R I D ():
        #self.frame_controller .grid (column= 0, row= 0, padx=(0,0), pady=(0,0))
       # self.frame_botones .grid (column= 1, row= 0, padx=0, pady=0, sticky='n')

        self.frame_controller .pack (side=LEFT, fill=BOTH)
        self.frame_botones .pack (side=LEFT, fill=BOTH) 

        #____G R I D___P R O P A G A T E ():
        self.frame_controller .pack_propagate (False)
        self.frame_botones .pack_propagate (False)
        #self.frame_config .pack_propagate (False)

    def gear_stacking(self):   # ACTIVA: CON CLICK IZQUIERDO EN LA RUEDA DE CONFIGURACION - QUITA Y PONE WIDGET, REDIMENSIONA LA VENTANA PRINCIPAL,ETC

        if  self._gear == True:                                    # PREDETERMINADO: TRUE
            #self.frame_botones .grid_remove()                      # BOTONES
            self.frame_botones .pack_forget()
            #self.frame_listmode .grid_remove()                     # MODO LISTA
            self.frame_listmode .pack_forget()

            self.frame_config .focus_set()                         # MODO CONFIGURACION
            #self.frame_config .grid (column=1, row=0, padx=0, pady=0, sticky=N) # creo borar stiky    ----------
            self.frame_config .pack (side=LEFT, fill=BOTH, expand=True)
            
            self._gear = False
            #self.master.geometry ('830x65')
   
        else:
            #self.frame_config .grid_remove()
            self.frame_config .pack_forget()

            self._gear = True 
            if self.frame_config .ckbutton5.variable.get() == True:   
                #self.frame_listmode .grid (column=1, row=0, padx=0, pady=0)  #-+-----------
                self.frame_listmode .pack (side=LEFT, fill=BOTH)
                self.frame_listmode .spinboxx.focus_set()
                #self.master.geometry ('250x65')
            else:
                #self.frame_botones .grid()
                self.frame_botones .pack (side=LEFT, fill=BOTH) 
                #self.frame_listmode .grid_remove()
                self.frame_listmode .forget()

   

############   G E S T I O N   DE  V E N T A N A S   S U P E R I O R E S  

    def windows_123 (self, var_1, var_2, var_3):
        
        #___V E N T A N A__°1:
        if self._open_1 == False: 
            #self.toplevel_LEFT = Toplevel()
            self.toplevel_LEFT = Toplevel_class (self, type='W')  #############################################################   VENTANA TOPLEVEL IZQUIERDA
            self.toplevel_LEFT .configure_toplevel ('220x690') #  metodo  ('izq', '220x690')

        self._open_1 = True     
                                
        container_frame_left = var_1 (self.toplevel_LEFT)  #  var_1 es un frame

        if self._frame_1 is not None:  
            self._frame_1 .destroy()
        self._frame_1 = container_frame_left
        self._frame_1 .pack()

        self.grip = ttk.Sizegrip(self._frame_1, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='center')
        ttk.Style().configure('TSizegrip', bg='black')
              
        #self.toplevel_LEFT .protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(1))
            

        #___V E N T A N A__°2:
        if self._open_2 == False:
            #self.toplevel_RIGHT = Toplevel()
            self.toplevel_RIGHT = Toplevel_class (self, type='W')  #############################################################   VENTANA TOPLEVEL DERECHA
            self.toplevel_RIGHT .configure_toplevel ('220x690')  # ('der', '220x690')

        self._open_2 = True

        container_frame_right = var_2 (self.toplevel_RIGHT)  # ES UN FRAME POSICIONADO EN TOPLEVEL

        if self._frame_2 is not None:
            self._frame_2 .destroy()
        self._frame_2 = container_frame_right
        self._frame_2 .pack()


        self.grip = ttk.Sizegrip(self._frame_2, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='center')
        ttk.Style().configure('TSizegrip', bg='black')

        #self.toplevel_RIGHT.protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(2))

        #_______ desde aqui falta completar este if
        #___V E N T A N A__°3:
        if self._open_3 == False:
            #self.toplevel_STUF = Toplevel()
            self.toplevel_STUF = Toplevel_class (self, type='W')  #############################################################   VENTANA TOPLEVEL STUFF
            self.toplevel_STUF .configure_toplevel ('620x190')     # ('stuf', '620x190')  

        self._open_3 = True

        container_frame_stuf = var_3 (self.toplevel_STUF)  # ES UN FRAME POSICIONADO EN TOPLEVEL

        if self._frame_3 is not None:
            self._frame_3 .destroy()
        self._frame_3 = container_frame_stuf
        self._frame_3 .pack()


        """ self.grip = ttk.Sizegrip(self._frame_3, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='center')
        ttk.Style().configure('TSizegrip', bg='black') """  # NO TIENE FRAME O IMAGEN TODAVIA

        #self.toplevel_STUF.protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(3))
        self.toplevel_LEFT .mainloop()

    def close_windows(self, number):

        if number == 1:
            self.toplevel_LEFT. destroy()
            self._open_1 = False

        if number == 2:
            self.toplevel_RIGHT. destroy()
            self._open_2 = False

        if number == 3:
            self.toplevel_STUF. destroy()
            self._open_3 = False


################################
class A1_class(Frame):   # Frame contenedor de ash y gear
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        path = 'E:/1-RICHI/MovilesDB'
        #_____Coleccion de Imágenes         
        self.Sublist= self.generate_list(path, 'S') 
        #_____C O N T E N E D O R E S:  [ 0 ]

        self.ash_controller()
        self.gear_controller()
        
    def ash_controller(self):  # IMAGE
        self.btn_ash = Button (self, image=self.Sublist[0], bg='#11161d', bd=0, activebackground='#11161d' , command=self.ash_minimize_windows)
        self.btn_ash .grid (column=0, row=0, padx=(6,6), pady=0)
        self.btn_ash .bind ('<Double-3>', self.ash_close_windows)
          
    def gear_controller(self):  # IMAGE
        self.btn_gear = Button (self, image=self.Sublist[1], bg='#11161d', bd=0, activebackground='#11161d', command=self.master.gear_stacking) 
        self.btn_gear .grid (column=0, row=1)
        #self.btn_gear .bind ('<Double-3>', self.master.otros)

    def ash_close_windows(self, event):   # ACTIVA: CON DOBLE CLICK DERECHO EN EL LOGO - CIERRA LAS VENTANAS 
    
        try:
            self.master.toplevel_LEFT .destroy() 
            self.master._open_1 = False

            self.master.toplevel_RIGHT .destroy()
            self.master._open_2 = False

            self.master.toplevel_STUF .destroy()
            self.master._open_3 = False
        except:
            pass

    def ash_minimize_windows(self):   # ACTIVA: CON CLICK IZQUIERDO AL LOGO - MINIMIZA LAS VENTANAS

        if self.master._open_1 == True or self.master._open_2 == True or self.master._open_3 == True:

            if self.master._minimize == False:
                if self.master._open_1 == True:
                    self.master.toplevel_LEFT .deiconify()   # MOSTRAR VENTANAS  
                if self.master._open_2 == True:
                    self.master.toplevel_RIGHT .deiconify()
                if self.master._open_3 == True:
                    self.master.toplevel_STUF .deiconify()

                self.master._minimize = True

            else: 
                if self.master._open_1 == True:
                    self.master.toplevel_LEFT .iconify()     # OCULTAR VENTANAS
                if self.master._open_2 == True:
                    self.master.toplevel_RIGHT .iconify() 
                if self.master._open_3 == True:    
                    self.master.toplevel_STUF .iconify()

                self.master._minimize = False

    def generate_list(self, file, option):   # INICIALIZA IMAGENES

        ouput = os.listdir(file)
        empty = []              
        if option == 'S':
            for i in ouput: 
                if 'SubList' in i :      
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    array = Image.fromarray (RGB)
                    img = ImageTk.PhotoImage (array)
                    empty. append (img)
            return empty

################################
class B1_class(Frame):   # Frame contenedor de botones
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        #_____C O N T E N E D O R E S:  [ 1 ]
        self.frame_1 = Frame (self, bg='#11161d')          # Color: Azul
        self.frame_1 .grid (padx=(10,10), pady=(6,6))

        self.mobile_button()

    def mobile_button(self):   # Metodo que crea -22- Botones (moviles)  #command = lambda:images(1))
        
        self.Frog_1 = Button (self.frame_1, text='Frog', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Frog_left_off, Frog_right, Frog_stuf)) 
        self.Fox_2 = Button (self.frame_1, text='Fox', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.windows_123 (Fox_left_off, Fox_right, Fox_stuf))         
        self.Boomer_3 = Button (self.frame_1, text='Boomer', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Boomer_left_off, Boomer_right, Boomer_stuf))             
        self.Ice_4 = Button (self.frame_1, text='Ice', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Ice_left_off, Ice_right, Ice_stuf))
        self.JD_5 = Button (self.frame_1, text='J.D', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Jd_left_off, Jd_right, Jd_stuf))
        self.Grub_6 = Button (self.frame_1, text='Grub', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Grub_left_off, Grub_right, Grub_stuf))   
        self.Lightning_7 = Button (self.frame_1, text='Lightning', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width=10, bd=0, command= lambda: self.master.windows_123 (Lightning_left_off, Lightning_right, Lightning_stuf))       
        self.Aduka_8 = Button (self.frame_1, text='Aduka', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Aduka_left_off, Aduka_right, Aduka_stuf))      
        self.Knight_9 = Button (self.frame_1, text='Knight', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.windows_123 (Knight_left_off, Knight_right, Knight_stuf))     
        self.Kalsiddon_10 = Button (self.frame_1, text='Kalsiddon', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Kalsiddon_left_off, Kalsiddon_right, Kalsiddon_stuf))
        self.Mage_11 = Button (self.frame_1, text='Mage', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Mage_left_off, Mage_right, Mage_stuf))     

        self.Randomizer_12 = Button (self.frame_1, text='Randomizer', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Randomizer_left_off, Randomizer_right, Randomizer_stuf)) 
        self.Jolteon_13 = Button (self.frame_1, text='Jolteon', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.windows_123 (Jolteon_left_off, Jolteon_right, Jolteon_stuf)) 
        self.Turtle_14 = Button (self.frame_1, text='Turtle', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Turtle_left_off, Turtle_right, Turtle_stuf))
        self.Armor_15 = Button (self.frame_1, text='Armor', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Armor_left_off, Armor_right, Armor_stuf))
        self.Asate_16 = Button (self.frame_1, text='A.Sate', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Asate_left_off, Asate_right, Asate_stuf))
        self.Raon_17 = Button (self.frame_1, text='Raon', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Raon_left_off, Raon_right, Raon_stuf)) 
        self.Trico_18 = Button (self.frame_1, text='Trico', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Trico_left_off, Trico_right, Trico_stuf))
        self.Nak_19 = Button (self.frame_1, text='Nak', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Nak_left_off, Nak_right, Nak_stuf)) 
        self.Bigfoot_20 = Button (self.frame_1, text='Bigfoot', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Bigfoot_left_off, Bigfoot_right, Bigfoot_stuf)) 
        self.Barney_21 = Button (self.frame_1, text='Barney', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.windows_123 (Barney_left_off, Barney_right, Barney_stuf)) 
        self.Dragon_22 = Button (self.frame_1, text='Dragon', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.windows_123 (Dragon_left_off, Dragon_right, Dragon_stuf))
                
        self.Frog_1 .grid (column= 1, row= 1, pady= 3, padx= (5,0))
        self.Fox_2 .grid (column= 2, row= 1, pady= 3, padx= (0,0))       
        self.Boomer_3 .grid (column= 3, row= 1, pady= 3, padx= (0,0))           
        self.Ice_4 .grid (column= 4, row= 1, pady= 3, padx= (0,0))
        self.JD_5 .grid (column= 5, row= 1, pady= 3, padx= (0,0))
        self.Grub_6 .grid (column= 6, row= 1, pady= 3, padx= (0,0))
        self.Lightning_7 .grid (column= 7, row= 1, pady= 3, padx= (0,0))
        self.Aduka_8 .grid (column= 8, row= 1, pady= 3, padx= (0,0))
        self.Knight_9 .grid (column= 9, row= 1, pady= 3, padx= (0,0))
        self.Kalsiddon_10 .grid (column= 10, row= 1, pady= 3, padx= (0,0))
        self.Mage_11 .grid (column= 11, row= 1, pady= 3, padx= (0,5))

        self.Randomizer_12 .grid (column= 1, row= 2, pady= 2, padx= (5,0))
        self.Jolteon_13 .grid (column= 2, row= 2, pady= 2, padx= (0,0))
        self.Turtle_14 .grid (column= 3, row= 2, pady= 2, padx= (0,0))
        self.Armor_15 .grid (column= 4, row= 2, pady= 2, padx= (0,0))
        self.Asate_16 .grid (column= 5, row= 2, pady= 2, padx= (0,0))
        self.Raon_17 .grid (column= 6, row= 2, pady= 2, padx= (0,0))
        self.Trico_18 .grid (column= 7, row= 2, pady= 2, padx= (0,0))
        self.Nak_19 .grid (column= 8, row= 2, pady= 2, padx= (0,0))
        self.Bigfoot_20 .grid (column= 9, row= 2, pady= 2, padx= (0,0))
        self.Barney_21 .grid (column= 10, row= 2, pady= 2, padx= (0,0))
        self.Dragon_22 .grid (column= 11, row= 2, pady= 2, padx= (0,5))

################################
class B2_class(Frame):   # Frame contenedor de checkbuttons y labels
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, kwargs)

        #_____C O N T E N E D O R E S:  [ 0 ]
 
        self.create_label()
        self.create_checkbutton()

    def cheeck(self): # ES UN EVENTP QUE ´PASA CUANDO CHECKBUTON 5 CAMBIOA DE VALOR 
        pass
        """ if self.variable.get() == False:
            self.variable.set(True)
        if self.variable.get() == True:
            self.variable.set(False)
        """

    def create_label(self):

        label_option1 = Label (self, text= 'Activar Aimbot :' , font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option2 = Label (self, text= 'Activar aimbot :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option3 = Label (self, text= 'Activar ddd ', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option4 = Label (self, text= 'Activar Modo On :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option5 = Label (self, text= 'Activar Modo Lista :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option6 = Label (self, text= 'Activar Modo Guía :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option7 = Label (self, text= 'Recordar Configuracion :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)

        label_option1 .grid (column=0, row=0, padx= (30,10), pady=(10,0), sticky=W)
        label_option2 .grid (column=0, row=1, padx= (30,10), pady=(0,0), sticky=W)
        label_option3 .grid (column=2, row=0, padx= (30,10), pady=(10,0), sticky=W)
        label_option4 .grid (column=2, row=1, padx= (30,10), pady=(0,0), sticky=W)
        label_option5 .grid (column=4, row=0, padx= (30,10), pady=(10,0), sticky=W)
        label_option6 .grid (column=4, row=1, padx= (30,10), pady=(0,0), sticky=W)   
        label_option7 .grid (column=6, row=0, padx= (30,10), pady=(10,0), sticky=W)
    
    def create_checkbutton(self):

        self.ckbutton1 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton2 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton3 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton4 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton5 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton6 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton7 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
    
        self.ckbutton1 .grid (column=1, row=0, pady=(10,0))
        self.ckbutton2 .grid (column=1, row=1, pady=(0,0))
        self.ckbutton3 .grid (column=3, row=0, pady=(10,0))
        self.ckbutton4 .grid (column=3, row=1, pady=(0,0))
        self.ckbutton5 .grid (column=5, row=0, pady=(10,0))
        self.ckbutton6 .grid (column=5, row=1, pady=(0,0))
        self.ckbutton7 .grid (column=7, row=0, padx=(0,200), pady=(10,0),)

################################          
class B3_class(Frame):   # Frame Contenedor de Spinbox y Listbox
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, kwargs)

        path = 'E:/1-RICHI/MovilesDB'
        #_____Coleccion de imagenes         
        self.Miniatures= self.generate_list(path, 'M')

        #_____C O N T E N E D O R E S___2:
        self.frame_1 = Frame (self, bg='#31343a', width=116, height=65)    # Color: Plomo       
        self.frame_2 = Frame (self, bg='#11161d', width=60, height=65)     # Color: Azul  

        self.container_2w = Frame (self.frame_1, width=116, height=20, bg='#11161d') 
        self.select_mobil = Label (self.frame_1, text='Seleccione  Mobil :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        self.miniature_mobil = Label (self.frame_2, image=self.Miniatures[0], bd= 0) 

        self.create_listbox (width=11, height=1)
        self.create_spinbox (width=13)

        #_____G R I D ():
        self.frame_1 .grid (column=0, row=0)                                     # MASTER A
        self.frame_2 .grid (column=1, row=0)                                     # MASTER B

        self.container_2w .grid (column=0, row=0, padx=0, pady=(0,2), sticky=N)  # SUB A.1
        self.select_mobil .grid (column=0, row=1, padx=11, pady=0)               # SUB A.2
        self.spinboxx .grid (column=0, row=2, padx=13, pady=(3,3))               # SUB A.3

        self.red_green .grid (column=0, row=0, padx=0, pady=0)                   # SUB.SUB A.1 .1 
        self.listboxx .grid (column=1, row=0, padx=12, pady=(1,0))               # SUB.SUB A.1 .2

        self.miniature_mobil .grid (padx=2, pady=3)                              # SUB B.1

        #_____G R I D___P R O P A G A T E ():
        self.frame_1 .grid_propagate(False)
        self.frame_2 .grid_propagate(False)
        self.container_2w .grid_propagate(False)
        
        #_____Variables de control:
        self._change = None
   

    def change_variable(self, *args):  # ACTIVA: SI SPINBOX_VARIABLE CAMBIA DE VALOR - BORRA LA LISTA DE LISTBOX, MANDA A LLAMAR A UPDATE Y CAMBIA LAS MINIATURAS

        spin = self.spinboxx.get().capitalize()

        if spin == '':                                                          # 1- SI SPINBOX ESTA VACIO.  2- BORRA LA LISTA DE LISTBOX.  3- DESHABILITA LISTBOX.
            self.listboxx .delete(0, END)
        else:                                                                      # 1- HABILITA LISTBOX.  2- CREA LISTA VACIA.  3- ITERANDO: 'self.spinbox_values'.
            list_new = []                                                          # 4- SI COINCIDE 'value' EN 'self.spinbox_values'.  5- AGREGA VALUE A LISTA.  6- SI LA LISTA NO ESTA VACIA.
            for index, i in enumerate(self.spinbox_values):                        # 10- LLAMA AL METODO: 'def update' Y PASA LA LISTA DE ARGUMENTO.
                if spin == i:                           
                    self.miniature_mobil .config(image= self.Miniatures[index])
                    self.spinboxx .icursor(END)
                if spin in i:
                    list_new .append(i)

            if list_new != []:         
                self.update(list_new)

            if spin == 'As':  
                self.listboxx.delete(0,1)

        if self.listboxx.get(0) != spin and self.listboxx.get(0) != '' or spin == '': 
            self.miniature_mobil .config(image= self.Miniatures[22])
        
    def update(self, list):  # ACTIVA: ** SI ES LLAMADO POR CHANGE_VARIABLE ** - BORRA LA LISTA DE LISTBOX EXISTENTE, AGREGA NUEVOS VALORES A LISTA Y BORRA DE NUEVO SI SE CUMPLE LA CONDICION
    
        self.listboxx .delete(0, END)                                    # 1- BORRA LA LISTA DE LISTBOX
        for i in list:                                                  # 1- ITERANDO: 'list_new'.  2- INSERTANDO ITERADOR 'i' A LISTBOX.  
            self.listboxx .insert(END, i)
        if self.listboxx.get(0) == self.spinbox_variable.get():
            self.listboxx .delete(0, END) 


    def listbox_select(self,event):  # ACTIVA: CON CLICK IZQUIERDO EN LISTBOX - 
       
        selection = self.listboxx .get(ANCHOR)                                                           # 1- BORRA EL CONTENIDO DE SPINBOX.  2- INSERTA EL ITEM SELECCIONADO DEL LISTBOX A SPINBOX                         
        
        if self.listboxx.get(0,END) != ():      
            self.spinboxx .delete(0, END) 
        self.spinboxx .insert(0, selection)
        self.listboxx .selection_clear(0,END)
 
        self.after(100, lambda: self.spinboxx.focus_set())

        #print('numero',self.listboxx.size())
          

    def listbox_enter(self, event):  # ACTIVA: CON TECLA ENTER - INSERTA EL VALOR DE LISTBOX A SPINBOX, MANDA LLAMAR A OPEN_WINDOWS  Y ABREN LAS VENTANAS
 
        listbx = self.listboxx.get(0)
        spinbx = self.spinboxx.get()

        if listbx != spinbx and listbx != '':
            self.spinboxx.delete(0, END)
            self.spinboxx.insert(0, listbx)
            
        self.open_windows(event) 
         
    def open_windows(self, event):  # ACTIVA: ** SI ES LLAMADO POR LISTBOX_SELECT ** - ABRE LAS VENTANAS
        
        left = [Frog_left_off, Fox_left_off, Boomer_left_off, Ice_left_off, Jd_left_off, Grub_left_off, Lightning_left_off, Aduka_left_off, Knight_left_off, Kalsiddon_left_off, Mage_left_off, Randomizer_left_off, Jolteon_left_off, Turtle_left_off, Armor_left_off, Asate_left_off, Raon_left_off, Trico_left_off, Nak_left_off, Bigfoot_left_off, Barney_left_off, Dragon_left_off,]
        right = [Frog_right, Fox_right, Boomer_right, Ice_right, Jd_right, Grub_right, Lightning_right, Aduka_right, Knight_right, Kalsiddon_right, Mage_right, Randomizer_right, Jolteon_right, Turtle_right, Armor_right, Asate_right, Raon_right, Trico_right, Nak_right, Bigfoot_right, Barney_right, Dragon_right]
        stuf = [Frog_stuf, Fox_stuf, Boomer_stuf, Ice_stuf, Jd_stuf, Grub_stuf, Lightning_stuf, Aduka_stuf, Knight_stuf, Kalsiddon_stuf, Mage_stuf, Randomizer_stuf, Jolteon_stuf, Turtle_stuf, Armor_stuf, Asate_stuf, Raon_stuf, Trico_stuf, Nak_stuf, Bigfoot_stuf, Barney_stuf, Dragon_stuf]

        for index, i in enumerate(self.spinbox_values):
            if self.spinboxx.get() == i:
                self.master.windows_123(left[index], right[index], stuf[index]) 
        
        if self._change is not None:
            self.after(10000, self.automatic_deletion) 

    def automatic_deletion(self):  # ACTIVA: ** SI ES LLAMADO POR OPEN_WINDOWS ** Y SI LA VARIABLE DE CONTROL NO ES NONE - LIMPIA SPINBOX

        self.spinboxx .delete(0, END)     


    def change_red_green(self, event):  # ACTIVA: CLICK IZQUIERDO EN RED_GREEN - CAMBIA IMAGEN ROJO-VERDE Y VICEVERSA

        if self._change is None:
            self.red_green .config (image=self.Miniatures[24])  
            self._change = True
        else:
            self.red_green .config (image=self.Miniatures[23])
            self._change = None

    def validate_text(self, text, arg): # SIEMPRE QUE INSERTE TEXTO EN SPINBOX - NO PERMITE NUMEROS,SIMBOLOS,ESPACIOS Y CONTROLA LA CANTIDAD

        if all (i not in "0123456789[{!¡¿?<>(|#$%&),_-°'´}] +-*/=" for i in text) and len(text) < 14:   
                return True                                                 
        return False  

    def create_spinbox(self, **args):
        
        self.spinboxx = Spinbox (self.frame_1, **args)
        
        self.spinbox_variable = StringVar()
        self.spinbox_values = ['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage', 'Randomizer', 'Jolteon', 'Turtle', 'Armor','A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']
        self.all_register = (self.register(self.validate_text), '%P', '%S')
        self.spinboxx.config (values=self.spinbox_values,
                             textvariable=self.spinbox_variable,
                             validate='key',
                             validatecommand=self.all_register,
                             justify='center',
                             wrap=True,
                             bd=0)

        self.spinboxx.icursor(END)

        self.spinboxx .bind ('<Double-1>', lambda *arg: self.spinboxx.delete(0, END))     # ACTIVA: CON DOBLE CLICK EN SPINBOX - LIMPIA SPINBOX
        self.spinboxx .bind ('<Return>', self.listbox_enter)                              # ACTIVA: CON TECLA ENTER - SELECCIONA EL INDICE 0 DEL LISTBOX  

        self.spinbox_variable .trace_add ('write', self.change_variable)  
        self.spinbox_variable .trace_add ('write', lambda *arg: self.spinbox_variable.set (self.spinbox_variable.get() .capitalize()))   # INSERTA EL VALOR OBTENIDO EN MAYUSCULA EL PRIMER STRING

    def create_listbox(self, **kwargs):
     
        self.red_green = Label (self.container_2w, image= self.Miniatures[23], width=11, bd=0) 

        self.listboxx = Listbox (self.container_2w, **kwargs)
        self.listboxx .config (font=('Calibri',9,'bold'),
                              bg='#11161d', fg='#00ff00',
                              borderwidth=0, bd=0,
                              highlightthickness=0,
                              highlightbackground='#11161d',  
                              highlightcolor='#11161d',  
                              selectbackground='#11161d', 
                              selectforeground='#ff8000',
                              activestyle='none',
                              justify='center',
                              selectmode=SINGLE,
                              takefocus=0)

        self.red_green .bind ("<Button-1>", self.change_red_green)
        self.listboxx .bind ('<<ListboxSelect>>', self.listbox_select)   # ACTIVA: CON CLICK IZQUIERDO EN EL LISTBOX - SELECCIONA 1 ITEM

    def generate_list (self, file, option):   # INICIALIZA IMAGENES

        ouput = os.listdir (file)
        empty = [] 
           
        if option == 'M':
            for i in ouput:  
                if 'Mini' in i :      
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    array = Image.fromarray (RGB)
                    img = ImageTk.PhotoImage (array)
                    empty. append (img)
            return empty

################################ 
class Checkbutton_class(Checkbutton):   
    def __init__(self, *args, **kwargs):
        Checkbutton.__init__(self, *args, **kwargs)

        self.variable = BooleanVar()
        self.configure(variable=self.variable)
    
    def checked(self):
        return self.variable.get()
    
    def check(self):
        self.variable.set(True)
    
    def uncheck(self):
        self.variable.set(False) 

    def value (self):
        if self.variable .get() == True: 
            pass  
   
################################

class Example(Frame):
    def __init__(self, master, index, *args, **kwargs):
        Frame.__init__(self, master, *args, kwargs)
        
        self.image = Image.fromarray (index)
        self.image_copy = self.image .copy()

        self.background = ImageTk.PhotoImage (self.image)

        self.img = Label (self, image= self.background)
        self.img .pack (fill= 'both', expand= True)
        self.img .bind ('<Configure>', self.resize)

    def resize(self, event):
        #self.xx, self.yy = self.
        
        self.image2 = self.image_copy .resize ((self.master .winfo_width(), self.master .winfo_height()))
        
        self.background2 = ImageTk.PhotoImage (self.image2)
        self.img .config (image= self.background2)
        #self.img .image = self.backgroundd



################################                           ################################
################################            EL             ################################ 
################################          INICIO           ################################ 
################################   F R A M E  " F R O G "  ################################  
################################                           ################################


class Frog_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [0] 

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [0][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [0][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

    
class Frog_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [0] 

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [0][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [0][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event):

        winfo_x, winfo_y = self.master.winfo_width(), self.master.winfo_height() 
        event_x, event_y = event.x, event.y
        h = event_x / winfo_x * 100 
        v = event_y / winfo_y * 100
    
        if int(h) >=0 and int(v) >=68 :  
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()
    

class Frog_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [0]
     pass

################################   F R A M E  " F O X "  ################################
################################   F R A M E  " F O X "  ################################


class Fox_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [1]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [1][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [1][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

 
class Fox_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [1]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [1][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [1][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        winfo_x, winfo_y = self.master.winfo_width(), self.master.winfo_height() 
        event_x, event_y = event.x, event.y
        h = event_x / winfo_x * 100 
        v = event_y / winfo_y * 100
    
        if int(h) >=0 and int(v) >=68 :  
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fox_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [1]
     pass

################################   F R A M E  " B O O M E R "  ################################
################################   F R A M E  " B O O M E R "  ################################ 





class Boomer_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [2]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs) 

        self.bind ('<Configure>', self.a)    # Ver si cambiar a self.master.bind
                
        self.fr_img_delay = Example (self, self.master.Images_1 [2][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [2][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)   #self.lbl_guia . place(x= 2, y= 48)  

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)


    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()
    
    def a(self, event):

        var_x = IntVar()  # Aqui lo puedo camvbiar a IntVar para que no  de un cero de mas 23.0 54.0 
        var_y = IntVar()
        width = self.master.winfo_width() / 35
        height = self.master.winfo_height() / 14
        w = int(width)
        h = int(height)
 
        var_x .set(w)    # aqui hay el 10% del ancho total
        getx = var_x .get()

        var_y .set(h)
        gety = var_y .get()       
        
        self.lbl_guia.place(x= getx, y= gety)
                
  
class Boomer_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [2]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.fr_img_base = Example (self, self.master.Images_1 [2][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [2][3], bd=0)  
 
        self.flecha = Label (self, text= '↑', font=('Calibri',30,'bold'), bg=  '#2f3337',fg='green2', width=1, height=1)
        self.alert_77 = Label (self, text= "Haga ' Click ' para mostrar:\nAngulo ' 77 '", font=('Bickham Script Pro',8  ,'bold'), bg=  '#2f3337',fg='white', width=50, height=2)
        
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)


        self.master.bind("<Button-1>", self.button1)      
        self.bind_motion = self.master.bind('<Motion>',self.motion)
        self.bind_leave = self.bind('<Leave>', lambda e: self.alert_77 .grid_forget())

        #______V A R I A B L E S  de  C O N T R O L  para los B I N D
        self.test = 'closed'
        self.motion = StringVar()
        self.motion.set('on')
        

    #_______M E T O D O   < B U T T O N - 1 >
    def button1(self, event): 

        self.pointer_width = event.x / self.master.winfo_width() * 100
        self.pointer_height = event.y / self.master.winfo_height() * 100
        x1, x2 = 0, 100
        y1, y2 = 68, 100  
                
        if x1 < (self.pointer_width) < x2  and  y1 < (self.pointer_height) < y2: 
            if self.test == 'closed':               
                self.fr_img_77 . grid(column=0, row=0)   # == {} (no mapeado)               
                self.test = 'open'
                self.motion.set('of')
                #print('se cambio de --ON-- a --OF-- ')
                
                self.flecha .grid(column=0, row=0, sticky=SE, ipadx=5) # VER SI ACEPTA VARIABLES
                
            else:
                self.fr_img_77 .grid_forget()
                self.test = 'closed'
                self.after(0, lambda e = self.motion: self.motion.set('on'))  ## analizae
                #print('se cambio de --OF-- a --ON-- ')
                
                self.flecha.grid_forget()


    #_______M E T O D O   < M O T I O N >
    def motion(self, event):      
 
        self.pointer_width_2 = event.x / self.master.winfo_width() * 100
        self.pointer_height_2 = event.y / self.master.winfo_height() * 100
        x1, x2 = 0, 100
        y1, y2 = 68, 100
        if self.motion.get()=='on':    
            if x1 < (self.pointer_width_2) < x2  and  y1 < (self.pointer_height_2) < y2:        
                self.alert_77 .grid (column=0, row=0, sticky=N, ipadx=5, ipady=5)
                #print(self.pointer_width_2)

            else:
                self.alert_77 .grid_forget() 
                #print('entre ala sala motion') 

        if self.fr_img_77 . grid_info() != {}:
            self.alert_77 .grid_forget() 

 
class Boomer_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [2]
     pass

################################  F R A M E  " I C E "  ################################
################################  F R A M E  " I C E "  ################################


class Ice_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [3]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [3][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [3][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Ice_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [3]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [3][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [3][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        winfo_x, winfo_y = self.master.winfo_width(), self.master.winfo_height() 
        event_x, event_y = event.x, event.y
        h = event_x / winfo_x * 100 
        v = event_y / winfo_y * 100
    
        if int(h) >=0 and int(v) >=68 :  
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Ice_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [3]
     pass

################################  F R A M E  " J D "  ################################
################################  F R A M E  " J D "  ################################


class Jd_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [4]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [4][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [4][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Jd_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [4]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [4][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [4][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        winfo_x, winfo_y = self.master.winfo_width(), self.master.winfo_height() 
        event_x, event_y = event.x, event.y
        h = event_x / winfo_x * 100 
        v = event_y / winfo_y * 100
    
        if int(h) >=0 and int(v) >=68 :  
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Jd_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [4]
     pass


################################  F R A M E  " G R U B "  ################################
################################  F R A M E  " G R U B "  ################################


class Grub_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [5]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [5][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [5][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Grub_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [5]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [5][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [5][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        winfo_x, winfo_y = self.master.winfo_width(), self.master.winfo_height() 
        event_x, event_y = event.x, event.y
        h = event_x / winfo_x * 100 
        v = event_y / winfo_y * 100
    
        if int(h) >=0 and int(v) >=68 :  
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Grub_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [5]
     pass


################################  F R A M E  " L I G H T "  ################################
################################  F R A M E  " L I G H T "  ################################


class Lightning_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [6]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [6][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [6][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Lightning_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [6]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [6][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [6][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Lightning_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [6]
     pass


################################  F R A M E  " A D U K A "  ################################
################################  F R A M E  " A D U K A "  ################################


class Aduka_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [7]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [7][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [7][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Aduka_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [7]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [7][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [7][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Aduka_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [7]
     pass


################################  F R A M E  " K N I G H T "  ################################
################################  F R A M E  " K N I G H T "  ################################


class Knight_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [8]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [8][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [8][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Knight_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [8]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [8][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [8][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Knight_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [8]
     pass


################################  F R A M E  " C A L Z I D D O N "  ################################
################################  F R A M E  " C A L Z I D D O N "  ################################


class Kalsiddon_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [9]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [9][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [9][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Kalsiddon_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [9]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [9][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [9][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Kalsiddon_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [9]
     pass


################################  F R A M E  " M A G E "  ################################
################################  F R A M E  " M A G E "  ################################


class Mage_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [10]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [10][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [10][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Mage_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [10]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [10][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [10][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Mage_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [10]
     pass


################################  F R A M E  " R A N D O M I Z E R "  ################################
################################  F R A M E  " R A N D O M I Z E R "  ################################


class Randomizer_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [11]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [11][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [11][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Randomizer_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [11]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [11][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [11][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Randomizer_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [11]
     pass


################################  F R A M E  " J O L T E O N "  ################################
################################  F R A M E  " J O L T E O N "  ################################


class Jolteon_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [12]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [12][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [12][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Jolteon_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [12]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [12][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [12][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Jolteon_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [12]
     pass


################################  F R A M E  " T U R T L E "  ################################
################################  F R A M E  " T U R T L E "  ################################

class Turtle_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [13]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [13][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [13][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Turtle_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [13]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [13][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [13][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Turtle_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [13]
     pass


################################  F R A M E  " A R M O R "  ################################
################################  F R A M E  " A R M O R "  ################################


class Armor_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [14]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [14][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [14][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Armor_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [14]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [14][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [14][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Armor_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [14]
     pass


################################  F R A M E  " A S A T E "  ################################
################################  F R A M E  " A S A T E "  ################################


class Asate_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [15]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [15][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [15][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Asate_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [15]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [15][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [15][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Asate_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [15]
     pass


################################  F R A M E  " R A O N "  ################################
################################  F R A M E  " R A O N "  ################################


class Raon_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [16]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [16][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [16][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Raon_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [16]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [16][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [16][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Raon_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [16]
     pass


################################  F R A M E  " T R I C O "  ################################
################################  F R A M E  " T R I C O "  ################################


class Trico_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [17]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [17][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [17][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Trico_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [17]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [17][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [17][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Trico_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [17]
     pass


################################  F R A M E  " N A K "  ################################
################################  F R A M E  " N A K "  ################################


class Nak_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [18]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [18][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [18][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Nak_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [18]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [18][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [18][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Nak_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [18]
     pass


################################  F R A M E  " B I G "  ################################
################################  F R A M E  " B I G "  ################################


class Bigfoot_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [19]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [19][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [19][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Bigfoot_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [19]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [19][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [19][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Bigfoot_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [19]
     pass


################################  F R A M E  " D R A G O N '1' "  ################################
################################  F R A M E  " D R A G O N '1' "  ################################


class Barney_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [20]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [20][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [20][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Barney_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [20]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [20][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [20][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Barney_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [20]
     pass


################################  F R A M E  " D R A G O N '2' "  ################################
################################  F R A M E  " D R A G O N '2' "  ################################


class Dragon_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [21] 

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [21][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [21][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Dragon_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [21]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [21][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [21][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Dragon_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [21]
     pass


################################            EL             ################################ 
################################            FIN            ################################
class _Toplevel (Toplevel):

    def __init__(self, master=None, barra=None, **kwargs):
        
        path = 'E:/1-RICHI/MovilesDB'
        #____Coleccion de imagenes:
        self.Images_1 = self.generate_list (path, 'I')
        Toplevel.__init__(self, master, **kwargs)
        #self.masters = master
        self.overrideredirect(True)
        self.master = master
        self._x = 0
        self._y = 0
        self.x0 = 50
        self.y0 = 50
        self.x1 = 100
        self.y1 = 100
        self.click = True

        self.borde = BarraTitulo(self, background="black") # #11161d
        self.borde.pack(side=TOP, fill=BOTH)

        if barra is '_top':
            self.frame_titlebar .buttons_height ()
        if barra is '_right':
            self.frame_titlebar .buttons_width ()


        #self.contenido = Interface(self)
        #self.contenido.pack(side=BOTTOM, fill=BOTH)  # esto es la liena blanco de arriba
        
 

        self.frame_titlebar.bind("<ButtonPress-1>", self.start_move)
        self.frame_titlebar.bind("<ButtonRelease-1>", self.stop_move)
        self.frame_titlebar.bind("<B1-Motion>", self.on_move)

        """ self.borde.label_title.bind("<ButtonPress-1>", self.start_move)
        self.borde.label_title.bind("<ButtonRelease-1>", self.stop_move)
        self.borde.label_title.bind("<B1-Motion>", self.on_move) """


        """ self.grip = ttk.Sizegrip (self.contenido, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='center')
        self.grip .bind ('<B1-Motion>', self.redimencionar) """
        #ttk.Style().configure('TSizegrip', background='black')

    """ def posi3(self):
        self.borde.pack(side=TOP, fill=BOTH) """

    def start_move(self, event):
        self._x = event.x
        self._y = event.y

    def redimencionar(self, event):
        self.x0 = self.winfo_rootx()
        self.y0 = self.winfo_rooty()
        self.x1 = self.winfo_pointerx()
        self.y1 = self.winfo_pointery()

        try:
            self. geometry('%sx%s' % ((self.x1 - self.x0),(self.y1 - self.y0)))
        except:
            pass
    
    def stop_move(self, event):
        self._x = None
        self._y = None

    def on_move(self, event):
        deltax = event.x - self._x
        deltay = event.y - self._y
        new_pos = "+{}+{}".format(self.winfo_x() + deltax, self.winfo_y() + deltay)

        self.geometry(new_pos)
        #self.master.geometry(new_pos)

        
          
    def configure_toplevel(self, size): #--------------------------------NO TOCAR (despues)
    #def configure_toplevel(self, head, size): #--------------------------------NO TOCAR (despues) 
        #self.title (head)    #  titulo
        self.geometry (size)  #  tamaño
        #self.resizable (1,1)
        #self.wm_attributes ('-topmost', True)
        #self.config (bg = 'magenta2')
        #self.wm_attributes ('-transparentcolor', 'magenta2')
        #self.overrideredirect(1)

    

    def generate_list(self, file, option):   # INICIALIZA IMAGENES

        ouput = os.listdir (file)
        empty = []                    
        if option == 'I': 
            _lst = [[] for x in range(22)]
            _str = ['Fro','Fox','Boo','Ice','JD','Gru','Lig','Adu','Kni','Kal','Mag','Ran','Jol','Tur','Arm','Asa','Rao','Tri','Nak','Big','Dr1','Dr2']
            for i in ouput:               
                for index,iter in enumerate(_str):
                    if iter in i: 
                        full = file + '/' + i
                        open = cv2.imread (full)
                        RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB) 
                        _lst[index].append(RGB)               
            return _lst        

################################
################################
################################
################################
################################
################################
################################
################################
################################
################################

class BarraTitulo(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master = master
        self.image_initializer()


    def close(self):
        self.master.destroy()
        self.master.master.destroy()

    def minimize(self):
        self.master.withdraw()
        self.master.master.iconify()
   

    def buttons_height(self):

        self.button_close = Button(self, image=self.image_close, command=self.close, bd=0, bg='black', activebackground='black')
        self.button_minimize = Button(self, image=self.image_minimize, command=self.minimize, bd=0, bg='black', activebackground='black')

        self.button_close .pack(side=TOP, pady=7)               # modo vertical
        self.button_minimize .pack(side=BOTTOM, pady=7)         # modo vertical
        
    def buttons_width(self):

        self.button_close = Button(self, image=self.image_close, command=self.close, bd=0, bg='black', activebackground='black')
        self.button_minimize = Button(self, image=self.image_minimize, command=self.minimize, bd=0, bg='black', activebackground='black')
        self.label_title = Label(self, text='', fg="white", bg="green")

        self.button_close .pack(side=RIGHT)                     # modo horizontal
        self.button_minimize .pack(side=RIGHT, padx=10)         # modo horizontal    
        self.label_title .pack(side=RIGHT, padx=0, pady=0)

    def image_initializer(self):
        self.image_close = PhotoImage(file= '11.png')
        self.image_maximize = PhotoImage(file= 'ma.png') 
        self.image_minimize = PhotoImage(file= '22.png')
        self.image_reduce = PhotoImage(file= 'ma2.png')
  
################################

class Toplevel_class(Toplevel):
    def __init__(self, master=None, type=None, **kwargs):
        Toplevel.__init__(self, master, **kwargs)

        path = 'E:/1-RICHI/MovilesDB'
        #____Coleccion de imagenes:
        self.Images_1 = self.generate_list (path, 'I')

        self.overrideredirect(True)
        self.master = master
        self._x = 0
        self._y = 0
        self.x0 = 50
        self.y0 = 50
        self.x1 = 100
        self.y1 = 100
        self.click = True

        if type == 'H':   # INTERFACE PRINCIPAL
            self.frame_titlebar = BarraTitulo(self, bg="black") # #11161d
            self.frame_titlebar .pack(side=RIGHT, fill=BOTH)
            self.frame_titlebar .buttons_height()

            self.frame_ashmanbot = Interface(self)
            self.frame_ashmanbot .pack(side=RIGHT, fill=BOTH)  # esto es la liena blanco de arriba

            #self.frame_ashmanbot .

        if type == 'W':   # VENTANAS ALTERNAS
            self.frame_titlebar = BarraTitulo(self, bg="black") # #11161d
            self.frame_titlebar .pack(side=TOP, fill=BOTH)
            self.frame_titlebar .buttons_width()

            #____S I Z E G R I P:
            """ self.grip = ttk.Sizegrip(self.master._frame_1, style='TSizegrip')
            self.grip .place (relx=1.0, rely=1.0, anchor='center')
            ttk.Style().configure('TSizegrip', bg='black') """
            #self.grip .bind ('<B1-Motion>', self.redimencionar)
            #____L A B E L:
            self.frame_titlebar .label_title .bind("<ButtonPress-1>", self.start_move)
            self.frame_titlebar .label_title .bind("<ButtonRelease-1>", self.stop_move)
            self.frame_titlebar .label_title .bind("<B1-Motion>", self.on_move)
            
   
        self.frame_titlebar .bind("<ButtonPress-1>", self.start_move)
        self.frame_titlebar .bind("<ButtonRelease-1>", self.stop_move)
        self.frame_titlebar .bind("<B1-Motion>", self.on_move)

        self.master .bind("<Map>", self.on_deiconify)
        self.master .bind("<Unmap>", self.on_iconify)

    def on_iconify(self, event):
        self.withdraw()

    def on_deiconify(self, event):
        self.deiconify()



    def start_move(self, event):
        self._x = event.x
        self._y = event.y

    def stop_move(self, event):
        self._x = None
        self._y = None

    def on_move(self, event):
        deltax = event.x - self._x
        deltay = event.y - self._y
        new_pos = "+{}+{}".format(self.winfo_x() + deltax, self.winfo_y() + deltay)

        self.geometry(new_pos)
        if type == 'H': 
            self.master.geometry(new_pos)    # aqui conflicto

    def configure_toplevel(self, size): #--------------------------------NO TOCAR (despues)
    #def configure_toplevel(self, head, size): #--------------------------------NO TOCAR (despues) 
        #self.title (head)    #  titulo
        self.geometry (size)  #  tamaño
        #self.resizable (1,1)
        self.wm_attributes ('-topmost', True)
        #self.config (bg = 'magenta2')
        #self.wm_attributes ('-transparentcolor', 'magenta2')
        #self.overrideredirect(1)

    def generate_list(self, file, option):   # INICIALIZA IMAGENES

        ouput = os.listdir (file)
        empty = []                    
        if option == 'I': 
            _lst = [[] for x in range(22)]
            _str = ['Fro','Fox','Boo','Ice','JD','Gru','Lig','Adu','Kni','Kal','Mag','Ran','Jol','Tur','Arm','Asa','Rao','Tri','Nak','Big','Dr1','Dr2']
            for i in ouput:               
                for index,iter in enumerate(_str):
                    if iter in i: 
                        full = file + '/' + i
                        open = cv2.imread (full)
                        RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB) 
                        _lst[index].append(RGB)               
            return _lst 

        
################################
#____
    """ class WindRoot(Tk):  # SIN FUNCIONAMIENTO
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        self.geometry('0x0')
        #self._title = StringVar(self.title())
        self.window = Toplevel_class(self, barra='_top')
        self.window.geometry('830x65')
        self.bind("<Map>", self.on_deiconify)
        self.bind("<Unmap>", self.on_iconify)


    def title(self, *args):
        if args:
            print(args)
            self._title.set(args[0])
        Tk.title(self, args) 

    def on_iconify(self, event):
        self.window.withdraw()

    def on_deiconify(self, event):
        self.window.deiconify()

    root =  WindRoot()
    root .wm_attributes("-alpha", 0.0 )
    app = Interface(root)
    app .pack()    
    root .mainloop() """

    """ root =  Tk()
    app = Interface(root)
    app .pack()    
    root .mainloop()
    """

class Aplicacion(Frame):
    def __init__(self, master, type, version=None, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs )

        path = 'E:/1-RICHI/MovilesDB'
        #____Coleccion de imagenes:
        self.Images_1 = self.generate_list (path, 'I')



        self.image_initializer()
        self.x = 0
        self.y = 0
        
        self.ventana = Toplevel(self.master)
        self.ventana .overrideredirect(1)
        #self.ventana .minsize(width=300, height=200)
        self.ventana .geometry('830x65+300+90')
       
        #__FRAME BARRA DE TITULO:aaaaaa
        if type == 'H':
            self.frame_titlebar = Frame (self.ventana, bg="black" )
            self.frame_titlebar .pack(side=RIGHT, fill=BOTH)
        
        if type == 'W':
            self.frame_titlebar = Frame (self.ventana, bg="black" )
            self.frame_titlebar .pack(side=TOP, fill=BOTH)
        #self.frame_titlebar .grid_propagate(0)
    

        #__FRAME DEL CONTENIDO:
        #if frame ==
        #self.frame_interface = Interface (self.ventana)
        #self.frame_interface .pack(side=RIGHT, fill=BOTH)


        #______DEL OTROOOOOOOOOOOOOOOOOOOOOOO
        if type == 'H':   # INTERFACE PRINCIPAL
            self.frame_interface = Interface (self.ventana)
            self.frame_interface .pack(side=RIGHT, fill=BOTH)
            #_________________________
            self.button_close = Button(self.frame_titlebar, image=self.image_close, command=self.close, bd=0, bg='black', activebackground='black')
            self.button_minimize = Button(self.frame_titlebar, image=self.image_minimize, command= lambda: self.master .iconify(), bd=0, bg='black', activebackground='black')

            self.button_close .pack(side=TOP, pady=7)               # modo vertical
            self.button_minimize .pack(side=BOTTOM, pady=7)         # modo vertical
            
        if type == 'w':

            self.button_close = Button(self.frame_titlebar, image=self.image_close, command=self.close, bd=0, bg='black', activebackground='black')
            self.button_minimize = Button(self.frame_titlebar, image=self.image_minimize, command= lambda: self.master .iconify(), bd=0, bg='black', activebackground='black')
            #self.label_title = Label(self, text='', fg="white", bg="green")

            self.button_close .pack(side=RIGHT)                     # modo horizontal
            self.button_minimize .pack(side=RIGHT, padx=10)         # modo horizontal    
            #self.label_title .pack(side=RIGHT, padx=0, pady=0)
        #_______________________________

        self.frame_titlebar .bind ('<ButtonPress-1>', self.start)
        self.frame_titlebar .bind ('<B1-Motion>', self.mover)
        self.master .bind ('<Map>', self.on_deiconify)
        self.master .bind ('<Unmap>', self.on_iconify)




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

        self.ventana.geometry(new_pos) # solo habia este
        #self.master.geometry(new_pos)
   
    def on_deiconify(self, event):
        self.ventana .deiconify()
        self.master .lower()

    def on_iconify(self, event):
        self.ventana .withdraw()
        self.master .iconify()

    #______DEL OTROOOOOOOOOOOOOOOOOOOOOOO


    def image_initializer(self):
        self.image_close = PhotoImage(file= '11.png')
        self.image_maximize = PhotoImage(file= 'ma.png') 
        self.image_minimize = PhotoImage(file= '22.png')
        self.image_reduce = PhotoImage(file= 'ma2.png')

    #def configure_toplevel(self, size): #--------------------------------NO TOCAR (despues)
        #def configure_toplevel(self, head, size): #--------------------------------NO TOCAR (despues) 
        #self.title (head)    #  titulo
        #self.ventana.geometry (size)  #  tamaño
        #self.resizable (1,1)
        #self.master.wm_attributes ('-topmost', True)
        #self.config (bg = 'magenta2')
        #self.wm_attributes ('-transparentcolor', 'magenta2')
        #self.overrideredirect(1)

    def generate_list(self, file, option):   # INICIALIZA IMAGENES

        ouput = os.listdir (file)
        empty = []                    
        if option == 'I': 
            _lst = [[] for x in range(22)]
            _str = ['Fro','Fox','Boo','Ice','JD','Gru','Lig','Adu','Kni','Kal','Mag','Ran','Jol','Tur','Arm','Asa','Rao','Tri','Nak','Big','Dr1','Dr2']
            for i in ouput:               
                for index,iter in enumerate(_str):
                    if iter in i: 
                        full = file + '/' + i
                        open = cv2.imread (full)
                        RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB) 
                        _lst[index].append(RGB)               
            return _lst 



def main (): #------------------------------------------------------------NO TOCAR

    root = Tk()
    root .title('Aplicación moderna')
    #root .wm_attributes("-alpha", 0.0 ) 
    app = Aplicacion (root, type='H')
    app .mainloop()

if __name__=="__main__":  #-------------------------------------------------------NO TOCAR 
    main()
