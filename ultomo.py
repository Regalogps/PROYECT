import os   # os.path.join(), os.listdir()
import sys  # sys.argv
from tkinter import * 
from PIL import Image, ImageTk


class ResizeCls(Frame):
    def __init__(self, master, index, *args, **kwargs):
        super().__init__(master, *args, kwargs)
        self.image = Image.open (index)
        self.image_copy = self.image .copy()

        self.background = ImageTk.PhotoImage (self.image)

        self.img = Label (self, image= self.background)
        self.img .pack (fill= 'both', expand= True)
        self.img .bind ('<Configure>', self.resize)

    def resize(self, event):
        self.image2 = self.image_copy .resize ((self.master .winfo_width(), self.master .winfo_height()))
        
        self.background2 = ImageTk.PhotoImage (self.image2)
        self.img .config (image= self.background2)

class TopCls(Frame):
    def __init__(self, master, folder, path_lst=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.folder = folder
        self.path_lst = [os.path.join(self.folder, name) for name in os.listdir(self.folder) if name.lower().endswith(('.png', '.jpg', '.gif'))]

        # Image 1:
        self.frame_image_delay_complete = ResizeCls(self, self.path_lst[0], bd=0)
        self.frame_image_delay_complete       .grid(column=0, row=0)

        # Image 2:
        self.frame_image_mobil_tutorial = ResizeCls(self, self.path_lst[1], bd=0)
        self.frame_image_mobil_tutorial       .grid(column=0, row=0)                             # [ NOT POSITIONED ]

        # Text: "Guia"
        self.lbl_text_guia                  = Label(self, text='Insert / hide image', font=('Calibri',7,'bold'), bg='black' , fg='white', bd=0)  
        self.lbl_text_guia                   .place(x=2, y=48)    
        self.lbl_text_guia                    .bind('<Button-1>', self.open_image_miniature)

        # Widgets Not Positioned:  
        self.frame_image_mobil_tutorial .grid_remove()

        # Event: To Posición the label[text= "Guia"]
        self.bind('<Configure>', self.new_position_text_guia)


        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


    def new_position_text_guia(self, event):
        toplevel_width  = self.master.winfo_width() / 35
        toplevel_height = self.master.winfo_height() / 13
        x = int(toplevel_width)
        y = int(toplevel_height)    
     
        self.lbl_text_guia .place(x=x, y=y)

    def open_image_miniature(self, event):
        if self.frame_image_mobil_tutorial .grid_info() == {}:
            self.frame_image_mobil_tutorial .grid()
        else:
            self.frame_image_mobil_tutorial .grid_remove()

#--- main ---

if len(sys.argv) > 1:
    folder = sys.argv[1]
    print('if:', folder, len(folder))
else:
    folder = os.getcwd()  # c:\Users\Usuario\Desktop\proyecto

root = Tk()
frm = TopCls(root, folder)
frm.pack()
root.mainloop()