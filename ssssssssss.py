import tkinter as tk

def callback(event):
    print("Deshabilitar el enlace durante 2 s")
    root.unbind("<a>", bind_id)
    root.after(2000, rebind)  # espere 2000 ms y vuelva a enlazar la tecla a

def rebind():
    global bind_id
    bind_id = root.bind("<a>", callback)
    print("Bindind on")


root = tk.Tk()
# almacenar el ID de enlace para poder desvincularlo
bind_id = root.bind("<a>", callback)

root.mainloop()