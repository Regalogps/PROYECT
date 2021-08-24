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
        self.geometry('220x690')

        path = 'E:/1-RICHI/MovilesDB'
        self.images = self.array(path, "todo")

        self.imgs_copy = self.array(path, "nada")
        
        #print(len(self.images))
        #self.imgs_copy = self.images .copy()
        # aquí creo una copia de self.images -
        # llamada: self.imgs_copy

        #frame = Example(self) 
        #frame .pack()
        self.fotos()
        #print(len(self.lista))
        #self.lista
       
        
        #self.lista[1].pack(fill=BOTH, expand=YES)
        
    def fotos(self):    #print(self.imgs)
        self.imgs = []

        for image in self.images:        
            # Crear la imagen, reescalarla, etc.
            self.l1 = Label(self, image=image)
            self.l1 .bind('<Configure>',self.resize)
            self.l1 .pack(fill=BOTH, expand=YES)
            # Y añadir el resultado a la lista
            self.imgs.append(self.l1)
            
        return self.imgs

        #self.imgs[4]
        #self.imgs[4].pack(fill=BOTH, expand=YES)
    
    def resize(self,event):
        pass
        
        """ width = self.winfo_width()
        height = self.winfo_height()
    
        for ind in range(110):
            v = self.imgs_copy[ind] .resize((width, height))
            va = ImageTk.PhotoImage(v)
            self.imgs[ind] .config(image= va)
            self.imgs[ind] .image = va """




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
        



def main (): #--------------------------------------------------------------------NO TOCAR 
    app = Principal()    
    app .mainloop()

if __name__=="__main__":  #-------------------------------------------------------NO TOCAR 
    main()
   