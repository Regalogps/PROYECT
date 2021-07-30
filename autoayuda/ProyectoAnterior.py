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


#________________________VENTANA RAIZ_____________________________________________________________________________________________________
   
class Principal():

     def __init__(self):  

          self.root = Tk ()                          # CAJA
          self.root.wm_attributes("-topmost", True)  # SUPERPONE LA VENTANA A OTRAS APLICACIONES ABIERTAS
          self.root.title ("_AshmanBot_")            # TITULO
          self.root.geometry ("850x100")             # TAMANIO DE LA VENTANA
          self.root.resizable (1,1)                  # OTORGA PERMISO PARA CAMBIAR DE TAMANIO ALA VENTANA
          self.root.config (bg="magenta2")           # CONFIGURA EL FONDO DE LA VENTANA, etc
          
          self.root.wm_attributes("-transparentcolor", "magenta2")
          
          #self.ventana.overrideredirect(1)
          #self.ventana.attributes("-toolwindow",-1)

          
          

     

#________________________CHECK BUTTON____________________________________________________________________________________________________

          #Boton_abre_ventanas = Button (self.root, text="Select", bg="green2", fg="black", width= 8, command= self.Multiventanas_123)
         # Boton_abre_ventanas . pack()
          #Boton_abre_ventanas . place(x=1, y=1)

          Select = Checkbutton(self.root, text="Open", bg="green2", fg="black", width= 4, height=1, command= self.Multiventanas_123, )
          Select.configure(font=("Arial",9,"bold"))
          Select.grid(column= 0, row= 0, padx=0)

          self.apertura_1.opened= False

