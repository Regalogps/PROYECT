#_____________SELF.CHECKBUTTON 5 :  MODO LISTA

        #_____C O N T E N E D O R E S:  (NO POSICIONADOS)
        self.frm_B3 = Frame (self, bg='#31343a', width=172, height=65)   # NO POSICIONADO     # Color: Plomo       
        self.frm_C1 = Frame (self, bg='#11161d', width=60, height=65)    # NO POSICIONADO     # Color: Azul  #11161d
        
        # LABEL DE TITULO : SELECCIONE MOBIL
        label_title = Label (self.frm_B3, text='Seleccione  Mobil :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)      # POSICIONADO

        # LABEL CONTENEDOR DE LAS MINIATURAS
        self.label_miniature = Label (self.frm_C1, image= self.Miniatures[0], bd= 0)                                                  # POSICIONADO

        # S T R I N G V A R
        self.spinbox_variable = StringVar()

        # LISTA DE NOMBRES DE MOVIL
        self.spinbox_values = ['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage', 'Randomizer', 'Jolteon', 'Turtle', 'Armor','A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']

        # FUNCION PARA HACER VALIDACIONES DE ENTRADA:  S P I N B O X
        self.all_register = (self.register(self.validate_text), '%P', '%S')

        # L I S T B O X  / POSICIONADO
        self.listbox = Listbox (self.frm_B3, font=('Calibri',9,'bold'), bg='#11161d', fg='#ff8000', width=15, height= 1, justify='center', highlightbackground='#11161d', highlightthickness=4, borderwidth=0, bd=0, selectbackground='#11161d', highlightcolor='#11161d', selectforeground='green2', activestyle='none',
                                )
        #self.listbox.configure(takefocus=0)  ####

        # INSERTANDO VALORES A:  L I S T B O X
        #self.update(self.spinbox_values)

                                
        # S P I N B O X  / POSICIONADO
        self.spinbox = Spinbox (self.frm_B3, width=13, bd=0, justify='center', wrap=True,
                                values=self.spinbox_values,                                      # DESDE AQUI PARA ABAJO SE HACEN LLAMADAS
                                textvariable=self.spinbox_variable, 
                                validate='key', validatecommand= self.all_register)                             
        # BIND:
        self.spinbox .bind ('<Return>', self.bind_spinbox)                                  # SE ACTIVA SI SPINBOX TIENE FOCO, Y SE PRESIONA LA TECLA ENTER: ABRE LAS VENTANAS
        self.spinbox .bind ('<Double-Button-1>', lambda *arg: self.spinbox.delete(0, END))   # ACTIVAR SI SE HACE DOBLE CLICK EN LA CAJA(spinbox): LIMPIA LA CAA
        self.listbox .bind ('<<ListboxSelect>>', self.listbox_select)   # SE ACTIVAR AL DAR CLICK EN EL LISTBOX

        #self.spinbox .bind ('<Return>', self.bind_listbox) 

        


        self.spinbox .bind ("<KeyRelease>", self.chanse)

        # TRACE ADD:
        self.spinbox_variable .trace_add ('write', self.change_miniature)  
        self.spinbox_variable .trace_add ('write', lambda *arg: self.spinbox_variable.set (self.spinbox_variable.get() .capitalize()))   # # SE ACTIVA SI INTRODUCE TEXTO: CAMBIA POR MAYUSCULA EL PRIMER ARGUMENTO

        

        #______Propagación:
        self.frm_B3 .grid_propagate(False)
        self.frm_C1 .grid_propagate(False)

        #______Posicionamientos:
        label_title .grid (column= 0, row=1, padx= 10, pady=(0,0), sticky= W)
        self.label_miniature .grid (padx= 2, pady= 3)

        self.listbox .grid (column= 0, row= 0, padx= (0,2), pady=(0, 2), sticky= NSEW)
        self.spinbox .grid (column= 0, row=2, padx=11, pady=(3,3), sticky= W)        


#_______ G L O S A R I O:
        # LISTBOX:    
        # width= 15 ---> NUMEROS DE CARACTERES PERMITIDOS
        # height= 1 ---> NUMERO DE FILAS OBSERVABLES
        # justify= 'center' ---> CENTRAR TEXTO INTERNO
        # highlightbackground= '#11161d' ---> COLOR DEL BORDE SIN FOCO
        # highlightthickness= 4 ---> TAMAÑO DEL BORDE EN PIXELES SIN FOCO
        # selectbackground= '#11161d' ---> COLOR DE BORDE CON FOCO
        # selectforeground= 'green2' ---> COLOR DE FONDO CON FOCO
        # activestyle= 'none' ---> SUBRAYADO DEL TEXTO CUANDO ES SELECCIONADO DESACTIVADO:'none'
#_______

    def validate_text(self, text, arg):   # SE ACTIVA SIEMPRE Y CUANDO INTENTE INGRESAR MAYUSCULAS O CADENAS SUPERIORES A 13 / LO LLAMA SPINBOX

        if all (i not in "0123456789 " for i in text) and len(text) < 14:      # TRUE = PERMITIR, FALSE = DENEGAR   
                return True                                                 
        return False                                                         
                    
    def gear_stacking(self):   # SE ACTIVA CON LA RUEDA DE CONFIGURACION

        if  self.gear == True:          # PREDETERMINADO: TRUE
            self.frm_B1 .grid_remove()  # B1: BOTONES          
            self.frm_B3 .grid_remove()  # B3: LISTBOX    ###??? necesita if?
            self.frm_C1 .grid_remove()  # C1: MINIATURA

            self.frm_B2 .focus_set()    # NECESARIO 
            self.frm_B2 .grid (column= 1, row= 0, padx=0, pady=0, sticky= N)               
            self.gear = False
            self.geometry ('816x65')       
    
        else:
            self.frm_B2 .grid_remove()
            if self.checkbutton5.variable.get() == True:   
                self.frm_B3 .grid (column= 1, row= 0, padx=0, pady=0, sticky= NW)
                self.frm_C1 .grid (column= 1, row= 0, padx=0, pady=0, sticky= NE)
                self.spinbox .focus_set()   # AKI TRABAJAR
                self.spinbox .icursor(END)
                self.geometry ('232x65')
            else:
                self.frm_B1 .grid ()
                self.frm_B3 .grid_remove()
                self.frm_C1 .grid_remove()
                
            self.gear = True    
    
    def change_miniature(self,*args):   # SE ACTIVA CADA VEZ QUE MODIFICA LA CAJA DEL SPINBOX
             
        for index, i in enumerate(self.spinbox_values):      
            if self.spinbox.get().capitalize() == i:                           
                self.label_miniature .config(image= self.Miniatures[index])
                self.spinbox.icursor(END)
            else:
                self.label_miniature .config(image= '')
        
    def chanse (self, event):   # SE ACTIVA CADA QUE SE SUELTA UNA TECLA

        #self.listbox.config(state= NORMAL)
        value = self.spinbox.get()

        if value == '':
            print('me ejec')                                  # 1- SI SPINBOX ESTA VACIO.  2- BORRA LA LISTA DE LISTBOX.  3- DESHABILITA LISTBOX.
            self.listbox .delete (0, END)
            
            #self.listbox .config (state= DISABLED)#
            print('Limpiando listbox: ', self.listbox.get(0, END)) ##### probar después (0,END)
        else:                                            # 1- HABILITA LISTBOX.  2- CREA LISTA VACIA.  3- ITERANDO: 'self.spinbox_values'.
            #self.listbox .config (state= NORMAL)#        # 4- SI COINCIDE 'value' EN 'self.spinbox_values'.  5- AGREGA VALUE A LISTA.  6- SI LA LISTA NO ESTA VACIA. 
            list_new = []                                # 10- LLAMA AL METODO: 'def update' Y PASA LA LISTA DE ARGUMENTO. 
            print('tambien entro')                                             
            for i in self.spinbox_values:          
                if value in i:
                    #self.listbox .config (state= NORMAL)#aaaaaaaaaaaa
                    list_new .append(i)
                    print('Agregando a la lista: ', list_new) 
                    
                #else:
                  #  self.listbox .config (state= DISABLED)#

            if list_new != []:
                print('mando lista')             
                self.update(list_new)

    def cheeck_5 (self):   # SE ACTIVA MARCANDO LA CASILLA : SELF.CHEECKBUTTON 5  # ESTE METODO ESTA SIN USOOOOOOOOOOOOOOOOOO
        self.checkbutton5.value()

    def bind_spinbox (self, event):  # SE ACTIVA CUANDO SPINBOX TIENE FOCO Y SE PRESIONA LA TECLA ENTER: ABRE LAS VENTANAS
        
        left = [Frog_left_off, Fox_left_off, Boomer_left_off, Ice_left_off, Jd_left_off, Grub_left_off, Lightning_left_off, Aduka_left_off, Knight_left_off, Kalsiddon_left_off, Mage_left_off, Randomizer_left_off, Jolteon_left_off, Turtle_left_off, Armor_left_off, Asate_left_off, Raon_left_off, Trico_left_off, Nak_left_off, Bigfoot_left_off, Barney_left_off, Dragon_left_off,]
        right = [Frog_right, Fox_right, Boomer_right, Ice_right, Jd_right, Grub_right, Lightning_right, Aduka_right, Knight_right, Kalsiddon_right, Mage_right, Randomizer_right, Jolteon_right, Turtle_right, Armor_right, Asate_right, Raon_right, Trico_right, Nak_right, Bigfoot_right, Barney_right, Dragon_right]
        stuf = [Frog_stuf, Fox_stuf, Boomer_stuf, Ice_stuf, Jd_stuf, Grub_stuf, Lightning_stuf, Aduka_stuf, Knight_stuf, Kalsiddon_stuf, Mage_stuf, Randomizer_stuf, Jolteon_stuf, Turtle_stuf, Armor_stuf, Asate_stuf, Raon_stuf, Trico_stuf, Nak_stuf, Bigfoot_stuf, Barney_stuf, Dragon_stuf]

        for index, i in enumerate(self.spinbox_values):
            if self.spinbox.get() == i:
                self.windows_123(left[index], right[index], stuf[index]) 
                self.spinbox.icursor(END)  # ESTA APRUEBA SI ES TOTLAMENTE NECESARIO 
                
    def minimize_windows (self): # METODO LOGO -----------------> SE ACTIVA DANDO CLICK AL LOGO

        if self.open_1 == True or self.open_2 == True or self.open_3 == True:

            if self.minimize == False:
                if self.open_1 == True:
                    self.toplevel_LEFT.deiconify()   # MOSTRAR VENTANAS  
                if self.open_2 == True:
                    self.toplevel_RIGHT.deiconify()
                if self.open_3 == True:
                    self.toplevel_STUF.deiconify()

                self.minimize = True

            else: 
                if self.open_1 == True:
                    self.toplevel_LEFT.iconify()     # OCULTAR VENTANAS
                if self.open_2 == True:
                    self.toplevel_RIGHT.iconify() 
                if self.open_3 == True:    
                    self.toplevel_STUF.iconify()

                self.minimize = False

    def ash_close_windows(self, event):   # SE ACTIVA DANDO DOBLE CLICK DERECHO EN EL LOGO

        self.toplevel_LEFT. destroy() 
        self.open_1 = False

        self.toplevel_RIGHT. destroy()
        self.open_2 = False

        self.toplevel_STUF. destroy()
        self.open_3 = False

    def update(self, list):     # LISTBOX LIMPIAR Y AGREGAR
        print('update')
        self.listbox .delete(0, END)                                    # 1- BORRA LA LISTA DE LISTBOX

        for i in list:                                                  # 1- ITERANDO: 'list_new'.  2- INSERTANDO ITERADOR 'i' A LISTBOX.  
            self.listbox .insert(END, i)                                # 3- SI EL CONTENIDO QUE SE OBSERVA EN LISTBOX ES IGUAL SPINBOX.  4- BORRA LA LISTA DE LISTBOX.
                                                                        # 5- 
            if self.listbox .get(0) == self.spinbox_variable .get(): 
                self.listbox .delete (0, END)            
                #self.listbox .config (state= DISABLED)#

            #else:
               # self.listbox .config (state= NORMAL)#

            if self.listbox .winfo_viewable():
                pass
                #self.after(4000, lambda : self.listbox.see(1))
                #self.after(8000, lambda : self.listbox.see(0))
                ##self.after(12000, lambda : self.listbox.see(0)) 
            
        print('Lista procesada completa', list)

        
    def listbox_select(self,event):      # LISTBOX ENTRY
        print('lis select')                                                               # 1- BORRA EL CONTENIDO DE SPINBOX.  2- INSERTA EL ITEM SELECCIONADO DEL LISTBOX A SPINBOX                           
        if self.listbox.get(0,END) != ():
            self.spinbox.delete(0, END) 
        self.spinbox.insert(0, self.listbox.get(ANCHOR))  # ADD   COMO HABIA H AY SE EJECUTABA ESTO Y RETURN FOCUS
        
        self.listbox.selection_clear(0,END)
        self.listbox.delete(0,END)
        self.after(100, self.return_focus) ### probar sin esto

        #print(sel
    def return_focus(self):
        print('afttter corriendo')
        self.listbox.delete(0,END)

        self.spinbox.focus_set()    
        self.spinbox.icursor(END)

    
    """ def bind_listbox(self, event):
        #self.listbox.get(0)
        print('no puedo entrar tmr')
        
        print('igual me ejecute')
        self.spinbox.delete(0, END)
        self.spinbox.insert(0, self.listbox.get(0)) """


############   M E T O D O S   P A R A   G E S T I O N A R   L A S   V E N T A N A S   S U P E R I O R E S   ############ 

    def windows_123 (self, var_1, var_2, var_3):

        if self.open_1 == False: 
            self.toplevel_LEFT = _Toplevel()  #############################################################   VENTANA TOPLEVEL IZQUIERDA
            self.toplevel_LEFT .configure_toplevel ('izq', '220x690') #  metodo 

        self.open_1 = True     
                                
        container_frame_left = var_1 (self.toplevel_LEFT)  #  var_1 es un frame

        if self._frame_1 is not None:  
            self._frame_1 .destroy()
        self._frame_1 = container_frame_left
        self._frame_1 .pack()
        
        
        self.toplevel_LEFT .protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(1))

