from tkinter import *
#from tkinter import Label, Frame, Spinbox, Listbox, Checkbutton, StringVar, IntVar
#from typing import Sized
from PIL import ImageTk, Image
import cv2
import imutils
import numpy as np
import os 

class App(Frame):
    def __init__(self, parents, *args, **kwargs):
        Frame.__init__(self, parents, *args, kwargs)

        path = 'E:/1-RICHI/MovilesDB'
        #_____Lista de Imágenes         
        self.Images_1 = self.generate_list (path, 'a')                          # Lista de imgs para las ventanas: 1 y 2
        self.Images_sublist= self.generate_list (path, 's')                     # Lista de imgs para la ventana: Interface
        self.Miniatures= self.generate_list (path, 'z') 


        e = Frm_B3_class (self)
        e . pack()

    def generate_list (self, file, option):   # INICIALIZA IMAGENES

        ouput = os.listdir (file)
        empty = [] 
                     
        if option == 'a': 
            _lst = [[] for x in range(22)]
            _str = ['Fro','Fox','Boo','Ice','JD','Gru','Lig','Adu','Kni','Kal','Mag','Ran','Jol','Tur','Arm','Asa','Rao','Tri','Nak','Big','Dr1','Dr2']
            for i in ouput:               
                for index,iter in enumerate(_str):
                    if iter in i: 
                        full = file + '/' + i
                        open = cv2.imread (full)
                        RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB) 
                        _lst[index].append(RGB)               
            return _lst        
           
        if option == 's':
            for i in ouput:
                #if i.split('.')[0] in ['SubList__00','SubList__01'] :  
                if 'SubList' in i :      
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    array = Image.fromarray (RGB)
                    img = ImageTk.PhotoImage (array)
                    empty. append (img)
            return empty


        if option == 'z':
            for i in ouput:  
                if 'Mini' in i :      
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    array = Image.fromarray (RGB)
                    img = ImageTk.PhotoImage (array)
                    empty. append (img)
            return empty




