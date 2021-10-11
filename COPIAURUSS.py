import os   # os.path.join(), os.listdir()
import sys  # sys.argv
import tkinter as tk 
from PIL import Image, ImageTk

class Array(tk.Frame):
    def __init__(self, master, path, *args):
        super().__init__(master, *args) 
        
        self.image = Image.open(path)
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = tk.Label(self, image=self.background_image)
        self.background.pack(fill='both', expand=True)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):
        self.image = self.img_copy.resize((self.master.winfo_width(), self.master.winfo_height()//2))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class Interface(tk.Frame):
    def __init__(self, master, folder, *args):
        super().__init__(master, *args)      
        self.folder = folder
        
        #self.path_lst = ['11.png','22.png','33.png','44.png']
        self.path_lst = [os.path.join(self.folder, name) for name in os.listdir(self.folder) if name.lower().endswith(('.png', '.jpg', '.gif'))]
        print(self.path_lst )
        
        self._frame_1 = None
        self._frame_2 = None
        self._open_1 = False
        self._open_2 = False
        
        index_1 = 0
        index_2 = 2
        
        self.button1 = tk.Button(self, text='pack 1',
                      command=lambda:self.windows(lambda top:ShowImage(top, index_1, index_2, self.path_lst),
                                                  lambda top2:ShowImage2(top2, index_1, index_2, self.path_lst)))
        self.button1.pack()
 
    def windows(self, var_1, var_2):
        if not self._open_1:
            self.top1 = tk.Toplevel(self.master)
            self.top1.geometry('200x200')
                                
        container = var_1(self.top1)

        if self._frame_1 is not None:  
            self._frame_1.destroy()
            
        self._frame_1 = container
        self._frame_1.pack(fill='both', expand=True)
        self._open_1 = True

        self.top1.protocol('WM_DELETE_WINDOW', lambda: self.closed(1))
    

        if not self._open_2:
            self.top2 = tk.Toplevel(self.master)
            self.top2.geometry('200x200')
                                
        container2 = var_2(self.top2)

        if self._frame_2 is not None:  
            self._frame_2.destroy()
            
        self._frame_2 = container2
        self._frame_2.pack(fill='both', expand=True)
        self._open_2 = True

        self.top2.protocol('WM_DELETE_WINDOW', lambda: self.closed(2))
    

    def closed(self, number):
        if number == 1:
            self.top1.destroy()
            self._open_1 = False
        if number == 2:
            self.top2.destroy()
            self._open_2 = False


class ShowImage(tk.Frame):
    def __init__(self, master, index_1, index_2, path_lst, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        if len(path_lst) > index_1:
            self.img = Array(self, path_lst[index_1])
            self.img.grid(column=0, row=0, sticky='news')
        
        if len(path_lst) > index_2:
            self.img2 = Array(self, path_lst[index_2])
            self.img2.grid(column=0, row=1, sticky='news')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)     
        self.grid_rowconfigure(1, weight=1)


class ShowImage2(tk.Frame):
    def __init__(self, master, index_1, index_2, path_lst, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        if len(path_lst) > index_1:
            self.img = Array(self, path_lst[index_1])
            self.img.grid(column=0, row=0, sticky='news')
        
        if len(path_lst) > index_2:
            self.img2 = Array(self, path_lst[index_2])
            self.img2.grid(column=0, row=1, sticky='news')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)     
        self.grid_rowconfigure(1, weight=1)

# --- main ---

if len(sys.argv) > 1:
    folder = sys.argv[1]
    print('if:', folder, len(folder))
else:
    folder = os.getcwd()  # c:\Users\Usuario\Desktop\proyect

root = tk.Tk()
frm = Interface(root, folder)
frm.pack()
root.mainloop()
