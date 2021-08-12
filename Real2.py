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

#____________________anadiendo al CONSTRUCTOR
# 
        self.__frame_1 = None
        self.__frame_2 = None
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
        self. attributes("-topmost", True)                 # SUPERPONE LA VENTANA A OTRAS APLICACIONES ABIERTAS
        self. wm_attributes("-transparentcolor", "magenta2")  # BORRA EL COLOR SELECCIONADO DE LA VENTANA
        #root.attributes("-alpha", 0.5 )          


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







#___ VENTANA TOPLEVEL IZQUIERDA

    def ventanass(self, var_1, var_2):

        if self.estado_1 == True: 
            self.TopLevel_IZQUIERDA = Ventanas_Toplevel()  # VENTANA TOPLEVEL
            self.TopLevel_IZQUIERDA . configurar_toplevel("izq", "210x690")

            self.estado_1 = False     
                                    
            nuevo_frame_izq = var_1(self.TopLevel_IZQUIERDA)  # ES UN FRAME POSICIONADO EN TOPLEVEL

            if self.__frame_1 is not None:  # Si frame_1 YA NO ES NONE ejecuta:
                self.__frame_1 . destroy()
            self.__frame_1 = nuevo_frame_izq
            self.__frame_1 . pack()


            self.TopLevel_IZQUIERDA.protocol("WM_DELETE_WINDOW",lambda:self.cerrar_1(1))
        
       


#___ VENTANA TOPLEVEL DERECHA

        if self.estado_2 == True:
            self.TopLevel_DERECHA = Ventanas_Toplevel()  # VENTANA TOPLEVEL
            self.TopLevel_DERECHA . configurar_toplevel("der", "210x690")

            self.estado_2=False

            nuevo_frame_der = var_2(self.TopLevel_DERECHA)  # ES UN FRAME POSICIONADO EN TOPLEVEL

            if self.__frame_2 is not None:
                self.__frame_2 . destroy()
            self.__frame_2 = nuevo_frame_der
            self.__frame_2 . pack()

            self.TopLevel_DERECHA.protocol("WM_DELETE_WINDOW", lambda:self.cerrar_1(2))

        

        

# Metodo para eliminar la ventana

    def cerrar_1(self, number):

        if number== 1:
            self.TopLevel_IZQUIERDA.destroy()
            self.estado_1=True

        if number== 2:
            self.TopLevel_DERECHA.destroy()
            self.estado_2=True

        #if number== 3:
        #    self.TopLevel_.destroy()
        #    self.estado_2=True











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
        

   
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-

class Ventanas_Toplevel (Toplevel):

    def __init__(self, *args, **kwargs): #---------------------------------------------------------NO TOCAR 
        Toplevel. __init__(self, *args, **kwargs) 
        #self.masters = masters
          
    def configurar_toplevel(self,titulo,tamano): #--------------------------------NO TOCAR (despues)

        
        self . title(titulo)
        self . geometry(tamano)
        self . resizable(1,1)
        self . wm_attributes("-topmost", True)
        self . config(bg = "magenta2")
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

        self.Boomer_3 = Button (self, text="Boomer", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= lambda: self.master.master.ventanass(Frame_boomer_IZQUIERDA, Frame_boomer_DERECHA))     

        self.Ice_4 = Button (self, text="Ice", font=("Calibri",9,"bold"), bg="#11161d", fg="white", width= 10, bd=0, command= lambda: self.master.master.ventanass(Frame_ice))

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


################################            EL             ################################ 
################################          INICIO           ################################ 
################################   F R A M E  " F R O G "  ################################  

