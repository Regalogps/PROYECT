from tkinter import *
from tkinter import ttk 
from tkinter import filedialog
from typing import Sized
from PIL import ImageTk, Image
import cv2
import imutils
import numpy as np
import os 
import sys

#global is_on
#is_on = True

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_DESDE AQUI EMPIEZA EL CODIGO-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-

class Interface(Tk):

    def __init__(self): #-------------------------------------------------------------NO TOCAR     
        Tk. __init__(self)                                                 # Llamando a Tk ()

        path = 'E:/1-RICHI/MovilesDB'                                      # Ruta de la carpeta
        self.Imageness = self.create_list (path, 'full') 
              
        self.Imagenes_copia = self.create_list (path, 'partial') 


        self.Imagenes = self.create_list (path, 'tres')
        #print(len(self.Imagenes))
        #print("este print esta en interfaz",self.Imagenes_copia[0])
        # Llamando a las Metodos de Configuracion 
        self. configure_interface()          
        self. widgets()   

#_______V A R I A B L E S  de  C O N T R O L  para las :  V E N T A N A S , izquierda; derecha; stuff
 
        self.__frame_1 = None
        self.__frame_2 = None
        self.__frame_3 = None

        self.open_1 = True  
        self.open_2 = True  
        self.open_3 = True

    def configure_interface(self):   # Configuracion de la ventana -------------------NO TOCAR (despues)
      
        #ventana.overrideredirect(1)
        #ventana.attributes("-toolwindow",-1)
        self.title ('_AshmanBot_')                                 #  BORRAR
        self.geometry ('1000x150')                                 # TAMANIO DE LA VENTANA
        self.resizable (1,1)                                       # OTORGA PERMISO PARA CAMBIAR DE TAMANIO ALA VENTANA
        self.config (bg='magenta2')                                # CONFIGURA EL FONDO DE LA VENTANA, etc
        self.attributes ('-topmost', True)                         # SUPERPONE LA VENTANA A OTRAS APLICACIONES ABIERTAS
        self.wm_attributes ('-transparentcolor', 'magenta2')       # BORRA EL COLOR SELECCIONADO DE LA VENTANA
        #root.attributes("-alpha", 0.5 )   

    def create_list (self, file, option):   # Metodo para leer todas las imageneS ------NO TOCAR
    
        pictures = os.listdir (file)
        self.list_1 = [] 
        self.list_2 = [] 




        self.list_3 = []




        if option == 'full':
            for i in pictures:
                if '.jpg' in i or '.png' in i:                         # VER SI ES NECESARIO SACAR DE LA LISTA A RUEDA Y AL LOGO

                    full = file + '/' + i
                    #print(ruta_completa)

                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    #arrayy = Image.fromarray (RGB)
                    #img = ImageTk.PhotoImage (array)

                    self.list_1 .append (RGB)
            return self.list_1
        
        if option == "partial" :
            for i in pictures:
                if ".jpg" in i or ".png" in i:        

                    full = file + '/' + i
                    #print(ruta_completa)

                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    array = Image.fromarray (RGB)
                    img = ImageTk.PhotoImage (array)

                    self.list_2 .append (img)
            return self.list_2



        if option == 'tres':
            for i in pictures:
                if '.jpg' in i or '.png' in i:                         # VER SI ES NECESARIO SACAR DE LA LISTA A RUEDA Y AL LOGO

                    full = file + '/' + i
                    #print(ruta_completa)

                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    array = Image.fromarray (RGB)
                    img = ImageTk.PhotoImage (array)

                    self.list_3 .append (img)
            return self.list_3
        
        
    def widgets(self):  # widgets de la ventana Principal ----------------------------NO TOCAR  EDITAR DESPUES A CLASE BOTON O LABEL

        self.frame_initial = Create_Frame (self, bg='#11161d', width=60, height=65)    # Frame Contenedor del logo y la rueda     
        self.frame_initial .img_gear()                                                # Metodo de la clase segundaria                                              
        self.frame_initial .img_ash()                                                 # Metodo de la clase segundaria
        self.frame_initial .grid (column= 0, row= 0, padx=(0,0), pady=(0,0))
        self.frame_initial .grid_propagate (0)

        self.frame_plomo = Create_Frame (self, bg='#31343a', width=756, height=65)     # Frame Contenedor del Contenedor de los Botones
        self.frame_plomo .grid (column= 1, row= 0, padx=0, pady=0, sticky='n')
        self.frame_plomo .grid_propagate (0)

        self.button_container = Create_Frame (self.frame_plomo, bg = '#11161d',)       # Frame Contenedor de los Botones
        self.button_container .img_moviles()                                          # Metodo de la clase segundaria                                             
        self.button_container .grid (padx = (10,0), pady = (6,0))  
     
    def configure_height(self):  # Metodo para configurar Frame ---------------------NO TOCAR

        self.winfo = self.frame_initial .winfo_reqheight()
         
        if self.winfo == 65:
            self.frame_initial .config (width=60, height=165)   
        else:
            self.frame_initial .config (width=60, height=65)

    def remove_frame(self):  # Metodo para Remover Frame ----------------------------NO TOCAR

        if self.frame_plomo .winfo_ismapped():      
            self.frame_plomo .grid_remove()   
        else:
            self.frame_plomo .grid()  

