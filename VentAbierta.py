from tkinter import *

root = Tk()

def n_ventana():
    #Reviso si la ventana está abierta
    #En caso de que la ventana esté abierta, no se abre otra.
    if(n_ventana.opened):
        return
    
    n_ventana.opened = True
    
    root2 = Toplevel(root)

    #Espero a que la ventana se cierre
    root2.wait_window()
    n_ventana.opened = False

#Establezco el valor inicial de n_ventana.opened.
#Como la ventana no estará abierta, le pondré False
n_ventana.opened = False

Button(root, text="Nueva Ventana", command=n_ventana).pack()

root.mainloop()
