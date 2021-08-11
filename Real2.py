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

class Interfaz (Tk):

    def __init__(self): #-------------------------------------------------------------NO TOCAR     
        Tk. __init__(self)    # Llamando a Tk ()

        self.path_1 = "E:/1-RICHI/MovilesDB"      # Ruta de la carpeta de imagenes
        self.Imagenes = self.leer_folder(self.path_1, "total")  # Llama al Metodo y guarda en una varible las imagenes
        self.Imagenes_copia = self.leer_folder(self.path_1, "parcial")  # Llama al Metodo y guarda en una varible las imagenes

        # Llamando a las Metodos de Configuracion 
        self. configurar_interfaz()          
        self. widgets()   

#__________________________anadiendo
# 
        self._frame = None
        #self.switch_frame() 
        
#______________
        self.estado_1 = True  
        self.estado_2 = True  

 
        self.mainloop ()


    def configurar_interfaz(self):   # Configuracion de la ventana -------------------NO TOCAR (despues)
      
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


    def leer_folder (self, path, lista):  # Metodo para leer todas las imageneS ------NO TOCAR

        imagenes = os.listdir(path)
        self.lista_parcial = [] 
        self.lista_total = [] 

        if lista == "parcial" :
            for i in imagenes:
                ruta_completa = path + "/" + i               
                #print (ruta_completa)

                abrir = cv2.imread (ruta_completa)
                RGB = cv2.cvtColor (abrir, cv2.COLOR_BGR2RGB)
                objeto = Image.fromarray (RGB)

                self.lista_parcial. append (objeto)

            return self.lista_parcial

        if lista == "total" :
            for i in imagenes:
                ruta_completa = path + "/" + i

                abrir = cv2.imread (ruta_completa)
                RGB = cv2.cvtColor (abrir, cv2.COLOR_BGR2RGB)
                objeto = Image.fromarray (RGB)
                photo = ImageTk.PhotoImage(objeto)

                self.lista_total. append (photo)

            return self.lista_total
        

    def widgets(self):  # widgets de la ventana Principal ----------------------------NO TOCAR  EDITAR DESPUES A CLASE BOTON O LABEL

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
     

    def configurar_height(self):  # Metodo para configurar Frame ---------------------NO TOCAR

        self.winfo = self.frame_inicial . winfo_reqheight()
         
        if self.winfo == 65:
            self.frame_inicial . config(width=60, height=165)   
        else:
            self.frame_inicial . config(width=60, height=65)


    def remover_frame(self):  # Metodo para Remover Frame ----------------------------NO TOCAR

        if self.frame_plomo.winfo_ismapped():      
            self.frame_plomo.grid_remove()   
        else:
            self.frame_plomo.grid()  


    def switch_frame(self, frame_class):

        new_frame = frame_class(self) #

        if self._frame is not None: #
            self._frame.destroy()  #

        self._frame = new_frame
        self._frame.pack()









    def ventanass(self, argumento_frame):

        if self.estado_1 == True: 
            self.Vent_IZQUIERDA = Ventanas_Toplevel()  # VENTANA TOPLEVEL

            self.estado_1 = False     
                                    
            nuevo_frame = argumento_frame(self.Ventana_izquierdAAA)  # ES UN FRAME POSICIONADO EN TOPLEVEL

            if self._frame is not None:
                self._frame.destroy()
                self._frame = nuevo_frame
                self._frame.pack()


            self.boomer.protocol("WM_DELETE_WINDOW",self.cerrar_1)


#___ ventana DERECHA

        if self.estado_2 == True:
            self.Vent_DERECHA = Ventanas_Toplevel()  # VENTANA TOPLEVEL

            self.estado_2=False

            nuevo_frame = argumento_frame(self.Ventana_izquierdAAA)  # ES UN FRAME POSICIONADO EN TOPLEVEL

            if self._frame is not None:
                self._frame.destroy()
                self._frame = nuevo_frame
                self._frame.pack()

            self.ice.protocol("WM_DELETE_WINDOW",self.cerrar_2)
 