#__________________________BOTONES_______________________________________________________________________________________________________         

          _1_Frog = Button (self.root, text="Frog", bg="gray18", fg="white", width= 9, command= self.apertura_1)
          _1_Frog. configure(font=("Arial",8,"bold"))
          _1_Frog. grid(column= 1, row= 0, padx=0)

          _2_Fox = Button (self.root, text="Fox", bg="gray18", fg="yellow", width= 9, command= self.Movil_trico)
          _2_Fox. configure(font=("Arial",8,"bold"))
          _2_Fox. grid(column= 2, row= 0, padx=0)

          _3_Boomer = Button (self.root, text="Boomer", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _3_Boomer. configure(font=("Arial",8,"bold"))
          _3_Boomer. grid(column= 3, row= 0, padx=0)

          _4_Ice = Button (self.root, text="Ice", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _4_Ice. configure(font=("Arial",8,"bold"))
          _4_Ice. grid(column= 4, row= 0, padx=0)

          _5_JD = Button (self.root, text="J.D", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _5_JD. configure(font=("Arial",8,"bold"))
          _5_JD. grid(column= 5, row= 0, padx=0)

          _6_Grub = Button (self.root, text="Grub", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _6_Grub. configure(font=("Arial",8,"bold"))
          _6_Grub. grid(column= 6, row= 0, padx=0)

          _7_Light = Button (self.root, text="Light", bg="gray18", fg="white", width=9, command= self.Movil_trico)
          _7_Light. configure(font=("Arial",8,"bold"))
          _7_Light. grid(column= 7, row= 0, padx=0)

          _8_Aduka = Button (self.root, text="Aduka", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _8_Aduka. configure(font=("Arial",8,"bold"))
          _8_Aduka. grid(column= 8, row= 0, padx=0)

          _9_Knight = Button (self.root, text="Knight", bg="gray18", fg="yellow", width= 9, command= self.Movil_trico)
          _9_Knight. configure(font=("Arial",8,"bold"))
          _9_Knight. grid(column= 9, row= 0, padx=0)

          _10_Calziddon = Button (self.root, text="Kalsiddon", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _10_Calziddon. configure(font=("Arial",8,"bold"))
          _10_Calziddon. grid(column= 10, row= 0, padx=0)

          _11_Mage = Button (self.root, text="Mage", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _11_Mage. configure(font=("Arial",8,"bold"))
          _11_Mage. grid(column= 11, row= 0, padx=0)

          _12_Randomizer = Button (self.root, text="Randomizer", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _12_Randomizer. configure(font=("Arial",8,"bold"))
          _12_Randomizer. grid(column= 1, row= 1, padx=0)

          _13_Jolteon = Button (self.root, text="Jolteon", bg="gray18", fg="yellow", width= 9, command= self.Movil_trico)
          _13_Jolteon. configure(font=("Arial",8,"bold"))
          _13_Jolteon. grid(column= 2, row= 1, padx=0)

          _14_Turtle = Button (self.root, text="Turtle", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _14_Turtle. configure(font=("Arial",8,"bold"))
          _14_Turtle. grid(column= 3, row= 1, padx=0)

          _15_Armor = Button (self.root, text="Armor", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _15_Armor. configure(font=("Arial",8,"bold"))
          _15_Armor. grid(column= 4, row= 1, padx=0)

          _16_Asate = Button (self.root, text="A.Sate", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _16_Asate. configure(font=("Arial",8,"bold"))
          _16_Asate. grid(column= 5, row= 1, padx=0)

          _17_Raon = Button (self.root, text="Raon", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _17_Raon. configure(font=("Arial",8,"bold"))
          _17_Raon. grid(column= 6, row= 1, padx=0)

          _18_Trico = Button (self.root, text="Trico", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _18_Trico. configure(font=("Arial",8,"bold"))
          _18_Trico. grid(column= 7, row= 1, padx=0)

          _19_Nak = Button (self.root, text="Nak", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _19_Nak. configure(font=("Arial",8,"bold"))
          _19_Nak. grid(column= 8, row= 1, padx=0)

          _20_Big = Button (self.root, text="Big", bg="gray18", fg="white", width= 9, command= self.Movil_trico)
          _20_Big. configure(font=("Arial",8,"bold"))
          _20_Big. grid(column= 9, row= 1, padx=0)

          _21_Dragon1 = Button (self.root, text="Dragon 1", bg="gray18", fg="yellow", width= 9, command= self.Movil_trico)
          _21_Dragon1. configure(font=("Arial",8,"bold"))
          _21_Dragon1. grid(column= 10, row= 1, padx=0)

          _22_Dragon2 = Button (self.root, text="Dragon 2", bg="gray18", fg="yellow", width= 9, command= self.Movil_trico)
          _22_Dragon2. configure(font=("Arial",8,"bold"))
          _22_Dragon2. grid(column= 11, row= 1, padx=0)

          
          

         # _1_Frog = Button (self.root, text="Frog", bg="gray18", fg="cyan", width= 10, command= self.Movil_trico)
         # Boton_trico . pack()
#_____________________________________________________________________________________________________________________________________

          self.root.mainloop()

#________________________llAMADAS__________________________________________________________________________________________________

     def Multiventanas_123 (self):

          self.Apertura_1 ()
          self.Apertura_2 ()
          self.Apertura_3 ()

     def Movil_trico(self):

          self.abrir_imagen_1()
          self.abrir_imagen_2()
          self.abrir_imagen_3()

#______________APERTURA___1________________________________________________________________________________________________________________________

     def apertura_1 (self):
          if self.apertura_1.opened:
               return
          self.apertura_1.opened= True
          
          self.hoja1 = Tk()
          self.hoja1 . wm_attributes("-topmost", True)
          self.hoja1 . title("Izq")
          self.hoja1 . geometry("195x690")
          self.hoja1 . config(bg = "magenta2")
          self.hoja1 . resizable(1,1)

          self.frame1 = Frame(self.hoja1)
          self.frame1 . pack(fill= "both", expand=1)
          
          self.frame1 . config(bg="blue")



          self.label1 = Label(self.frame1)
          self.label1 . pack()



          self.hoja1.wait_window()

          self.apertura_1.opened= False

      
     
   

     def abrir_imagen_1 (self):

          tricoIZ = cv2.imread("1Trico.jpg")                      # Leyendo la imagen
          #tricoIZQ = imutils.resize(tricoIZ, height=500)          # Redimensionando la misma imagen
          tricoIZQ = cv2.cvtColor(tricoIZ, cv2.COLOR_BGR2RGB)    # Cambiando a RGB
         
          im2 = Image.fromarray(tricoIZQ)                         # Presentando la imagen NO SE SABE BIEN QUE HACE

          Trico_izquierda = ImageTk.PhotoImage(image = im2)        # Insertando la imagen dendo del SCRIPT
       
          self.label1.configure(image = Trico_izquierda)           # Configurando el " Label "
          self.label1.image = Trico_izquierda                      # LO MISMO AL PARECER NO SE SABE BIEN   

#______________APERTURA___2_______________________________________________________________________________________________________________________

     def Apertura_2 (self):

          self.hoja2 = Toplevel()
          self.hoja2 . wm_attributes("-topmost", True)
          self.hoja2 . title("Der")
          self.hoja2 . geometry("195x690")
          self.hoja2 . config(bg = "magenta2")
          self.hoja2 . resizable(1,1)
          self.label2 = Label(self.hoja2)
          self.label2 . pack()
          

     def abrir_imagen_2 (self):

          tricoDE = cv2.imread("2Trico.jpg")            
          tricoDER = imutils.resize(tricoDE, height=500) 
          tricoDER = cv2.cvtColor(tricoDER, cv2.COLOR_BGR2RGB)

          im3 = Image.fromarray(tricoDER)                   

          Trico_derecha = ImageTk.PhotoImage(image = im3)           

          self.label2.configure(image = Trico_derecha)                  
          self.label2.image = Trico_derecha                             

#______________APERTURA___3_______________________________________________________________________________________________________________________

     def Apertura_3 (self):

          self.hoja3 = Toplevel()
          self.hoja3 . wm_attributes("-topmost", True)
          self.hoja3 . title("Regla1")
          self.hoja3 . geometry("195x690")
          self.hoja3 . config(bg = "magenta2")
          self.hoja3 . resizable(1,1)
          self.label3 = Label(self.hoja3)
          self.label3 . pack()

     def abrir_imagen_3 (self):

          tricoGAM = cv2.imread("3Trico.jpg")            
          tricoGAME = imutils.resize(tricoGAM, height=500) 
          tricoGAME = cv2.cvtColor(tricoGAME, cv2.COLOR_BGR2RGB)

          im4 = Image.fromarray(tricoGAME)                   

          Trico_gamestuf = ImageTk.PhotoImage(image = im4)           

          self.label3.configure(image = Trico_gamestuf)                  
          self.label3.image = Trico_gamestuf                             
#_____________________________________________________________________________________________________________________________________________
  
          

     def salir (self):
          sys.exit()


if __name__ == "__main__":
     
     app = Principal()
     