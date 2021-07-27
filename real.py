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


global is_on
is_on = True

'''
        if self.Frame_root.winfo_ismapped():
            self.Frame_root.grid_remove()

            self.Boton_On_Off . place(x= 416, y= 0)
            self.buscador.place(x= 311, y= 0)        
        else:
            self.Frame_root.grid()

            self.Boton_On_Off . place(x= 416, y= 50)
            self.buscador.place(x= 311, y= 51)
'''
class Ventanas():

    def aperturas_Frog (self):

        self.apertura_1 ()        
        self.apertura_2 ()
        self.apertura_3 ()

#______________APERTURA___1____________________________________
    
    def apertura_1 (self):
            
        self.hoja1 = Toplevel()
        self.hoja1 . wm_attributes("-topmost", True)
        self.hoja1 . title("Izq")
        self.hoja1 . geometry("195x690")
        self.hoja1 . config(bg = "magenta2")
        self.hoja1 . resizable(1,1)
  
        trico_izquierda = cv2.imread ("1Trico.jpg")                          # Leyendo la imagen
        trico_IZQUIERDA = cv2.cvtColor (trico_izquierda, cv2.COLOR_BGR2RGB)  # Cambiando a RGB

        TRICO_IZQ = Image.fromarray (trico_IZQUIERDA)                        # Convierte la imagen en un objeto para utilizar

        self.COPIA_1 = TRICO_IZQ.copy()                             
        TRICO_IZQUIERDA = ImageTk.PhotoImage(TRICO_IZQ)                      # Insertando la imagen dendo del SCRIPT

        self.label1 = Label (self.hoja1, image = TRICO_IZQUIERDA)
        self.label1. bind ('<Configure>', self.resize_image_1)
        self.label1. pack (fill=BOTH, expand = YES) 
#____________________________________________________________________
                                                                     #   
        self._1_Frog.config(state= "disable")                        #
                                                                     #
        self.hoja1.protocol("WM_DELETE_WINDOW", self.cerrando)       #  
                                                                     #   
    def cerrando (self):                                             #                                           
            self.hoja1. destroy()                                    #
            self.hoja2. destroy()                                    #
            self.hoja3. destroy()                                    # 
                                                                     #  
            self._1_Frog.config(state= "normal")                     # 
#____________________________________________________________________#

    def resize_image_1 (self,event):
        new_width = event.width
        new_height = event.height

        Imagen1 = self.COPIA_1 . resize ((new_width, new_height))
        TRICO_IZQUIERDA_FUNCION = ImageTk.PhotoImage(Imagen1)

        self.label1.config(image = TRICO_IZQUIERDA_FUNCION)                  # Configurando el " Label
        self.label1.image = TRICO_IZQUIERDA_FUNCION                          # Configurando el " Label - no sabe bien


#______________APERTURA___2____________________________________

    def apertura_2 (self):

        self.hoja2 = Toplevel()
        self.hoja2 . wm_attributes("-topmost", True)
        self.hoja2 . title("Der")
        self.hoja2 . geometry("195x690")
        self.hoja2 . config(bg = "magenta2")
        self.hoja2 . resizable(1,1)
          
        trico_derecha = cv2.imread ("2Trico.jpg")                          
        trico_DERECHA = cv2.cvtColor (trico_derecha, cv2.COLOR_BGR2RGB) 

        TRICO_DER = Image.fromarray (trico_DERECHA)                        

        self.COPIA_2 = TRICO_DER.copy()                             
        TRICO_DERECHA = ImageTk.PhotoImage(TRICO_DER)                     

        self.label2 = Label (self.hoja2, image = TRICO_DERECHA)
        self.label2. bind ('<Configure>', self.resize_image_2)
        self.label2. pack (fill=BOTH, expand = YES) 
#____________________________________________________________________
        self._1_Frog.config(state= "disable")                        #                    
        self.hoja2.protocol("WM_DELETE_WINDOW", self.cerrando)       #
#____________________________________________________________________#
        
    def resize_image_2 (self,event):
        new_width = event.width
        new_height = event.height

        Imagen2 = self.COPIA_2 . resize ((new_width, new_height))
        TRICO_DERECHA_FUNCION = ImageTk.PhotoImage(Imagen2)

        self.label2.config(image = TRICO_DERECHA_FUNCION)                  
        self.label2.image = TRICO_DERECHA_FUNCION   

