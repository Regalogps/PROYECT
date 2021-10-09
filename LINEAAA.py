import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Calculadora Basica")

mi_frame = tk.Frame(root)
mi_frame.pack()

# -------- Pantalla --------
pantalla = tk.Entry(mi_frame)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="white", justify="right")

filas = [["7", "8", "9", "*"],
         ["4", "5", "6", "-"],
         ["1", "2", "3", "+"],
         ["/", "0", ",", "="]]

for x, fila in enumerate(filas):
    if x == 0:
        print(fila)
        for y, texto in enumerate(fila):
            boton = tk.Button(
                mi_frame, text=texto, font=("Roboto Cn", 14),
                relief="ridge", width=3, bd=1)
            boton.grid(row=x + 2, column=y + 1, padx=2)

root.mainloop()