class Frame_frog_IZQUIERDA (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_DELAY = Label(self, image= self.master.master.Imagenes [0], bd=0)
        self.lbl_DELAY . grid(column=0, row=0)
        self.lbl_DELAY . grid_propagate(0)

        self.lbl_MEDIR = Label(self, image= self.master.master.Imagenes [1], bd=0)       
        self.lbl_MEDIR . grid(column=0, row=0, sticky="n")
        
        self.lbl_guia = Label(self.lbl_DELAY, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_guia . bind("<Button-1>", self.ocultar)
        self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_guia . grid_propagate (0)
        
    def ocultar_med (self, event=None): 

        if self.lbl_MEDIR . grid_info() == {}:  # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.lbl_MEDIR . grid(column=0, row=0, sticky="n")      # Metodo para ocultar # Este metodo devuelve {} si es 
        else:
            self.lbl_MEDIR . grid_forget()



class Frame_frog_DERECHA (Frame):  #------------------------------- DERECHA :  BASE  /  77

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_BASE = Label(self, image= self.master.master.Imagenes [2], bd=0)
        self.lbl_BASE . grid(column=0, row=0)
        self.lbl_BASE . grid_propagate(0)

        self.lbl_77 = Label(self, image= self.master.master.Imagenes [3], bd=0)       
        self.lbl_77 . grid(column=0, row=0, sticky="n")
        
        self.lbl_guia = Label(self.lbl_BASE, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_guia . bind("<Button-1>", self.ocultar)
        self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_guia . grid_propagate (0)
        
    def ocultar_med (self, event=None): 

        if self.lbl_77 . grid_info() == {}:  # Metodo de info de un widget
            self.lbl_77 . grid(column=0, row=0, sticky="n")      
        else:
            self.lbl_77 . grid_forget()



class Frame_frog_STUFF (Frame):  #-------------------------------- REGLA: GAME STUFF
     pass           



################################   F R A M E  " F O X "  ################################

class Frame_fox_IZQUIERDA (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_DELAY = Label(self, image= self.master.master.Imagenes [4], bd=0)
        self.lbl_DELAY . grid(column=0, row=0)
        self.lbl_DELAY . grid_propagate(0)

        self.lbl_MEDIR = Label(self, image= self.master.master.Imagenes [5], bd=0)       
        self.lbl_MEDIR . grid(column=0, row=0, sticky="n")
        
        self.lbl_guia = Label(self.lbl_DELAY, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_guia . bind("<Button-1>", self.ocultar)
        self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_guia . grid_propagate (0)
        
    def ocultar_med (self, event=None): 

        if self.lbl_MEDIR . grid_info() == {}:  # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.lbl_MEDIR . grid(column=0, row=0, sticky="n")      # Metodo para ocultar # Este metodo devuelve {} si es 
        else:
            self.lbl_MEDIR . grid_forget()



class Frame_fox_DERECHA (Frame):  #------------------------------- DERECHA :  BASE  /  77

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_BASE = Label(self, image= self.master.master.Imagenes [6], bd=0)
        self.lbl_BASE . grid(column=0, row=0)
        self.lbl_BASE . grid_propagate(0)

        self.lbl_77 = Label(self, image= self.master.master.Imagenes [7], bd=0)       
        self.lbl_77 . grid(column=0, row=0, sticky="n")
        
        self.lbl_guia = Label(self.lbl_BASE, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_guia . bind("<Button-1>", self.ocultar)
        self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_guia . grid_propagate (0)
        
    def ocultar_med (self, event=None): 

        if self.lbl_77 . grid_info() == {}:  # Metodo de info de un widget
            self.lbl_77 . grid(column=0, row=0, sticky="n")      
        else:
            self.lbl_77 . grid_forget()



class Frame_fox_STUFF (Frame):  #-------------------------------- REGLA: GAME STUFF
     pass           




################################   F R A M E  " B O O M E R "  ################################ 

class Frame_boomer_IZQUIERDA (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_DELAY = Label(self, image= self.master.master.Imagenes [8], bd=0)
        self.lbl_DELAY . grid(column=0, row=0)
        self.lbl_DELAY . grid_propagate(0)

        self.lbl_MEDIR = Label(self, image= self.master.master.Imagenes [9], bd=0)       
        self.lbl_MEDIR . grid(column=0, row=0, sticky="n")
        
        self.lbl_guia = Label(self.lbl_DELAY, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_guia . bind("<Button-1>", self.ocultar)
        self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_guia . grid_propagate (0)
        
    def ocultar (self, event=None): 

        if self.lbl_MEDIR . grid_info() == {}:  # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.lbl_MEDIR . grid(column=0, row=0, sticky="n")      # Metodo para ocultar # Este metodo devuelve {} si es 
        else:
            self.lbl_MEDIR . grid_forget()



class Frame_boomer_DERECHA (Frame):  #------------------------------- DERECHA :  BASE  /  77

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_BASE = Label(self, image= self.master.master.Imagenes [10], bd=0)
        self.lbl_BASE . grid(column=0, row=0)
        self.lbl_BASE . grid_propagate(0)

        self.lbl_77 = Label(self, image= self.master.master.Imagenes [11], bd=0)       
        self.lbl_77 . grid(column=0, row=0, sticky="ne")

        self.lbl_FLECHA = Label(self, image= self.master.master.Imagenes [108], bd=0)       
        self.lbl_FLECHA . grid(column=0, row=0, sticky="se")
     
        self.lbl_quitar_columna77 = Label(self.lbl_BASE, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_borrar_columna77 . bind("<Button-1>", self.ocultar)
        self.lbl_borrar_columna77 . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_borrar_columna77 . grid_propagate (0)
        
    def ocultar (self, event=None): 

        if self.lbl_77 . grid_info() == {} and self.lbl_FLECHA . grid_info() == {} :  # Metodo de info de un widget

            self.lbl_77 . grid(column=0, row=0, sticky="ne")
            self.lbl_FLECHA . grid(column=0, row=0, sticky="se")        
     
        else:
            self.lbl_77 . grid_forget()
            self.lbl_FLECHA . grid_forget()


       



class Frame_boomer_STUFF (Frame):  #-------------------------------- REGLA: GAME STUFF
     pass


################################  F R A M E  " I C E "  ################################

class Frame_ice_IZQUIERDA (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_DELAY = Label(self, image= self.master.master.Imagenes [12], bd=0)
        self.lbl_DELAY . grid(column=0, row=0)
        self.lbl_DELAY . grid_propagate(0)

        self.lbl_MEDIR = Label(self, image= self.master.master.Imagenes [13], bd=0)       
        self.lbl_MEDIR . grid(column=0, row=0, sticky="n")
        
        self.lbl_guia = Label(self.lbl_DELAY, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_guia . bind("<Button-1>", self.ocultar)
        self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_guia . grid_propagate (0)
        
    def ocultar(self, event=None): 

        if self.lbl_MEDIR . grid_info() == {}:  # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.lbl_MEDIR . grid(column=0, row=0, sticky="n")      # Metodo para ocultar # Este metodo devuelve {} si es 
        else:
            self.lbl_MEDIR . grid_forget()



class Frame_ice_DERECHA (Frame):  #------------------------------- DERECHA :  BASE  /  77

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lbl_BASE = Label(self, image= self.master.master.Imagenes [14], bd=0)
        self.lbl_BASE . grid(column=0, row=0)
        self.lbl_BASE . grid_propagate(0)

        self.lbl_77 = Label(self, image= self.master.master.Imagenes [15], bd=0)       
        self.lbl_77 . grid(column=0, row=0, sticky="ne")
        
        self.lbl_guia = Label(self.lbl_BASE, text="Guia", font=("Calibri",8,"bold"), bg="black" , fg="white", bd=0)  # Desaparece al presionarse error
        self.lbl_guia . bind("<Button-1>", self.ocultar)
        self.lbl_guia . grid(column=0, row=0, padx=2, pady=61)
        self.lbl_guia . grid_propagate (0)
        
    def ocultar (self, event=None): 

        if self.lbl_77 . grid_info() == {}:  # Metodo de info de un widget
            self.lbl_77 . grid(column=0, row=0, sticky="n")      
        else:
            self.lbl_77 . grid_forget()



class Frame_ice_STUFF (Frame):  #-------------------------------- REGLA: GAME STUFF
     pass



################################            EL             ################################ 
################################            FIN            ################################


def main (): #--------------------------------------------------------------------NO TOCAR 

    app_1 = Interfaz ()    

if __name__=="__main__":  #-------------------------------------------------------NO TOCAR 
    main ()
   