#_______

        if self.open_2 == False:
            self.toplevel_RIGHT = _Toplevel()  #############################################################   VENTANA TOPLEVEL DERECHA
            self.toplevel_RIGHT .configure_toplevel ('der', '220x690')

        self.open_2 = True

        container_frame_right = var_2 (self.toplevel_RIGHT)  # ES UN FRAME POSICIONADO EN TOPLEVEL

        if self._frame_2 is not None:
            self._frame_2 .destroy()
        self._frame_2 = container_frame_right
        self._frame_2 .pack()


        self.toplevel_RIGHT.protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(2))

#_______ desde aqui falta completar este if
        
        if self.open_3 == False:
            self.toplevel_STUF = _Toplevel()  #############################################################   VENTANA TOPLEVEL STUFF
            self.toplevel_STUF .configure_toplevel ('stuf', '620x190')

        self.open_3 = True

        container_frame_stuf = var_3 (self.toplevel_STUF)  # ES UN FRAME POSICIONADO EN TOPLEVEL

        if self._frame_3 is not None:
            self._frame_3 .destroy()
        self._frame_3 = container_frame_stuf
        self._frame_3 .pack()


        self.toplevel_STUF.protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(3))





    def close_windows(self, number):

        if number == 1:
            self.toplevel_LEFT. destroy()
            self.open_1 = False

        if number == 2:
            self.toplevel_RIGHT. destroy()
            self.open_2 = False

        if number == 3:
            self.toplevel_STUF. destroy()
            self.open_3 = False