############   M E T O D O S   P A R A   G E S T I O N A R   L A S   V E N T A N A S   S U P E R I O R E S   ############ 

    def windows_123(self, var_1, var_2, var_3):

        if self.open_1 == True: 
            self.toplevel_LEFT = _Toplevel()  #############################################################   VENTANA TOPLEVEL IZQUIERDA
            self.toplevel_LEFT .configure_toplevel ('izq', '220x690') #  metodo 

        self.open_1 = False     
                                
        container_frame_left = var_1 (self.toplevel_LEFT)  #  var_1 es un frame

        if self.__frame_1 is not None:  
            self.__frame_1 .destroy()
        self.__frame_1 = container_frame_left
        self.__frame_1 .pack()
        
        self.toplevel_LEFT .protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(1))

#_______

        if self.open_2 == True:
            self.toplevel_RIGHT = _Toplevel()  #############################################################   VENTANA TOPLEVEL DERECHA
            self.toplevel_RIGHT .configure_toplevel ('der', '220x690')

        self.open_2 = False

        container_frame_right = var_2 (self.toplevel_RIGHT)  # ES UN FRAME POSICIONADO EN TOPLEVEL

        if self.__frame_2 is not None:
            self.__frame_2 .destroy()
        self.__frame_2 = container_frame_right
        self.__frame_2 .pack()


        self.toplevel_RIGHT.protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(2))

#_______ desde aqui falta completar este if
        
        if self.open_3 == True:
            self.toplevel_STUF = _Toplevel()  #############################################################   VENTANA TOPLEVEL STUFF
            self.toplevel_STUF .configure_toplevel ('der', '620x190')

        self.open_3 = False

        container_frame_stuff = var_3 (self.toplevel_STUF)  # ES UN FRAME POSICIONADO EN TOPLEVEL

        if self.__frame_3 is not None:
            self.__frame_3 .destroy()
        self.__frame_3 = container_frame_stuff
        self.__frame_3 .pack()


        self.toplevel_STUF.protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(3))





    def close_windows(self, number):

        if number == 1:
            self.toplevel_LEFT. destroy()
            self.open_1 = True

        if number == 2:
            self.toplevel_RIGHT. destroy()
            self.open_2 = True

        if number == 3:
            self.toplevel_STUF. destroy()
            self.open_3 = True


#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-

class _Toplevel (Toplevel):

    def __init__(self, *args): #---------------------------------------------------------NO TOCAR 
        Toplevel. __init__(self, *args) 
        #self.masters = master
          
    def configure_toplevel(self, head, size): #--------------------------------NO TOCAR (despues)
     
        self.title (head)    #  titulo
        self.geometry (size)  #  tamaño
        self.resizable (1,1)
        self.wm_attributes ('-topmost', True)
        self.config (bg = 'magenta2')
        self.wm_attributes ('-transparentcolor', 'magenta2')

#   desde ahy que editar...

    def widgets_toplevel(self, name):

        self.label0 = name
        self.label0 = Label (self, image = self.master.Imagenes [0])
        self.label0. bind ('<Configure>', self.resize_image)
        self.label0. pack (fill=BOTH, expand = YES)

    def resize_image(self, event):

        new_width = event.width
        new_height = event.height

        var1 = self.master.Imagenes_copia [0].resize((new_width, new_height))
        var2 = ImageTk.PhotoImage(var1)

        self.label0 . config (image = var2) 
        self.label0 . image = var2 


