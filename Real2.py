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



global Imagenes
Imagenes = None

global is_on
is_on = True


#__________________________________________
class Interfaz(Tk):

    def __init__(self):      
        Tk. __init__(self)    # Llamando a Tk ()

        global Imagenes
        path_1 = "E:/1-RICHI/MovilesDB"      # Ruta de la carpeta de imagenes
     
        Imagenes = self.leer_folder(path_1)   # Llama al Metodo y guarda en una varible las imagenes
        #print (Imagenes)
        self. configurar_interfaz()
        self. widgets()  
 
        self.mainloop ()


    def configurar_interfaz(self):   # Configuracion de la ventana
      
        #ventana.overrideredirect(1)
        #ventana.attributes("-toolwindow",-1)
        self. title ("_AshmanBot_")                           #  BORRAR
        self. geometry ("1000x150")                           # TAMANIO DE LA VENTANA
        self. resizable (1,1)                                 # OTORGA PERMISO PARA CAMBIAR DE TAMANIO ALA VENTANA
        self. config (bg="magenta2")                          # CONFIGURA EL FONDO DE LA VENTANA, etc
        self. wm_attributes("-topmost", True)                 # SUPERPONE LA VENTANA A OTRAS APLICACIONES ABIERTAS
        self. wm_attributes("-transparentcolor", "magenta2")  # BORRA EL COLOR SELECCIONADO DE LA VENTANA
        #root.attributes("-alpha", 0.5 )          
        #self.path_1 = "E:/1-RICHI/MovilesDB"                 # Ruta de la carpeta que tiene todas las imagenes
        #self.Leer_folder (self.path_1)                       # Llamando a la funcion para que lea la carpetaa


    def leer_folder (self, path):  # Metodo para leer todas las imagenes

        Imagenes = os.listdir(path)
        self.lista = []              
        
        for i in Imagenes:
            ruta_completa = path + "/" + i

            #print (ruta_completa)

            abrir = cv2.imread (ruta_completa)
            RGB = cv2.cvtColor (abrir, cv2.COLOR_BGR2RGB)
            objeto = Image.fromarray (RGB)

            photo = ImageTk.PhotoImage(objeto)

            self.lista. append (photo)

        return self.lista
        

    def widgets(self):  # widgets de la ventana Principal

        self.frame_inicial = Create_Frame (self, bg="#11161d", width=60, height=65)   # Frame Contenedor del logo y la rueda 
        self.frame_inicial . grid (column= 0, row= 0, padx=(0,0), pady=(0,0))
        self.frame_inicial . grid_propagate (0)     
        self.frame_inicial . btn_img_rueda ()   # Metodo de la clase segundaria                                              
        self.frame_inicial . btn_img_ash ()      # Metodo de la clase segundaria

        self.frame_plomo = Create_Frame (self, bg="#31343a", width=756, height=65)    # Frame Contenedor del Contenedor de los Botones
        self.frame_plomo . grid (column= 1, row= 0, padx=0, pady=0, sticky="n")
        self.frame_plomo . grid_propagate (0)

        self.contenedor_de_botones = Create_Frame (self.frame_plomo, bg = "#11161d",)  # Frame Contenedor de los Botones
        self.contenedor_de_botones . btn_moviles ()    # Metodo de la clase segundaria                                             
        self.contenedor_de_botones . grid (padx = (10,0), pady = (6,0))  
     

    def configurar_height(self):  # Metodo para configurar Frame

        self.winfo = self.frame_inicial . winfo_reqheight()
         
        if self.winfo == 65:
            self.frame_inicial . config(width=60, height=165)   
        else:
            self.frame_inicial . config(width=60, height=65)


    def remover_frame(self):  # Metodo para Remover Frame

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

    def abrir_toplevel (self):
    
        try:  #--------------------------------------------------codifo recuperado
            self.hoja1.winfo_viewable()  #-----------------------codifo recuperado
        except Exception as err:         #-----------------------codifo recuperado
            self.hoja1 = Ventanas()
            self.hoja1.transient(self)

            self.hoja1.configurar_toplevel("izq","195x690")
            self.hoja1.widgets_toplevel("labelll")



#_______
        try:  #--------------------------------------------------codifo recuperado       
            self.hoja2.winfo_viewable()  #-----------------------codifo recuperado
        except Exception as err:         #-----------------------codifo recuperado
            self.hoja2 = Ventanas()
            self.hoja2.transient( self)

            self.hoja2.configurar_toplevel("der","195x690")
#_______      

        try:  #--------------------------------------------------codifo recuperado
            self.hoja3.winfo_viewable()  #-----------------------codifo recuperado
        except Exception as err:         #-----------------------codifo recuperado
            self.hoja3 = Ventanas()
            #self.hoja3.transient( self) #-----------------------codifo recuperado

            self.hoja3.configurar_toplevel("stuf","700x190")
 