class Frm_B3_class(Frame):
    def __init__(self, parents, *args, **kwargs):
        Frame.__init__(self, parents, *args, kwargs)
    
        #_____C O N T E N E D O R E S:
        self.frm_B3 = Frame (self, bg='#31343a', width=172, height=65)     # Color: Plomo       
        self.frm_C1 = Frame (self, bg='#11161d', width=60, height=65)      # Color: Azul  #11161d

        #_____L A B E L:  NUMERO DE FILAS EXISTENTES   
        self.label_filas = Label (self.frm_B3, width=18, bg='#11161d', fg='#969696', bd=2, anchor= E) 

        #_____L A B E L:  SELECCIONE MOBIL
        label_title = Label (self.frm_B3, text='Seleccione  Mobil :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)      

        #_____L A B E L:  MINIATURAS
        self.label_miniature = Label (self.frm_C1, image=self.master.Miniatures[0], bd= 0)                                                   



        #_____L I S T B O X  / POSICIONADO
        #self.listbox = listv 
        self.listbox = Listbox_class (self.label_filas, width=11, height=1)  
                           
        #_____S P I N B O X  / POSICIONADO
        #self.spinbox = spinv
        self.spinbox = Spinbox_class (self.frm_B3, width=13, bd=0)                             



        #__________Posicionamientos:
        self.frm_B3 .grid (column=0, row=0, padx=0, pady=0)
        self.frm_C1 .grid (column=1, row=0, padx=0, pady=0)

        self.label_filas .grid (column=0, row=0, padx=(0,5), pady=(0,2), sticky=N)  
        label_title .grid (column=0, row=1, padx=10, pady=(0,0), sticky=W)
        self.label_miniature .grid (padx=2, pady=3)

        self.listbox .grid ( padx=(19,0), pady=(0,5), sticky=N)
        self.spinbox .grid (column=0, row=2, padx=11, pady=(3,3), sticky=W)   

        #__________Propagación:
        ##self.frm_B3 .grid_propagate(False)
        ##self.frm_C1 .grid_propagate(False)
        self.label_filas .grid_propagate(False)
        self.listbox .grid_propagate(False)

                              
############################################################################################################################
############################################################################################################################  
#    
class Spinbox_class(Spinbox, Frm_B3_class):

    def __init__(self, master, **args):     
        Spinbox.__init__(self, master, **args)
        
        
        self.spinbox_variable = StringVar() # ?poner padre?
        self.spinbox_values = ['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage', 'Randomizer', 'Jolteon', 'Turtle', 'Armor','A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']
        self.all_register = (self.register(self.validate_text), '%P', '%S')

        self.config (values=self.spinbox_values,                                      # DESDE AQUI PARA ABAJO SE HACEN LLAMADAS
                     textvariable=self.spinbox_variable, 
                     validate='key', 
                     validatecommand=self.all_register,
                     justify='center',
                     wrap=True,
                     bd=0)                                                
              
        self.bind ('<Double-Button-1>', lambda *arg: self.delete(0, END))   # ACTIVA: CON DOBLE CLICK EN SPINBOX - LIMPIA SPINBOX
        self.bind ('<Return>', self.bind_spinbox)  # ACTIVA: CON TECLA ENTER - ABRE LAS VENTANAS
        self.bind ('<Return>', self.bind_listbox)  # ACTIVA: CON TECLA ENTER - SELECCIONA EL INDICE 0 DEL LISTBOX Y LLAMA AL METODO(EVENT) DEF SELF.BIND.SPINBOX   #||||||
       
        self.spinbox_variable .trace_add ('write', self.change_miniature)  
        self.spinbox_variable .trace_add ('write', lambda *arg: self.spinbox_variable.set (self.spinbox_variable.get() .capitalize()))   # INSERTA EL VALOR OBTENIDO EN MAYUSCULA EL PRIMER STRING
       

    def validate_text(self, text, arg): # HECHO     # ACTIVA: SIEMPRE QUE INSERTE TEXTO EN SPINBOX - NO PERMITE NUMEROS,SIMBOLOS,ESPACIOS Y CONTROLA LA CANTIDAD

        if all (i not in "0123456789[{!¡¿?<>(|#$%&),_-°'´}] +-*/=" for i in text) and len(text) < 14:   
            return True                                                 
        return False  
        
        # TRUE = PERMITIR
        # FALSE = DENEGAR

    def bind_listbox(self, event):  # HECHO     #ACTIVA: TECLA ENTER - SELECCIONA LISTBOX Y LLAMA A SELF.BIND.SPINBOX
 
        print('QUERIENDO ENTRAR A IFF BIND')
        listbox = self.listbox.get(0)
        spinbox = self .get()
        #print('valor de list:', listbox)
        #print('valor de spin:', spinbox)

        if listbox != spinbox and listbox != '':
            self .delete(0, END)
            self .insert(0, listbox)
            
        self.bind_spinbox(event)  

    def bind_spinbox(self, event): # HECHO   # ACTIVA: CON TECLA ENTER SI SPINBOX TIENE FOCO - ABRE LAS VENTANAS
        
        left = [Frog_left_off, Fox_left_off, Boomer_left_off, Ice_left_off, Jd_left_off, Grub_left_off, Lightning_left_off, Aduka_left_off, Knight_left_off, Kalsiddon_left_off, Mage_left_off, Randomizer_left_off, Jolteon_left_off, Turtle_left_off, Armor_left_off, Asate_left_off, Raon_left_off, Trico_left_off, Nak_left_off, Bigfoot_left_off, Barney_left_off, Dragon_left_off,]
        right = [Frog_right, Fox_right, Boomer_right, Ice_right, Jd_right, Grub_right, Lightning_right, Aduka_right, Knight_right, Kalsiddon_right, Mage_right, Randomizer_right, Jolteon_right, Turtle_right, Armor_right, Asate_right, Raon_right, Trico_right, Nak_right, Bigfoot_right, Barney_right, Dragon_right]
        stuf = [Frog_stuf, Fox_stuf, Boomer_stuf, Ice_stuf, Jd_stuf, Grub_stuf, Lightning_stuf, Aduka_stuf, Knight_stuf, Kalsiddon_stuf, Mage_stuf, Randomizer_stuf, Jolteon_stuf, Turtle_stuf, Armor_stuf, Asate_stuf, Raon_stuf, Trico_stuf, Nak_stuf, Bigfoot_stuf, Barney_stuf, Dragon_stuf]

        for index, i in enumerate(self.spinbox_values):
            if self .get() == i:
                self.master. windows_123(left[index], right[index], stuf[index]) 
                self .icursor(END)  # ESTA APRUEBA SI ES TOTLAMENTE NECESARIO 
  
    def change_miniature(self, *args):   # ACTIVA: SI SPINBOX_VARIABLE CAMBIA DE VALOR - BORRA LA LISTA DE LISTBOX, MANDA A LLAMAR A UPDATE Y CAMBIA LAS MINIATURAS

        spinbox = self.get() .capitalize()

        if spinbox == '':                                                          
            self.listbox .delete(0, END)  ##
        else:                                                                    
            list_new = []                                                       
            for index, i in enumerate(self.spinbox_values):                      
                if spinbox == i:                           
                    self.label_miniature .config(image= self.master.Miniatures[index])
                    self .icursor(END)
                if spinbox in i:
                    list_new .append(i)
                    print(list_new)

            if list_new != []:         
                self.update(list_new)

            if spinbox == 'As':  
                self.listbox.delete(0,1)

        if self.listbox.get(0) != spinbox and self.listbox.get(0) != '' or spinbox == '': 
            self.label_miniature .config(image= self.master.Miniatures[22])

        # print('111', self.spinbox_variable.get()) # DEVUELVE: PRIMER CARACTER EN MAYUSCULA
        # print('222', self.spinbox.get())          # DEVUELVE: PRIMER CARACTER EN MINUSCULA
 
    def update(self, list):  # ACTIVA: SI EL METODO CHANGE_MINIATURE LA MANDA A LLAMAR - BORRA LA LISTA DE LISTBOX EXISTENTE, AGREGA NUEVOS VALORES A LISTA Y BORRA DE NUEVO SI SE CUMPLE LA CONDICION
        
        self.listbox .delete(0, END)                                    # 1- BORRA LA LISTA DE LISTBOX
        print('entre estando vacio')
        for i in list:                                                  # 1- ITERANDO: 'list_new'.  2- INSERTANDO ITERADOR 'i' A LISTBOX.  
            self.listbox .insert(END, i) 
        if self.listbox.get(0) == self.spinbox_variable.get():  #|||
            self .delete(0, END) 

############################################################################################################################
############################################################################################################################
#       
class Listbox_class(Listbox, Frm_B3_class):    # HECHO

    def __init__(self, master, **kwargs):
        Listbox.__init__(self, master, **kwargs)
        
        self.config (font=('Calibri',9,'bold'), 
                     bg='#11161d', fg='#00ff00', 
                     borderwidth=0, bd=0,
                     highlightthickness=0,
                     highlightbackground='#11161d',
                     highlightcolor='#11161d',
                     selectbackground='#11161d', 
                     selectforeground='#ff8000', 
                     activestyle='none',  
                     justify='center',                                      
                     selectmode=SINGLE,
                     takefocus=0,
                     )   
 
        self.bind ('<<ListboxSelect>>', self.listbox_select)   # ACTIVA: CON CLICK IZQUIERDO EN EL LISTBOX - SELECCIONA 1 ITEM
        
    
    def listbox_select(self,event):  # HECHO   # ACTIVA: CON CLICK IZQUIERDO EN LISTBOX - 
       
        selection = self.get(ANCHOR)                                                                              
        
        if self.get(0,END) != ():      
            self.spinbox .delete(0, END) 
        self.spinbox .insert(0, selection)
        self.selection_clear(0,END)
 
        self.after(100, lambda: self.spinbox.focus_set())

        print('numero',self.size())

#__________________G L O S A R I O:
        # LISTBOX:    
        # width= 15 ---> NUMEROS DE CARACTERES PERMITIDOS
        # height= 1 ---> NUMERO DE FILAS OBSERVABLES
        # justify= 'center' ---> CENTRAR TEXTO INTERNO
        # highlightbackground= '#11161d' ---> COLOR DEL BORDE SIN FOCO
        # highlightthickness= 4 ---> TAMAÑO DEL BORDE EN PIXELES SIN FOCO
        # selectbackground= '#11161d' ---> COLOR DE BORDE CON FOCO
        # selectforeground= 'green2' ---> COLOR DE FONDO CON FOCO
        # activestyle= 'none' ---> SUBRAYADO DEL TEXTO CUANDO ES SELECCIONADO DESACTIVADO:'none'
#__________________
                   

root = Tk()
root.geometry('250x130+100+100')   
app =   App (root)
app . pack()
root.mainloop()                         
                  
    

    

    
 
