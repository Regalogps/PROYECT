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


def leer_folder (self, path, lista):  # Metodo para leer todas las imageneS ------NO TOCAR

        imagenes = os.listdir(path)
        self.lista_parcial = [] 
        self.lista_total = [] 

        if lista == "parcial" :
            for i in imagenes:
                if i . split(".")[-1] not is ["jpeg", "png"]:
                    continue
                ruta_completa = path + "/" + i               
                #print (ruta_completa)

                abrir = cv2.imread (ruta_completa)
                if abrir is None:
                    continue
                RGB = cv2.cvtColor (abrir, cv2.COLOR_BGR2RGB)
                objeto = Image.fromarray (RGB)

                self.lista_parcial. append (objeto)

            return self.lista_parcial

        if lista == "total" :
            for i in imagenes:
                if i . split(".")[-1] not is ["jpeg", "png"]:
                    continue
                ruta_completa = path + "/" + i

                abrir = cv2.imread (ruta_completa)
                if abrir is None:
                    continue
                RGB = cv2.cvtColor (abrir, cv2.COLOR_BGR2RGB)
                objeto = Image.fromarray (RGB)
                photo = ImageTk.PhotoImage(objeto)

                self.lista_total. append (photo)

            return self.lista_total