#__________________________________________
class Ventanas (Toplevel):
    def __init__(self): 
        Toplevel. __init__(self) 
        #self.masters = masters
          
    def configurar_toplevel(self,titulo,tamano):

        self . wm_attributes("-topmost", True)
        self . title(titulo)
        self . geometry(tamano)
        self . config(bg = "magenta2")
        self . resizable(1,1)

    def widgets_toplevel(self, name):
        self.label0 = name
        self.label0 = Label (self, image = Imagenes [0])
        self.label0. bind ('<Configure>', self.resize_image_1)
        self.label0. pack (fill=BOTH, expand = YES)

    def resize_image_1(self, event):

        ImagenesCopia = Imagenes
        # crear una copia de toda la lista es creo la solucion
        new_width = event.width
        new_height = event.height

        Imagen1 = ImagenesCopia [0] . resize ((new_width, new_height))
        Imagen2 = ImageTk.PhotoImage(Imagen1)

        self.label0 . config (image = Imagen2 [0])                  # Configurando el " Label
        self.label0 . image = Imagen2 [0] 


#___________________________________________
class Create_Frame (Frame):   

    def __init__(self, parent, **kwargs):
        Frame.__init__(self, parent, **kwargs)   # Llamando a Frame ()  #, **kwargs : pasar mas valores al momento de la llamada (diccionarios)
        #self.master = master
        

    def btn_img_ash(self):  # Metodo que crea -1- Boton (logo)
        
        self.img_ash = Button (self, image = Imagenes [107], bg="#11161d", bd=0, activebackground="#11161d" , command= self.master.remover_frame)
        self.img_ash . grid(column= 0, row= 0, padx=3, pady=1)

            
    def btn_img_rueda(self):  # Metodo que crea -1- Boton (rueda)

        self.img_config = Button (self, image = Imagenes [110], bg="#11161d", bd=0, activebackground="#11161d", command= self.master.configurar_height)
        self.img_config . grid (column=0, row= 1)

        
    def btn_moviles(self):  # Metodo que crea -22- Botones (moviles)

        self.Frog_1 = Button (self, text="Frog", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.abrir_toplevel)

        self.Fox_2 = Button (self, text="Fox", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)

        self.Boomer_3 = Button (self, text="Boomer", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)      

        self.Ice_4 = Button (self, text="Ice", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)

        self.JD_5 = Button (self, text="J.D", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)

        self.Grub_6 = Button (self, text="Grub", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)   

        self.Light_7 = Button (self, text="Light", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width=10, bd=0, command= self.Movil_trico)       

        self.Aduka_8 = Button (self, text="Aduka", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)       

        self.Knight_9 = Button (self, text="Knight", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)      

        self.Calziddon_10 = Button (self, text="Kalsiddon", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)

        self.Mage_11 = Button (self, text="Mage", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)    
   

        self.Randomizer_12 = Button (self, text="Randomizer", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
 
        self.Jolteon_13 = Button (self, text="Jolteon", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)
 
        self.Turtle_14 = Button (self, text="Turtle", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)

        self.Armor_15 = Button (self, text="Armor", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)

        self.Asate_16 = Button (self, text="A.Sate", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)

        self.Raon_17 = Button (self, text="Raon", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
 
        self.Trico_18 = Button (self, text="Trico", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)

        self.Nak_19 = Button (self, text="Nak", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
 
        self.Big_20 = Button (self, text="Big", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
 
        self.Dragon1_21 = Button (self, text="Dragon 1", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)
 
        self.Dragon2_22 = Button (self, text="Dragon 2", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)

        self.Frog_1 . grid (column= 1, row= 1, pady=3, padx=(5,0))
        self.Fox_2. grid (column= 2, row= 1, pady=3, padx=(0,0))
        self.Boomer_3. grid (column= 3, row= 1, pady=3, padx=(0,0))      
        self.Ice_4. grid (column= 4, row= 1, pady=3, padx=(0,0))
        self.JD_5. grid (column= 5, row= 1, pady=3, padx=(0,0))
        self.Grub_6. grid (column= 6, row= 1, pady=3, padx=(0,0))
        self.Light_7. grid (column= 7, row= 1, pady=3, padx=(0,0))
        self.Aduka_8. grid (column= 8, row= 1, pady=3, padx=(0,0))
        self.Knight_9. grid (column= 9, row= 1, pady=3, padx=(0,0))
        self.Calziddon_10. grid (column= 10, row= 1, pady=3, padx=(0,0))
        self.Mage_11. grid (column= 11, row= 1, pady=3, padx=(0,5))
        self.Randomizer_12. grid (column= 1, row= 2, pady=2, padx=(5,0))

        self.Jolteon_13. grid (column= 2, row= 2, pady=2, padx=(0,0))
        self.Turtle_14. grid (column= 3, row= 2, pady=2, padx=(0,0))
        self.Armor_15. grid (column= 4, row= 2, pady=2, padx=(0,0))
        self.Asate_16. grid (column= 5, row= 2, pady=2, padx=(0,0))
        self.Raon_17. grid (column= 6, row= 2, pady=2, padx=(0,0))
        self.Trico_18. grid (column= 7, row= 2, pady=2, padx=(0,0))
        self.Nak_19. grid (column= 8, row= 2, pady=2, padx=(0,0))
        self.Big_20. grid (column= 9, row= 2, pady=2, padx=(0,0))
        self.Dragon1_21. grid (column= 10, row= 2, pady=2, padx=(0,0))
        self.Dragon2_22. grid (column= 11, row= 2, pady=2, padx=(0,5))


    def Movil_trico(self):
        pass

#__________________________________________

def main ():

    app_1 = Interfaz ()  
    #app_1 . mainloop ()    
#___________________________________________

if __name__=="__main__":
    main ()
   
