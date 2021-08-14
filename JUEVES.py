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


class Interfaz (Tk):

    def __init__(self): #-------------------------------------------------------------NO TOCAR     
        Tk. __init__(self)    # Llamando a Tk ()
        self. title("PRIMERPINRAAAAAA")
        self. config (bg = "magenta2")

        self.path_1 = "E:/1-RICHI/MovilesDB"      # Ruta de la carpeta de imagenes
        self.Imagenes = self.leer_folder(self.path_1, "total")  # Llama al Metodo y guarda en una varible las imagenes
        self.Imagenes_copia = self.leer_folder(self.path_1, "parcial")  # Llama al Metodo y guarda en una varible las imagenes
        self.crear_vent()

        

        self.listasss= self.for_img()

        
        #print (self.listasss)   ####  NO CUENTA
        #print (len(self.listasss)) ####  NO CUENTA



    def for_img(self):

        self.lista_label = [] 

        for i in self.Imagenes:
           
           img = Label(self, image = i)
           img.bind('<Configure>',self.resizes)
           #img.pack(fill=BOTH, expand=YES)
           
           self.lista_label.append(img)

        return self.lista_label


    
    def resizes(self,event):
        pass

    def leer_folder (self, path, lista):  # Metodo para leer todas las imageneS ------NO TOCAR

        imagenes = os.listdir(path)
        self.lista_parcial = [] 
        self.lista_total = [] 

        if lista == "parcial" :
            for i in imagenes:
                if ".jpg" in i or ".png" in i:        

                    ruta_completa = path + "/" + i               

                    abrir = cv2.imread (ruta_completa)
                    if abrir is None:                                     
                        continue
                    RGB = cv2.cvtColor (abrir, cv2.COLOR_BGR2RGB)
                    objeto = Image.fromarray (RGB)

                    self.lista_parcial. append (objeto)

            return self.lista_parcial

        if lista == "total" :
            for i in imagenes:
                if ".jpg" in i or ".png" in i:        # VER SI ES NECESARIO SACAR DE LA LISTA A RUEDA Y AL LOGO

                    ruta_completa = path + "/" + i
                    #print(ruta_completa)

                    abrir = cv2.imread (ruta_completa)
                    if abrir is None:                 #  if por si hay conflicto de algun tipo (observar)
                        continue
                    RGB = cv2.cvtColor (abrir, cv2.COLOR_BGR2RGB)
                    objeto = Image.fromarray (RGB)
                    photo = ImageTk.PhotoImage(objeto)

                    self.lista_total. append (photo)

            return self.lista_total
         
    def crear_vent (self):
        self.vent1 = Toplevel()
        self.vent1 . title("SEGUDDDDD")
        self.frame_derecha = Frame_boomer_DERECHA(self.vent1, width=150, height=150)  #frame
        self.frame_derecha.pack()

        #lavel = Label(self, image=self.Imagenes[4])
       # lavel . pack

###################################################################################################
###################################################################################################
###################################################################################################

class Frame_boomer_DERECHA (Frame, Interfaz):  #------------------------------- DERECHA :  BASE  /  77

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        
        #self.listasss
        self.listasss

       # VAR_1 = self.lista_de_label[4]
       # VAR_1.pack()

           #print(self.lista_label)
        #print(self.lista_label)
        #print(len(self.lista_label))


    def resizes(self,event):
        pass
    def resize(self,event):

        self.lista_2 = []
        new_width = event.width
        new_height = event.height

        for iterador in self.master.Imagenes_copia:
            oro = ImageTk.PhotoImage( iterador .resize((new_width, new_height)))   
            #self.lista_2.append(oro)
            #for ee in self.lista_label.config(image=oro):
            for ee in self.lista_label:
                tmr =  ee . config(image=oro)
                
                self.lista_2.append(tmr)

        print(self.lista_2)
           


       # self.label0 . config (image = var2)     # Configurando el " Label
        #self.label0 . image = var2 



app_1 = Interfaz()

app_1 . mainloop ()






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
        '''