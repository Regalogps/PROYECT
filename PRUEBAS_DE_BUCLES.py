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

        self.path_1 = "E:/1-RICHI/MovilesDB"      # Ruta de la carpeta de imagenes
        self.Imagenes = self.leer_folder(self.path_1, "total")  # Llama al Metodo y guarda en una varible las imagenes
        #self.Imagenes_copia = self.leer_folder(self.path_1, "parcial")  # Llama al Metodo y guarda en una varible las imagenes

        print(len(self.Imagenes))

  
    def leer_folder (self, path, lista): 

        imagenes = os.listdir(path)
        self.lista_parcial = [] 
        self.lista_total = [] 


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
            

        

        if lista == "parcial" :
            for i in imagenes:
                #if i . split(".")[-1] not in ["jpeg", "png"]:
                #    continue
                ruta_completa = path + "/" + i               
                #print (ruta_completa)

                abrir = cv2.imread (ruta_completa)
                if abrir is None:
                    continue
                RGB = cv2.cvtColor (abrir, cv2.COLOR_BGR2RGB)
                objeto = Image.fromarray (RGB)

                self.lista_parcial. append (objeto)

            return self.lista_parcial


app_1 = Interfaz ()    
app_1 . mainloop ()