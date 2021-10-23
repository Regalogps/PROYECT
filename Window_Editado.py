import tkinter as tk



class BarraTitulo(tk.Frame):
    def __init__(self, parent=None, title=None, **kwargs):
        super(BarraTitulo, self).__init__(parent, **kwargs)
        self.parent = parent
        self.title = title if title else tk.StringVar('')
        self.btn_close = tk.Button(self, text="X", command=self.close)
        self.btn_minimize = tk.Button(self, text="_", command=self.minimize)
        self.title_lb = tk.Label(self, textvariable=self.title, fg="white", bg="black")
        self.btn_close.pack(side=tk.RIGHT, padx=10, pady=10)
        self.btn_minimize.pack(side=tk.RIGHT, pady=10)
        self.title_lb.pack(side=tk.BOTTOM, padx=10, pady=10)

    def close(self):
        self.parent.destroy()
        self.parent.parent.destroy()

    def minimize(self):
        self.parent.withdraw()
        self.parent.parent.iconify()


class VentanaSinBordes(tk.Toplevel):
    def __init__(self, parent=None, **kwargs):
        super(VentanaSinBordes, self).__init__(parent, **kwargs)
        self.overrideredirect(True)
        self.parent = parent
        self._x = 0
        self._y = 0

        self.borde = BarraTitulo(self, title=self.parent._title, background="black")
        self.contenido = tk.Frame(self)
        self.borde.pack(side=tk.TOP, fill=tk.BOTH)
        self.contenido.pack(side=tk.TOP, fill=tk.BOTH)
        self.borde.bind("<ButtonPress-1>", self.start_move)
        self.borde.bind("<ButtonRelease-1>", self.stop_move)
        self.borde.bind("<B1-Motion>", self.on_move)
        self.borde.title_lb.bind("<ButtonPress-1>", self.start_move)
        self.borde.title_lb.bind("<ButtonRelease-1>", self.stop_move)
        self.borde.title_lb.bind("<B1-Motion>", self.on_move)

    def start_move(self, event):
        self._x = event.x
        self._y = event.y

    def stop_move(self, event):
        self._x = None
        self._y = None

    def on_move(self, event):
        deltax = event.x - self._x
        deltay = event.y - self._y
        new_pos = "+{}+{}".format(self.winfo_x() + deltax, self.winfo_y() + deltay)
        self.geometry(new_pos)
        self.parent.geometry(new_pos)


class WindRoot(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(WindRoot, self).__init__(*args, **kwargs)
        self.resizable(False, False)
        self.geometry('0x0')
        self._title = tk.StringVar(self.title())
        self.window = VentanaSinBordes(self)
        self.window.geometry('400x200')
        self.bind("<Map>", self.on_deiconify)
        self.bind("<Unmap>", self.on_iconify)


    def title(self, *args):
        if args:
            self._title.set(args[0])
        super(WindRoot, self).title(args)

    def on_iconify(self, event):
        self.window.withdraw()

    def on_deiconify(self, event):
        self.window.deiconify()


if __name__ == '__main__':
    root = WindRoot()
    root.title('Ventana sin bordes')
    root.mainloop()