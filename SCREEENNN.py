
class MoveGlobalCls():
    def __init__(self):
        self._x = 0
        self._y = 0

        self._unmovable = []
        
    def make_unmovable(self, *widgets):
        self._unmovable.extend(widgets)
        
    def _is_movable(self, widget):
        return widget not in self._unmovable
    

    def start_move_global(self, event):        
        self._x = event.x
        self._y = event.y
   
    def stop_move_global(self, event):
        self._x = None
        self._y = None

        #___< R E L E A S E >:  Orden de ejecucion: 2
        try:                                              # LANZA UN ERROR: porque no reconoce el widget
            if event.widget.winfo_class() == 'Button':
                event.widget["state"] = "normal"
        except: pass
        #____________________________________________

    def on_move_global(self, event):
        if not self._is_movable(event.widget):
            return

        deltax = event.x - self._x
        deltay = event.y - self._y
        
        _class = event.widget.winfo_class()
        _toplevel = event.widget.winfo_toplevel()

        new_position = "+{}+{}".format (_toplevel.winfo_x() + deltax, _toplevel.winfo_y() + deltay)
        if not _class == 'TSizegrip':                 # Si la variable que se quiere mover es 'TSizegrip' no se mueve la ventana (SOLUCION)
            _toplevel.geometry(new_position)            # Mueve todas las ventanas en general menos root     
        if isinstance(_toplevel.master, Tk) == True :  # otro: if _toplevel.master == RootCls:
            _toplevel.master.geometry(new_position)     # Mueve la ventana root

        #___< M O T I O N >:  Orden de ejecucion: 1
        if event.widget.winfo_class() == 'Button':
            event.widget["state"] = "disabled"
        #__________________________________________



        print('5555555555555555555555',type(str(event.widget)))
        print('print:', event.widget.winfo_parent())
        if event.widget.winfo_parent() == '.!toplevel_class.!interface.!a1_class':
            print(88888)

 

        wi


    def pantalla_completa(self):
        screen_x = self.master.winfo_screenwidth()
        screen_y = self.master.winfo_screenheight()

        width_1 = screen_x * 20 / 100   # Ancho de la ventana  Aprox: 20% de 1200 = 220
        height_1 = screen_y - 50        # Alto de la ventana   Aprox: 800 - 50 = 750
        pos_x1 = 0                      # Posición en eje x
        pos_y1 = 20                     # Posición en eje y
        
        pos_x2 = width_1 * 4

        width_2 = screen_x *
        height_2 = screen_y 
        
        window_izq = ('{}x{}+{}+{}'.format(width_1, heigth_1, pos_x1, pos_y1))
        window_der = ('{}x{}+{}+{}'.format(width_1, height_1, pos_x2, pos_y1))
        window_stuf = ('{}x{}+{}+{}'.format(width_1, height_1, pos_x2, pos_y1))
   
        new_pos = "+{}+{}".format(self.winfo_x() + deltax, self.winfo_y() + deltay)
