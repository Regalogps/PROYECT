import tkinter as tk

class classA:

    def __init__(self):
        self.root = tk.Tk()
        btn = tk.Button(self.root, text="New window", command=self.windows)
        btn.pack()

    def windows(self):
        try:
            self.root2.winfo_viewable()
        except Exception as err:
            self.root2 = tk.Toplevel(self.root)
            self.root2.transient( self.root )
        else:
            print( "Toplevel created" )

app = classA()
app.root.mainloop()