#______________APERTURA___3___________________________________

    def apertura_3 (self):

        self.hoja3 = Toplevel()
        self.hoja3 . wm_attributes("-topmost", True)
        self.hoja3 . title("Regla1")
        self.hoja3 . geometry("195x690")
        self.hoja3 . config(bg = "magenta2")
        self.hoja3 . resizable(1,1)

        trico_stuf = cv2.imread ("LOGONS.png")                          
        trico_STUF = cv2.cvtColor (trico_stuf, cv2.COLOR_BGR2RGB) 

        TRICO_GAME = Image.fromarray (trico_STUF)                        

        self.COPIA_3 = TRICO_GAME.copy()                             
        TRICO_GAME_STUFF = ImageTk.PhotoImage(TRICO_GAME)                     

        self.label3 = Label (self.hoja3, image = TRICO_GAME_STUFF)
        self.label3. bind ('<Configure>', self.resize_image_3)
        self.label3. pack (fill=BOTH, expand = YES) 
#____________________________________________________________________
        self._1_Frog.config(state= "disable")                        # 
        self.hoja3.protocol("WM_DELETE_WINDOW", self.cerrando)       #
#____________________________________________________________________#

    def resize_image_3 (self,event):
        new_width = event.width
        new_height = event.height

        Imagen3 = self.COPIA_3 . resize ((new_width, new_height))
        TRICO_GAME_STUF_FUNCION = ImageTk.PhotoImage(Imagen3)

        self.label3.config(image = TRICO_GAME_STUF_FUNCION)                  
        self.label3.image = TRICO_GAME_STUF_FUNCION 
        


#__________________________________________________

class Principal(Ventanas):

    def __init__(self):

        #ventana.overrideredirect(1)
        #ventana.attributes("-toolwindow",-1)
        

        root = Tk ()                                         # CAJA
        root. title ("_AshmanBot_")                          #  BORRAR
        root. geometry ("1000x150")                           # TAMANIO DE LA VENTANA
        root. resizable (1,1)                                # OTORGA PERMISO PARA CAMBIAR DE TAMANIO ALA VENTANA
        root. config (bg="magenta2")                         # CONFIGURA EL FONDO DE LA VENTANA, etc
        root. wm_attributes("-topmost", True)                # SUPERPONE LA VENTANA A OTRAS APLICACIONES ABIERTAS
        root.wm_attributes("-transparentcolor", "magenta2")  # BORRA EL COLOR SELECCIONADO DE LA VENTANA
        #root.attributes("-alpha", 0.5 )   
#_________________________________________________________________________
        path_1 = "E:/1-RICHI/MovilesDB"
        self.Leer_folder (path_1)       # Llamando a la funcion para que lea la carpetaa
#_________________________________________________________________________
     
        #self.Frame0 = Frame (root, bg="green", width=130, height=120)
        #self.Frame0 . grid(column= 0, row= 0)
        #self.Frame0 . grid_propagate(0)
        
        self.Cuadro_de_inicio = Frame (root, bg="#11161d", width=60, height=65)
        self.Cuadro_de_inicio . grid(column= 0, row= 0, padx=(0,0), pady=(0,0))
        self.Cuadro_de_inicio . grid_propagate(0)

        self.Configuracion = Button (self.Cuadro_de_inicio, image = self.Lista1[110],bg="#11161d", bd=0, activebackground="#11161d", command= self.Max_cuadro_inicial )
        self.Configuracion . grid (column=0, row= 1)
#_______________________________________________________


        #self.buscador = Spinbox(self.Cuadro_de_inicio)
        #self.buscador.config(width= 12)
        #self.buscador.grid(column = 0, row = 1, padx=(3,3), pady=(8,0))

        #self.dialogo = Label (self.Frame0, bg= "blue", width=0, height=50)
        #self.dialogo . grid (column=0, row=0)

#_______________________________________________________

        self.Fondo_plomo = Frame (root, bg="#282b30", width=756, height=65)    # Este frame es contenedor del contenedor de los botones COLOR plomo
        self.Fondo_plomo . grid (column= 1, row= 0, padx=0, pady=0, sticky="n")
        self.Fondo_plomo . grid_propagate (0)
        

        self.Botones = Frame (self.Fondo_plomo, bg = "#11161d")                  # Este frame es contenedor de los botones COLOR azul marino
        self.Botones . grid (padx = (10,0), pady = (6,0))
#_______________________________________________________

        self.Botones_off ()                                   # Llamando a la funcion

        root.mainloop ()
