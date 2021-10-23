import tkinter as tk


root = tk.Tk()
root.geometry("300x100")

def on_validate(P):
    """ print(f"Nombre del widget: {W}")                                   #a
    print(f"Acción: {d} (0=eliminar, 1=insertar, -1=otras)")               #b
    print(f"Indice del caracter a insertar/eliminar: {i}")                 #a
    print(f"Texto a insertar/eliminar: '{S}'")                             #b
    print(f"Texto del Entry antes de insertar: '{s}'")                     #a
    print(f"Texto del Entry si se valida: '{P}'") 
    print(f"Tipo de la validación actual: {v}")                            #a
    print(f"Tipo de la validación que lanzó el evento: {V}") """           #a

    # Retornamos True si es válido o False en caso contrario
    if all(i not in "0123456789 " for i in P):
        return True
    return False

vcmd = (root.register(on_validate),'%P')


entry = tk.Entry(root,validate="key", validatecommand=vcmd)
entry.pack(side=tk.LEFT)
root.mainloop()