#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-

class Checkbutton_class (Checkbutton):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variable = BooleanVar(self)
        self.configure(variable=self.variable)
    
    def checked(self):
        return self.variable.get()
    
    """ def check(self):
        self.variable.set(True)
    
    def uncheck(self):
        self.variable.set(False) """

    def value (self):

        if self.variable .get() == True: 
            pass  
            #self.master.master.frm_B2 .grid_remove()  #
            #self.master.master.frm_B3 .grid (column= 1, row= 0, padx=0, pady=0, sticky= NW)
            #self.spinbox .focus_set()    # aki trabajar                                           
            #self.master.master.frm_b3 .grid (column= 1, row= 0, padx=0, pady=0, sticky= NW)
        else:
            pass
            #self.master.master.frm_B3 .grid_remove()
            #self.master.master.frm_b3 .grid_remove() #
           # self.master.master.frm_B1 .focus_set()
 
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-

class _Toplevel (Toplevel):

    def __init__(self, *args): #---------------------------------------------------------NO TOCAR 
        Toplevel. __init__(self, *args) 
        #self.masters = master
          
    def configure_toplevel(self, head, size): #--------------------------------NO TOCAR (despues)
     
        self.title (head)    #  titulo
        self.geometry (size)  #  tamaño
        self.resizable (1,1)
        self.wm_attributes ('-topmost', True)
        self.config (bg = 'magenta2')
        self.wm_attributes ('-transparentcolor', 'magenta2')

    def widgets_toplevel(self):
        pass

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-