#_____________________________________METODOS  DE  PRINCIPAL__________________________________

    def Botones_off (self):           # BOTONES DE TODOS LOS MOVILES

        self.Frog_1 = Button (self.Botones, text="Frog", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.aperturas_Frog)
        self.Frog_1 . grid (column= 1, row= 1, pady=3, padx=(5,0))

        self.Fox_2 = Button (self.Botones, text="Fox", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)
        self.Fox_2. grid (column= 2, row= 1, pady=3, padx=(0,0))

        self.Boomer_3 = Button (self.Botones, text="Boomer", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)      
        self.Boomer_3. grid (column= 3, row= 1, pady=3, padx=(0,0))

        self.Ice_4 = Button (self.Botones, text="Ice", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Ice_4. grid (column= 4, row= 1, pady=3, padx=(0,0))

        self.JD_5 = Button (self.Botones, text="J.D", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.JD_5. grid (column= 5, row= 1, pady=3, padx=(0,0))

        self.Grub_6 = Button (self.Botones, text="Grub", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)   
        self.Grub_6. grid (column= 6, row= 1, pady=3, padx=(0,0))

        self.Light_7 = Button (self.Botones, text="Light", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width=10, bd=0, command= self.Movil_trico)       
        self.Light_7. grid (column= 7, row= 1, pady=3, padx=(0,0))

        self.Aduka_8 = Button (self.Botones, text="Aduka", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)       
        self.Aduka_8. grid (column= 8, row= 1, pady=3, padx=(0,0))

        self.Knight_9 = Button (self.Botones, text="Knight", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)      
        self.Knight_9. grid (column= 9, row= 1, pady=3, padx=(0,0))

        self.Calziddon_10 = Button (self.Botones, text="Kalsiddon", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Calziddon_10. grid (column= 10, row= 1, pady=3, padx=(0,0))

        self.Mage_11 = Button (self.Botones, text="Mage", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)    
        self.Mage_11. grid (column= 11, row= 1, pady=3, padx=(0,5))


        self.Randomizer_12 = Button (self.Botones, text="Randomizer", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Randomizer_12. grid (column= 1, row= 2, pady=2, padx=(5,0))

        self.Jolteon_13 = Button (self.Botones, text="Jolteon", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)
        self.Jolteon_13. grid (column= 2, row= 2, pady=2, padx=(0,0))

        self.Turtle_14 = Button (self.Botones, text="Turtle", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Turtle_14. grid (column= 3, row= 2, pady=2, padx=(0,0))

        self.Armor_15 = Button (self.Botones, text="Armor", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Armor_15. grid (column= 4, row= 2, pady=2, padx=(0,0))

        self.Asate_16 = Button (self.Botones, text="A.Sate", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Asate_16. grid (column= 5, row= 2, pady=2, padx=(0,0))

        self.Raon_17 = Button (self.Botones, text="Raon", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Raon_17. grid (column= 6, row= 2, pady=2, padx=(0,0))

        self.Trico_18 = Button (self.Botones, text="Trico", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Trico_18. grid (column= 7, row= 2, pady=2, padx=(0,0))

        self.Nak_19 = Button (self.Botones, text="Nak", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Nak_19. grid (column= 8, row= 2, pady=2, padx=(0,0))

        self.Big_20 = Button (self.Botones, text="Big", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.Movil_trico)
        self.Big_20. grid (column= 9, row= 2, pady=2, padx=(0,0))

        self.Dragon1_21 = Button (self.Botones, text="Dragon 1", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)
        self.Dragon1_21. grid (column= 10, row= 2, pady=2, padx=(0,0))

        self.Dragon2_22 = Button (self.Botones, text="Dragon 2", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.Movil_trico)
        self.Dragon2_22. grid (column= 11, row= 2, pady=2, padx=(0,5))

#______________________________BOTON PARA OCULTAR LOS BOTONES DE MOVILES____________________________

        self. Logo_Ash = Button (self.Cuadro_de_inicio, image = self. Lista1 [107], bg="#11161d", bd=0, activebackground="#11161d" , command= self.Metodo_Toggle)
        self. Logo_Ash . grid(column= 0, row= 0, padx=3, pady=1)     
#______________________________________
        
    def Leer_folder (self, path):      # Funcion para leer todas las imagenes 
        Imagenes = os.listdir(path)
        self.Lista1 = []              # OJO ver si es recomendable declarar la lista dentro de la funcion o afuera como una variable de clase
        
        for i in Imagenes:
            ruta_completa = path + "/" + i

            #print (ruta_completa)

            Abrir = cv2.imread (ruta_completa)
            Rgb = cv2.cvtColor (Abrir, cv2.COLOR_BGR2RGB)
            Objeto = Image.fromarray (Rgb)

            Photo = ImageTk.PhotoImage(Objeto)

            self.Lista1. append (Photo)

        return self.Lista1
#_____________________________________      
        
    
    def Metodo_Toggle (self):

        global is_on

        if is_on:
            self.Logo_Ash.config(image = self.Lista1[107])  
            is_on = False

        else:
            self.Logo_Ash.config(image = self.Lista1[107]) # aki es el 108 que seria OFF
            is_on = True


        if self.Botones.winfo_ismapped():
            self.Botones.grid_remove()
    
        else:
            self.Botones.grid()

#___________________________________
    def Movil_trico (self):  # BORRAR ESTA FUNCION 
        pass 
#___________________________________

    def Max_cuadro_inicial(self):
        self.Cuadro_de_inicio.config(width=60, height=100)

        


if __name__=="__main__":

    app = Principal()
    

    