#__________Metodo para eliminar la ventana

    def cerrar_1(self):
        self.boomer.destroy()
        self.estado_1=True

    def cerrar_2(self):
        self.ice.destroy()
        self.estado_2=True









#_______________________________________
    def abrir_toplevel (self,boton):    #
#_______________________________________#
        try: 
            self.Ventana_izquierda.winfo_viewable() 
            
        except Exception as err:        
#____________________________________


            self.Ventana_izquierda = Ventanas_Toplevel()  # CREANDO <---VENTANA IZQUIERDA---> (TOPLEVEL)                                                                        # despues iba  #self.hoja1.transient(self) #__desde aqui es mi codifgo           
            # Llamando alos metodos de clase : TOPLEVEL:

            self.Ventana_izquierda . configurar_toplevel("izq","205x690")  # CONFIGURANDO LA VENTANA IZQUIERDA

            if boton == 1:
                
                self.sapo = Frame_frog(self.Ventana_izquierda) # CREO EL FRAME Y LO POSICIONO EN VENTANA IZQ
                self.sapo . grid (column=0, row=0)
                

            if boton == 2:
                self.fox = Frame_fox(self.Ventana_izquierda) # CREO EL FRAME
                self.fox . grid (column=0, row=0)
                

        '''
#____________________________________
        try:        
            self.Ventana_derecha.winfo_viewable()  #-----------------------codifo recuperado

        except Exception as err:         
#____________________________________

            self.Ventana_derecha = Ventanas_Toplevel()  # CREANDO <---VENTANA DERECHA---> (TOPLEVEL)
            # Llamando alos metodos de clase : TOPLEVEL:


            self.Ventana_derecha . configurar_toplevel("der","195x690") 
            #self.hoja2.
        
#____________________________________
        try:  
            self.Ventana_stuff.winfo_viewable()  

        except Exception as err:  
#____________________________________

            self.Ventana_stuff = Ventanas_Toplevel()  # CREANDO <---VENTANA GAME STUF---> (TOPLEVEL)
            # Llamando alos metodos de clase : TOPLEVEL:
            

            self.Ventana_stuff . configurar_toplevel("stuf","700x190")
        '''

   
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-

class Ventanas_Toplevel (Toplevel):

    def __init__(self, *args, **kwargs): #---------------------------------------------------------NO TOCAR 
        Toplevel. __init__(self, *args, **kwargs) 
        #self.masters = masters
          
    def configurar_toplevel(self,titulo,tamano): #--------------------------------NO TOCAR (despues)

        self . wm_attributes("-topmost", True)
        self . title(titulo)
        self . geometry(tamano)
        self . config(bg = "magenta2")
        self . resizable(1,1)
        self . wm_attributes("-transparentcolor", "magenta2")

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

        self.label0 . config (image = var2)     # Configurando el " Label
        self.label0 . image = var2 



#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-

