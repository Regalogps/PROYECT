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



global Lista2
Lista2 = None

global is_on
is_on = True


class Interfaz_juego(Tk):

    def __init__(self):
        
        Tk. __init__(self)                     # Llamando a Tkkkkk

        
        self.path_1 = "E:/1-RICHI/MovilesDB"      # Ruta de la carpeta que tiene todas las imagenes

        global Lista2
        Lista2 = self.Leer_folder(self.path_1)     # Llamando a la metodo Leer_forder y guardandola en una variable el return : Lista2
        self. configurar_interfaz()
        self. widget_creator()                   # Llamando a la metodo de configuracion de la ventana raiz

    def configurar_interfaz(self):                   # Configuracion de la ventana principal , no tiene nada mas                        
        
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


    def Leer_folder (self, path):                # Funcion para leer todas las imagenes 

        Imagenes = os.listdir(path)
        self.Lista1 = []              
        
        for i in Imagenes:
            ruta_completa = path + "/" + i

            #print (ruta_completa)

            Abrir = cv2.imread (ruta_completa)
            Rgb = cv2.cvtColor (Abrir, cv2.COLOR_BGR2RGB)
            Objeto = Image.fromarray (Rgb)

            Photo = ImageTk.PhotoImage(Objeto)

            self.Lista1. append (Photo)

        return self.Lista1
        

    def widget_creator(self):                    # Objetos creados de la clase Frame

        self.marco = Frame (self, width= 50 , height=50)
        self.marco . grid (column=1, row= 1)
        self.marco . grid_propagate (0)
    
        self.frame_inicial = Class_Frame (self, bg="#11161d", width=60, height=65)       # Frama inicial donde se aloja el boton del LOGO "Ash"
        self.frame_inicial . btn_img_rueda ()                                                       # boton config                                                                          
        self.frame_inicial . btn_img_ash()                                                           # boton logo ash
        self.frame_inicial . grid (column= 0, row= 0, padx=(0,0), pady=(0,0))
        self.frame_inicial . grid_propagate (0)

        self.frame_plomo = Class_Frame (self, bg="#31343a", width=756, height=65)        # Frame inicial donde se aloja el frame que tiene alos botones
        self.frame_plomo . grid (column= 1, row= 0, padx=0, pady=0, sticky="n")
        self.frame_plomo . grid_propagate (0)

        self.contenedor_de_botones = Class_Frame (self.frame_plomo, bg = "#11161d",)     # Frame contenedor de los botones 
        self.contenedor_de_botones . btn_moviles ()                                                  # botones de los moviles
        self.contenedor_de_botones . grid (padx = (10,0), pady = (6,0))  

        print (isinstance(self.frame_inicial, Frame))

    def Config_frame_inicial(self):

        self.winfo = self.frame_inicial . winfo_reqheight()
         
        if self.winfo == 65:
            self.frame_inicial . config(width=60, height=165)
    
        else:
            self.frame_inicial . config(width=60, height=65)


    def Metodo_Logo2(self):
            
        global is_on
        
        if is_on:
            self.img_ash . config (image = Lista2[107])  
            is_on = False

        else:
            self.img_ash . config (image = Lista2[109]) 
            is_on = True
        '''
        
        if self.frame_plomo.winfo_ismapped():      
            self.frame_plomo.grid_remove()
    
        else:
            self.frame_plomo.grid() 

        '''
    def Metodo_Logo(self):  

        

        if self.marco.winfo_ismapped():      
            self.marco.grid_remove()
    
        else:
            self.marco.grid()   
        
#______________________________________________________________________________________________________________________________________________________________________________________