#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-

class Create_Frame (Frame):   

    def __init__(self, *args, **kwargs):   #---------------------------------------NO TOCAR (despues) 
        Frame.__init__(self, *args, **kwargs)   # Llamando a Frame ()  #, **kwargs : pasar mas valores al momento de la llamada (diccionarios)

    def img_ash(self):   # Metodo que crea -1- Boton (logo) -------------------NO TOCAR (despues)
        
        self.btn_ash = Button (self, image= self.master.Imagenes_copia [107], bg= '#11161d', bd= 0, activebackground= '#11161d' , command= self.master.remove_frame)
        self.btn_ash .grid (column= 0, row= 0, padx= 3, pady= 1)
          
    def img_gear(self):   # Metodo que crea -1- Boton (rueda)-----------------NO TOCAR (despues)

        self.btn_gear = Button (self, image= self.master.Imagenes_copia [110], bg= '#11161d', bd= 0, activebackground= '#11161d', command= self.master.configure_height)
        self.btn_gear .grid (column= 0, row= 1)
       
    def img_moviles(self):   # Metodo que crea -22- Botones (moviles)  #command = lambda:images(1))
        '''
        self.Frog_1 = Button (self, text='Frog', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_frog_IZQUIERDA, Frame_frog_DERECHA, Frame_frog_STUFF)) 

        self.Fox_2 = Button (self, text='Fox', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_fox_IZQUIERDA, Frame_fox_DERECHA, Frame_fox_STUFF)) 
        '''
        self.Boomer_3 = Button (self, text='Boomer', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (_Frame_boomer_IZQUIERDA, _Frame_boomer_DERECHA, _Frame_boomer_STUFF))     
        '''
        self.Ice_4 = Button (self, text='Ice', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_ice_IZQUIERDA, Frame_ice_DERECHA, Frame_ice_STUFF))

        self.JD_5 = Button (self, text='J.D', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_jd_IZQUIERDA, Frame_jd_DERECHA, Frame_jd_STUFF))

        self.Grub_6 = Button (self, text='Grub', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_grub_IZQUIERDA, Frame_grub_DERECHA, Frame_grub_STUFF))   

        self.Light_7 = Button (self, text='Light', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width=10, bd=0, command= lambda: self.master.master.windows_123 (Frame_light_IZQUIERDA, Frame_light_DERECHA, Frame_light_STUFF))       

        self.Aduka_8 = Button (self, text='Aduka', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_aduka_IZQUIERDA, Frame_aduka_DERECHA, Frame_aduka_STUFF))      

        self.Knight_9 = Button (self, text='Knight', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_knight_IZQUIERDA, Frame_knight_DERECHA, Frame_knight_STUFF))     

        self.Calziddon_10 = Button (self, text='Kalsiddon', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_kalsiddon_IZQUIERDA, Frame_kalsiddon_DERECHA, Frame_kalsiddon_STUFF))

        self.Mage_11 = Button (self, text='Mage', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_mage_IZQUIERDA, Frame_mage_DERECHA, Frame_mage_STUFF))  
   

        self.Randomizer_12 = Button (self, text='Randomizer', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_randomizer_IZQUIERDA, Frame_randomizer_DERECHA, Frame_randomizer_STUFF))
 
        self.Jolteon_13 = Button (self, text='Jolteon', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_jolteon_IZQUIERDA, Frame_jolteon_DERECHA, Frame_jolteon_STUFF))
 
        self.Turtle_14 = Button (self, text='Turtle', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_turtle_IZQUIERDA, Frame_turtle_DERECHA, Frame_turtle_STUFF))

        self.Armor_15 = Button (self, text='Armor', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_armor_IZQUIERDA, Frame_armor_DERECHA, Frame_armor_STUFF))

        self.Asate_16 = Button (self, text='A.Sate', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_asate_IZQUIERDA, Frame_asate_DERECHA, Frame_asate_STUFF))

        self.Raon_17 = Button (self, text='Raon', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_raon_IZQUIERDA, Frame_raon_DERECHA, Frame_raon_STUFF))
 
        self.Trico_18 = Button (self, text='Trico', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_trico_IZQUIERDA, Frame_trico_DERECHA, Frame_trico_STUFF))

        self.Nak_19 = Button (self, text='Nak', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_nak_IZQUIERDA, Frame_nak_DERECHA, Frame_nak_STUFF))
 
        self.Big_20 = Button (self, text='Big', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_big_IZQUIERDA, Frame_big_DERECHA, Frame_big_STUFF))
 
        self.Dragon1_21 = Button (self, text='Dragon 1', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_dragon1_IZQUIERDA, Frame_dragon1_DERECHA, Frame_dragon1_STUFF))
 
        self.Dragon2_22 = Button (self, text='Dragon 2', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frame_dragon2_IZQUIERDA, Frame_dragon2_DERECHA, Frame_dragon2_STUFF))
        '''
        '''
        self.Frog_1 .grid (column= 1, row= 1, pady= 3, padx= (5,0))
        self.Fox_2 .grid (column= 2, row= 1, pady= 3, padx= (0,0))
        '''
        self.Boomer_3 .grid (column= 3, row= 1, pady= 3, padx= (0,0))   
        '''   
        self.Ice_4 .grid (column= 4, row= 1, pady= 3, padx= (0,0))
        self.JD_5 .grid (column= 5, row= 1, pady= 3, padx= (0,0))
        self.Grub_6 .grid (column= 6, row= 1, pady= 3, padx= (0,0))
        self.Light_7 .grid (column= 7, row= 1, pady= 3, padx= (0,0))
        self.Aduka_8 .grid (column= 8, row= 1, pady= 3, padx= (0,0))
        self.Knight_9 .grid (column= 9, row= 1, pady= 3, padx= (0,0))
        self.Calziddon_10 .grid (column= 10, row= 1, pady= 3, padx= (0,0))
        self.Mage_11 .grid (column= 11, row= 1, pady= 3, padx= (0,5))

        self.Randomizer_12 .grid (column= 1, row= 2, pady= 2, padx= (5,0))
        self.Jolteon_13 .grid (column= 2, row= 2, pady= 2, padx= (0,0))
        self.Turtle_14 .grid (column= 3, row= 2, pady= 2, padx= (0,0))
        self.Armor_15 .grid (column= 4, row= 2, pady= 2, padx= (0,0))
        self.Asate_16 .grid (column= 5, row= 2, pady= 2, padx= (0,0))
        self.Raon_17 .grid (column= 6, row= 2, pady= 2, padx= (0,0))
        self.Trico_18 .grid (column= 7, row= 2, pady= 2, padx= (0,0))
        self.Nak_19 .grid (column= 8, row= 2, pady= 2, padx= (0,0))
        self.Big_20 .grid (column= 9, row= 2, pady= 2, padx= (0,0))
        self.Dragon1_21 .grid (column= 10, row= 2, pady= 2, padx= (0,0))
        self.Dragon2_22 .grid (column= 11, row= 2, pady= 2, padx= (0,5))
        '''


