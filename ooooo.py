import tkinter as tk
from tkinter import messagebox



class Teclado(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.entry_var = tk.StringVar()
        vcmd = (self.register(self.on_validate), '%P')
        self.entry_text = tk.Entry(self,
                                   validate="key",
                                   validatecommand=vcmd,
                                   textvariable=self.entry_var,
                                   widt=10
                                   )
        self.entry_text.bind('<Return>', self.on_enter)
        self.entry_text.config(relief=tk.RIDGE)
        self.entry_text.pack()

    def on_validate(self, P):
        if len(P) > 9:
            self.bell()
            return False
        return True

    def on_enter(self, event):
        text = self.entry_var.get()
        if len(text) < 9:
            self.bell()
            messagebox.showinfo("Error", "Debe ingresar nueve caracteres")
        else:   
            print(text)
            # self.miCur.execute("INSERT INTO REGISTRO2 VALUES(NULL,  %s)", text)
            # self.miCon.commit()


if __name__ == "__main__":
    root = tk.Tk()
    Teclado(root).pack(fill="both", expand=True)
    root.geometry("200x50+0+0")
    root.mainloop()