class Create_Frame (Frame):   

    def __init__(self, *args, **kwargs):   #---------------------------------------NO TOCAR (despues) 
        Frame.__init__(self, *args, **kwargs)   # Llamando a Frame ()  #, **kwargs : pasar mas valores al momento de la llamada (diccionarios)

    def img_ash(self):   # Metodo que crea -1- Boton (logo) -------------------NO TOCAR (despues)
        
        self.btn_ash = Button (self, image= self.master.Images_sublist [3], bg= '#11161d', bd= 0, activebackground= '#11161d' , command= self.master.minimize_windows)
        self.btn_ash .grid (column= 0, row= 0, padx= (6,6), pady= 0)

        self.btn_ash .bind ('<Double-Button-3>', self.master.ash_close_windows)
          
    def img_gear(self):   # Metodo que crea -1- Boton (rueda)-----------------NO TOCAR (despues)

        self.btn_gear = Button (self, image= self.master.Images_sublist [1], bg= '#11161d', bd= 0, activebackground= '#11161d', command= self.master.gear_stacking)        # akl era  command= self.master.configure_height
        self.btn_gear .grid (column= 0, row= 1)
       
    def img_moviles(self):   # Metodo que crea -22- Botones (moviles)  #command = lambda:images(1))
        
        self.Frog_1 = Button (self, text='Frog', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Frog_left_off, Frog_right, Frog_stuf)) 
        self.Fox_2 = Button (self, text='Fox', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fox_left_off, Fox_right, Fox_stuf))         
        self.Boomer_3 = Button (self, text='Boomer', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Boomer_left_off, Boomer_right, Boomer_stuf))             
        self.Ice_4 = Button (self, text='Ice', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Ice_left_off, Ice_right, Ice_stuf))
        self.JD_5 = Button (self, text='J.D', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Jd_left_off, Jd_right, Jd_stuf))
        self.Grub_6 = Button (self, text='Grub', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Grub_left_off, Grub_right, Grub_stuf))   
        self.Lightning_7 = Button (self, text='Lightning', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width=10, bd=0, command= lambda: self.master.master.windows_123 (Lightning_left_off, Lightning_right, Lightning_stuf))       
        self.Aduka_8 = Button (self, text='Aduka', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Aduka_left_off, Aduka_right, Aduka_stuf))      
        self.Knight_9 = Button (self, text='Knight', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Knight_left_off, Knight_right, Knight_stuf))     
        self.Kalsiddon_10 = Button (self, text='Kalsiddon', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Kalsiddon_left_off, Kalsiddon_right, Kalsiddon_stuf))
        self.Mage_11 = Button (self, text='Mage', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Mage_left_off, Mage_right, Mage_stuf))     

        self.Randomizer_12 = Button (self, text='Randomizer', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Randomizer_left_off, Randomizer_right, Randomizer_stuf)) 
        self.Jolteon_13 = Button (self, text='Jolteon', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Jolteon_left_off, Jolteon_right, Jolteon_stuf)) 
        self.Turtle_14 = Button (self, text='Turtle', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Turtle_left_off, Turtle_right, Turtle_stuf))
        self.Armor_15 = Button (self, text='Armor', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Armor_left_off, Armor_right, Armor_stuf))
        self.Asate_16 = Button (self, text='A.Sate', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Asate_left_off, Asate_right, Asate_stuf))
        self.Raon_17 = Button (self, text='Raon', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Raon_left_off, Raon_right, Raon_stuf)) 
        self.Trico_18 = Button (self, text='Trico', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Trico_left_off, Trico_right, Trico_stuf))
        self.Nak_19 = Button (self, text='Nak', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Nak_left_off, Nak_right, Nak_stuf)) 
        self.Bigfoot_20 = Button (self, text='Bigfoot', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Bigfoot_left_off, Bigfoot_right, Bigfoot_stuf)) 
        self.Barney_21 = Button (self, text='Barney', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Barney_left_off, Barney_right, Barney_stuf)) 
        self.Dragon_22 = Button (self, text='Dragon', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Dragon_left_off, Dragon_right, Dragon_stuf))
                
        self.Frog_1 .grid (column= 1, row= 1, pady= 3, padx= (5,0))
        self.Fox_2 .grid (column= 2, row= 1, pady= 3, padx= (0,0))       
        self.Boomer_3 .grid (column= 3, row= 1, pady= 3, padx= (0,0))           
        self.Ice_4 .grid (column= 4, row= 1, pady= 3, padx= (0,0))
        self.JD_5 .grid (column= 5, row= 1, pady= 3, padx= (0,0))
        self.Grub_6 .grid (column= 6, row= 1, pady= 3, padx= (0,0))
        self.Lightning_7 .grid (column= 7, row= 1, pady= 3, padx= (0,0))
        self.Aduka_8 .grid (column= 8, row= 1, pady= 3, padx= (0,0))
        self.Knight_9 .grid (column= 9, row= 1, pady= 3, padx= (0,0))
        self.Kalsiddon_10 .grid (column= 10, row= 1, pady= 3, padx= (0,0))
        self.Mage_11 .grid (column= 11, row= 1, pady= 3, padx= (0,5))