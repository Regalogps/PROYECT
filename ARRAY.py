
from tkinter import*
from PIL import Image, ImageTk

class Array(Frame):
    def __init__(self, master, path, *args):
        Frame.__init__(self, master, *args)       
        self.image = Image.open(path)
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill='both', expand=True)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):
        self.image = self.img_copy .resize ((self.master .winfo_width(), self.master .winfo_height()))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class Interface(Frame):
    def __init__(self, master, *args):
        Frame.__init__(self, master, *args)
        self._frame_1 = None
        self._open_1 = False
        self.path_lst = ['11.png', '22.png']
        self.button1 = Button(self, text='pack 1',
                      command= lambda:self.windows(Show_image))
        self.button1 .pack()
        
 
    def windows(self, var_1):
        if not self._open_1:
            self.top1 = Toplevel(self.master)
            self.top1 .geometry('200x200')
                                
        container = var_1(self.top1)

        if self._frame_1 is not None:  
            self._frame_1 .destroy()
        self._frame_1 = container
        self._frame_1 .pack()
        self._open_1 = True

        self.top1.protocol ('WM_DELETE_WINDOW', lambda: self.closed(1))
    
    def closed(self, number):
        if number == 1:
            self.top1. destroy()
            self._open_1 = False


class Show_image(Frame):   # Frame contenedor de ash y gear
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.img = Array(self, self.master.path_lst[0] )
        self.img . grid(column=0, row=1)
       

        # I intend to display 3 images 
        # in this frame, but how 
        # should I do it?

root = Tk()
frm = Interface(root)
frm .pack()
root.mainloop()

