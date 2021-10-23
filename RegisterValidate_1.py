import tkinter as tk


root = tk.Tk()
root.geometry("300x100")

def on_validate(d, i, P, s, S, v, V, W):
    print(f"Nombre del widget: {W}")
    print(f"Acción: {d} (0=eliminar, 1=insertar, -1=otras)") 
    print(f"Indice del caracter a insertar/eliminar: {i}")
    print(f"Texto a insertar/eliminar: '{S}'")
    print(f"Texto del Entry antes de insertar: '{s}'")
    print(f"Texto del Entry si se valida: '{P}'")
    print(f"Tipo de la validación actual: {v}")
    print(f"Tipo de la validación que lanzó el evento: {V}")

    # Retornamos True si es válido o False en caso contrario
    if all(c in "0123456789" for c in P):
        return True
    return False

vcmd = (root.register(on_validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')


entry = tk.Entry(root,validate="key", validatecommand=vcmd)
entry.pack(side=tk.LEFT)
root.mainloop()