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


class claseA(Tk):

    def __init__(self):      
        Tk. __init__(self)                     
        self. configurar_interfaz()
        self. widget_creator()                   

    def configurar_interfaz(self):  
        pass                                         

    def widget_creator(self):                    
        self.frame_plomo = claseB (self)        
        self.frame_plomo . grid ()
   
    def Metodo(self):                
        if self.frame_plomo.winfo_ismapped():      
            self.frame_plomo.grid_remove()    
        else:
            self.frame_plomo.grid()   
        

class claseB (Frame, claseA): 

    def __init__(self, parent):
        Frame.__init__(self, parent)    

    def BOTON_1(self):
        self.img_ash = Button (self , command= self.Metodo_Logo) . grid()

if __name__=="__main__":
    
    app= claseA()  
    app . mainloop ()     