class Create_Frame (Frame):   

    def __init__(self, parent, **kwargs): #---------------------------------------NO TOCAR (despues) 
        Frame.__init__(self, parent, **kwargs)   # Llamando a Frame ()  #, **kwargs : pasar mas valores al momento de la llamada (diccionarios)
        #self.master = master
        

    def btn_img_ash(self):  # Metodo que crea -1- Boton (logo) -------------------NO TOCAR (despues)
        
        self.img_ash = Button (self, image = self.master.Imagenes [107], bg="#11161d", bd=0, activebackground="#11161d" , command= self.master.remover_frame)
        self.img_ash . grid(column= 0, row= 0, padx=3, pady=1)

            
    def btn_img_rueda(self):  # Metodo que crea -1- Boton (rueda)-----------------NO TOCAR (despues)

        self.img_config = Button (self, image = self.master.Imagenes [110], bg="#11161d", bd=0, activebackground="#11161d", command= self.master.configurar_height)
        self.img_config . grid (column=0, row= 1)

        
    def btn_moviles(self):  # Metodo que crea -22- Botones (moviles)  #command = lambda:images(1))

        self.Frog_1 = Button (self, text="Frog", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= lambda: self.master.master.abrir_toplevel(1))

        self.Fox_2 = Button (self, text="Fox", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= lambda: self.master.master.abrir_toplevel(2))

        self.Boomer_3 = Button (self, text="Boomer", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.ventanass)      

        self.Ice_4 = Button (self, text="Ice", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.ventanass)

        self.JD_5 = Button (self, text="J.D", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.abrir_toplevel)

        self.Grub_6 = Button (self, text="Grub", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.abrir_toplevel)   

        self.Light_7 = Button (self, text="Light", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width=10, bd=0, command= self.master.master.abrir_toplevel)       

        self.Aduka_8 = Button (self, text="Aduka", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.abrir_toplevel)       

        self.Knight_9 = Button (self, text="Knight", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.master.master.abrir_toplevel)      

        self.Calziddon_10 = Button (self, text="Kalsiddon", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.abrir_toplevel)

        self.Mage_11 = Button (self, text="Mage", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.abrir_toplevel)    
   

        self.Randomizer_12 = Button (self, text="Randomizer", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.abrir_toplevel)
 
        self.Jolteon_13 = Button (self, text="Jolteon", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.master.master.abrir_toplevel)
 
        self.Turtle_14 = Button (self, text="Turtle", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.abrir_toplevel)

        self.Armor_15 = Button (self, text="Armor", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.abrir_toplevel)

        self.Asate_16 = Button (self, text="A.Sate", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.abrir_toplevel)

        self.Raon_17 = Button (self, text="Raon", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.abrir_toplevel)
 
        self.Trico_18 = Button (self, text="Trico", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.abrir_toplevel)

        self.Nak_19 = Button (self, text="Nak", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.abrir_toplevel)
 
        self.Big_20 = Button (self, text="Big", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= self.master.master.abrir_toplevel)
 
        self.Dragon1_21 = Button (self, text="Dragon 1", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.master.master.abrir_toplevel)
 
        self.Dragon2_22 = Button (self, text="Dragon 2", font=("Calibri",9,"bold"), bg="#11161d", fg="yellow", width= 10, bd=0, command= self.master.master.abrir_toplevel)

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



class Frame_frog (Frame): 

    def __init__(self, master):
        Frame.__init__(self, master)

        self.label_base = Label(self, image= self.master.master.Imagenes [0], bd=0)
        self.label_base . grid(column=0, row=0)
        self.label_base . grid_propagate(0)

        self.label_medir = Label(self, image= self.master.master.Imagenes [1], bd=0)       
        #self.label_medir . grid(column=0, row=0, sticky="n")
        
        self.label_ocultar = Label(self.label_base, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.label_ocultar . bind("<Button-1>", self.ocultar)
        self.label_ocultar . grid(column=0, row=0, padx=2, pady=61)
        self.label_ocultar . grid_propagate (0)
        
    def ocultar (self, event=None): 

        if self.label_medir . grid_info() != {}:  # Metodo de mapeado     
            self.label_medir . grid_forget()      # Metodo para ocultar # Este metodo devuelve {} si es
        else:
            self.label_medir . grid(column=0, row=0, sticky="n")


#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_           

class Frame_fox (Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.label_base = Label(self, image= self.master.master.Imagenes [4], bd=0)
        self.label_base . grid(column=0, row=0)
        self.label_base . grid_propagate(0)

        self.label_medir = Label(self, image= self.master.master.Imagenes [5], bd=0)
        #self.label_medir . grid(column=0, row=0, sticky="n")

        self.label_ocultar = Label(self.label_base, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  
        self.label_ocultar . bind("<Button-1>", self.ocultar)
        self.label_ocultar . grid(column=0, row=0, padx=2, pady=61)
        self.label_ocultar . grid_propagate (0)

    def ocultar (self, event=None): 

        if self.label_medir . grid_info() != {}:  # Metodo de mapeado 
            self.label_medir . grid_forget()      # Metodo para ocultar
        else:
            self.label_medir . grid(column=0, row=0, sticky="n")




def main (): #--------------------------------------------------------------------NO TOCAR 

    app_1 = Interfaz ()    
#___________________________________________

if __name__=="__main__":  #-------------------------------------------------------NO TOCAR 
    main ()
   