class Example(Frame):
    def __init__(self, master, indice, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

    def img (self, indice):
        #self.master = master
        self.image = Image.fromarray(indice)
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill='both', expand=True)
        self.background.bind('<Configure>', self._resize_image)



    def _resize_image(self, event):

        self.image = self.img_copy.resize((self.master.winfo_width(), self.master.winfo_height()))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.config(image=self.background_image)
        self.background.image = self.background_image



################################            EL             ################################ 
################################          INICIO           ################################ 
################################   F R A M E  " F R O G "  ################################  

class Frame_frog_IZQUIERDA (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_DELAY = Label(self, image= self.master.master.Imagenes [0], bd=0)
        self.lbl_DELAY . grid(column=0, row=0)
        self.lbl_DELAY . grid_propagate(0)

        self.lbl_MEDIR = Label(self, image= self.master.master.Imagenes [1], bd=0)       
        self.lbl_MEDIR . grid(column=0, row=0, sticky="n")
        
        self.lbl_guia = Label(self.lbl_DELAY, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_guia . bind("<Button-1>", self.ocultar)
        self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_guia . grid_propagate (0)
        
    def ocultar_med (self, event=None): 

        if self.lbl_MEDIR . grid_info() == {}:  # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.lbl_MEDIR . grid(column=0, row=0, sticky="n")      # Metodo para ocultar # Este metodo devuelve {} si es 
        else:
            self.lbl_MEDIR . grid_forget()



class Frame_frog_DERECHA (Frame):  #------------------------------- DERECHA :  BASE  /  77

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_BASE = Label(self, image= self.master.master.Imagenes [2], bd=0)
        self.lbl_BASE . grid(column=0, row=0)
        self.lbl_BASE . grid_propagate(0)

        self.lbl_77 = Label(self, image= self.master.master.Imagenes [3], bd=0)       
        self.lbl_77 . grid(column=0, row=0, sticky="n")
        
        self.lbl_guia = Label(self.lbl_BASE, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_guia . bind("<Button-1>", self.ocultar)
        self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_guia . grid_propagate (0)
        
    def ocultar_med (self, event=None): 

        if self.lbl_77 . grid_info() == {}:  # Metodo de info de un widget
            self.lbl_77 . grid(column=0, row=0, sticky="n")      
        else:
            self.lbl_77 . grid_forget()



class Frame_frog_STUFF (Frame):  #-------------------------------- REGLA: GAME STUFF
     pass           



################################   F R A M E  " F O X "  ################################

class Frame_fox_IZQUIERDA (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_DELAY = Label(self, image= self.master.master.Imagenes [4], bd=0)
        self.lbl_DELAY . grid(column=0, row=0)
        self.lbl_DELAY . grid_propagate(0)

        self.lbl_MEDIR = Label(self, image= self.master.master.Imagenes [5], bd=0)       
        self.lbl_MEDIR . grid(column=0, row=0, sticky="n")
        
        self.lbl_guia = Label(self.lbl_DELAY, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_guia . bind("<Button-1>", self.ocultar)
        self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_guia . grid_propagate (0)
        
    def ocultar_med (self, event=None): 

        if self.lbl_MEDIR . grid_info() == {}:  # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.lbl_MEDIR . grid(column=0, row=0, sticky="n")      # Metodo para ocultar # Este metodo devuelve {} si es 
        else:
            self.lbl_MEDIR . grid_forget()



class Frame_fox_DERECHA (Frame):  #------------------------------- DERECHA :  BASE  /  77

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_BASE = Label(self, image= self.master.master.Imagenes [6], bd=0)
        self.lbl_BASE . grid(column=0, row=0)
        self.lbl_BASE . grid_propagate(0)

        self.lbl_77 = Label(self, image= self.master.master.Imagenes [7], bd=0)       
        self.lbl_77 . grid(column=0, row=0, sticky="n")
        
        self.lbl_guia = Label(self.lbl_BASE, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_guia . bind("<Button-1>", self.ocultar)
        self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_guia . grid_propagate (0)
        
    def ocultar_med (self, event=None): 

        if self.lbl_77 . grid_info() == {}:  # Metodo de info de un widget
            self.lbl_77 . grid(column=0, row=0, sticky="n")      
        else:
            self.lbl_77 . grid_forget()



class Frame_fox_STUFF (Frame):  #-------------------------------- REGLA: GAME STUFF
     pass           




################################   F R A M E  " B O O M E R "  ################################ 

class _Frame_boomer_IZQUIERDA (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.frame_img_DELAY = Example (self, self.master.master.Imageness [8], bd=0)
        self.frame_img_DELAY .pack()
        #self.frame_img_DELAY .pack_propagate

        self.frame_img_SIMULADOR = Example (self, self.master.master.Imageness [9], bd=0)  
        self.frame_img_SIMULADOR .pack()
        self.frame_img_SIMULADOR .pack_propagate

        #self.frame_guia = Label (self.frame_img_DELAY, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        #self.frame_guia . bind("<Button-1>", self.ocultar)
        #self.frame_guia . grid(padx= 2, pady= 61)


        #self.lbl_DELAY = Label(self, image= self.master.master.Imagenes [8], bd=0)
        #self.lbl_DELAY . grid(column=0, row=0)
        #self.lbl_DELAY . grid_propagate(0) 

        #self.lbl_MEDIR = Label(self, image= self.master.master.Imagenes [9], bd=0)       
        #self.lbl_MEDIR . grid(column=0, row=0, sticky="n")
        
        #self.lbl_guia = Label(self.lbl_DELAY, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        #self.lbl_guia . bind("<Button-1>", self.ocultar)
        #self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        #self.lbl_guia . grid_propagate (0)
        
    def ocultar (self, event=None): 

        if self.frame_img_SIMULADOR .pack_info() == {}:                      # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.frame_img_SIMULADOR .pack()  
        else:
            self.frame_img_SIMULADOR .pack_forget()
    
class _Frame_boomer_DERECHA (Frame):  #------------------------------- DERECHA :  BASE  /  77

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        pass
        '''
        self.pack_propagate(1)

        self.lbl_BASE = Label(self, image= self.master.master.Imagenes [10], bd=0)
        self.lbl_BASE . bind("<Button-1>", self.ocultar)
        self.lbl_BASE . grid(column=0, row=0, sticky="ne")
        self.lbl_BASE . grid_propagate(0)

        self.lbl_77 = Label(self, image= self.master.master.Imagenes [11], bd=0)       
        self.lbl_77 . grid(column=0, row=0, sticky="ne")

        self.lbl_FLECHA = Label(self, image= self.master.master.Imagenes [108], bd=0)       
        self.lbl_FLECHA . grid(column=0, row=0, sticky="se")
        

    def ocultar (self, event=None): 

        x, y = event.x, event.y
        print(x, y)
    
        if x >=115 :

            if self.lbl_77 . grid_info() == {} and self.lbl_FLECHA . grid_info() == {} :  # Metodo de info de un widget

                self.lbl_77 . grid(column=0, row=0, sticky="ne")
                self.lbl_FLECHA . grid(column=0, row=0, sticky="se")        
        
            else:
                self.lbl_77 . grid_forget()
                self.lbl_FLECHA . grid_forget()
        
        '''

class _Frame_boomer_STUFF (Frame):  #-------------------------------- REGLA: GAME STUFF
     pass





class Frame_boomer_IZQUIERDA (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR
    pass
    

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)      

        self.lbl_DELAY = Label(self, image= self.master.master.Imagenes [8], bd=0)
        self.lbl_DELAY . grid(column=0, row=0)

      
        #self.lbl_DELAY . grid_propagate(0) 

        self.lbl_MEDIR = Label(self, image= self.master.master.Imagenes [9], bd=0)       
        self.lbl_MEDIR . grid(column=0, row=0, sticky="n")
        
        #self.lbl_guia = Label(self.lbl_DELAY, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
       # self.lbl_guia . bind("<Button-1>", self.ocultar)
        #self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        #self.lbl_guia . grid_propagate (0)
        
    def ocultar (self, event=None): 

        if self.lbl_MEDIR . grid_info() == {}:                      # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.lbl_MEDIR . grid(column=0, row=0, sticky="n")      
        else:
            self.lbl_MEDIR . grid_forget()
    
class Frame_boomer_DERECHA (Frame):  #------------------------------- DERECHA :  BASE  /  77

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
      
        self.pack_propagate(1)

        self.lbl_BASE = Label(self, image= self.master.master.Imagenes [10], bd=0)
        self.lbl_BASE . bind("<Button-1>", self.ocultar)
        self.lbl_BASE . grid(column=0, row=0, sticky="ne")
        self.lbl_BASE . grid_propagate(0)

        self.lbl_77 = Label(self, image= self.master.master.Imagenes [11], bd=0)       
        self.lbl_77 . grid(column=0, row=0, sticky="ne")

        self.lbl_FLECHA = Label(self, image= self.master.master.Imagenes [108], bd=0)       
        self.lbl_FLECHA . grid(column=0, row=0, sticky="se")
        

    def ocultar (self, event=None): 

        x, y = event.x, event.y
        print(x, y)
    
        if x >=115 :

            if self.lbl_77 . grid_info() == {} and self.lbl_FLECHA . grid_info() == {} :  # Metodo de info de un widget

                self.lbl_77 . grid(column=0, row=0, sticky="ne")
                self.lbl_FLECHA . grid(column=0, row=0, sticky="se")        
        
            else:
                self.lbl_77 . grid_forget()
                self.lbl_FLECHA . grid_forget()

class Frame_boomer_STUFF (Frame):  #-------------------------------- REGLA: GAME STUFF
     pass

################################  F R A M E  " I C E "  ################################

class Frame_ice_IZQUIERDA (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR#

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_DELAY = Label(self, image= self.master.master.Imagenes [12], bd=0)
        self.lbl_DELAY . grid(column=0, row=0)
        self.lbl_DELAY . grid_propagate(0)

        self.lbl_MEDIR = Label(self, image= self.master.master.Imagenes [13], bd=0)       
        self.lbl_MEDIR . grid(column=0, row=0, sticky="n")
        
        self.lbl_guia = Label(self.lbl_DELAY, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_guia . bind("<Button-1>", self.ocultar)
        self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_guia . grid_propagate (0)
        
    def ocultar(self, event=None): 

        if self.lbl_MEDIR . grid_info() == {}:  # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.lbl_MEDIR . grid(column=0, row=0, sticky="n")      # Metodo para ocultar # Este metodo devuelve {} si es 
        else:
            self.lbl_MEDIR . grid_forget()



class Frame_ice_DERECHA (Frame):  #------------------------------- DERECHA :  BASE  /  77

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_BASE = Label(self, image= self.master.master.Imagenes [14], bd=0)
        self.lbl_BASE . grid(column=0, row=0)
        self.lbl_BASE . grid_propagate(0)

        self.lbl_77 = Label(self, image= self.master.master.Imagenes [15], bd=0)       
        self.lbl_77 . grid(column=0, row=0, sticky="ne")
        
        self.lbl_guia = Label(self.lbl_BASE, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_guia . bind("<Button-1>", self.ocultar)
        self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_guia . grid_propagate (0)
        
    def ocultar (self, event=None): 

        if self.lbl_77 . grid_info() == {}:  # Metodo de info de un widget
            self.lbl_77 . grid(column=0, row=0, sticky="n")      
        else:
            self.lbl_77 . grid_forget()



class Frame_ice_STUFF (Frame):  #-------------------------------- REGLA: GAME STUFF
     pass


################################  F R A M E  " J D "  ################################

class Frame_jd_IZQUIERDA (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_DELAY = Label(self, image= self.master.master.Imagenes [16], bd=0)
        self.lbl_DELAY . grid(column=0, row=0)
        self.lbl_DELAY . grid_propagate(0)

        self.lbl_MEDIR = Label(self, image= self.master.master.Imagenes [17], bd=0)       
        #self.lbl_MEDIR . grid(column=0, row=0, sticky="n")
        
        self.lbl_guia = Label(self.lbl_DELAY, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_guia . bind("<Button-1>", self.ocultar)
        self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_guia . grid_propagate (0)
        
    def ocultar (self, event=None): 

        if self.lbl_MEDIR . grid_info() == {}:  # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.lbl_MEDIR . grid(column=0, row=0, sticky="n")      # Metodo para ocultar # Este metodo devuelve {} si es 
        else:
            self.lbl_MEDIR . grid_forget()



class Frame_jd_DERECHA (Frame):  #------------------------------- DERECHA :  BASE  /  77

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_BASE = Label(self, image= self.master.master.Imagenes [18], bd=0)
        self.lbl_BASE . grid(column=0, row=0)
        self.lbl_BASE . grid_propagate(0)

        self.lbl_77 = Label(self, image= self.master.master.Imagenes [19], bd=0)       
        self.lbl_77 . grid(column=0, row=0, sticky="ne")

        self.lbl_FLECHA = Label(self, image= self.master.master.Imagenes [108], bd=0)       
        self.lbl_FLECHA . grid(column=0, row=0, sticky="se")
     
        self.lbl_quitar_columna77 = Label(self.lbl_BASE, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_quitar_columna77 . bind("<Button-1>", self.ocultar)
        self.lbl_quitar_columna77 . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_quitar_columna77 . grid_propagate (0)
        
    def ocultar (self, event=None): 

        if self.lbl_77 . grid_info() == {} and self.lbl_FLECHA . grid_info() == {} :  # Metodo de info de un widget

            self.lbl_77 . grid(column=0, row=0, sticky="ne")
            self.lbl_FLECHA . grid(column=0, row=0, sticky="se")        
     
        else:
            self.lbl_77 . grid_forget()
            self.lbl_FLECHA . grid_forget()



class Frame_jd_STUFF (Frame):  #-------------------------------- REGLA: GAME STUFF
     pass


################################            EL             ################################ 
################################            FIN            ################################


def main (): #--------------------------------------------------------------------NO TOCAR 
    app = Interface()    
    app .mainloop()

if __name__=="__main__":  #-------------------------------------------------------NO TOCAR 
    main()
   