class Class_Frame (Frame, Interfaz_juego):     # hereda primordialmente de Frame y despues hereda de Class interfaz porque tiene todas las imagenes

    def __init__(self, parent, **kwargs):

        Frame.__init__(self, parent, **kwargs)     # **kwargs se usa para llamar a mas atributos en el momento de crear el objeto de la clase "Class_Frame"

        #self.master = master
        #Interfaz_juego. __init__(self)

    def btn_img_ash(self):
        self.img_ash = Button (self, image = Lista2 [107], bg="#11161d", bd=0, activebackground="#11161d" , command= self.Metodo_Logo)
        self.img_ash . grid(column= 0, row= 0, padx=3, pady=1)

            
    def btn_img_rueda(self):

        self.img_config = Button (self, image = Lista2 [110], bg="#11161d", bd=0, activebackground="#11161d", command= self.Config_frame_inicial)
        self.img_config . grid (column=0, row= 1)

        
    def btn_moviles(self):

        self.Frog_1 = Button (self, text="Frog", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Aperturas_Ventanas)
        self.Frog_1 . grid (column= 1, row= 1, pady=3, padx=(5,0))

        self.Fox_2 = Button (self, text="Fox", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)
        self.Fox_2. grid (column= 2, row= 1, pady=3, padx=(0,0))

        self.Boomer_3 = Button (self, text="Boomer", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)      
        self.Boomer_3. grid (column= 3, row= 1, pady=3, padx=(0,0))

        self.Ice_4 = Button (self, text="Ice", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Ice_4. grid (column= 4, row= 1, pady=3, padx=(0,0))

        self.JD_5 = Button (self, text="J.D", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.JD_5. grid (column= 5, row= 1, pady=3, padx=(0,0))

        self.Grub_6 = Button (self, text="Grub", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)   
        self.Grub_6. grid (column= 6, row= 1, pady=3, padx=(0,0))

        self.Light_7 = Button (self, text="Light", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width=10, bd=0, command= self.Movil_trico)       
        self.Light_7. grid (column= 7, row= 1, pady=3, padx=(0,0))

        self.Aduka_8 = Button (self, text="Aduka", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)       
        self.Aduka_8. grid (column= 8, row= 1, pady=3, padx=(0,0))

        self.Knight_9 = Button (self, text="Knight", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)      
        self.Knight_9. grid (column= 9, row= 1, pady=3, padx=(0,0))

        self.Calziddon_10 = Button (self, text="Kalsiddon", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Calziddon_10. grid (column= 10, row= 1, pady=3, padx=(0,0))

        self.Mage_11 = Button (self, text="Mage", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)    
        self.Mage_11. grid (column= 11, row= 1, pady=3, padx=(0,5))


        self.Randomizer_12 = Button (self, text="Randomizer", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Randomizer_12. grid (column= 1, row= 2, pady=2, padx=(5,0))

        self.Jolteon_13 = Button (self, text="Jolteon", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)
        self.Jolteon_13. grid (column= 2, row= 2, pady=2, padx=(0,0))

        self.Turtle_14 = Button (self, text="Turtle", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Turtle_14. grid (column= 3, row= 2, pady=2, padx=(0,0))

        self.Armor_15 = Button (self, text="Armor", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Armor_15. grid (column= 4, row= 2, pady=2, padx=(0,0))

        self.Asate_16 = Button (self, text="A.Sate", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Asate_16. grid (column= 5, row= 2, pady=2, padx=(0,0))

        self.Raon_17 = Button (self, text="Raon", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Raon_17. grid (column= 6, row= 2, pady=2, padx=(0,0))

        self.Trico_18 = Button (self, text="Trico", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Trico_18. grid (column= 7, row= 2, pady=2, padx=(0,0))

        self.Nak_19 = Button (self, text="Nak", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Nak_19. grid (column= 8, row= 2, pady=2, padx=(0,0))

        self.Big_20 = Button (self, text="Big", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Big_20. grid (column= 9, row= 2, pady=2, padx=(0,0))

        self.Dragon1_21 = Button (self, text="Dragon 1", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)
        self.Dragon1_21. grid (column= 10, row= 2, pady=2, padx=(0,0))

        self.Dragon2_22 = Button (self, text="Dragon 2", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)
        self.Dragon2_22. grid (column= 11, row= 2, pady=2, padx=(0,5))


        



    def Aperturas_Ventanas(self):
        pass

    def Movil_trico(self):
        pass



#____________________________________________________________________________________________________________________________________________________________________________________


def main():

    app= Interfaz_juego ()  
    app . mainloop ()


        
#____________________________________________________________________________________________________________________________________________________________________________________

if __name__=="__main__":
    main ()
   
