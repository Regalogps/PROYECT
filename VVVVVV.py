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


class Principal(Tk):

    def __init__(self):
        super().__init__()

        path = 'E:/1-RICHI/MovilesDB'
        self.images = self.array(path, "todo")

        self.imgs_copy = self.array(path, "nada")
        
        #print(len(self.images))
        #self.imgs_copy = self.images .copy()
        # aquí creo una copia de self.images -
        # llamada: self.imgs_copy

        #frame = Example(self) 
        #frame .pack()
        self.lista = self.fotos()
        #print(len(self.lista))
       

    def array (self, file, option):   # Metodo para leer todas las imageneS ------NO TOCAR
    
        pictures = os.listdir (file)
        self.list_0 = [] 
        self.list_1 = [] 

        if option == "todo" :
            for i in pictures:
                if ".jpg" in i or ".png" in i:        

                    full = file + '/' + i

                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    array = Image.fromarray (RGB)
                    img = ImageTk.PhotoImage (array)

                    self.list_0 .append (img)
            return self.list_0

        if option == 'nada':
            for i in pictures:
                if '.jpg' in i or '.png' in i:                         # VER SI ES NECESARIO SACAR DE LA LISTA A RUEDA Y AL LOGO
                    full = file + '/' + i
 
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    array = Image.fromarray (RGB)
                    #img = ImageTk.PhotoImage (array)

                    self.list_1 .append (array)
            return self.list_1
        

    '''
    class Example(Frame):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # se supone que en este punto el atributo self.images existe
            # y ya está inicializado con una lista de imágenes. Vamos a 
            # inicializar ahora la lista de imgs
            self.imgs = []

    '''
    def fotos (self):
        self.imgs = []

        for image in self.images:
            # Crear la imagen, reescalarla, etc.
            img = Label(self, image=image)
            img.bind('<Configure>',self.resize)
            img.pack(fill=BOTH, expand=YES)
            # Y añadir el resultado a la lista
            self.imgs.append(img)

        return self.imgs

    def resize(self,event):
        self.lista2 = []
        # En este punto se supone que existe una lista llamada 
        # self.imgs_copy,que es una copia de self.images
        for img_copy in self.imgs_copy:
            pass
          # ImageTk.PhotoImage(img_copy.resize((self.master.winfo_width(), self.master.winfo_height()))
        # Me quedó en este punto,¿que más debería definir en este ciclo for




def main (): #--------------------------------------------------------------------NO TOCAR 
    app = Principal()    
    app .mainloop()

if __name__=="__main__":  #-------------------------------------------------------NO TOCAR 
    main()
   